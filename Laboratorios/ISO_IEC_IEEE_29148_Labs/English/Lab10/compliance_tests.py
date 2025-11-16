#!/usr/bin/env python3
"""
Requirements Compliance & Audit Test Suite
ISO/IEC/IEEE 29148:2011 Compliance Testing
"""

import unittest
import json
import os
import sys
import time
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
import hashlib

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestComplianceMonitor(unittest.TestCase):
    """Test cases for compliance monitoring functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'compliance_config.json'
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def test_compliance_monitor_initialization(self):
        """Test compliance monitor initialization"""
        from compliance_monitor import ComplianceMonitor

        monitor = ComplianceMonitor(self.config_file)
        self.assertTrue(monitor.is_initialized)
        self.assertEqual(len(monitor.rules), len(self.get_total_rules()))

    def test_rule_loading(self):
        """Test loading compliance rules from config"""
        from compliance_monitor import ComplianceMonitor

        monitor = ComplianceMonitor(self.config_file)
        monitor.load_rules()

        # Check if all rules from config are loaded
        expected_rule_count = self.get_total_rules()
        self.assertEqual(len(monitor.rules), len(expected_rule_count))

        # Check if rule attributes are properly loaded
        for standard in self.config['compliance']['standards']:
            for rule in self.config['compliance']['standards'][standard]['rules']:
                rule_id = rule['id']
                self.assertIn(rule_id, [r.id for r in monitor.rules])

    def test_compliance_check_single_rule(self):
        """Test checking compliance for a single rule"""
        from compliance_monitor import ComplianceMonitor, ComplianceStatus

        monitor = ComplianceMonitor(self.config_file)
        requirement = {
            'id': 'REQ-001',
            'text': 'The system shall authenticate users before granting access.'
        }

        # Test a rule that should pass
        result = monitor.check_rule('CR-001', requirement)
        self.assertEqual(result.status, ComplianceStatus.COMPLIANT)

        # Test a rule that should fail
        requirement = {
            'text': 'The system should authenticate users and also allow guest access and provide admin functionality.'
        }
        result = monitor.check_rule('CR-002', requirement)
        self.assertEqual(result.status, ComplianceStatus.NON_COMPLIANT)

    def test_compliance_check_all_rules(self):
        """Test checking compliance for all rules"""
        from compliance_monitor import ComplianceMonitor

        monitor = ComplianceMonitor(self.config_file)
        requirements = [
            {
                'id': 'REQ-001',
                'text': 'The system shall authenticate users before granting access.'
            },
            {
                'id': 'REQ-002',
                'text': 'The system shall encrypt all stored passwords.'
            }
        ]

        results = monitor.check_compliance(requirements)
        self.assertTrue(len(results) > 0)
        self.assertTrue(any(r.status == 'compliant' for r in results))

    def test_compliance_report_generation(self):
        """Test generating compliance report"""
        from compliance_monitor import ComplianceMonitor

        monitor = ComplianceMonitor(self.config_file)
        requirements = [
            {
                'id': 'REQ-001',
                'text': 'The system shall authenticate users before granting access.'
            },
            {
                'id': 'REQ-002',
                'text': 'The system shall encrypt all stored passwords.'
            }
        ]

        results = monitor.check_compliance(requirements)
        report = monitor.generate_report(results)

        self.assertIn('summary', report)
        self.assertIn('details', report)
        self.assertIn('compliance_score', report['summary'])
        self.assertTrue(len(report['details']) > 0)

    def get_total_rules(self):
        """Helper method to count total rules in config"""
        rules = []
        for standard in self.config['compliance']['standards']:
            for rule in self.config['compliance']['standards'][standard]['rules']:
                rules.append(rule['id'])
        return rules


class TestAuditTrail(unittest.TestCase):
    """Test cases for audit trail functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'compliance_config.json'
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def test_audit_trail_initialization(self):
        """Test audit trail initialization"""
        from audit_trail import AuditTrail

        audit = AuditTrail(self.config_file)
        self.assertTrue(audit.is_initialized)
        self.assertEqual(audit.retention_period, self.config['audit']['retention_period_days'])
        self.assertEqual(audit.encryption_enabled, self.config['audit']['encryption']['enabled'])

    def test_log_entry_creation(self):
        """Test creating audit log entries"""
        from audit_trail import AuditTrail, AuditEvent

        audit = AuditTrail(self.config_file)
        entry = audit.log_event(
            user_id='user123',
            action='create',
            object_type='requirement',
            object_id='REQ-001',
            details='Created new requirement'
        )

        self.assertEqual(entry.user_id, 'user123')
        self.assertEqual(entry.action, 'create')
        self.assertEqual(entry.object_type, 'requirement')
        self.assertEqual(entry.object_id, 'REQ-001')
        self.assertEqual(entry.details, 'Created new requirement')
        self.assertIsNotNone(entry.timestamp)
        self.assertIsNotNone(entry.entry_id)

    def test_audit_log_retrieval(self):
        """Test retrieving audit logs"""
        from audit_trail import AuditTrail

        audit = AuditTrail(self.config_file)
        # Add some log entries
        for i in range(5):
            audit.log_event(
                user_id=f'user{i}',
                action='create',
                object_type='requirement',
                object_id=f'REQ-00{i}',
                details=f'Created requirement {i}'
            )

        # Test retrieval
        logs = audit.get_logs()
        self.assertEqual(len(logs), 5)

        # Test filtering by user
        logs = audit.get_logs(user_id='user1')
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].user_id, 'user1')

        # Test filtering by action
        logs = audit.get_logs(action='create')
        self.assertEqual(len(logs), 5)

        # Test filtering by object type
        logs = audit.get_logs(object_type='requirement')
        self.assertEqual(len(logs), 5)

        # Test filtering by date range
        yesterday = datetime.now() - timedelta(days=1)
        logs = audit.get_logs(start_date=yesterday)
        self.assertEqual(len(logs), 5)

        future = datetime.now() + timedelta(days=1)
        logs = audit.get_logs(end_date=future)
        self.assertEqual(len(logs), 5)

    def test_tamper_proof_logs(self):
        """Test tamper-proof log mechanism"""
        from audit_trail import AuditTrail

        audit = AuditTrail(self.config_file)
        # Add some log entries
        for i in range(3):
            audit.log_event(
                user_id=f'user{i}',
                action='create',
                object_type='requirement',
                object_id=f'REQ-00{i}',
                details=f'Created requirement {i}'
            )

        # Verify hash chain
        self.assertTrue(audit.verify_log_integrity())

        # Tamper with a log entry
        audit.logs[1].details = "Tampered details"

        # Verification should fail
        self.assertFalse(audit.verify_log_integrity())

    def test_log_export(self):
        """Test exporting audit logs"""
        from audit_trail import AuditTrail

        audit = AuditTrail(self.config_file)
        # Add some log entries
        for i in range(5):
            audit.log_event(
                user_id=f'user{i}',
                action='create',
                object_type='requirement',
                object_id=f'REQ-00{i}',
                details=f'Created requirement {i}'
            )

        # Export logs
        export_data = audit.export_logs(format='json')
        self.assertIsNotNone(export_data)
        self.assertTrue(len(export_data) > 0)

        # Check that exported data can be parsed
        parsed_data = json.loads(export_data)
        self.assertEqual(len(parsed_data), 5)


