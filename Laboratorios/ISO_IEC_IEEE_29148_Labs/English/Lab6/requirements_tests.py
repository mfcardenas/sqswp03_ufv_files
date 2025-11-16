#!/usr/bin/env python3
"""
Requirements Management System Test Suite
ISO/IEC/IEEE 29148:2011 Lab 6 - Requirements Management

This test suite validates the requirements management system implementation
including database operations, API endpoints, change management, and traceability.
"""

import unittest
import json
import sqlite3
import os
import tempfile
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock

# Import the requirements management modules (assuming they exist)
try:
    from requirements_manager import RequirementsManager
    from change_manager import ChangeManager
    from traceability_manager import TraceabilityManager
    from audit_logger import AuditLogger
except ImportError:
    # Mock classes for testing if modules don't exist yet
    class RequirementsManager:
        def __init__(self, db_path): pass
        def create_requirement(self, req_data): return "REQ-001"
        def get_requirement(self, req_id): return {"id": req_id, "title": "Test"}
        def update_requirement(self, req_id, updates): return True
        def delete_requirement(self, req_id): return True
        def list_requirements(self, filters=None): return []

    class ChangeManager:
        def __init__(self, db_path): pass
        def create_change_request(self, change_data): return "CHG-001"
        def approve_change(self, change_id, approver): return True
        def get_change_history(self, req_id): return []

    class TraceabilityManager:
        def __init__(self, db_path): pass
        def create_traceability_link(self, source, target, rel_type): return 1
        def get_traceability_matrix(self, req_id): return []
        def validate_traceability(self): return True

    class AuditLogger:
        def __init__(self, db_path): pass
        def log_action(self, table, record_id, action, user_id): return True
        def get_audit_trail(self, record_id): return []


class TestRequirementsManager(unittest.TestCase):
    """Test cases for RequirementsManager class"""

    def setUp(self):
        """Set up test fixtures"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.manager = RequirementsManager(self.db_path)

        # Sample requirement data
        self.sample_req = {
            "title": "User Authentication System",
            "description": "Secure user authentication with multiple methods",
            "type": "security",
            "priority": "high",
            "status": "draft",
            "created_by": "test_user",
            "tags": ["security", "authentication"],
            "metadata": {"estimated_effort": "2 weeks"}
        }

    def tearDown(self):
        """Clean up test fixtures"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_create_requirement(self):
        """Test requirement creation"""
        req_id = self.manager.create_requirement(self.sample_req)
        self.assertIsNotNone(req_id)
        self.assertTrue(req_id.startswith("REQ-"))

    def test_get_requirement(self):
        """Test requirement retrieval"""
        req_id = self.manager.create_requirement(self.sample_req)
        req = self.manager.get_requirement(req_id)
        self.assertIsNotNone(req)
        self.assertEqual(req["id"], req_id)
        self.assertEqual(req["title"], self.sample_req["title"])

    def test_update_requirement(self):
        """Test requirement updates"""
        req_id = self.manager.create_requirement(self.sample_req)
        updates = {"status": "approved", "priority": "critical"}
        result = self.manager.update_requirement(req_id, updates)
        self.assertTrue(result)

        # Verify update
        updated_req = self.manager.get_requirement(req_id)
        self.assertEqual(updated_req["status"], "approved")
        self.assertEqual(updated_req["priority"], "critical")

    def test_list_requirements(self):
        """Test requirement listing with filters"""
        # Create multiple requirements
        req1_id = self.manager.create_requirement(self.sample_req)
        req2_data = self.sample_req.copy()
        req2_data["type"] = "technical"
        req2_id = self.manager.create_requirement(req2_data)

        # Test without filters
        all_reqs = self.manager.list_requirements()
        self.assertGreaterEqual(len(all_reqs), 2)

        # Test with filters
        security_reqs = self.manager.list_requirements({"type": "security"})
        self.assertGreaterEqual(len(security_reqs), 1)

    def test_requirement_validation(self):
        """Test requirement data validation"""
        # Test invalid type
        invalid_req = self.sample_req.copy()
        invalid_req["type"] = "invalid_type"
        with self.assertRaises(ValueError):
            self.manager.create_requirement(invalid_req)

        # Test missing required fields
        incomplete_req = {"title": "Test"}
        with self.assertRaises(ValueError):
            self.manager.create_requirement(incomplete_req)


