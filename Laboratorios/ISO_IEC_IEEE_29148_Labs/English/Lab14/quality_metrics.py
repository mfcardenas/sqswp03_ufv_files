"""
Quality Metrics Module for ISO/IEC/IEEE 29148:2011 
Requirements Quality Assurance System

This module implements a comprehensive quality metrics engine for assessing 
requirements quality according to ISO/IEC/IEEE 29148:2011 standards.
"""

import json
import os
import re
import datetime
import math
import pandas as pd
import numpy as np
from collections import defaultdict, Counter


class QualityMetric:
    """Base class for all quality metrics"""
    
    def __init__(self, name, description, weight=1.0, threshold=0.7):
        """
        Initialize a quality metric
        
        Args:
            name (str): Name of the metric
            description (str): Description of what the metric measures
            weight (float): Relative importance of this metric (default: 1.0)
            threshold (float): Minimum acceptable score (0.0-1.0) (default: 0.7)
        """
        self.name = name
        self.description = description
        self.weight = weight
        self.threshold = threshold
        self.score = 0.0
        self.data = {}
    
    def measure(self, requirement):
        """
        Measure the quality of a requirement based on this metric
        
        Args:
            requirement (dict): The requirement to measure
            
        Returns:
            float: Quality score between 0.0 and 1.0
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def is_passing(self):
        """Check if the metric score exceeds the threshold"""
        return self.score >= self.threshold
    
    def get_result(self):
        """Get the metric results as a dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'score': self.score,
            'threshold': self.threshold,
            'weight': self.weight,
            'passing': self.is_passing(),
            'data': self.data
        }


class CompletenessMetric(QualityMetric):
    """Measures the completeness of requirements"""
    
    def __init__(self, required_fields=None, weight=1.0, threshold=0.8):
        """
        Initialize the completeness metric
        
        Args:
            required_fields (list): List of fields that should be present
            weight (float): Metric weight
            threshold (float): Minimum acceptable score
        """
        super().__init__(
            name="Completeness",
            description="Measures if requirements contain all necessary information",
            weight=weight,
            threshold=threshold
        )
        
        self.required_fields = required_fields or [
            'id', 'title', 'description', 'type', 'priority', 
            'status', 'rationale', 'verification_method'
        ]
    
    def measure(self, requirement):
        """
        Measure completeness by checking for required fields
        
        Args:
            requirement (dict): The requirement to measure
            
        Returns:
            float: Completeness score (0.0-1.0)
        """
        if not requirement:
            return 0.0
        
        # Count fields that are present and non-empty
        present_fields = sum(1 for field in self.required_fields 
                            if field in requirement and requirement[field])
        
        # Calculate completeness score
        score = present_fields / len(self.required_fields)
        
        # Track missing fields for reporting
        missing_fields = [field for field in self.required_fields 
                         if field not in requirement or not requirement[field]]
        
        self.data[requirement.get('id', 'unknown')] = {
            'score': score,
            'missing_fields': missing_fields,
            'present_fields': present_fields,
            'total_fields': len(self.required_fields)
        }
        
        return score


