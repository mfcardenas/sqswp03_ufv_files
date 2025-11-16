#!/usr/bin/env python3
"""
Requirements Risk Assessor Module
ISO/IEC/IEEE 29148:2011 Risk Assessment Implementation
"""

import json
import os
import sys
import logging
import random
from datetime import datetime
from typing import List, Dict, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("risk_assessor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RiskAssessor:
    """Main class for risk assessment"""
    
    def __init__(self, config_file: str):
        """
        Initialize risk assessor
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.risk_levels = []
        self.risk_categories = []
        self.risk_factors = []
        self.impact_levels = []
        self.probability_levels = []
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the risk assessor"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            # Load configuration data
            self.risk_levels = self.config["riskManagement"]["riskLevels"]
            self.risk_categories = self.config["riskManagement"]["riskCategories"]
            self.risk_factors = self.config["riskManagement"]["riskFactors"]
            self.impact_levels = self.config["riskManagement"]["riskMatrix"]["impactLevels"]
            self.probability_levels = self.config["riskManagement"]["riskMatrix"]["probabilityLevels"]
            
            self.is_initialized = True
            logger.info("Risk assessor initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize risk assessor: {str(e)}")
            self.is_initialized = False
    
    def calculate_risk_score(self, impact: int, probability: int) -> int:
        """
        Calculate risk score based on impact and probability
        
        Args:
            impact: Impact level (1-5)
            probability: Probability level (1-5)
            
        Returns:
            int: Risk score
        """
        # Simple multiplication for risk score
        return impact * probability
    
    def determine_risk_level(self, score: int) -> str:
        """
        Determine risk level based on score
        
        Args:
            score: Risk score
            
        Returns:
            str: Risk level ID (high, medium, low, very-low)
        """
        # Find the appropriate risk level based on score thresholds
        for level in sorted(self.risk_levels, key=lambda x: x["scoreThreshold"], reverse=True):
            if score >= level["scoreThreshold"]:
                return level["id"]
        
        # Default to lowest level if no match found
        return self.risk_levels[-1]["id"]
    
    def assess_requirement(self, requirement: Dict[str, Any], risk_factors: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Assess risk for a single requirement
        
        Args:
            requirement: Requirement data
            risk_factors: Optional list of risk factors to consider
            
        Returns:
            Dict[str, Any]: Risk assessment result
        """
        if not risk_factors:
            risk_factors = self.risk_factors
        
        # Extract relevant requirement data for assessment
        req_id = requirement.get("id", "unknown")
        logger.info(f"Assessing risk for requirement {req_id}")
        
        # Analyze requirement to determine impact and probability
        impact = self._analyze_impact(requirement)
        probability = self._analyze_probability(requirement, risk_factors)
        
        # Calculate risk score and level
        risk_score = self.calculate_risk_score(impact, probability)
        risk_level = self.determine_risk_level(risk_score)
        
        # Identify specific risk factors for this requirement
        identified_factors = self._identify_risk_factors(requirement, risk_factors)
        
        # Create assessment result
        assessment = {
            "requirement_id": req_id,
            "impact": impact,
            "probability": probability,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "risk_factors": identified_factors,
            "assessment_date": datetime.now().isoformat(),
            "notes": self._generate_assessment_notes(requirement, risk_level, identified_factors)
        }
        
        logger.info(f"Risk assessment for {req_id}: Level={risk_level}, Score={risk_score}")
        return assessment
    
    def assess_requirements(self, requirements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Assess risk for multiple requirements
        
        Args:
            requirements: List of requirements to assess
            
        Returns:
            List[Dict[str, Any]]: List of risk assessment results
        """
        assessments = []
        
        for req in requirements:
            assessment = self.assess_requirement(req)
            assessments.append(assessment)
        
        return assessments
    
    def _analyze_impact(self, requirement: Dict[str, Any]) -> int:
        """
        Analyze requirement to determine impact level
        
        Args:
            requirement: Requirement data
            
        Returns:
            int: Impact level (1-5)
        """
        # In a real implementation, this would use NLP or rules to determine impact
        # For this lab, we'll use a simplified approach
        
        # Check for high impact indicators
        high_impact_keywords = ["critical", "essential", "mandatory", "security", "safety", "compliance"]
        req_text = requirement.get("description", "").lower()
        
        impact_score = 3  # Default to medium impact
        
        # Check for high priority requirements
        if requirement.get("stakeholder_priority", "").lower() in ["critical", "high"]:
            impact_score += 1
        
        # Check for high impact keywords
        if any(keyword in req_text for keyword in high_impact_keywords):
            impact_score += 1
        
        # Check for requirements with many dependencies
        dependencies = requirement.get("dependencies", [])
        if len(dependencies) >= 3:
            impact_score += 1
        
        # Ensure impact is within 1-5 range
        return max(1, min(5, impact_score))
    
    def _analyze_probability(self, requirement: Dict[str, Any], risk_factors: List[Dict[str, Any]]) -> int:
        """
        Analyze requirement to determine probability level
        
        Args:
            requirement: Requirement data
            risk_factors: List of risk factors to consider
            
        Returns:
            int: Probability level (1-5)
        """
        # In a real implementation, this would use more sophisticated analysis
        # For this lab, we'll use a simplified approach
        
        probability_score = 2  # Default to low probability
        
        # Check for complexity
        complexity = requirement.get("complexity", "").lower()
        if complexity == "high":
            probability_score += 2
        elif complexity == "medium":
            probability_score += 1
        
        # Check for external dependencies
        dependencies = requirement.get("dependencies", [])
        external_deps = [dep for dep in dependencies if "external" in dep or "third-party" in dep]
        if external_deps:
            probability_score += 1
        
        # Check for new technologies or approaches
        req_text = requirement.get("description", "").lower()
        novelty_keywords = ["new", "novel", "innovative", "first time", "experimental"]
        if any(keyword in req_text for keyword in novelty_keywords):
            probability_score += 1
        
        # Ensure probability is within 1-5 range
        return max(1, min(5, probability_score))
    
    def _identify_risk_factors(self, requirement: Dict[str, Any], risk_factors: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Identify specific risk factors for a requirement
        
        Args:
            requirement: Requirement data
            risk_factors: List of risk factors to consider
            
        Returns:
            List[Dict[str, Any]]: List of identified risk factors
        """
        identified_factors = []
        req_text = requirement.get("description", "").lower()
        
        for factor in risk_factors:
            factor_id = factor["id"]
            
            # Check for complexity factor
            if factor_id == "complexity" and requirement.get("complexity", "").lower() in ["high", "medium"]:
                identified_factors.append({
                    "id": factor_id,
                    "name": factor["name"],
                    "weight": factor["weight"],
                    "evidence": f"Requirement has {requirement.get('complexity', '').lower()} complexity"
                })
            
            # Check for dependencies factor
            elif factor_id == "dependencies" and requirement.get("dependencies", []):
                identified_factors.append({
                    "id": factor_id,
                    "name": factor["name"],
                    "weight": factor["weight"],
                    "evidence": f"Requirement has {len(requirement.get('dependencies', []))} dependencies"
                })
            
            # Check for novelty factor
            elif factor_id == "novelty":
                novelty_keywords = ["new", "novel", "innovative", "first time", "experimental"]
                if any(keyword in req_text for keyword in novelty_keywords):
                    identified_factors.append({
                        "id": factor_id,
                        "name": factor["name"],
                        "weight": factor["weight"],
                        "evidence": "Requirement involves new or novel approach"
                    })
            
            # Check for resources factor
            elif factor_id == "resources" and "resource" in req_text:
                identified_factors.append({
                    "id": factor_id,
                    "name": factor["name"],
                    "weight": factor["weight"],
                    "evidence": "Requirement has resource constraints or dependencies"
                })
            
            # Check for timeline factor
            elif factor_id == "timeline" and requirement.get("timeline_constraint", False):
                identified_factors.append({
                    "id": factor_id,
                    "name": factor["name"],
                    "weight": factor["weight"],
                    "evidence": "Requirement has timeline constraints"
                })
        
        return identified_factors
    
    def _generate_assessment_notes(self, requirement: Dict[str, Any], risk_level: str, risk_factors: List[Dict[str, Any]]) -> str:
        """
        Generate assessment notes
        
        Args:
            requirement: Requirement data
            risk_level: Risk level
            risk_factors: Identified risk factors
            
        Returns:
            str: Assessment notes
        """
        notes = f"Requirement assessed as {risk_level} risk. "
        
        if risk_factors:
            notes += f"Key risk factors: {', '.join(f['name'] for f in risk_factors)}. "
        
        if risk_level in ["high", "medium"]:
            notes += "Consider implementing risk mitigation measures. "
        
        return notes
    
    def get_risk_metrics(self, assessments: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate risk metrics from a list of assessments
        
        Args:
            assessments: List of risk assessments
            
        Returns:
            Dict[str, Any]: Risk metrics
        """
        total = len(assessments)
        
        if total == 0:
            return {
                "total": 0,
                "high": 0,
                "medium": 0,
                "low": 0,
                "very-low": 0,
                "high_percentage": 0,
                "medium_percentage": 0,
                "low_percentage": 0,
                "very_low_percentage": 0,
                "average_score": 0
            }
        
        # Count assessments by risk level
        high = sum(1 for a in assessments if a["risk_level"] == "high")
        medium = sum(1 for a in assessments if a["risk_level"] == "medium")
        low = sum(1 for a in assessments if a["risk_level"] == "low")
        very_low = sum(1 for a in assessments if a["risk_level"] == "very-low")
        
        # Calculate percentages
        high_percentage = (high / total) * 100
        medium_percentage = (medium / total) * 100
        low_percentage = (low / total) * 100
        very_low_percentage = (very_low / total) * 100
        
        # Calculate average score
        average_score = sum(a["risk_score"] for a in assessments) / total
        
        return {
            "total": total,
            "high": high,
            "medium": medium,
            "low": low,
            "very-low": very_low,
            "high_percentage": high_percentage,
            "medium_percentage": medium_percentage,
            "low_percentage": low_percentage,
            "very_low_percentage": very_low_percentage,
            "average_score": average_score
        }


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python risk_assessor.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    assessor = RiskAssessor(config_file)
    
    if not assessor.is_initialized:
        print("Failed to initialize risk assessor")
        sys.exit(1)
    
    print("Risk assessor initialized successfully.")
    
    # Example usage
    test_requirement = {
        "id": "REQ-TEST-001",
        "description": "The system shall authenticate users with biometric verification.",
        "complexity": "high",
        "dependencies": ["payment gateway", "user database"],
        "stakeholder_priority": "critical"
    }
    
    assessment = assessor.assess_requirement(test_requirement)
    
    print(f"Risk assessment for {test_requirement['id']}:")
    print(f"  Risk Level: {assessment['risk_level']}")
    print(f"  Risk Score: {assessment['risk_score']}")
    print(f"  Impact: {assessment['impact']}")
    print(f"  Probability: {assessment['probability']}")
    print(f"  Notes: {assessment['notes']}")