class TestRegulatoryReporting(unittest.TestCase):
    """Test cases for regulatory reporting functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'compliance_config.json'
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def test_report_engine_initialization(self):
        """Test report engine initialization"""
        from regulatory_reporting import ReportEngine

        engine = ReportEngine(self.config_file)
        self.assertTrue(engine.is_initialized)
        self.assertEqual(len(engine.report_types), len(self.config['reporting']['report_types']))
        self.assertEqual(len(engine.formats), len(self.config['reporting']['formats']))

    def test_report_generation(self):
        """Test generating regulatory reports"""
        from regulatory_reporting import ReportEngine

        engine = ReportEngine(self.config_file)
        
        # Create test data
        compliance_data = {
            'rules': [
                {
                    'id': 'CR-001',
                    'standard': 'iso29148',
                    'description': 'Requirements must have unique identifiers',
                    'status': 'compliant',
                    'severity': 'high'
                },
                {
                    'id': 'CR-002',
                    'standard': 'iso29148',
                    'description': 'Requirements must be atomic',
                    'status': 'non-compliant',
                    'severity': 'critical'
                }
            ],
            'summary': {
                'total_rules': 2,
                'compliant_rules': 1,
                'non_compliant_rules': 1,
                'compliance_score': 50
            }
        }
        
        # Generate summary report
        report = engine.generate_report(
            report_type='compliance_summary',
            standard='iso29148',
            data=compliance_data,
            format='json'
        )
        
        self.assertIsNotNone(report)
        self.assertTrue(len(report) > 0)
        
        # Parse report data
        report_data = json.loads(report)
        self.assertIn('summary', report_data)
        self.assertIn('compliance_score', report_data['summary'])
        self.assertEqual(report_data['summary']['compliance_score'], 50)

    def test_report_scheduling(self):
        """Test report scheduling functionality"""
        from regulatory_reporting import ReportEngine

        engine = ReportEngine(self.config_file)
        
        # Check scheduled reports
        schedules = engine.get_scheduled_reports()
        self.assertEqual(len(schedules), len(self.config['reporting']['scheduled_reports']['schedules']))
        
        # Schedule a new report
        new_schedule = {
            'report_type': 'non_compliance',
            'frequency': 'weekly',
            'day': 'friday',
            'time': '16:00',
            'recipients': ['test@example.com']
        }
        
        engine.schedule_report(new_schedule)
        
        # Check updated schedules
        updated_schedules = engine.get_scheduled_reports()
        self.assertEqual(len(updated_schedules), len(schedules) + 1)


class TestIntegration(unittest.TestCase):
    """Integration test cases"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'compliance_config.json'

    def test_compliance_audit_integration(self):
        """Test integration between compliance checking and audit logging"""
        from compliance_monitor import ComplianceMonitor
        from audit_trail import AuditTrail

        monitor = ComplianceMonitor(self.config_file)
        audit = AuditTrail(self.config_file)
        
        # Create a requirement
        requirement = {
            'id': 'REQ-TEST-001',
            'text': 'The system shall provide secure authentication.'
        }
        
        # Check compliance
        results = monitor.check_compliance([requirement])
        
        # Log the compliance check in the audit trail
        audit.log_event(
            user_id='testuser',
            action='check',
            object_type='requirement',
            object_id=requirement['id'],
            details=f'Performed compliance check on requirement {requirement["id"]}'
        )
        
        # Verify the audit log contains the entry
        logs = audit.get_logs(object_id=requirement['id'])
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].action, 'check')

    def test_reporting_audit_integration(self):
        """Test integration between reporting and audit logging"""
        from regulatory_reporting import ReportEngine
        from audit_trail import AuditTrail

        engine = ReportEngine(self.config_file)
        audit = AuditTrail(self.config_file)
        
        # Create test data
        compliance_data = {
            'rules': [
                {
                    'id': 'CR-001',
                    'standard': 'iso29148',
                    'description': 'Requirements must have unique identifiers',
                    'status': 'compliant',
                    'severity': 'high'
                }
            ],
            'summary': {
                'total_rules': 1,
                'compliant_rules': 1,
                'non_compliant_rules': 0,
                'compliance_score': 100
            }
        }
        
        # Generate report
        report_id = 'RPT-TEST-001'
        report = engine.generate_report(
            report_type='compliance_summary',
            standard='iso29148',
            data=compliance_data,
            format='json',
            report_id=report_id
        )
        
        # Log report generation in audit trail
        audit.log_event(
            user_id='testuser',
            action='generate',
            object_type='report',
            object_id=report_id,
            details=f'Generated compliance summary report {report_id}'
        )
        
        # Verify the audit log contains the entry
        logs = audit.get_logs(object_id=report_id)
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].action, 'generate')