class ClarityMetric(QualityMetric):
    """Measures the clarity and readability of requirements"""
    
    def __init__(self, weight=1.0, threshold=0.7):
        """Initialize the clarity metric"""
        super().__init__(
            name="Clarity",
            description="Measures the clarity and readability of requirements",
            weight=weight,
            threshold=threshold
        )
        
        # Ambiguous words that should be avoided in requirements
        self.ambiguous_terms = [
            'adequate', 'as appropriate', 'as required', 'as applicable', 
            'if possible', 'when necessary', 'user-friendly', 'easy to use',
            'flexible', 'approximately', 'quick', 'efficient', 'several',
            'sufficient', 'suitable', 'enough', 'somehow', 'minimal', 
            'maximized', 'minimized', 'optimized', 'robust', 'many', 'few',
            'better', 'improved', 'reliable', 'some', 'fast', 'slow'
        ]
    
    def measure(self, requirement):
        """
        Measure clarity of a requirement
        
        Args:
            requirement (dict): The requirement to measure
            
        Returns:
            float: Clarity score (0.0-1.0)
        """
        if not requirement or 'description' not in requirement:
            return 0.0
        
        description = requirement.get('description', '')
        
        if not description:
            self.data[requirement.get('id', 'unknown')] = {
                'score': 0.0,
                'ambiguous_terms': [],
                'sentence_length_score': 0.0,
                'ambiguity_score': 0.0
            }
            return 0.0
        
        # Check for ambiguous terms
        found_terms = []
        for term in self.ambiguous_terms:
            pattern = r'\b' + re.escape(term) + r'\b'
            if re.search(pattern, description, re.IGNORECASE):
                found_terms.append(term)
        
        # Count sentences and calculate average length
        sentences = re.split(r'[.!?]+', description)
        valid_sentences = [s.strip() for s in sentences if s.strip()]
        if not valid_sentences:
            sentence_length_score = 0.0
        else:
            avg_length = sum(len(s.split()) for s in valid_sentences) / len(valid_sentences)
            # Ideal length is between 10-20 words
            if 10 <= avg_length <= 20:
                sentence_length_score = 1.0
            else:
                # Penalize for sentences that are too short or too long
                sentence_length_score = max(0, 1 - abs(avg_length - 15) / 15)
        
        # Calculate ambiguity score (inverse of ambiguous terms)
        ambiguity_score = max(0, 1 - len(found_terms) / 10)
        
        # Final clarity score is average of sentence length and ambiguity scores
        score = (sentence_length_score + ambiguity_score) / 2
        
        self.data[requirement.get('id', 'unknown')] = {
            'score': score,
            'ambiguous_terms': found_terms,
            'sentence_length_score': sentence_length_score,
            'ambiguity_score': ambiguity_score
        }
        
        return score


class ConsistencyMetric(QualityMetric):
    """Measures the consistency of requirements terminology and structure"""
    
    def __init__(self, weight=1.0, threshold=0.8):
        """Initialize the consistency metric"""
        super().__init__(
            name="Consistency",
            description="Measures the consistency of terminology and structure",
            weight=weight,
            threshold=threshold
        )
        self.terminology = defaultdict(list)
        self.inconsistencies = defaultdict(list)
    
    def measure(self, requirement, all_requirements=None):
        """
        Measure consistency of a requirement against all other requirements
        
        Args:
            requirement (dict): The requirement to measure
            all_requirements (list): All requirements for comparison
            
        Returns:
            float: Consistency score (0.0-1.0)
        """
        if not requirement or 'description' not in requirement or not all_requirements:
            return 0.0
        
        req_id = requirement.get('id', 'unknown')
        description = requirement.get('description', '')
        
        # Extract key terms from the requirement
        if description:
            terms = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', description)
            for term in terms:
                self.terminology[term].append(req_id)
        
        # Check for terminology consistency issues
        terminology_score = 1.0
        
        # For each key term, check for similar terms that might be inconsistent
        for term in self.terminology:
            # Find similar terms using a simple similarity measure
            similar_terms = [t for t in self.terminology if t != term and 
                            self._similarity(term, t) > 0.8]
            
            if similar_terms:
                # Log inconsistency
                self.inconsistencies[req_id].append({
                    'term': term,
                    'similar_terms': similar_terms
                })
                
                # Reduce score based on number of inconsistencies
                terminology_score -= 0.1 * min(len(similar_terms), 5)
        
        # Ensure score is within bounds
        terminology_score = max(0, min(terminology_score, 1.0))
        
        # Store result for this requirement
        self.data[req_id] = {
            'score': terminology_score,
            'inconsistencies': self.inconsistencies.get(req_id, [])
        }
        
        return terminology_score
    
    def _similarity(self, term1, term2):
        """
        Calculate simple similarity between two terms
        
        Args:
            term1 (str): First term
            term2 (str): Second term
            
        Returns:
            float: Similarity score (0.0-1.0)
        """
        # Simple case-insensitive Jaccard similarity
        set1 = set(term1.lower())
        set2 = set(term2.lower())
        
        if not set1 or not set2:
            return 0.0
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union


