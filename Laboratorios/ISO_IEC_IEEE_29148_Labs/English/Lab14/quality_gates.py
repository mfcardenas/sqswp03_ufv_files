"""
Quality Gates Module for ISO/IEC/IEEE 29148:2011 
Requirements Quality Assurance System

This module implements quality gates for requirements validation
according to ISO/IEC/IEEE 29148:2011 standards.
"""

import json
import os
import datetime
import time
import logging
import threading
from enum import Enum
from collections import defaultdict
from quality_metrics import QualityAssessor


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('quality_gates')


class GateStatus(Enum):
    """Status of a quality gate"""
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"
    WAIVED = "waived"
    IN_PROGRESS = "in_progress"


class GateType(Enum):
    """Types of quality gates"""
    AUTOMATIC = "automatic"
    MANUAL = "manual"
    HYBRID = "hybrid"


class QualityGate:
    """Base class for quality gates"""
    
    def __init__(self, name, description, criteria=None, gate_type=GateType.AUTOMATIC):
        """
        Initialize a quality gate
        
        Args:
            name (str): Name of the gate
            description (str): Description of what the gate checks
            criteria (dict): Criteria for passing the gate
            gate_type (GateType): Type of gate (automatic, manual, hybrid)
        """
        self.name = name
        self.description = description
        self.criteria = criteria or {}
        self.gate_type = gate_type
        self.status = GateStatus.PENDING
        self.status_reason = ""
        self.last_run = None
        self.data = {}
    
    def evaluate(self, requirements=None, assessment_results=None):
        """
        Evaluate if the gate passes or fails
        
        Args:
            requirements (list): Requirements to evaluate
            assessment_results (dict): Quality assessment results
            
        Returns:
            bool: True if the gate passes, False otherwise
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_result(self):
        """Get the gate results as a dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'status': self.status.value,
            'status_reason': self.status_reason,
            'last_run': self.last_run,
            'gate_type': self.gate_type.value,
            'criteria': self.criteria,
            'data': self.data
        }
    
    def _update_status(self, passed, reason=""):
        """
        Update the gate status
        
        Args:
            passed (bool): Whether the gate passed
            reason (str): Reason for the status
        """
        self.status = GateStatus.PASSED if passed else GateStatus.FAILED
        self.status_reason = reason
        self.last_run = datetime.datetime.now().isoformat()
    
    def waive(self, reason):
        """
        Waive the gate (mark as passed even if it would fail)
        
        Args:
            reason (str): Reason for waiving the gate
        """
        self.status = GateStatus.WAIVED
        self.status_reason = reason
        self.last_run = datetime.datetime.now().isoformat()


class OverallQualityGate(QualityGate):
    """Gate that checks overall quality score"""
    
    def __init__(self, name="Overall Quality", description="Checks overall quality score", 
                 min_score=0.7, min_passing_ratio=0.8):
        """
        Initialize the overall quality gate
        
        Args:
            name (str): Name of the gate
            description (str): Description of what the gate checks
            min_score (float): Minimum acceptable overall score (0.0-1.0)
            min_passing_ratio (float): Minimum ratio of passing requirements (0.0-1.0)
        """
        criteria = {
            'min_score': min_score,
            'min_passing_ratio': min_passing_ratio
        }
        super().__init__(name, description, criteria, GateType.AUTOMATIC)
    
    def evaluate(self, requirements=None, assessment_results=None):
        """
        Evaluate if the gate passes or fails
        
        Args:
            requirements (list): Requirements to evaluate (not used)
            assessment_results (dict): Quality assessment results
            
        Returns:
            bool: True if the gate passes, False otherwise
        """
        if not assessment_results or 'summary' not in assessment_results:
            self._update_status(False, "No assessment results available")
            return False
        
        summary = assessment_results['summary']
        overall_score = summary.get('average_score', 0.0)
        total_reqs = summary.get('total_requirements', 0)
        passing_reqs = summary.get('total_passing', 0)
        
        if total_reqs == 0:
            passing_ratio = 0.0
        else:
            passing_ratio = passing_reqs / total_reqs
        
        # Determine if the gate passes
        min_score = self.criteria.get('min_score', 0.7)
        min_passing_ratio = self.criteria.get('min_passing_ratio', 0.8)
        
        passes_score = overall_score >= min_score
        passes_ratio = passing_ratio >= min_passing_ratio
        
        # Overall pass/fail
        passes = passes_score and passes_ratio
        
        # Update status
        reason = f"Overall score: {overall_score:.2f} (min: {min_score}), " \
                 f"Passing ratio: {passing_ratio:.2f} (min: {min_passing_ratio})"
        
        self._update_status(passes, reason)
        
        # Store additional data
        self.data = {
            'overall_score': overall_score,
            'passing_ratio': passing_ratio,
            'total_requirements': total_reqs,
            'passing_requirements': passing_reqs,
            'passes_score': passes_score,
            'passes_ratio': passes_ratio
        }
        
        return passes


