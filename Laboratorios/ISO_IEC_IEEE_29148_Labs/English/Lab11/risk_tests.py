#!/usr/bin/env python3
"""
Requirements Risk Management Test Suite
ISO/IEC/IEEE 29148:2011 Risk Management Testing
"""

import unittest
import json
import os
import sys
import time
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestRiskAssessment(unittest.TestCase):
    """Test cases for risk assessment functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'risk_config.json'
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
        
        # Create a RiskAssessor instance with mock data
        from risk_assessor import RiskAssessor
        self.risk_assessor = RiskAssessor(self.config_file)

    def test_risk_assessor_initialization(self):
        """Test risk assessor initialization"""
        self.assertTrue(self.risk_assessor.is_initialized)
        self.assertEqual(len(self.risk_assessor.risk_levels), len(self.config['riskManagement']['riskLevels']))
        self.assertEqual(len(self.risk_assessor.risk_categories), len(self.config['riskManagement']['riskCategories']))

    def test_risk_score_calculation(self):
        """Test risk score calculation"""
        # Test various impact and probability combinations
        test_cases = [
            {"impact": 5, "probability": 5, "expected_score": 25, "expected_level": "high"},
            {"impact": 4, "probability": 4, "expected_score": 16, "expected_level": "high"},
            {"impact": 3, "probability": 3, "expected_score": 9, "expected_level": "medium"},
            {"impact": 2, "probability": 2, "expected_score": 4, "expected_level": "low"},
            {"impact": 1, "probability": 1, "expected_score": 1, "expected_level": "very-low"}
        ]
        
        for test_case in test_cases:
            score = self.risk_assessor.calculate_risk_score(test_case["impact"], test_case["probability"])
            level = self.risk_assessor.determine_risk_level(score)
            
            self.assertEqual(score, test_case["expected_score"], 
                             f"Score for impact={test_case['impact']}, probability={test_case['probability']}")
            self.assertEqual(level, test_case["expected_level"], 
                            f"Level for score={score}")

    def test_requirement_risk_assessment(self):
        """Test assessing risk for a requirement"""
        requirement = {
            "id": "REQ-TEST-001",
            "description": "The system shall authenticate users with biometric verification.",
            "complexity": "high",
            "dependencies": ["payment gateway", "user database"],
            "stakeholder_priority": "critical"
        }
        
        risk_factors = [
            {"id": "complexity", "name": "Complexity", "weight": 1.5},
            {"id": "dependencies", "name": "External Dependencies", "weight": 1.2}
        ]
        
        assessment = self.risk_assessor.assess_requirement(requirement, risk_factors)
        
        self.assertIsNotNone(assessment)
        self.assertEqual(assessment["requirement_id"], requirement["id"])
        self.assertIn("impact", assessment)
        self.assertIn("probability", assessment)
        self.assertIn("risk_score", assessment)
        self.assertIn("risk_level", assessment)
        self.assertIn("risk_factors", assessment)
        
        # Verify risk factors are included
        self.assertTrue(any(factor["id"] == "complexity" for factor in assessment["risk_factors"]))
        self.assertTrue(any(factor["id"] == "dependencies" for factor in assessment["risk_factors"]))

    def test_risk_level_determination(self):
        """Test determining risk level from score"""
        # Extract thresholds from config
        thresholds = {level["id"]: level["scoreThreshold"] for level in self.config["riskManagement"]["riskLevels"]}
        
        # Test at threshold boundaries
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["high"]), "high")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["medium"]), "medium")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["low"]), "low")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["very-low"]), "very-low")
        
        # Test just above thresholds
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["high"] + 1), "high")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["medium"] + 1), "medium")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["low"] + 1), "low")
        
        # Test just below thresholds
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["high"] - 1), "medium")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["medium"] - 1), "low")
        self.assertEqual(self.risk_assessor.determine_risk_level(thresholds["low"] - 1), "very-low")

    def test_bulk_risk_assessment(self):
        """Test assessing risk for multiple requirements"""
        requirements = [
            {
                "id": "REQ-TEST-001",
                "description": "The system shall authenticate users with biometric verification.",
                "complexity": "high",
                "dependencies": ["payment gateway", "user database"],
                "stakeholder_priority": "critical"
            },
            {
                "id": "REQ-TEST-002",
                "description": "The system shall display user profiles.",
                "complexity": "low",
                "dependencies": ["user database"],
                "stakeholder_priority": "medium"
            },
            {
                "id": "REQ-TEST-003",
                "description": "The system shall generate reports in PDF format.",
                "complexity": "medium",
                "dependencies": ["reporting engine"],
                "stakeholder_priority": "high"
            }
        ]
        
        assessments = self.risk_assessor.assess_requirements(requirements)
        
        self.assertEqual(len(assessments), len(requirements))
        
        # Verify assessments contain expected fields
        for assessment in assessments:
            self.assertIn("requirement_id", assessment)
            self.assertIn("impact", assessment)
            self.assertIn("probability", assessment)
            self.assertIn("risk_score", assessment)
            self.assertIn("risk_level", assessment)
            self.assertIn("risk_factors", assessment)
        
        # Check requirement IDs match
        req_ids = [req["id"] for req in requirements]
        assessment_req_ids = [assessment["requirement_id"] for assessment in assessments]
        self.assertEqual(set(req_ids), set(assessment_req_ids))


class TestRiskMitigation(unittest.TestCase):
    """Test cases for risk mitigation functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'risk_config.json'
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
        
        # Create a RiskMitigation instance with mock data
        from risk_mitigation import RiskMitigation
        self.risk_mitigation = RiskMitigation(self.config_file)

    def test_mitigation_initialization(self):
        """Test mitigation initialization"""
        self.assertTrue(self.risk_mitigation.is_initialized)
        self.assertEqual(len(self.risk_mitigation.strategies), len(self.config["riskManagement"]["mitigationStrategies"]))
        self.assertEqual(len(self.risk_mitigation.statuses), len(self.config["riskManagement"]["mitigationStatuses"]))

    def test_create_mitigation_action(self):
        """Test creating a mitigation action"""
        action_data = {
            "related_risk": "REQ-TEST-001",
            "description": "Implement third-party biometric authentication library",
            "strategy": "mitigate",
            "owner": "John Smith",
            "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        }
        
        action = self.risk_mitigation.create_action(action_data)
        
        self.assertIsNotNone(action)
        self.assertIn("id", action)
        self.assertEqual(action["related_risk"], action_data["related_risk"])
        self.assertEqual(action["description"], action_data["description"])
        self.assertEqual(action["strategy"], action_data["strategy"])
        self.assertEqual(action["owner"], action_data["owner"])
        self.assertEqual(action["due_date"], action_data["due_date"])
        self.assertEqual(action["status"], "open")  # Default status should be open

    def test_update_mitigation_action(self):
        """Test updating a mitigation action"""
        # First create an action
        action_data = {
            "related_risk": "REQ-TEST-001",
            "description": "Implement third-party biometric authentication library",
            "strategy": "mitigate",
            "owner": "John Smith",
            "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        }
        
        action = self.risk_mitigation.create_action(action_data)
        action_id = action["id"]
        
        # Now update it
        update_data = {
            "status": "in-progress",
            "owner": "Jane Doe",
            "description": "Implement third-party biometric authentication library with additional security measures"
        }
        
        updated_action = self.risk_mitigation.update_action(action_id, update_data)
        
        self.assertEqual(updated_action["id"], action_id)
        self.assertEqual(updated_action["status"], update_data["status"])
        self.assertEqual(updated_action["owner"], update_data["owner"])
        self.assertEqual(updated_action["description"], update_data["description"])
        
        # Verify other fields remain unchanged
        self.assertEqual(updated_action["related_risk"], action["related_risk"])
        self.assertEqual(updated_action["strategy"], action["strategy"])
        self.assertEqual(updated_action["due_date"], action["due_date"])

    def test_get_actions_by_risk(self):
        """Test getting mitigation actions for a specific risk"""
        # Create multiple actions for the same risk
        risk_id = "REQ-TEST-002"
        
        action_data_1 = {
            "related_risk": risk_id,
            "description": "Action 1",
            "strategy": "mitigate",
            "owner": "John Smith",
            "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        }
        
        action_data_2 = {
            "related_risk": risk_id,
            "description": "Action 2",
            "strategy": "transfer",
            "owner": "Jane Doe",
            "due_date": (datetime.now() + timedelta(days=45)).strftime("%Y-%m-%d")
        }
        
        # Create some actions for a different risk
        other_action = {
            "related_risk": "REQ-TEST-003",
            "description": "Other Action",
            "strategy": "avoid",
            "owner": "Mike Johnson",
            "due_date": (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")
        }
        
        self.risk_mitigation.create_action(action_data_1)
        self.risk_mitigation.create_action(action_data_2)
        self.risk_mitigation.create_action(other_action)
        
        # Get actions for the specific risk
        actions = self.risk_mitigation.get_actions_by_risk(risk_id)
        
        self.assertEqual(len(actions), 2)
        self.assertTrue(all(action["related_risk"] == risk_id for action in actions))
        
        # Verify descriptions match
        descriptions = [action["description"] for action in actions]
        self.assertIn("Action 1", descriptions)
        self.assertIn("Action 2", descriptions)

    def test_get_overdue_actions(self):
        """Test getting overdue mitigation actions"""
        # Create some actions with different due dates
        past_due = {
            "related_risk": "REQ-TEST-001",
            "description": "Overdue Action",
            "strategy": "mitigate",
            "owner": "John Smith",
            "due_date": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        }
        
        future_due = {
            "related_risk": "REQ-TEST-002",
            "description": "Future Action",
            "strategy": "mitigate",
            "owner": "Jane Doe",
            "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        }
        
        self.risk_mitigation.create_action(past_due)
        self.risk_mitigation.create_action(future_due)
        
        # Get overdue actions
        overdue_actions = self.risk_mitigation.get_overdue_actions()
        
        self.assertEqual(len(overdue_actions), 1)
        self.assertEqual(overdue_actions[0]["description"], "Overdue Action")
        
        # Mark overdue action as completed
        self.risk_mitigation.update_action(overdue_actions[0]["id"], {"status": "completed"})
        
        # Check that completed actions are not included in overdue list
        updated_overdue = self.risk_mitigation.get_overdue_actions()
        self.assertEqual(len(updated_overdue), 0)


class TestRiskReporting(unittest.TestCase):
    """Test cases for risk reporting functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'risk_config.json'
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
        
        # Create a RiskReporting instance with mock data
        from risk_reporting import RiskReporting
        self.risk_reporting = RiskReporting(self.config_file)

    def test_reporting_initialization(self):
        """Test reporting initialization"""
        self.assertTrue(self.risk_reporting.is_initialized)
        self.assertEqual(len(self.risk_reporting.report_templates), len(self.config["reporting"]["templates"]))
        self.assertEqual(len(self.risk_reporting.scheduled_reports), len(self.config["reporting"]["scheduledReports"]))

    def test_generate_summary_report(self):
        """Test generating a summary report"""
        # Create test data
        test_data = {
            "risk_counts": {
                "total": 24,
                "high": 6,
                "medium": 10,
                "low": 8,
                "very-low": 0
            },
            "risk_trends": {
                "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
                "high": [8, 7, 6, 6],
                "medium": [9, 9, 10, 10],
                "low": [7, 8, 8, 8]
            },
            "high_risks": [
                {
                    "id": "REQ-001",
                    "description": "The system shall authenticate users with multi-factor authentication.",
                    "risk_level": "high",
                    "risk_score": 15,
                    "impact": 5,
                    "probability": 3
                },
                {
                    "id": "REQ-002",
                    "description": "The system shall process payments within 3 seconds.",
                    "risk_level": "high",
                    "risk_score": 16,
                    "impact": 4,
                    "probability": 4
                }
            ]
        }
        
        report = self.risk_reporting.generate_report("summary", test_data)
        
        self.assertIsNotNone(report)
        self.assertIn("title", report)
        self.assertIn("generated_at", report)
        self.assertIn("sections", report)
        
        # Verify sections exist
        section_titles = [section["title"] for section in report["sections"]]
        self.assertIn("Risk Overview", section_titles)
        self.assertIn("Risk Trends", section_titles)
        self.assertIn("High Risk Requirements", section_titles)
        
        # Verify risk counts in overview section
        overview_section = next(section for section in report["sections"] if section["title"] == "Risk Overview")
        self.assertEqual(overview_section["data"]["total"], test_data["risk_counts"]["total"])
        self.assertEqual(overview_section["data"]["high"], test_data["risk_counts"]["high"])
        
        # Verify high risks section
        high_risks_section = next(section for section in report["sections"] if section["title"] == "High Risk Requirements")
        self.assertEqual(len(high_risks_section["data"]["risks"]), len(test_data["high_risks"]))

    def test_export_report(self):
        """Test exporting a report in different formats"""
        # Create a simple report
        report_data = {
            "title": "Risk Summary Report",
            "generated_at": datetime.now().isoformat(),
            "sections": [
                {
                    "title": "Risk Overview",
                    "data": {
                        "total": 24,
                        "high": 6,
                        "medium": 10,
                        "low": 8
                    }
                }
            ]
        }
        
        # Test JSON export
        json_export = self.risk_reporting.export_report(report_data, "json")
        self.assertIsNotNone(json_export)
        parsed_json = json.loads(json_export)
        self.assertEqual(parsed_json["title"], report_data["title"])
        
        # Test CSV export
        csv_export = self.risk_reporting.export_report(report_data, "csv")
        self.assertIsNotNone(csv_export)
        self.assertIn("Risk Overview", csv_export)
        
        # Test HTML export
        html_export = self.risk_reporting.export_report(report_data, "html")
        self.assertIsNotNone(html_export)
        self.assertIn("<html", html_export.lower())
        self.assertIn("risk summary report", html_export.lower())

    def test_schedule_report(self):
        """Test scheduling a report"""
        schedule_data = {
            "name": "Test Weekly Report",
            "template": "summary",
            "frequency": "weekly",
            "day": "monday",
            "recipients": ["test@example.com"],
            "format": "pdf"
        }
        
        result = self.risk_reporting.schedule_report(schedule_data)
        
        self.assertTrue(result)
        self.assertEqual(len(self.risk_reporting.scheduled_reports), len(self.config["reporting"]["scheduledReports"]) + 1)
        
        # Verify new schedule is in the list
        new_schedule = next((s for s in self.risk_reporting.scheduled_reports if s["name"] == schedule_data["name"]), None)
        self.assertIsNotNone(new_schedule)
        self.assertEqual(new_schedule["frequency"], schedule_data["frequency"])
        self.assertEqual(new_schedule["day"], schedule_data["day"])
        
        # Test getting due reports
        due_reports = self.risk_reporting.get_due_reports()
        self.assertIsNotNone(due_reports)


class TestIntegration(unittest.TestCase):
    """Integration test cases"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'risk_config.json'
        
        # Create instances of all modules
        from risk_assessor import RiskAssessor
        from risk_mitigation import RiskMitigation
        from risk_reporting import RiskReporting
        
        self.risk_assessor = RiskAssessor(self.config_file)
        self.risk_mitigation = RiskMitigation(self.config_file)
        self.risk_reporting = RiskReporting(self.config_file)

    def test_end_to_end_flow(self):
        """Test end-to-end risk management flow"""
        # 1. Assess risk for a requirement
        requirement = {
            "id": "REQ-TEST-001",
            "description": "The system shall authenticate users with biometric verification.",
            "complexity": "high",
            "dependencies": ["payment gateway", "user database"],
            "stakeholder_priority": "critical"
        }
        
        assessment = self.risk_assessor.assess_requirement(requirement)
        
        # 2. Create mitigation actions based on assessment
        action_data = {
            "related_risk": assessment["requirement_id"],
            "description": f"Mitigate {assessment['risk_level']} risk: Implement third-party biometric library",
            "strategy": "mitigate",
            "owner": "John Smith",
            "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        }
        
        action = self.risk_mitigation.create_action(action_data)
        
        # 3. Generate a report including the assessment and action
        report_data = {
            "risk_counts": {
                "total": 1,
                "high": 1 if assessment["risk_level"] == "high" else 0,
                "medium": 1 if assessment["risk_level"] == "medium" else 0,
                "low": 1 if assessment["risk_level"] == "low" else 0,
                "very-low": 1 if assessment["risk_level"] == "very-low" else 0
            },
            "requirements": [
                {
                    "id": requirement["id"],
                    "description": requirement["description"],
                    "risk_level": assessment["risk_level"],
                    "risk_score": assessment["risk_score"],
                    "impact": assessment["impact"],
                    "probability": assessment["probability"]
                }
            ],
            "actions": [action]
        }
        
        report = self.risk_reporting.generate_report("detailed", report_data)
        
        # Verify the report contains the requirement and action
        req_section = next((s for s in report["sections"] if "Requirements" in s["title"]), None)
        self.assertIsNotNone(req_section)
        self.assertEqual(len(req_section["data"]["requirements"]), 1)
        self.assertEqual(req_section["data"]["requirements"][0]["id"], requirement["id"])
        
        actions_section = next((s for s in report["sections"] if "Actions" in s["title"]), None)
        self.assertIsNotNone(actions_section)
        self.assertEqual(len(actions_section["data"]["actions"]), 1)
        self.assertEqual(actions_section["data"]["actions"][0]["id"], action["id"])


def run_all_tests():
    """Run all test cases"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRiskAssessment))
    test_suite.addTest(unittest.makeSuite(TestRiskMitigation))
    test_suite.addTest(unittest.makeSuite(TestRiskReporting))
    test_suite.addTest(unittest.makeSuite(TestIntegration))
    
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(test_suite)


if __name__ == '__main__':
    run_all_tests()