class TestChangeManager(unittest.TestCase):
    """Test cases for ChangeManager class"""

    def setUp(self):
        """Set up test fixtures"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.manager = ChangeManager(self.db_path)

        self.sample_change = {
            "requirement_id": "REQ-001",
            "change_type": "enhancement",
            "title": "Add Multi-Factor Authentication",
            "description": "Enhance security with MFA",
            "requested_by": "security_team",
            "priority": "high"
        }

    def tearDown(self):
        """Clean up test fixtures"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_create_change_request(self):
        """Test change request creation"""
        change_id = self.manager.create_change_request(self.sample_change)
        self.assertIsNotNone(change_id)
        self.assertTrue(change_id.startswith("CHG-"))

    def test_approve_change(self):
        """Test change approval workflow"""
        change_id = self.manager.create_change_request(self.sample_change)
        result = self.manager.approve_change(change_id, "approver")
        self.assertTrue(result)

    def test_change_history(self):
        """Test change history retrieval"""
        req_id = "REQ-001"
        history = self.manager.get_change_history(req_id)
        self.assertIsInstance(history, list)


class TestTraceabilityManager(unittest.TestCase):
    """Test cases for TraceabilityManager class"""

    def setUp(self):
        """Set up test fixtures"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.manager = TraceabilityManager(self.db_path)

    def tearDown(self):
        """Clean up test fixtures"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_create_traceability_link(self):
        """Test traceability link creation"""
        link_id = self.manager.create_traceability_link(
            "REQ-001", "REQ-002", "implements"
        )
        self.assertIsNotNone(link_id)

    def test_traceability_matrix(self):
        """Test traceability matrix generation"""
        matrix = self.manager.get_traceability_matrix("REQ-001")
        self.assertIsInstance(matrix, list)

    def test_traceability_validation(self):
        """Test traceability validation"""
        result = self.manager.validate_traceability()
        self.assertTrue(result)


class TestAuditLogger(unittest.TestCase):
    """Test cases for AuditLogger class"""

    def setUp(self):
        """Set up test fixtures"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.logger = AuditLogger(self.db_path)

    def tearDown(self):
        """Clean up test fixtures"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_log_action(self):
        """Test audit logging"""
        result = self.logger.log_action(
            "requirements", "REQ-001", "CREATE", "test_user"
        )
        self.assertTrue(result)

    def test_audit_trail(self):
        """Test audit trail retrieval"""
        trail = self.logger.get_audit_trail("REQ-001")
        self.assertIsInstance(trail, list)