class MetricQualityGate(QualityGate):
    """Gate that checks specific quality metrics"""
    
    def __init__(self, name="Metric Quality", description="Checks specific quality metrics", 
                 metrics=None, min_scores=None):
        """
        Initialize the metric quality gate
        
        Args:
            name (str): Name of the gate
            description (str): Description of what the gate checks
            metrics (list): List of metrics to check
            min_scores (dict): Minimum scores for each metric
        """
        self.metrics = metrics or ["Completeness", "Clarity", "Verifiability"]
        min_scores = min_scores or {}
        
        # Set default minimum scores if not provided
        for metric in self.metrics:
            if metric not in min_scores:
                min_scores[metric] = 0.7
        
        criteria = {
            'metrics': self.metrics,
            'min_scores': min_scores
        }
        super().__init__(name, description, criteria, GateType.AUTOMATIC)
    
    def evaluate(self, requirements=None, assessment_results=None):
        """
        Evaluate if the gate passes or fails
        
        Args:
            requirements (list): Requirements to evaluate (not used)
            assessment_results (dict): Quality assessment results
            
        Returns:
            bool: True if the gate passes, False otherwise
        """
        if not assessment_results or 'summary' not in assessment_results:
            self._update_status(False, "No assessment results available")
            return False
        
        summary = assessment_results['summary']
        metrics_summary = summary.get('metrics_summary', {})
        
        # Check each metric against its minimum score
        metrics_status = {}
        all_passing = True
        
        for metric in self.metrics:
            if metric not in metrics_summary:
                metrics_status[metric] = {
                    'available': False,
                    'score': 0.0,
                    'min_score': self.criteria['min_scores'].get(metric, 0.7),
                    'passing': False
                }
                all_passing = False
                continue
            
            metric_data = metrics_summary[metric]
            metric_score = metric_data.get('average_score', 0.0)
            min_score = self.criteria['min_scores'].get(metric, 0.7)
            
            passing = metric_score >= min_score
            
            metrics_status[metric] = {
                'available': True,
                'score': metric_score,
                'min_score': min_score,
                'passing': passing
            }
            
            if not passing:
                all_passing = False
        
        # Update status
        reasons = []
        for metric, status in metrics_status.items():
            if status['available']:
                reasons.append(f"{metric}: {status['score']:.2f} (min: {status['min_score']})")
            else:
                reasons.append(f"{metric}: Not available")
        
        reason = ", ".join(reasons)
        self._update_status(all_passing, reason)
        
        # Store additional data
        self.data = {
            'metrics_status': metrics_status,
            'all_metrics_passing': all_passing
        }
        
        return all_passing


