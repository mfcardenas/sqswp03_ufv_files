#!/usr/bin/env python3
"""
Requirements Change Request Module
ISO/IEC/IEEE 29148:2011 Change Management Implementation
"""

import json
import os
import sys
import logging
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("change_management.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ChangeRequest:
    """Change request data model"""
    
    def __init__(self, request_data: Dict[str, Any]):
        """
        Initialize a change request
        
        Args:
            request_data: Initial request data
        """
        # Required fields
        self.id = request_data.get("id", f"CR-{str(uuid.uuid4())[:8]}")
        self.title = request_data["title"]
        self.description = request_data["description"]
        self.requester = request_data["requester"]
        
        # Optional fields with defaults
        self.affected_requirements = request_data.get("affected_requirements", [])
        self.type = request_data.get("type", "modification")
        self.priority = request_data.get("priority", "medium")
        self.status = request_data.get("status", "submitted")
        self.created_at = request_data.get("created_at", datetime.now().isoformat())
        self.updated_at = request_data.get("updated_at", self.created_at)
        self.assigned_to = request_data.get("assigned_to", "")
        self.due_date = request_data.get("due_date", "")
        self.category = request_data.get("category", "functional")
        self.impact_level = request_data.get("impact_level", "medium")
        self.justification = request_data.get("justification", "")
        self.approvals = request_data.get("approvals", [])
        self.rejection_reason = request_data.get("rejection_reason", "")
        self.notes = request_data.get("notes", [])
        self.attachments = request_data.get("attachments", [])
        self.history = request_data.get("history", [])
        
        # Add creation event to history if not already present
        if not self.history:
            self.add_history_event("Created change request")
    
    def add_history_event(self, description: str, details: Dict[str, Any] = None) -> None:
        """
        Add an event to the change request history
        
        Args:
            description: Event description
            details: Additional event details
        """
        event = {
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "details": details or {}
        }
        self.history.append(event)
    
    def update_status(self, new_status: str, comment: str = "") -> None:
        """
        Update the status of the change request
        
        Args:
            new_status: New status value
            comment: Optional comment about the status change
        """
        old_status = self.status
        self.status = new_status
        self.updated_at = datetime.now().isoformat()
        
        # Add to history
        self.add_history_event(
            f"Status changed from {old_status} to {new_status}",
            {"old_status": old_status, "new_status": new_status, "comment": comment}
        )
    
    def add_approval(self, approver: str, decision: str, comments: str = "") -> None:
        """
        Add an approval record to the change request
        
        Args:
            approver: Name of the approver
            decision: Approval decision (approved/rejected)
            comments: Optional comments from the approver
        """
        approval = {
            "approver": approver,
            "decision": decision,
            "timestamp": datetime.now().isoformat(),
            "comments": comments
        }
        self.approvals.append(approval)
        self.updated_at = datetime.now().isoformat()
        
        # Add to history
        self.add_history_event(
            f"Approval {decision} by {approver}",
            {"approver": approver, "decision": decision, "comments": comments}
        )
    
    def add_note(self, author: str, content: str) -> None:
        """
        Add a note to the change request
        
        Args:
            author: Note author
            content: Note content
        """
        note = {
            "author": author,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.notes.append(note)
        self.updated_at = datetime.now().isoformat()
        
        # Add to history
        self.add_history_event(
            f"Note added by {author}",
            {"author": author, "note": content}
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert change request to dictionary
        
        Returns:
            Dict representation of the change request
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "requester": self.requester,
            "affected_requirements": self.affected_requirements,
            "type": self.type,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "assigned_to": self.assigned_to,
            "due_date": self.due_date,
            "category": self.category,
            "impact_level": self.impact_level,
            "justification": self.justification,
            "approvals": self.approvals,
            "rejection_reason": self.rejection_reason,
            "notes": self.notes,
            "attachments": self.attachments,
            "history": self.history
        }


class ChangeManager:
    """Main class for change request management"""
    
    def __init__(self, config_file: str):
        """
        Initialize change manager
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.change_types = []
        self.change_statuses = []
        self.priority_levels = []
        self.impact_levels = []
        self.categories = []
        self.approval_workflows = {}
        self.change_requests = []
        self.storage_file = "change_requests.json"
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the change manager"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            # Load configuration data
            self.change_types = self.config["changeManagement"]["changeTypes"]
            self.change_statuses = self.config["changeManagement"]["changeStatuses"]
            self.priority_levels = self.config["changeManagement"]["priorityLevels"]
            self.impact_levels = self.config["changeManagement"]["impactLevels"]
            self.categories = self.config["changeManagement"]["categories"]
            self.approval_workflows = self.config["changeManagement"]["approvalWorkflows"]
            
            # Load existing change requests if available
            self._load_change_requests()
            
            self.is_initialized = True
            logger.info("Change manager initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize change manager: {str(e)}")
            self.is_initialized = False
    
    def initialize_workflows(self) -> None:
        """Initialize approval workflows"""
        try:
            # Load workflow definitions from config
            for workflow_id, workflow in self.approval_workflows.items():
                logger.info(f"Initialized workflow: {workflow_id} - {workflow['name']}")
            
            logger.info(f"Initialized {len(self.approval_workflows)} approval workflows")
        except Exception as e:
            logger.error(f"Failed to initialize workflows: {str(e)}")
    
    def _load_change_requests(self) -> None:
        """Load existing change requests"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    change_data = json.load(f)
                    self.change_requests = [ChangeRequest(data) for data in change_data]
                logger.info(f"Loaded {len(self.change_requests)} change requests")
            except Exception as e:
                logger.error(f"Failed to load change requests: {str(e)}")
                self.change_requests = []
        else:
            self.change_requests = []
    
    def _save_change_requests(self) -> None:
        """Save change requests to storage"""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([cr.to_dict() for cr in self.change_requests], f, indent=2)
            logger.info(f"Saved {len(self.change_requests)} change requests")
        except Exception as e:
            logger.error(f"Failed to save change requests: {str(e)}")
    
    def create_change_request(self, request_data: Dict[str, Any]) -> ChangeRequest:
        """
        Create a new change request
        
        Args:
            request_data: Change request data
            
        Returns:
            ChangeRequest: Created change request
        """
        # Validate required fields
        required_fields = ["title", "description", "requester"]
        for field in required_fields:
            if field not in request_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Create change request
        change_request = ChangeRequest(request_data)
        
        # Add to list
        self.change_requests.append(change_request)
        
        # Save changes
        self._save_change_requests()
        
        logger.info(f"Created change request {change_request.id}: {change_request.title}")
        return change_request
    
    def get_change_request(self, request_id: str) -> Optional[ChangeRequest]:
        """
        Get change request by ID
        
        Args:
            request_id: ID of the change request
            
        Returns:
            Optional[ChangeRequest]: Change request or None if not found
        """
        for cr in self.change_requests:
            if cr.id == request_id:
                return cr
        return None
    
    def update_change_request(self, request_id: str, update_data: Dict[str, Any]) -> Optional[ChangeRequest]:
        """
        Update an existing change request
        
        Args:
            request_id: ID of the change request to update
            update_data: Updated request data
            
        Returns:
            Optional[ChangeRequest]: Updated change request or None if not found
        """
        change_request = self.get_change_request(request_id)
        
        if not change_request:
            logger.warning(f"Change request not found: {request_id}")
            return None
        
        # Update fields
        non_updatable_fields = ["id", "created_at", "history"]
        updated_fields = []
        
        for key, value in update_data.items():
            if key in non_updatable_fields:
                continue
            
            if hasattr(change_request, key) and getattr(change_request, key) != value:
                old_value = getattr(change_request, key)
                setattr(change_request, key, value)
                updated_fields.append({"field": key, "old_value": old_value, "new_value": value})
        
        if updated_fields:
            # Update timestamp
            change_request.updated_at = datetime.now().isoformat()
            
            # Add to history
            change_request.add_history_event(
                "Updated change request fields",
                {"updated_fields": updated_fields}
            )
            
            # Save changes
            self._save_change_requests()
            
            logger.info(f"Updated change request {request_id}")
        
        return change_request
    
    def delete_change_request(self, request_id: str) -> bool:
        """
        Delete a change request
        
        Args:
            request_id: ID of the change request to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        change_request = self.get_change_request(request_id)
        
        if not change_request:
            logger.warning(f"Change request not found: {request_id}")
            return False
        
        # Remove from list
        self.change_requests = [cr for cr in self.change_requests if cr.id != request_id]
        
        # Save changes
        self._save_change_requests()
        
        logger.info(f"Deleted change request {request_id}")
        return True
    
    def get_change_requests(self, filters: Dict[str, Any] = None) -> List[ChangeRequest]:
        """
        Get change requests, optionally filtered
        
        Args:
            filters: Optional filters to apply
            
        Returns:
            List[ChangeRequest]: List of change requests
        """
        if not filters:
            return self.change_requests
        
        filtered_requests = self.change_requests
        
        # Apply filters
        for key, value in filters.items():
            if key == "status":
                filtered_requests = [cr for cr in filtered_requests if cr.status == value]
            elif key == "priority":
                filtered_requests = [cr for cr in filtered_requests if cr.priority == value]
            elif key == "type":
                filtered_requests = [cr for cr in filtered_requests if cr.type == value]
            elif key == "requester":
                filtered_requests = [cr for cr in filtered_requests if cr.requester == value]
            elif key == "assigned_to":
                filtered_requests = [cr for cr in filtered_requests if cr.assigned_to == value]
            elif key == "category":
                filtered_requests = [cr for cr in filtered_requests if cr.category == value]
            elif key == "impact_level":
                filtered_requests = [cr for cr in filtered_requests if cr.impact_level == value]
        
        return filtered_requests
    
    def update_change_status(self, request_id: str, new_status: str, comment: str = "") -> Optional[ChangeRequest]:
        """
        Update the status of a change request
        
        Args:
            request_id: ID of the change request
            new_status: New status value
            comment: Optional comment about the status change
            
        Returns:
            Optional[ChangeRequest]: Updated change request or None if not found
        """
        change_request = self.get_change_request(request_id)
        
        if not change_request:
            logger.warning(f"Change request not found: {request_id}")
            return None
        
        # Validate status
        valid_statuses = [status["id"] for status in self.change_statuses]
        if new_status not in valid_statuses:
            logger.warning(f"Invalid status: {new_status}")
            return None
        
        # Update status
        change_request.update_status(new_status, comment)
        
        # Save changes
        self._save_change_requests()
        
        logger.info(f"Updated status of change request {request_id} to {new_status}")
        return change_request
    
    def add_approval(self, request_id: str, approver: str, decision: str, comments: str = "") -> Optional[ChangeRequest]:
        """
        Add an approval to a change request
        
        Args:
            request_id: ID of the change request
            approver: Name of the approver
            decision: Approval decision (approved/rejected)
            comments: Optional comments from the approver
            
        Returns:
            Optional[ChangeRequest]: Updated change request or None if not found
        """
        change_request = self.get_change_request(request_id)
        
        if not change_request:
            logger.warning(f"Change request not found: {request_id}")
            return None
        
        # Validate decision
        if decision not in ["approved", "rejected"]:
            logger.warning(f"Invalid decision: {decision}")
            return None
        
        # Add approval
        change_request.add_approval(approver, decision, comments)
        
        # Update status based on decision
        if decision == "approved":
            # Check if all approvals are complete for the current workflow
            workflow = self._get_workflow_for_change(change_request)
            if workflow and self._is_fully_approved(change_request, workflow):
                change_request.update_status("approved", "All approvals complete")
        elif decision == "rejected":
            change_request.update_status("rejected", f"Rejected by {approver}: {comments}")
            change_request.rejection_reason = comments
        
        # Save changes
        self._save_change_requests()
        
        logger.info(f"Added {decision} approval to change request {request_id} by {approver}")
        return change_request
    
    def add_note(self, request_id: str, author: str, content: str) -> Optional[ChangeRequest]:
        """
        Add a note to a change request
        
        Args:
            request_id: ID of the change request
            author: Note author
            content: Note content
            
        Returns:
            Optional[ChangeRequest]: Updated change request or None if not found
        """
        change_request = self.get_change_request(request_id)
        
        if not change_request:
            logger.warning(f"Change request not found: {request_id}")
            return None
        
        # Add note
        change_request.add_note(author, content)
        
        # Save changes
        self._save_change_requests()
        
        logger.info(f"Added note to change request {request_id} by {author}")
        return change_request
    
    def get_approval_workflow(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """
        Get approval workflow by ID
        
        Args:
            workflow_id: ID of the workflow
            
        Returns:
            Optional[Dict[str, Any]]: Workflow or None if not found
        """
        return self.approval_workflows.get(workflow_id)
    
    def _get_workflow_for_change(self, change_request: ChangeRequest) -> Optional[Dict[str, Any]]:
        """
        Get the appropriate workflow for a change request
        
        Args:
            change_request: Change request
            
        Returns:
            Optional[Dict[str, Any]]: Workflow or None if not found
        """
        # Determine workflow based on impact level and category
        impact = change_request.impact_level
        category = change_request.category
        
        # Try to find a specific workflow
        workflow_id = f"{category}_{impact}"
        if workflow_id in self.approval_workflows:
            return self.approval_workflows[workflow_id]
        
        # Try to find a category-specific workflow
        if category in self.approval_workflows:
            return self.approval_workflows[category]
        
        # Try to find an impact-specific workflow
        if impact in self.approval_workflows:
            return self.approval_workflows[impact]
        
        # Default to standard workflow
        if "standard" in self.approval_workflows:
            return self.approval_workflows["standard"]
        
        return None
    
    def _is_fully_approved(self, change_request: ChangeRequest, workflow: Dict[str, Any]) -> bool:
        """
        Check if a change request has all required approvals
        
        Args:
            change_request: Change request
            workflow: Approval workflow
            
        Returns:
            bool: True if all approvals are complete
        """
        # Get required approvers
        required_approvers = workflow.get("approvers", [])
        
        # Get current approvals
        approvals = change_request.approvals
        
        # Check if all required approvers have approved
        approved_by = [a["approver"] for a in approvals if a["decision"] == "approved"]
        
        # Check if there are any rejections
        for approval in approvals:
            if approval["decision"] == "rejected":
                return False
        
        # Check if all required approvers have approved
        for approver in required_approvers:
            if approver not in approved_by:
                return False
        
        return True
    
    def get_change_status_counts(self) -> Dict[str, int]:
        """
        Get counts of change requests by status
        
        Returns:
            Dict[str, int]: Counts of change requests by status
        """
        counts = {}
        
        for status in self.change_statuses:
            status_id = status["id"]
            counts[status_id] = len([cr for cr in self.change_requests if cr.status == status_id])
        
        return counts
    
    def get_change_priority_counts(self) -> Dict[str, int]:
        """
        Get counts of change requests by priority
        
        Returns:
            Dict[str, int]: Counts of change requests by priority
        """
        counts = {}
        
        for priority in self.priority_levels:
            priority_id = priority["id"]
            counts[priority_id] = len([cr for cr in self.change_requests if cr.priority == priority_id])
        
        return counts
    
    def get_change_type_counts(self) -> Dict[str, int]:
        """
        Get counts of change requests by type
        
        Returns:
            Dict[str, int]: Counts of change requests by type
        """
        counts = {}
        
        for type_info in self.change_types:
            type_id = type_info["id"]
            counts[type_id] = len([cr for cr in self.change_requests if cr.type == type_id])
        
        return counts
    
    def get_changes_requiring_approval(self, approver: str) -> List[ChangeRequest]:
        """
        Get change requests that require approval from a specific approver
        
        Args:
            approver: Name of the approver
            
        Returns:
            List[ChangeRequest]: List of change requests requiring approval
        """
        requiring_approval = []
        
        for cr in self.change_requests:
            # Skip if not in review status
            if cr.status != "in_review":
                continue
            
            # Get workflow
            workflow = self._get_workflow_for_change(cr)
            if not workflow:
                continue
            
            # Check if approver is required
            required_approvers = workflow.get("approvers", [])
            if approver not in required_approvers:
                continue
            
            # Check if already approved by this approver
            already_approved = False
            for approval in cr.approvals:
                if approval["approver"] == approver:
                    already_approved = True
                    break
            
            if not already_approved:
                requiring_approval.append(cr)
        
        return requiring_approval
    
    def get_overdue_changes(self) -> List[ChangeRequest]:
        """
        Get overdue change requests
        
        Returns:
            List[ChangeRequest]: List of overdue change requests
        """
        today = datetime.now().date()
        overdue_changes = []
        
        for cr in self.change_requests:
            # Skip completed or rejected changes
            if cr.status in ["approved", "rejected", "implemented", "closed"]:
                continue
            
            # Check if due date exists and is in the past
            if cr.due_date:
                try:
                    due_date = datetime.strptime(cr.due_date, "%Y-%m-%d").date()
                    if due_date < today:
                        overdue_changes.append(cr)
                except ValueError:
                    # Skip changes with invalid date format
                    continue
        
        return overdue_changes


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python change_request.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    manager = ChangeManager(config_file)
    
    if not manager.is_initialized:
        print("Failed to initialize change manager")
        sys.exit(1)
    
    print("Change manager initialized successfully.")
    
    # Initialize workflows
    manager.initialize_workflows()
    
    # Example usage
    change_data = {
        "title": "Update Authentication Requirements",
        "description": "Change authentication method from basic to OAuth 2.0",
        "requester": "John Smith",
        "affected_requirements": ["REQ-SEC-001", "REQ-SEC-002"],
        "type": "modification",
        "priority": "high",
        "category": "security",
        "impact_level": "medium",
        "justification": "Improved security and compliance with industry standards"
    }
    
    change_request = manager.create_change_request(change_data)
    
    print(f"Created change request {change_request.id}: {change_request.title}")
    print(f"Status: {change_request.status}")
    print(f"Priority: {change_request.priority}")
    print(f"Type: {change_request.type}")
    print(f"Category: {change_request.category}")
    print(f"Impact Level: {change_request.impact_level}")