class VerifiabilityMetric(QualityMetric):
    """Measures if requirements are testable and verifiable"""
    
    def __init__(self, weight=1.0, threshold=0.7):
        """Initialize the verifiability metric"""
        super().__init__(
            name="Verifiability",
            description="Measures if requirements are testable and verifiable",
            weight=weight,
            threshold=threshold
        )
        
        # Patterns that indicate verifiability
        self.verifiable_patterns = [
            r'\b(measure|test|verify|validate|check|confirm|determine)\b',
            r'\b(at least|at most|maximum|minimum|exactly)\b',
            r'\b(greater than|less than|equal to)\b',
            r'\b\d+(\.\d+)?\s*(percent|%|seconds|minutes|hours|days)\b',
            r'\bmust\s+(?!not)(be|have|provide|support|allow|enable|ensure)\b'
        ]
        
        # Patterns that indicate non-verifiability
        self.non_verifiable_patterns = [
            r'\b(may|might|could|should|would)\b',
            r'\b(generally|normally|typically|usually|often|sometimes)\b',
            r'\b(adequate|appropriate|reasonable|sufficient)\b'
        ]
    
    def measure(self, requirement):
        """
        Measure verifiability of a requirement
        
        Args:
            requirement (dict): The requirement to measure
            
        Returns:
            float: Verifiability score (0.0-1.0)
        """
        if not requirement or 'description' not in requirement:
            return 0.0
        
        req_id = requirement.get('id', 'unknown')
        description = requirement.get('description', '')
        
        if not description:
            self.data[req_id] = {
                'score': 0.0,
                'verifiable_matches': [],
                'non_verifiable_matches': []
            }
            return 0.0
        
        # Check for verifiable patterns
        verifiable_matches = []
        for pattern in self.verifiable_patterns:
            matches = re.findall(pattern, description, re.IGNORECASE)
            if matches:
                verifiable_matches.extend(matches)
        
        # Check for non-verifiable patterns
        non_verifiable_matches = []
        for pattern in self.non_verifiable_patterns:
            matches = re.findall(pattern, description, re.IGNORECASE)
            if matches:
                non_verifiable_matches.extend(matches)
        
        # Calculate score based on presence of verifiable and absence of non-verifiable terms
        verifiable_score = min(1.0, len(verifiable_matches) * 0.2)
        non_verifiable_penalty = min(0.8, len(non_verifiable_matches) * 0.2)
        
        score = max(0, verifiable_score - non_verifiable_penalty)
        
        # Check if verification method is specified
        if 'verification_method' in requirement and requirement['verification_method']:
            score += 0.3
            score = min(1.0, score)
        
        self.data[req_id] = {
            'score': score,
            'verifiable_matches': verifiable_matches,
            'non_verifiable_matches': non_verifiable_matches,
            'has_verification_method': 'verification_method' in requirement and bool(requirement['verification_method'])
        }
        
        return score


class TraceabilityMetric(QualityMetric):
    """Measures if requirements have proper traceability links"""
    
    def __init__(self, weight=1.0, threshold=0.6):
        """Initialize the traceability metric"""
        super().__init__(
            name="Traceability",
            description="Measures if requirements have proper traceability links",
            weight=weight,
            threshold=threshold
        )
    
    def measure(self, requirement, requirement_links=None):
        """
        Measure traceability of a requirement
        
        Args:
            requirement (dict): The requirement to measure
            requirement_links (dict): Dictionary of requirement links
            
        Returns:
            float: Traceability score (0.0-1.0)
        """
        if not requirement:
            return 0.0
        
        req_id = requirement.get('id', 'unknown')
        
        # Check for traceability fields
        trace_fields = [
            'parent_id', 'related_ids', 'depends_on', 'source', 
            'rationale', 'stakeholder'
        ]
        
        # Count present traceability fields
        present_fields = sum(1 for field in trace_fields 
                           if field in requirement and requirement[field])
        
        # Base score on presence of traceability fields
        base_score = present_fields / len(trace_fields)
        
        # Check for bidirectional traceability if links are provided
        if requirement_links and req_id in requirement_links:
            links = requirement_links[req_id]
            
            # Check if links are bidirectional
            bidirectional_count = 0
            for linked_req in links:
                if linked_req in requirement_links and req_id in requirement_links[linked_req]:
                    bidirectional_count += 1
            
            # Calculate bidirectional score
            if links:
                bidirectional_score = bidirectional_count / len(links)
            else:
                bidirectional_score = 0.0
            
            # Final score is weighted average of base and bidirectional scores
            score = 0.7 * base_score + 0.3 * bidirectional_score
        else:
            score = base_score
        
        self.data[req_id] = {
            'score': score,
            'present_trace_fields': present_fields,
            'total_trace_fields': len(trace_fields),
            'has_links': requirement_links is not None and req_id in requirement_links
        }
        
        return score


