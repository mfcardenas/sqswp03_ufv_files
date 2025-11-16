#!/usr/bin/env python3
"""
Requirements Compliance Monitoring Module
ISO/IEC/IEEE 29148:2011 Compliance Checking
"""

import json
import re
import os
import sys
import logging
from enum import Enum
from datetime import datetime
from typing import List, Dict, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("compliance_monitor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ComplianceStatus(Enum):
    """Enumeration of compliance statuses"""
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partial"
    NOT_APPLICABLE = "not_applicable"
    UNKNOWN = "unknown"


class ComplianceRule:
    """Class representing a compliance rule"""
    
    def __init__(self, rule_data: Dict[str, Any]):
        """Initialize compliance rule from rule data"""
        self.id = rule_data.get('id', '')
        self.standard = rule_data.get('standard', '')
        self.description = rule_data.get('description', '')
        self.severity = rule_data.get('severity', 'medium')
        self.check_type = rule_data.get('check_type', 'pattern')
        self.check_value = rule_data.get('check_value', '')
        self.check_operator = rule_data.get('check_operator', 'contains')
        self.metadata = rule_data.get('metadata', {})
    
    def check(self, requirement: Dict[str, Any]) -> bool:
        """
        Check if a requirement complies with this rule
        
        Args:
            requirement: The requirement to check
            
        Returns:
            bool: True if compliant, False if non-compliant
        """
        if self.check_type == 'pattern':
            return self._check_pattern(requirement)
        elif self.check_type == 'property':
            return self._check_property(requirement)
        elif self.check_type == 'length':
            return self._check_length(requirement)
        elif self.check_type == 'custom':
            return self._check_custom(requirement)
        else:
            logger.warning(f"Unknown check type '{self.check_type}' for rule {self.id}")
            return False
    
    def _check_pattern(self, requirement: Dict[str, Any]) -> bool:
        """Check requirement text against a regex pattern"""
        text = requirement.get('text', '')
        
        if self.check_operator == 'contains':
            return self.check_value in text
        elif self.check_operator == 'not_contains':
            return self.check_value not in text
        elif self.check_operator == 'matches':
            pattern = re.compile(self.check_value)
            return bool(pattern.search(text))
        elif self.check_operator == 'not_matches':
            pattern = re.compile(self.check_value)
            return not bool(pattern.search(text))
        else:
            return False
    
    def _check_property(self, requirement: Dict[str, Any]) -> bool:
        """Check if a requirement has a specific property"""
        if '.' in self.check_value:
            parts = self.check_value.split('.')
            current = requirement
            for part in parts:
                if part not in current:
                    return False
                current = current[part]
            return True
        else:
            return self.check_value in requirement
    
    def _check_length(self, requirement: Dict[str, Any]) -> bool:
        """Check the length of requirement text"""
        text = requirement.get('text', '')
        length = len(text.split())
        
        if self.check_operator == 'equals':
            return length == int(self.check_value)
        elif self.check_operator == 'less_than':
            return length < int(self.check_value)
        elif self.check_operator == 'greater_than':
            return length > int(self.check_value)
        elif self.check_operator == 'between':
            min_val, max_val = map(int, self.check_value.split(','))
            return min_val <= length <= max_val
        else:
            return False
    
    def _check_custom(self, requirement: Dict[str, Any]) -> bool:
        """Custom check implementation for specific rules"""
        if self.id == 'CR-001':
            # Check if requirement has a unique ID
            return 'id' in requirement and requirement['id'].strip() != ''
        elif self.id == 'CR-002':
            # Check if requirement is atomic (contains only one "shall" statement)
            text = requirement.get('text', '')
            shall_count = len(re.findall(r'\bshall\b', text.lower()))
            return shall_count == 1
        elif self.id == 'CR-003':
            # Check if requirement uses proper terminology
            text = requirement.get('text', '').lower()
            bad_terms = ['should', 'may', 'might', 'could']
            return not any(term in text.split() for term in bad_terms)
        else:
            logger.warning(f"No custom check implementation for rule {self.id}")
            return False


class ComplianceResult:
    """Class representing the result of a compliance check"""
    
    def __init__(self, rule_id: str, requirement_id: str, status: ComplianceStatus, 
                 message: str = '', severity: str = 'medium', details: Dict[str, Any] = None):
        """Initialize compliance result"""
        self.rule_id = rule_id
        self.requirement_id = requirement_id
        self.status = status
        self.message = message
        self.severity = severity
        self.details = details or {}
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            'rule_id': self.rule_id,
            'requirement_id': self.requirement_id,
            'status': self.status.value,
            'message': self.message,
            'severity': self.severity,
            'details': self.details,
            'timestamp': self.timestamp
        }