class ComplianceQualityGate(QualityGate):
    """Gate that checks compliance with specific requirements"""
    
    def __init__(self, name="Compliance", description="Checks compliance with specific requirements", 
                 required_fields=None, required_patterns=None, forbidden_patterns=None):
        """
        Initialize the compliance quality gate
        
        Args:
            name (str): Name of the gate
            description (str): Description of what the gate checks
            required_fields (list): Fields that must be present in all requirements
            required_patterns (dict): Patterns that must be present in specific fields
            forbidden_patterns (dict): Patterns that must not be present in specific fields
        """
        required_fields = required_fields or ['id', 'description', 'type', 'priority']
        required_patterns = required_patterns or {}
        forbidden_patterns = forbidden_patterns or {}
        
        criteria = {
            'required_fields': required_fields,
            'required_patterns': required_patterns,
            'forbidden_patterns': forbidden_patterns
        }
        super().__init__(name, description, criteria, GateType.AUTOMATIC)
    
    def evaluate(self, requirements=None, assessment_results=None):
        """
        Evaluate if the gate passes or fails
        
        Args:
            requirements (list): Requirements to evaluate
            assessment_results (dict): Quality assessment results (not used)
            
        Returns:
            bool: True if the gate passes, False otherwise
        """
        if not requirements:
            self._update_status(False, "No requirements available")
            return False
        
        # Check compliance for each requirement
        compliance_issues = defaultdict(list)
        
        for req in requirements:
            req_id = req.get('id', 'unknown')
            
            # Check required fields
            for field in self.criteria['required_fields']:
                if field not in req or not req[field]:
                    compliance_issues[req_id].append(f"Missing required field: {field}")
            
            # Check required patterns
            for field, pattern in self.criteria['required_patterns'].items():
                if field in req and req[field]:
                    if not re.search(pattern, str(req[field])):
                        compliance_issues[req_id].append(
                            f"Field '{field}' does not match required pattern: {pattern}"
                        )
            
            # Check forbidden patterns
            for field, pattern in self.criteria['forbidden_patterns'].items():
                if field in req and req[field]:
                    if re.search(pattern, str(req[field])):
                        compliance_issues[req_id].append(
                            f"Field '{field}' contains forbidden pattern: {pattern}"
                        )
        
        # Determine if the gate passes
        non_compliant = len([req_id for req_id, issues in compliance_issues.items() if issues])
        total_reqs = len(requirements)
        
        if total_reqs == 0:
            compliance_ratio = 0.0
        else:
            compliance_ratio = (total_reqs - non_compliant) / total_reqs
        
        passes = compliance_ratio == 1.0  # All requirements must be compliant
        
        # Update status
        if passes:
            reason = "All requirements are compliant"
        else:
            reason = f"{non_compliant} of {total_reqs} requirements have compliance issues"
        
        self._update_status(passes, reason)
        
        # Store additional data
        self.data = {
            'compliance_ratio': compliance_ratio,
            'total_requirements': total_reqs,
            'non_compliant_requirements': non_compliant,
            'compliance_issues': compliance_issues
        }
        
        return passes


