#!/usr/bin/env python3
"""
Requirements Approval Workflow Module
ISO/IEC/IEEE 29148:2011 Approval Workflow Implementation
"""

import json
import os
import sys
import logging
import uuid
import smtplib
import email.message
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Union, Callable

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("approval_workflow.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ApprovalWorkflow:
    """Main class for approval workflow management"""
    
    def __init__(self, config_file: str):
        """
        Initialize approval workflow
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.workflows = {}
        self.roles = {}
        self.users = {}
        self.storage_file = "approval_workflows.json"
        self.email_enabled = False
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the approval workflow"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            # Load configuration data
            self.workflows = self.config.get("approvalWorkflows", {})
            self.roles = self.config.get("roles", {})
            self.users = self.config.get("users", {})
            
            # Check email configuration
            email_config = self.config.get("emailConfig", {})
            self.email_enabled = email_config.get("enabled", False)
            
            self.is_initialized = True
            logger.info("Approval workflow initialized successfully")
            logger.info(f"Loaded {len(self.workflows)} workflow definitions")
            logger.info(f"Email notifications {'enabled' if self.email_enabled else 'disabled'}")
        except Exception as e:
            logger.error(f"Failed to initialize approval workflow: {str(e)}")
            self.is_initialized = False
    
    def get_workflow_definition(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """
        Get workflow definition by ID
        
        Args:
            workflow_id: ID of the workflow
            
        Returns:
            Optional[Dict[str, Any]]: Workflow definition or None if not found
        """
        return self.workflows.get(workflow_id)
    
    def get_workflow_for_request(self, change_request: Dict[str, Any]) -> str:
        """
        Determine appropriate workflow for a change request
        
        Args:
            change_request: Change request data
            
        Returns:
            str: ID of the appropriate workflow
        """
        # Extract relevant attributes
        impact_level = change_request.get("impact_level", "medium")
        category = change_request.get("category", "functional")
        priority = change_request.get("priority", "medium")
        
        # Try to find specific workflow
        specific_id = f"{category}_{impact_level}"
        if specific_id in self.workflows:
            return specific_id
        
        # Try by category
        if category in self.workflows:
            return category
        
        # Try by impact level
        if impact_level in self.workflows:
            return impact_level
        
        # Try by priority
        if priority in self.workflows:
            return priority
        
        # Default to standard workflow
        if "standard" in self.workflows:
            return "standard"
        
        # If no standard workflow, use the first available
        if self.workflows:
            return list(self.workflows.keys())[0]
        
        # If no workflows defined, create a basic one
        logger.warning("No workflows defined, using default")
        return "default"
    
    def start_approval_process(self, change_request: Dict[str, Any], workflow_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Start approval process for a change request
        
        Args:
            change_request: Change request data
            workflow_id: Optional workflow ID to use
            
        Returns:
            Dict[str, Any]: Approval process data
        """
        if not workflow_id:
            workflow_id = self.get_workflow_for_request(change_request)
        
        workflow_def = self.get_workflow_definition(workflow_id)
        
        if not workflow_def:
            logger.warning(f"Workflow not found: {workflow_id}, using default")
            workflow_def = {
                "name": "Default Workflow",
                "description": "Basic approval workflow",
                "steps": [
                    {
                        "id": "review",
                        "name": "Review",
                        "approvers": ["manager"],
                        "requiredApprovals": 1
                    }
                ]
            }
        
        # Create approval process
        process_id = f"AP-{str(uuid.uuid4())[:8]}"
        
        # Initialize process
        process = {
            "id": process_id,
            "change_request_id": change_request.get("id"),
            "workflow_id": workflow_id,
            "status": "in_progress",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "steps": [],
            "current_step_index": 0,
            "approvals": [],
            "rejections": [],
            "comments": [],
            "history": []
        }
        
        # Initialize steps
        for step_def in workflow_def.get("steps", []):
            step = {
                "id": step_def["id"],
                "name": step_def["name"],
                "status": "pending",
                "approvers": step_def["approvers"],
                "required_approvals": step_def.get("requiredApprovals", len(step_def["approvers"])),
                "approvals": [],
                "started_at": None,
                "completed_at": None
            }
            process["steps"].append(step)
        
        # Set first step to active if there are steps
        if process["steps"]:
            process["steps"][0]["status"] = "active"
            process["steps"][0]["started_at"] = datetime.now().isoformat()
            
            # Send notifications
            self._send_step_notifications(process, 0, change_request)
        
        # Add start event to history
        self._add_history_event(process, "Approval process started", 
                               {"workflow": workflow_id, "change_request": change_request.get("id")})
        
        logger.info(f"Started approval process {process_id} for change request {change_request.get('id')}")
        return process
    
    def record_approval(self, process: Dict[str, Any], step_index: int, approver: str, 
                       decision: str, comments: str = "") -> Dict[str, Any]:
        """
        Record an approval or rejection
        
        Args:
            process: Approval process data
            step_index: Index of the current step
            approver: Name of the approver
            decision: Approval decision (approved/rejected)
            comments: Optional comments
            
        Returns:
            Dict[str, Any]: Updated approval process
        """
        # Validate step index
        if step_index < 0 or step_index >= len(process["steps"]):
            logger.error(f"Invalid step index: {step_index}")
            return process
        
        # Get current step
        step = process["steps"][step_index]
        
        # Validate approver
        if approver not in step["approvers"]:
            logger.warning(f"Invalid approver {approver} for step {step['name']}")
            return process
        
        # Validate step status
        if step["status"] != "active":
            logger.warning(f"Cannot record approval for {step['status']} step")
            return process
        
        # Check if approver already approved/rejected
        for approval in step["approvals"]:
            if approval["approver"] == approver:
                logger.warning(f"Approver {approver} already provided a decision")
                return process
        
        # Record approval
        approval = {
            "approver": approver,
            "decision": decision,
            "timestamp": datetime.now().isoformat(),
            "comments": comments
        }
        
        step["approvals"].append(approval)
        
        # Add to process level lists
        if decision == "approved":
            process["approvals"].append(approval)
        else:
            process["rejections"].append(approval)
        
        # Add comment if provided
        if comments:
            self._add_comment(process, approver, comments)
        
        # Add to history
        self._add_history_event(process, f"Step {step['name']} {decision} by {approver}", approval)
        
        # Update process
        process["updated_at"] = datetime.now().isoformat()
        
        # Check if step is complete
        self._check_step_completion(process, step_index)
        
        logger.info(f"Recorded {decision} for step {step['name']} by {approver}")
        return process
    
    def _check_step_completion(self, process: Dict[str, Any], step_index: int) -> None:
        """
        Check if current step is complete and advance if necessary
        
        Args:
            process: Approval process data
            step_index: Index of the current step
        """
        step = process["steps"][step_index]
        
        # Count approvals and rejections
        approvals = sum(1 for a in step["approvals"] if a["decision"] == "approved")
        rejections = sum(1 for a in step["approvals"] if a["decision"] == "rejected")
        
        # Check if any rejection (automatic rejection)
        if rejections > 0:
            step["status"] = "rejected"
            step["completed_at"] = datetime.now().isoformat()
            process["status"] = "rejected"
            
            self._add_history_event(process, f"Step {step['name']} rejected", 
                                   {"step": step["name"], "reason": "Rejection received"})
            
            self._add_history_event(process, "Approval process rejected", 
                                   {"step": step["name"]})
            return
        
        # Check if enough approvals
        if approvals >= step["required_approvals"]:
            step["status"] = "approved"
            step["completed_at"] = datetime.now().isoformat()
            
            self._add_history_event(process, f"Step {step['name']} approved", 
                                   {"step": step["name"], "approvals": approvals})
            
            # Check if this is the last step
            if step_index == len(process["steps"]) - 1:
                process["status"] = "approved"
                self._add_history_event(process, "Approval process completed", 
                                      {"result": "approved"})
            else:
                # Advance to next step
                next_index = step_index + 1
                process["current_step_index"] = next_index
                
                next_step = process["steps"][next_index]
                next_step["status"] = "active"
                next_step["started_at"] = datetime.now().isoformat()
                
                self._add_history_event(process, f"Advanced to step {next_step['name']}", 
                                      {"from": step["name"], "to": next_step["name"]})
                
                # Send notifications for next step
                self._send_step_notifications(process, next_index)
    
    def _add_comment(self, process: Dict[str, Any], author: str, content: str) -> None:
        """
        Add a comment to the approval process
        
        Args:
            process: Approval process data
            author: Comment author
            content: Comment content
        """
        comment = {
            "author": author,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        
        process["comments"].append(comment)
    
    def _add_history_event(self, process: Dict[str, Any], description: str, details: Dict[str, Any] = None) -> None:
        """
        Add an event to the approval process history
        
        Args:
            process: Approval process data
            description: Event description
            details: Additional event details
        """
        event = {
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "details": details or {}
        }
        
        process["history"].append(event)
    
    def _send_step_notifications(self, process: Dict[str, Any], step_index: int, 
                               change_request: Dict[str, Any] = None) -> None:
        """
        Send notifications to approvers for the current step
        
        Args:
            process: Approval process data
            step_index: Index of the current step
            change_request: Optional change request data
        """
        if not self.email_enabled:
            logger.info("Email notifications disabled")
            return
        
        step = process["steps"][step_index]
        
        # Get approver email addresses
        approver_emails = []
        for approver_id in step["approvers"]:
            user = self.users.get(approver_id)
            if user and "email" in user:
                approver_emails.append(user["email"])
        
        if not approver_emails:
            logger.warning("No approver emails found")
            return
        
        # Get change request details if not provided
        if not change_request:
            # In a real implementation, this would fetch the change request
            change_request = {"id": process["change_request_id"], "title": "Change Request"}
        
        # Send emails
        subject = f"Approval Required: {change_request.get('title', 'Change Request')}"
        body = f"""
        Your approval is required for the following change request:
        
        ID: {change_request.get('id')}
        Title: {change_request.get('title', 'Change Request')}
        
        Step: {step['name']}
        
        Please review and provide your decision.
        """
        
        try:
            self._send_email(approver_emails, subject, body)
            logger.info(f"Sent approval notifications for step {step['name']} to {len(approver_emails)} approvers")
        except Exception as e:
            logger.error(f"Failed to send notifications: {str(e)}")
    
    def _send_email(self, recipients: List[str], subject: str, body: str) -> bool:
        """
        Send email notification
        
        Args:
            recipients: List of recipient email addresses
            subject: Email subject
            body: Email body
            
        Returns:
            bool: True if sent successfully, False otherwise
        """
        # This is a placeholder for actual email sending
        # In a real implementation, this would use SMTP or an email service
        
        # Get email configuration
        email_config = self.config.get("emailConfig", {})
        
        if not email_config.get("enabled", False):
            logger.info("Email notifications disabled")
            return False
        
        # Log the email that would be sent
        logger.info(f"Would send email to {', '.join(recipients)}")
        logger.info(f"Subject: {subject}")
        logger.info(f"Body: {body}")
        
        # In a real implementation, this would send the actual email
        return True
    
    def get_approval_status(self, process: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get approval status summary
        
        Args:
            process: Approval process data
            
        Returns:
            Dict[str, Any]: Approval status summary
        """
        # Count approvals and rejections
        total_approvals = len(process["approvals"])
        total_rejections = len(process["rejections"])
        
        # Calculate step completion
        steps_total = len(process["steps"])
        steps_completed = sum(1 for step in process["steps"] if step["status"] in ["approved", "rejected"])
        steps_approved = sum(1 for step in process["steps"] if step["status"] == "approved")
        steps_rejected = sum(1 for step in process["steps"] if step["status"] == "rejected")
        
        # Get current step
        current_step = None
        if process["status"] == "in_progress" and process["current_step_index"] < len(process["steps"]):
            current_step = process["steps"][process["current_step_index"]]
        
        # Prepare status summary
        status_summary = {
            "process_id": process["id"],
            "change_request_id": process["change_request_id"],
            "status": process["status"],
            "created_at": process["created_at"],
            "updated_at": process["updated_at"],
            "approvals": {
                "total": total_approvals,
                "rejections": total_rejections
            },
            "steps": {
                "total": steps_total,
                "completed": steps_completed,
                "approved": steps_approved,
                "rejected": steps_rejected,
                "progress": (steps_completed / steps_total) * 100 if steps_total > 0 else 0
            },
            "current_step": {
                "name": current_step["name"] if current_step else None,
                "status": current_step["status"] if current_step else None,
                "approvers": current_step["approvers"] if current_step else [],
                "approvals_received": len(current_step["approvals"]) if current_step else 0,
                "approvals_required": current_step["required_approvals"] if current_step else 0
            } if current_step else None
        }
        
        return status_summary
    
    def cancel_approval_process(self, process: Dict[str, Any], reason: str) -> Dict[str, Any]:
        """
        Cancel an approval process
        
        Args:
            process: Approval process data
            reason: Cancellation reason
            
        Returns:
            Dict[str, Any]: Updated approval process
        """
        # Check if already completed
        if process["status"] not in ["in_progress", "pending"]:
            logger.warning(f"Cannot cancel {process['status']} approval process")
            return process
        
        # Update process status
        process["status"] = "cancelled"
        process["updated_at"] = datetime.now().isoformat()
        
        # Update current step
        if process["current_step_index"] < len(process["steps"]):
            current_step = process["steps"][process["current_step_index"]]
            current_step["status"] = "cancelled"
            current_step["completed_at"] = datetime.now().isoformat()
        
        # Add to history
        self._add_history_event(process, "Approval process cancelled", {"reason": reason})
        
        logger.info(f"Cancelled approval process {process['id']}: {reason}")
        return process
    
    def is_approved(self, process: Dict[str, Any]) -> bool:
        """
        Check if approval process is fully approved
        
        Args:
            process: Approval process data
            
        Returns:
            bool: True if approved, False otherwise
        """
        return process["status"] == "approved"
    
    def is_rejected(self, process: Dict[str, Any]) -> bool:
        """
        Check if approval process is rejected
        
        Args:
            process: Approval process data
            
        Returns:
            bool: True if rejected, False otherwise
        """
        return process["status"] == "rejected"
    
    def get_pending_approvals(self, approver: str) -> List[Dict[str, Any]]:
        """
        Get pending approvals for a specific approver
        
        Args:
            approver: Approver ID
            
        Returns:
            List[Dict[str, Any]]: List of pending approval processes
        """
        # This is a placeholder function that would typically interact with a database
        # In a real implementation, this would fetch actual pending approvals
        
        logger.info(f"Querying pending approvals for {approver}")
        
        # Return empty list for demo purposes
        return []
    
    def register_approval_callback(self, callback: Callable[[Dict[str, Any]], None]) -> None:
        """
        Register a callback function to be called when approval status changes
        
        Args:
            callback: Callback function that takes the approval process as argument
        """
        # This is a placeholder function for demonstration purposes
        # In a real implementation, this would store the callback for later use
        
        logger.info("Registered approval callback")


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python approval_workflow.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    workflow = ApprovalWorkflow(config_file)
    
    if not workflow.is_initialized:
        print("Failed to initialize approval workflow")
        sys.exit(1)
    
    print("Approval workflow initialized successfully.")
    
    # Example usage
    change_request = {
        "id": "CR-12345",
        "title": "Update Authentication Requirements",
        "description": "Change authentication method from basic to OAuth 2.0",
        "requester": "John Smith",
        "impact_level": "medium",
        "category": "security",
        "priority": "high"
    }
    
    # Start approval process
    process = workflow.start_approval_process(change_request)
    
    print(f"Started approval process {process['id']} for change request {change_request['id']}")
    print(f"Workflow: {process['workflow_id']}")
    print(f"Status: {process['status']}")
    
    # Example approval
    if process["steps"]:
        step_index = 0
        approver = process["steps"][step_index]["approvers"][0]
        
        print(f"\nRecording approval from {approver}...")
        process = workflow.record_approval(process, step_index, approver, "approved", "Looks good to me!")
        
        # Get status
        status = workflow.get_approval_status(process)
        
        print(f"\nApproval Status:")
        print(f"Status: {status['status']}")
        print(f"Steps: {status['steps']['completed']}/{status['steps']['total']} completed")
        if status['current_step']:
            print(f"Current Step: {status['current_step']['name']}")
            print(f"Approvals: {status['current_step']['approvals_received']}/{status['current_step']['approvals_required']}")