class ComplianceMonitor:
    """Main class for compliance monitoring"""
    
    def __init__(self, config_file: str):
        """
        Initialize compliance monitor
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.rules = []
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the compliance monitor"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            self.load_rules()
            self.is_initialized = True
            logger.info("Compliance monitor initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize compliance monitor: {str(e)}")
            self.is_initialized = False
    
    def load_rules(self) -> None:
        """Load compliance rules from configuration"""
        self.rules = []
        
        try:
            for standard in self.config['compliance']['standards']:
                standard_data = self.config['compliance']['standards'][standard]
                for rule_data in standard_data.get('rules', []):
                    rule_data['standard'] = standard
                    rule = ComplianceRule(rule_data)
                    self.rules.append(rule)
            
            logger.info(f"Loaded {len(self.rules)} compliance rules")
        except Exception as e:
            logger.error(f"Failed to load compliance rules: {str(e)}")
    
    def check_rule(self, rule_id: str, requirement: Dict[str, Any]) -> ComplianceResult:
        """
        Check compliance for a single rule
        
        Args:
            rule_id: The ID of the rule to check
            requirement: The requirement to check
            
        Returns:
            ComplianceResult: Result of the compliance check
        """
        rule = next((r for r in self.rules if r.id == rule_id), None)
        
        if not rule:
            return ComplianceResult(
                rule_id=rule_id,
                requirement_id=requirement.get('id', 'unknown'),
                status=ComplianceStatus.UNKNOWN,
                message=f"Rule {rule_id} not found",
                severity='low'
            )
        
        is_compliant = rule.check(requirement)
        
        if is_compliant:
            return ComplianceResult(
                rule_id=rule_id,
                requirement_id=requirement.get('id', 'unknown'),
                status=ComplianceStatus.COMPLIANT,
                message=f"Requirement complies with rule {rule_id}",
                severity=rule.severity
            )
        else:
            return ComplianceResult(
                rule_id=rule_id,
                requirement_id=requirement.get('id', 'unknown'),
                status=ComplianceStatus.NON_COMPLIANT,
                message=f"Requirement does not comply with rule {rule_id}: {rule.description}",
                severity=rule.severity
            )
    
    def check_compliance(self, requirements: List[Dict[str, Any]]) -> List[ComplianceResult]:
        """
        Check compliance for all rules against a list of requirements
        
        Args:
            requirements: List of requirements to check
            
        Returns:
            List[ComplianceResult]: Results of all compliance checks
        """
        results = []
        
        for requirement in requirements:
            for rule in self.rules:
                result = self.check_rule(rule.id, requirement)
                results.append(result)
        
        return results
    
    def generate_report(self, results: List[ComplianceResult]) -> Dict[str, Any]:
        """
        Generate a compliance report from check results
        
        Args:
            results: List of compliance check results
            
        Returns:
            Dict[str, Any]: Compliance report
        """
        total_checks = len(results)
        compliant = sum(1 for r in results if r.status == ComplianceStatus.COMPLIANT)
        non_compliant = sum(1 for r in results if r.status == ComplianceStatus.NON_COMPLIANT)
        other = total_checks - compliant - non_compliant
        
        compliance_score = 0
        if total_checks > 0:
            compliance_score = int((compliant / total_checks) * 100)
        
        # Group results by requirement
        results_by_req = {}
        for result in results:
            req_id = result.requirement_id
            if req_id not in results_by_req:
                results_by_req[req_id] = []
            results_by_req[req_id].append(result.to_dict())
        
        # Group results by standard
        results_by_std = {}
        for result in results:
            rule = next((r for r in self.rules if r.id == result.rule_id), None)
            if not rule:
                continue
                
            std = rule.standard
            if std not in results_by_std:
                results_by_std[std] = {
                    'total': 0,
                    'compliant': 0,
                    'non_compliant': 0,
                    'compliance_score': 0
                }
            
            results_by_std[std]['total'] += 1
            if result.status == ComplianceStatus.COMPLIANT:
                results_by_std[std]['compliant'] += 1
            elif result.status == ComplianceStatus.NON_COMPLIANT:
                results_by_std[std]['non_compliant'] += 1
        
        # Calculate standard-specific compliance scores
        for std in results_by_std:
            std_data = results_by_std[std]
            if std_data['total'] > 0:
                std_data['compliance_score'] = int((std_data['compliant'] / std_data['total']) * 100)
        
        # Create report
        report = {
            'summary': {
                'total_checks': total_checks,
                'compliant_checks': compliant,
                'non_compliant_checks': non_compliant,
                'other_checks': other,
                'compliance_score': compliance_score,
                'standards': results_by_std,
                'timestamp': datetime.now().isoformat()
            },
            'details': {
                'by_requirement': results_by_req
            }
        }
        
        return report
    
    def get_rule_by_id(self, rule_id: str) -> Optional[ComplianceRule]:
        """
        Get a rule by its ID
        
        Args:
            rule_id: The ID of the rule to get
            
        Returns:
            Optional[ComplianceRule]: The rule, or None if not found
        """
        return next((r for r in self.rules if r.id == rule_id), None)
    
    def get_rules_by_standard(self, standard: str) -> List[ComplianceRule]:
        """
        Get all rules for a specific standard
        
        Args:
            standard: The standard to get rules for
            
        Returns:
            List[ComplianceRule]: List of rules for the standard
        """
        return [r for r in self.rules if r.standard == standard]


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python compliance_monitor.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    monitor = ComplianceMonitor(config_file)
    
    if not monitor.is_initialized:
        print("Failed to initialize compliance monitor")
        sys.exit(1)
    
    print(f"Loaded {len(monitor.rules)} compliance rules")