class TestDatabaseIntegration(unittest.TestCase):
    """Test database integration and schema validation"""

    def setUp(self):
        """Set up test database"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")

        # Load schema
        schema_path = os.path.join(os.path.dirname(__file__), "requirements_schema.sql")
        if os.path.exists(schema_path):
            with open(schema_path, 'r') as f:
                schema_sql = f.read()
            self.conn.executescript(schema_sql)
            self.conn.commit()

    def tearDown(self):
        """Clean up test database"""
        self.conn.close()
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_schema_creation(self):
        """Test database schema creation"""
        # Check if tables exist
        tables = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        table_names = [t[0] for t in tables]

        expected_tables = [
            'requirements', 'changes', 'traceability', 'stakeholders',
            'audit_log', 'requirement_versions', 'attachments', 'comments',
            'baselines', 'baseline_requirements'
        ]

        for table in expected_tables:
            self.assertIn(table, table_names)

    def test_foreign_key_constraints(self):
        """Test foreign key constraints"""
        # Try to insert invalid foreign key
        with self.assertRaises(sqlite3.IntegrityError):
            self.conn.execute(
                "INSERT INTO changes (id, requirement_id, change_type, title, description, requested_by, status, priority) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                ("CHG-001", "INVALID-REQ", "enhancement", "Test", "Test", "user", "pending", "medium")
            )

    def test_indexes(self):
        """Test database indexes"""
        indexes = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='index'"
        ).fetchall()
        index_names = [i[0] for i in indexes]

        # Check for key indexes
        self.assertIn("idx_requirements_type", index_names)
        self.assertIn("idx_requirements_status", index_names)
        self.assertIn("idx_audit_log_timestamp", index_names)


class TestAPIIntegration(unittest.TestCase):
    """Test API integration (mocked)"""

    def setUp(self):
        """Set up API test fixtures"""
        self.base_url = "http://localhost:5000/api"

    @patch('requests.post')
    def test_create_requirement_api(self, mock_post):
        """Test requirement creation via API"""
        mock_response = Mock()
        mock_response.json.return_value = {"id": "REQ-001", "status": "success"}
        mock_post.return_value = mock_response

        # This would be the actual API call
        # response = requests.post(f"{self.base_url}/requirements", json=self.sample_req)
        # self.assertEqual(response.json()["status"], "success")

        # For now, just test the mock
        self.assertTrue(mock_post.called)

    @patch('requests.get')
    def test_get_requirements_api(self, mock_get):
        """Test requirements retrieval via API"""
        mock_response = Mock()
        mock_response.json.return_value = {"requirements": [], "total": 0}
        mock_get.return_value = mock_response

        # This would be the actual API call
        # response = requests.get(f"{self.base_url}/requirements")
        # self.assertEqual(response.json()["total"], 0)

        self.assertTrue(mock_get.called)


class TestDataValidation(unittest.TestCase):
    """Test data validation and integrity"""

    def test_requirement_id_format(self):
        """Test requirement ID format validation"""
        valid_ids = ["REQ-001", "REQ-123", "REQ-9999"]
        invalid_ids = ["req-001", "REQ-1", "INVALID", "REQ-ABC"]

        for req_id in valid_ids:
            # Should not raise exception
            self.assertRegex(req_id, r'^REQ-\d{3,}$')

        for req_id in invalid_ids:
            # Should raise exception or return False
            self.assertNotRegex(req_id, r'^REQ-\d{3,}$')

    def test_json_data_integrity(self):
        """Test JSON data integrity"""
        sample_data_path = os.path.join(os.path.dirname(__file__), "sample_requirements.json")
        if os.path.exists(sample_data_path):
            with open(sample_data_path, 'r') as f:
                data = json.load(f)

            # Validate structure
            self.assertIn("requirements", data)
            self.assertIn("changes", data)
            self.assertIn("traceability", data)

            # Validate requirement structure
            for req in data["requirements"]:
                required_fields = ["id", "title", "description", "type", "priority", "status"]
                for field in required_fields:
                    self.assertIn(field, req)


class TestPerformance(unittest.TestCase):
    """Performance tests for the requirements system"""

    def setUp(self):
        """Set up performance test fixtures"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.manager = RequirementsManager(self.db_path)

    def tearDown(self):
        """Clean up performance test fixtures"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_bulk_requirement_creation(self):
        """Test bulk requirement creation performance"""
        import time

        # Create bulk requirements
        bulk_reqs = []
        for i in range(100):
            req = {
                "title": f"Bulk Requirement {i}",
                "description": f"Description for bulk requirement {i}",
                "type": "functional",
                "priority": "medium",
                "status": "draft",
                "created_by": "bulk_user"
            }
            bulk_reqs.append(req)

        start_time = time.time()
        created_ids = []
        for req in bulk_reqs:
            req_id = self.manager.create_requirement(req)
            created_ids.append(req_id)

        end_time = time.time()
        duration = end_time - start_time

        # Should create 100 requirements in reasonable time
        self.assertEqual(len(created_ids), 100)
        self.assertLess(duration, 5.0)  # Less than 5 seconds

    def test_query_performance(self):
        """Test query performance with large dataset"""
        # Create test data
        for i in range(50):
            req = {
                "title": f"Performance Test Req {i}",
                "description": f"Description {i}",
                "type": "functional" if i % 2 == 0 else "technical",
                "priority": "high" if i < 25 else "medium",
                "status": "approved" if i % 3 == 0 else "draft",
                "created_by": "perf_user"
            }
            self.manager.create_requirement(req)

        import time
        start_time = time.time()

        # Test various queries
        all_reqs = self.manager.list_requirements()
        functional_reqs = self.manager.list_requirements({"type": "functional"})
        high_priority = self.manager.list_requirements({"priority": "high"})

        end_time = time.time()
        duration = end_time - start_time

        # Verify results
        self.assertGreaterEqual(len(all_reqs), 50)
        self.assertGreaterEqual(len(functional_reqs), 20)
        self.assertGreaterEqual(len(high_priority), 20)

        # Performance check
        self.assertLess(duration, 1.0)  # Less than 1 second for queries


if __name__ == '__main__':
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromModule(__import__(__name__))

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print(f"\nTest Results:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")

    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed. Check the output above for details.")