class ManualReviewGate(QualityGate):
    """Gate that requires manual review and approval"""
    
    def __init__(self, name="Manual Review", description="Requires manual review and approval", 
                 reviewers=None, approval_criteria=None):
        """
        Initialize the manual review gate
        
        Args:
            name (str): Name of the gate
            description (str): Description of what the gate checks
            reviewers (list): List of reviewers
            approval_criteria (str): Criteria for approval
        """
        reviewers = reviewers or []
        approval_criteria = approval_criteria or "All reviewers must approve"
        
        criteria = {
            'reviewers': reviewers,
            'approval_criteria': approval_criteria
        }
        super().__init__(name, description, criteria, GateType.MANUAL)
        
        self.approvals = {}
    
    def evaluate(self, requirements=None, assessment_results=None):
        """
        Evaluate if the gate passes or fails
        
        Args:
            requirements (list): Requirements to evaluate (not used)
            assessment_results (dict): Quality assessment results (not used)
            
        Returns:
            bool: True if the gate passes, False otherwise
        """
        # Manual gates are evaluated based on approvals
        # This method just checks if all required approvals are present
        
        if not self.criteria['reviewers']:
            self._update_status(False, "No reviewers specified")
            return False
        
        # Check if all reviewers have approved
        all_approved = all(self.approvals.get(reviewer, {}).get('approved', False) 
                         for reviewer in self.criteria['reviewers'])
        
        # Update status
        if all_approved:
            reason = "All reviewers have approved"
        else:
            approved = [reviewer for reviewer in self.criteria['reviewers'] 
                      if self.approvals.get(reviewer, {}).get('approved', False)]
            pending = [reviewer for reviewer in self.criteria['reviewers'] 
                      if reviewer not in approved]
            
            reason = f"Approved by: {', '.join(approved) if approved else 'none'}. " \
                     f"Pending: {', '.join(pending) if pending else 'none'}"
        
        self._update_status(all_approved, reason)
        
        # Store additional data
        self.data = {
            'approvals': self.approvals,
            'all_approved': all_approved
        }
        
        return all_approved
    
    def add_approval(self, reviewer, approved, comments=None):
        """
        Add a reviewer approval
        
        Args:
            reviewer (str): Name of the reviewer
            approved (bool): Whether the reviewer approves
            comments (str): Optional comments
            
        Returns:
            bool: True if the approval was added, False otherwise
        """
        if reviewer not in self.criteria['reviewers']:
            return False
        
        self.approvals[reviewer] = {
            'approved': approved,
            'comments': comments,
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        # Re-evaluate the gate
        self.evaluate()
        
        return True


class GatePhase:
    """A phase in the quality gate process"""
    
    def __init__(self, name, description, gates=None, required_gates=None):
        """
        Initialize a gate phase
        
        Args:
            name (str): Name of the phase
            description (str): Description of the phase
            gates (list): List of gates in this phase
            required_gates (list): Names of gates that must pass for the phase to pass
        """
        self.name = name
        self.description = description
        self.gates = gates or []
        self.required_gates = required_gates or [gate.name for gate in self.gates]
        self.status = GateStatus.PENDING
        self.status_reason = ""
        self.last_run = None
    
    def evaluate(self, requirements=None, assessment_results=None):
        """
        Evaluate all gates in this phase
        
        Args:
            requirements (list): Requirements to evaluate
            assessment_results (dict): Quality assessment results
            
        Returns:
            bool: True if the phase passes, False otherwise
        """
        if not self.gates:
            self._update_status(False, "No gates in this phase")
            return False
        
        # Evaluate each gate
        for gate in self.gates:
            gate.evaluate(requirements, assessment_results)
        
        # Check if all required gates pass
        required_passing = all(gate.status == GateStatus.PASSED 
                             for gate in self.gates 
                             if gate.name in self.required_gates)
        
        # Update status
        if required_passing:
            reason = "All required gates passed"
        else:
            failing_gates = [gate.name for gate in self.gates 
                           if gate.name in self.required_gates 
                           and gate.status != GateStatus.PASSED]
            
            reason = f"Gates failing: {', '.join(failing_gates)}"
        
        self._update_status(required_passing, reason)
        
        return required_passing
    
    def _update_status(self, passed, reason=""):
        """
        Update the phase status
        
        Args:
            passed (bool): Whether the phase passed
            reason (str): Reason for the status
        """
        self.status = GateStatus.PASSED if passed else GateStatus.FAILED
        self.status_reason = reason
        self.last_run = datetime.datetime.now().isoformat()
    
    def get_result(self):
        """Get the phase results as a dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'status': self.status.value,
            'status_reason': self.status_reason,
            'last_run': self.last_run,
            'required_gates': self.required_gates,
            'gates': [gate.get_result() for gate in self.gates]
        }


class QualityGateSystem:
    """Main class for managing quality gates"""
    
    def __init__(self, config_file=None):
        """
        Initialize the quality gate system
        
        Args:
            config_file (str): Path to configuration file
        """
        self.phases = []
        self.config = {}
        self.results = {}
        self.assessor = None
        
        # Load configuration if provided
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            
            # Initialize from config
            self._init_from_config()
        else:
            # Initialize default gates
            self._init_default_gates()
    
    def _init_from_config(self):
        """Initialize gates and phases from configuration"""
        if 'phases' not in self.config:
            self._init_default_gates()
            return
        
        for phase_config in self.config['phases']:
            gates = []
            
            for gate_config in phase_config.get('gates', []):
                gate_type = gate_config.get('type', 'automatic')
                
                if gate_type == 'overall':
                    gate = OverallQualityGate(
                        name=gate_config.get('name', 'Overall Quality'),
                        description=gate_config.get('description', 'Checks overall quality score'),
                        min_score=gate_config.get('min_score', 0.7),
                        min_passing_ratio=gate_config.get('min_passing_ratio', 0.8)
                    )
                
                elif gate_type == 'metric':
                    gate = MetricQualityGate(
                        name=gate_config.get('name', 'Metric Quality'),
                        description=gate_config.get('description', 'Checks specific quality metrics'),
                        metrics=gate_config.get('metrics', ["Completeness", "Clarity", "Verifiability"]),
                        min_scores=gate_config.get('min_scores', {})
                    )
                
                elif gate_type == 'compliance':
                    gate = ComplianceQualityGate(
                        name=gate_config.get('name', 'Compliance'),
                        description=gate_config.get('description', 'Checks compliance with specific requirements'),
                        required_fields=gate_config.get('required_fields'),
                        required_patterns=gate_config.get('required_patterns'),
                        forbidden_patterns=gate_config.get('forbidden_patterns')
                    )
                
                elif gate_type == 'manual':
                    gate = ManualReviewGate(
                        name=gate_config.get('name', 'Manual Review'),
                        description=gate_config.get('description', 'Requires manual review and approval'),
                        reviewers=gate_config.get('reviewers', []),
                        approval_criteria=gate_config.get('approval_criteria')
                    )
                
                else:
                    logger.warning(f"Unknown gate type: {gate_type}")
                    continue
                
                gates.append(gate)
            
            phase = GatePhase(
                name=phase_config.get('name', 'Phase'),
                description=phase_config.get('description', 'Gate phase'),
                gates=gates,
                required_gates=phase_config.get('required_gates')
            )
            
            self.phases.append(phase)
    
    def _init_default_gates(self):
        """Initialize default gates and phases"""
        # Initial Quality Phase
        initial_gates = [
            OverallQualityGate(
                name="Initial Quality",
                description="Checks basic quality criteria",
                min_score=0.6,
                min_passing_ratio=0.7
            ),
            ComplianceQualityGate(
                name="Basic Compliance",
                description="Checks basic compliance with requirements structure"
            )
        ]
        
        initial_phase = GatePhase(
            name="Initial Quality",
            description="Basic quality checks",
            gates=initial_gates
        )
        
        # Detailed Quality Phase
        detailed_gates = [
            MetricQualityGate(
                name="Core Metrics",
                description="Checks core quality metrics",
                metrics=["Completeness", "Clarity", "Verifiability"],
                min_scores={"Completeness": 0.8, "Clarity": 0.7, "Verifiability": 0.7}
            ),
            MetricQualityGate(
                name="Advanced Metrics",
                description="Checks advanced quality metrics",
                metrics=["Consistency", "Traceability", "Feasibility"],
                min_scores={"Consistency": 0.7, "Traceability": 0.6, "Feasibility": 0.7}
            )
        ]
        
        detailed_phase = GatePhase(
            name="Detailed Quality",
            description="Detailed quality checks",
            gates=detailed_gates
        )
        
        # Final Approval Phase
        final_gates = [
            OverallQualityGate(
                name="Final Quality",
                description="Checks final quality criteria",
                min_score=0.8,
                min_passing_ratio=0.9
            ),
            ManualReviewGate(
                name="Manager Approval",
                description="Requires approval from management",
                reviewers=["Project Manager", "Requirements Manager"]
            )
        ]
        
        final_phase = GatePhase(
            name="Final Approval",
            description="Final approval checks",
            gates=final_gates
        )
        
        self.phases = [initial_phase, detailed_phase, final_phase]
    
    def run_gates(self, requirements=None, assessment_results=None, phase_name=None):
        """
        Run quality gates
        
        Args:
            requirements (list): Requirements to evaluate
            assessment_results (dict): Quality assessment results
            phase_name (str): Name of the phase to run, or None for all phases
            
        Returns:
            dict: Gate results
        """
        if not requirements and not assessment_results:
            logger.error("No requirements or assessment results provided")
            return None
        
        # Create a quality assessor if needed
        if assessment_results is None:
            if self.assessor is None:
                self.assessor = QualityAssessor()
                self.assessor.requirements = requirements
            
            # Run assessment
            assessment_results = self.assessor.assess_all_requirements()
        
        # Run gates for the specified phase or all phases
        if phase_name:
            # Find the phase by name
            phase = next((p for p in self.phases if p.name == phase_name), None)
            
            if phase:
                phase.evaluate(requirements, assessment_results)
                self.results = {
                    'phase_results': [phase.get_result()],
                    'all_phases_passing': phase.status == GateStatus.PASSED,
                    'timestamp': datetime.datetime.now().isoformat()
                }
            else:
                logger.error(f"Phase not found: {phase_name}")
                return None
        else:
            # Run all phases
            for phase in self.phases:
                phase.evaluate(requirements, assessment_results)
            
            # Check if all phases pass
            all_passing = all(phase.status == GateStatus.PASSED for phase in self.phases)
            
            self.results = {
                'phase_results': [phase.get_result() for phase in self.phases],
                'all_phases_passing': all_passing,
                'timestamp': datetime.datetime.now().isoformat()
            }
        
        return self.results
    
    def get_gate_by_name(self, gate_name):
        """
        Get a gate by name
        
        Args:
            gate_name (str): Name of the gate
            
        Returns:
            QualityGate: The gate, or None if not found
        """
        for phase in self.phases:
            for gate in phase.gates:
                if gate.name == gate_name:
                    return gate
        
        return None
    
    def add_approval(self, gate_name, reviewer, approved, comments=None):
        """
        Add an approval to a manual gate
        
        Args:
            gate_name (str): Name of the gate
            reviewer (str): Name of the reviewer
            approved (bool): Whether the reviewer approves
            comments (str): Optional comments
            
        Returns:
            bool: True if the approval was added, False otherwise
        """
        gate = self.get_gate_by_name(gate_name)
        
        if gate and isinstance(gate, ManualReviewGate):
            return gate.add_approval(reviewer, approved, comments)
        
        return False
    
    def export_results(self, output_file=None):
        """
        Export gate results to a file
        
        Args:
            output_file (str): Path to output file
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        if not self.results:
            logger.warning("No results to export")
            return False
        
        if not output_file:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"gate_results_{timestamp}.json"
        
        try:
            with open(output_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error exporting results: {e}")
            return False
    
    def load_results(self, input_file):
        """
        Load gate results from a file
        
        Args:
            input_file (str): Path to input file
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        if not os.path.exists(input_file):
            logger.error(f"File not found: {input_file}")
            return False
        
        try:
            with open(input_file, 'r') as f:
                self.results = json.load(f)
            return True
        except Exception as e:
            logger.error(f"Error loading results: {e}")
            return False
    
    def create_gate_schedule(self, schedule_file=None):
        """
        Create a schedule for running gates periodically
        
        Args:
            schedule_file (str): Path to schedule file
            
        Returns:
            bool: True if schedule was created successfully, False otherwise
        """
        if not schedule_file:
            schedule_file = "gate_schedule.json"
        
        schedule = {
            'schedule': [
                {
                    'phase': phase.name,
                    'frequency': 'daily',
                    'time': '00:00',
                    'active': True
                }
                for phase in self.phases
            ],
            'created': datetime.datetime.now().isoformat()
        }
        
        try:
            with open(schedule_file, 'w') as f:
                json.dump(schedule, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error creating schedule: {e}")
            return False
    
    def run_scheduled_gates(self, schedule_file=None, requirements_file=None):
        """
        Run gates according to schedule
        
        Args:
            schedule_file (str): Path to schedule file
            requirements_file (str): Path to requirements file
            
        Returns:
            bool: True if scheduled gates were run successfully, False otherwise
        """
        if not schedule_file:
            schedule_file = "gate_schedule.json"
        
        if not os.path.exists(schedule_file):
            logger.error(f"Schedule file not found: {schedule_file}")
            return False
        
        try:
            with open(schedule_file, 'r') as f:
                schedule = json.load(f)
        except Exception as e:
            logger.error(f"Error loading schedule: {e}")
            return False
        
        # Load requirements if needed
        requirements = None
        if requirements_file and os.path.exists(requirements_file):
            try:
                with open(requirements_file, 'r') as f:
                    requirements = json.load(f)
            except Exception as e:
                logger.error(f"Error loading requirements: {e}")
                return False
        
        # Run gates for each scheduled phase
        for phase_schedule in schedule['schedule']:
            if not phase_schedule.get('active', True):
                continue
            
            phase_name = phase_schedule['phase']
            logger.info(f"Running scheduled gates for phase: {phase_name}")
            
            # Run gates for this phase
            self.run_gates(requirements=requirements, phase_name=phase_name)
            
            # Export results
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"gate_results_{phase_name.replace(' ', '_')}_{timestamp}.json"
            self.export_results(output_file)
        
        return True
    
    def start_monitoring(self, interval=86400, requirements_file=None):
        """
        Start continuous monitoring of quality gates
        
        Args:
            interval (int): Monitoring interval in seconds (default: 1 day)
            requirements_file (str): Path to requirements file
            
        Returns:
            bool: True if monitoring was started successfully, False otherwise
        """
        if not requirements_file:
            logger.error("Requirements file not specified")
            return False
        
        def monitor_gates():
            while True:
                logger.info("Running quality gates monitoring")
                
                # Load requirements
                requirements = None
                if os.path.exists(requirements_file):
                    try:
                        with open(requirements_file, 'r') as f:
                            requirements = json.load(f)
                    except Exception as e:
                        logger.error(f"Error loading requirements: {e}")
                        time.sleep(interval)
                        continue
                
                # Run gates
                self.run_gates(requirements=requirements)
                
                # Export results
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                output_file = f"gate_monitoring_{timestamp}.json"
                self.export_results(output_file)
                
                # Sleep until next run
                time.sleep(interval)
        
        # Start monitoring in a background thread
        monitor_thread = threading.Thread(target=monitor_gates, daemon=True)
        monitor_thread.start()
        
        logger.info(f"Quality gate monitoring started with interval: {interval} seconds")
        return True


# Run as standalone module
if __name__ == "__main__":
    import argparse
    import re
    
    parser = argparse.ArgumentParser(description='Requirements Quality Gates Tool')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--requirements', help='Path to requirements file')
    parser.add_argument('--phase', help='Name of the phase to run')
    parser.add_argument('--output', help='Path to output file')
    parser.add_argument('--schedule', action='store_true', 
                        help='Create a gate schedule')
    parser.add_argument('--monitor', action='store_true',
                        help='Start continuous monitoring')
    parser.add_argument('--interval', type=int, default=86400,
                        help='Monitoring interval in seconds')
    
    args = parser.parse_args()
    
    # Create quality gate system
    gate_system = QualityGateSystem(args.config)
    
    # Load requirements
    requirements = None
    if args.requirements and os.path.exists(args.requirements):
        with open(args.requirements, 'r') as f:
            requirements = json.load(f)
        print(f"Loaded {len(requirements)} requirements")
    
    # Create schedule if requested
    if args.schedule:
        if gate_system.create_gate_schedule():
            print("Gate schedule created successfully")
    
    # Start monitoring if requested
    elif args.monitor:
        if gate_system.start_monitoring(args.interval, args.requirements):
            print(f"Gate monitoring started with interval: {args.interval} seconds")
            # Keep the main thread alive
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("Monitoring stopped")
    
    # Run gates
    else:
        results = gate_system.run_gates(requirements=requirements, phase_name=args.phase)
        
        if results:
            all_passing = results.get('all_phases_passing', False)
            print(f"Gate evaluation complete. All phases passing: {all_passing}")
            
            # Export results
            if gate_system.export_results(args.output):
                print(f"Results exported to {args.output or 'default output file'}")
        else:
            print("Gate evaluation failed")