class FeasibilityMetric(QualityMetric):
    """Measures if requirements are technically feasible"""
    
    def __init__(self, weight=1.0, threshold=0.7):
        """Initialize the feasibility metric"""
        super().__init__(
            name="Feasibility",
            description="Measures if requirements are technically feasible",
            weight=weight,
            threshold=threshold
        )
        
        # Terms that might indicate feasibility concerns
        self.feasibility_concern_terms = [
            r'\b(impossible|infeasible|cannot|never|always|all|none|every|any|100%)\b',
            r'\b(real-time|instantaneous|immediate|instant|zero|no delay)\b',
            r'\b(unlimited|infinite|indefinite|endless|boundless)\b',
            r'\b(perfect|flawless|error-free|fail-safe|foolproof)\b'
        ]
    
    def measure(self, requirement, complexity_threshold=7):
        """
        Measure feasibility of a requirement
        
        Args:
            requirement (dict): The requirement to measure
            complexity_threshold (int): Threshold for complexity warnings
            
        Returns:
            float: Feasibility score (0.0-1.0)
        """
        if not requirement or 'description' not in requirement:
            return 0.0
        
        req_id = requirement.get('id', 'unknown')
        description = requirement.get('description', '')
        
        if not description:
            self.data[req_id] = {
                'score': 0.0,
                'concern_matches': [],
                'complexity_score': 0.0
            }
            return 0.0
        
        # Check for terms that might indicate feasibility concerns
        concern_matches = []
        for pattern in self.feasibility_concern_terms:
            matches = re.findall(pattern, description, re.IGNORECASE)
            if matches:
                concern_matches.extend(matches)
        
        # Calculate concern score (higher is better, fewer concerns)
        concern_score = max(0, 1 - (len(concern_matches) * 0.2))
        
        # Calculate complexity score based on requirement length and structure
        word_count = len(description.split())
        if word_count <= 20:
            complexity_score = 1.0
        elif word_count <= 50:
            complexity_score = 0.8
        elif word_count <= 100:
            complexity_score = 0.6
        else:
            complexity_score = 0.4
        
        # Count conditional statements, which increase complexity
        conditions = len(re.findall(r'\b(if|when|unless|until|while|although|though)\b', 
                                  description, re.IGNORECASE))
        
        # Adjust complexity score based on conditions
        if conditions > complexity_threshold:
            complexity_score *= 0.7
        
        # Final score is weighted average of concern and complexity scores
        score = 0.6 * concern_score + 0.4 * complexity_score
        
        self.data[req_id] = {
            'score': score,
            'concern_matches': concern_matches,
            'complexity_score': complexity_score,
            'word_count': word_count,
            'condition_count': conditions
        }
        
        return score