class TestPerformance(unittest.TestCase):
    """Performance test cases"""

    def setUp(self):
        """Set up test fixtures"""
        self.config_file = 'compliance_config.json'

    def test_compliance_check_performance(self):
        """Test performance of compliance checking"""
        from compliance_monitor import ComplianceMonitor
        import time

        monitor = ComplianceMonitor(self.config_file)
        
        # Create a large set of requirements
        requirements = []
        for i in range(100):
            requirements.append({
                'id': f'REQ-PERF-{i:03d}',
                'text': f'The system shall provide feature {i}.'
            })
        
        # Measure time to check compliance
        start_time = time.time()
        results = monitor.check_compliance(requirements)
        end_time = time.time()
        
        # Compliance check should be under 1 second for 100 requirements
        self.assertLess(end_time - start_time, 1.0)

    def test_audit_log_performance(self):
        """Test performance of audit logging"""
        from audit_trail import AuditTrail
        import time

        audit = AuditTrail(self.config_file)
        
        # Measure time to add many log entries
        start_time = time.time()
        for i in range(1000):
            audit.log_event(
                user_id=f'user{i % 10}',
                action='create',
                object_type='requirement',
                object_id=f'REQ-PERF-{i:03d}',
                details=f'Created requirement {i}'
            )
        end_time = time.time()
        
        # Adding 1000 log entries should be under 2 seconds
        self.assertLess(end_time - start_time, 2.0)
        
        # Measure time to retrieve filtered logs
        start_time = time.time()
        logs = audit.get_logs(user_id='user5')
        end_time = time.time()
        
        # Retrieving filtered logs should be under 0.5 seconds
        self.assertLess(end_time - start_time, 0.5)


def run_all_tests():
    """Run all test cases"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestComplianceMonitor))
    test_suite.addTest(unittest.makeSuite(TestAuditTrail))
    test_suite.addTest(unittest.makeSuite(TestRegulatoryReporting))
    test_suite.addTest(unittest.makeSuite(TestIntegration))
    test_suite.addTest(unittest.makeSuite(TestPerformance))
    
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(test_suite)


if __name__ == '__main__':
    run_all_tests()