class QualityAssessor:
    """Main class for assessing requirements quality"""
    
    def __init__(self, config_file=None):
        """
        Initialize the quality assessor
        
        Args:
            config_file (str): Path to configuration file
        """
        self.metrics = []
        self.config = {}
        self.results = {}
        self.requirements = []
        self.req_links = {}
        
        # Load configuration if provided
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        
        # Initialize default metrics
        self._init_default_metrics()
    
    def _init_default_metrics(self):
        """Initialize the default set of quality metrics"""
        self.metrics = [
            CompletenessMetric(weight=1.0, threshold=0.8),
            ClarityMetric(weight=1.0, threshold=0.7),
            ConsistencyMetric(weight=0.8, threshold=0.8),
            VerifiabilityMetric(weight=1.0, threshold=0.7),
            TraceabilityMetric(weight=0.8, threshold=0.6),
            FeasibilityMetric(weight=0.7, threshold=0.7)
        ]
    
    def load_quality_standards(self, standards_file=None):
        """
        Load quality standards from a file
        
        Args:
            standards_file (str): Path to standards file
        """
        if not standards_file and 'standards_file' in self.config:
            standards_file = self.config['standards_file']
        
        if standards_file and os.path.exists(standards_file):
            with open(standards_file, 'r') as f:
                standards = json.load(f)
            
            # Update metric configurations based on standards
            if 'metrics' in standards:
                for metric_conf in standards['metrics']:
                    # Find the corresponding metric
                    for metric in self.metrics:
                        if metric.name.lower() == metric_conf['name'].lower():
                            # Update metric properties
                            if 'weight' in metric_conf:
                                metric.weight = metric_conf['weight']
                            if 'threshold' in metric_conf:
                                metric.threshold = metric_conf['threshold']
                            break
    
    def load_requirements(self, requirements_file=None):
        """
        Load requirements from a file
        
        Args:
            requirements_file (str): Path to requirements file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        if not requirements_file and 'requirements_file' in self.config:
            requirements_file = self.config['requirements_file']
        
        if requirements_file and os.path.exists(requirements_file):
            with open(requirements_file, 'r') as f:
                self.requirements = json.load(f)
            
            # Extract requirement links
            self._extract_requirement_links()
            return True
        
        return False
    
    def _extract_requirement_links(self):
        """Extract links between requirements"""
        self.req_links = {}
        
        # Collect all possible link fields
        link_fields = ['parent_id', 'related_ids', 'depends_on']
        
        for req in self.requirements:
            req_id = req.get('id')
            if not req_id:
                continue
            
            links = []
            
            # Collect all links from this requirement
            for field in link_fields:
                if field in req and req[field]:
                    if isinstance(req[field], list):
                        links.extend(req[field])
                    else:
                        links.append(req[field])
            
            if links:
                self.req_links[req_id] = links
    
    def assess_requirement(self, requirement):
        """
        Assess the quality of a single requirement
        
        Args:
            requirement (dict): The requirement to assess
            
        Returns:
            dict: Assessment results
        """
        req_id = requirement.get('id', 'unknown')
        results = {'id': req_id, 'metrics': {}, 'overall_score': 0.0}
        
        total_weight = sum(metric.weight for metric in self.metrics)
        weighted_sum = 0.0
        
        for metric in self.metrics:
            # Special case for consistency and traceability metrics
            if isinstance(metric, ConsistencyMetric):
                score = metric.measure(requirement, self.requirements)
            elif isinstance(metric, TraceabilityMetric):
                score = metric.measure(requirement, self.req_links)
            else:
                score = metric.measure(requirement)
            
            # Store individual metric score
            results['metrics'][metric.name] = {
                'score': score,
                'passing': score >= metric.threshold,
                'threshold': metric.threshold,
                'weight': metric.weight
            }
            
            # Add to weighted sum
            weighted_sum += score * metric.weight
        
        # Calculate overall score
        if total_weight > 0:
            results['overall_score'] = weighted_sum / total_weight
        
        # Determine overall pass/fail
        passing_metrics = sum(1 for m in results['metrics'].values() if m['passing'])
        results['passing'] = passing_metrics == len(self.metrics)
        results['passing_ratio'] = passing_metrics / len(self.metrics)
        
        # Store timestamp
        results['timestamp'] = datetime.datetime.now().isoformat()
        
        return results
    
    def assess_all_requirements(self):
        """
        Assess the quality of all requirements
        
        Returns:
            dict: Assessment results for all requirements
        """
        self.results = {
            'requirements': {},
            'summary': {
                'total_requirements': len(self.requirements),
                'total_passing': 0,
                'average_score': 0.0,
                'metrics_summary': {},
                'timestamp': datetime.datetime.now().isoformat()
            }
        }
        
        # Assess each requirement
        for req in self.requirements:
            req_id = req.get('id')
            if not req_id:
                continue
            
            self.results['requirements'][req_id] = self.assess_requirement(req)
        
        # Calculate summary statistics
        if self.results['requirements']:
            # Count passing requirements
            passing_reqs = sum(1 for res in self.results['requirements'].values() 
                             if res['passing'])
            
            self.results['summary']['total_passing'] = passing_reqs
            
            # Calculate average overall score
            avg_score = sum(res['overall_score'] for res in self.results['requirements'].values()) 
            avg_score /= len(self.results['requirements'])
            
            self.results['summary']['average_score'] = avg_score
            
            # Calculate metric-specific summaries
            for metric in self.metrics:
                metric_scores = [res['metrics'][metric.name]['score'] 
                                for res in self.results['requirements'].values()]
                
                self.results['summary']['metrics_summary'][metric.name] = {
                    'average_score': sum(metric_scores) / len(metric_scores),
                    'passing': sum(1 for score in metric_scores if score >= metric.threshold),
                    'threshold': metric.threshold
                }
        
        return self.results
    
    def get_quality_trends(self, history_file=None):
        """
        Calculate quality trends over time
        
        Args:
            history_file (str): Path to quality history file
            
        Returns:
            dict: Quality trends
        """
        if not history_file and 'history_file' in self.config:
            history_file = self.config['history_file']
        
        history = []
        if history_file and os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
        
        # Add current results to history
        if self.results:
            current_summary = {
                'timestamp': self.results['summary']['timestamp'],
                'average_score': self.results['summary']['average_score'],
                'total_requirements': self.results['summary']['total_requirements'],
                'total_passing': self.results['summary']['total_passing'],
                'metrics': {}
            }
            
            for metric, data in self.results['summary']['metrics_summary'].items():
                current_summary['metrics'][metric] = data['average_score']
            
            history.append(current_summary)
            
            # Save updated history
            if history_file:
                with open(history_file, 'w') as f:
                    json.dump(history, f, indent=2)
        
        # Calculate trends
        trends = {
            'overall': self._calculate_trend([entry['average_score'] for entry in history]),
            'passing_rate': self._calculate_trend([entry['total_passing'] / entry['total_requirements'] 
                                                 for entry in history]),
            'metrics': {}
        }
        
        # Calculate metric-specific trends
        for metric in self.metrics:
            metric_scores = []
            for entry in history:
                if 'metrics' in entry and metric.name in entry['metrics']:
                    metric_scores.append(entry['metrics'][metric.name])
            
            if metric_scores:
                trends['metrics'][metric.name] = self._calculate_trend(metric_scores)
        
        return trends
    
    def _calculate_trend(self, values):
        """
        Calculate trend from a series of values
        
        Args:
            values (list): List of numerical values
            
        Returns:
            dict: Trend information
        """
        if not values or len(values) < 2:
            return {'direction': 'stable', 'change': 0.0}
        
        # Calculate simple linear regression
        n = len(values)
        x = list(range(n))
        y = values
        
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
        
        if denominator == 0:
            slope = 0
        else:
            slope = numerator / denominator
        
        # Determine direction
        if abs(slope) < 0.01:
            direction = 'stable'
        elif slope > 0:
            direction = 'improving'
        else:
            direction = 'declining'
        
        # Calculate percent change from first to last
        if values[0] == 0:
            percent_change = 0
        else:
            percent_change = (values[-1] - values[0]) / values[0] * 100
        
        return {
            'direction': direction,
            'change': percent_change,
            'slope': slope,
            'current': values[-1],
            'previous': values[-2] if len(values) > 1 else values[-1]
        }
    
    def get_improvement_recommendations(self):
        """
        Generate improvement recommendations based on quality assessment
        
        Returns:
            dict: Improvement recommendations
        """
        if not self.results:
            return {}
        
        recommendations = {
            'overall': [],
            'by_metric': {},
            'by_requirement': {}
        }
        
        # Overall recommendations
        avg_score = self.results['summary']['average_score']
        if avg_score < 0.6:
            recommendations['overall'].append(
                "Overall quality is low. Consider comprehensive requirements review."
            )
        elif avg_score < 0.8:
            recommendations['overall'].append(
                "Overall quality is moderate. Focus on failing metrics to improve."
            )
        
        # Metric-specific recommendations
        for metric_name, data in self.results['summary']['metrics_summary'].items():
            if data['average_score'] < data['threshold']:
                recommendations['by_metric'][metric_name] = []
                
                if metric_name == "Completeness":
                    recommendations['by_metric'][metric_name].append(
                        "Many requirements are missing essential fields. "
                        "Ensure all requirements have ID, title, description, type, and priority."
                    )
                
                elif metric_name == "Clarity":
                    recommendations['by_metric'][metric_name].append(
                        "Requirements contain ambiguous language. "
                        "Avoid terms like 'adequate', 'appropriate', or 'as required'."
                    )
                
                elif metric_name == "Consistency":
                    recommendations['by_metric'][metric_name].append(
                        "Terminology is inconsistent across requirements. "
                        "Create a glossary of terms and use consistent naming."
                    )
                
                elif metric_name == "Verifiability":
                    recommendations['by_metric'][metric_name].append(
                        "Requirements are not easily verifiable. "
                        "Include specific, measurable criteria in each requirement."
                    )
                
                elif metric_name == "Traceability":
                    recommendations['by_metric'][metric_name].append(
                        "Requirements lack proper traceability links. "
                        "Ensure each requirement links to its source and related requirements."
                    )
                
                elif metric_name == "Feasibility":
                    recommendations['by_metric'][metric_name].append(
                        "Some requirements may not be technically feasible. "
                        "Review requirements with terms like 'instantaneous', 'perfect', or 'unlimited'."
                    )
        
        # Requirement-specific recommendations
        for req_id, result in self.results['requirements'].items():
            if not result['passing']:
                failing_metrics = [name for name, data in result['metrics'].items() 
                                  if not data['passing']]
                
                if failing_metrics:
                    recommendations['by_requirement'][req_id] = [
                        f"Requirement fails on metrics: {', '.join(failing_metrics)}. "
                        f"Overall score: {result['overall_score']:.2f}"
                    ]
        
        return recommendations
    
    def export_results(self, output_file=None, format='json'):
        """
        Export quality assessment results to a file
        
        Args:
            output_file (str): Path to output file
            format (str): Output format ('json' or 'csv')
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        if not self.results:
            return False
        
        if not output_file:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"quality_assessment_{timestamp}.{format}"
        
        try:
            if format.lower() == 'json':
                with open(output_file, 'w') as f:
                    json.dump(self.results, f, indent=2)
                return True
            
            elif format.lower() == 'csv':
                # Create a flattened DataFrame for CSV export
                rows = []
                
                for req_id, result in self.results['requirements'].items():
                    row = {
                        'requirement_id': req_id,
                        'overall_score': result['overall_score'],
                        'passing': result['passing']
                    }
                    
                    # Add metric-specific scores
                    for metric_name, metric_data in result['metrics'].items():
                        row[f"{metric_name}_score"] = metric_data['score']
                        row[f"{metric_name}_passing"] = metric_data['passing']
                    
                    rows.append(row)
                
                df = pd.DataFrame(rows)
                df.to_csv(output_file, index=False)
                return True
            
            else:
                print(f"Unsupported export format: {format}")
                return False
                
        except Exception as e:
            print(f"Error exporting results: {e}")
            return False


# Run as standalone module
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Requirements Quality Metrics Tool')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--requirements', help='Path to requirements file')
    parser.add_argument('--standards', help='Path to quality standards file')
    parser.add_argument('--output', help='Path to output file')
    parser.add_argument('--format', choices=['json', 'csv'], default='json',
                        help='Output format (json or csv)')
    
    args = parser.parse_args()
    
    # Create quality assessor
    assessor = QualityAssessor(args.config)
    
    # Load standards if provided
    if args.standards:
        assessor.load_quality_standards(args.standards)
    
    # Load requirements
    if assessor.load_requirements(args.requirements):
        print(f"Loaded {len(assessor.requirements)} requirements")
        
        # Assess requirements
        results = assessor.assess_all_requirements()
        print(f"Assessment complete. Overall score: {results['summary']['average_score']:.2f}")
        
        # Export results
        if assessor.export_results(args.output, args.format):
            print(f"Results exported to {args.output or 'default output file'}")
        
        # Generate recommendations
        recommendations = assessor.get_improvement_recommendations()
        if recommendations['overall']:
            print("\nOverall Recommendations:")
            for rec in recommendations['overall']:
                print(f"- {rec}")
    else:
        print("Error: Could not load requirements file")
