#!/usr/bin/env python3
"""
Requirements Risk Mitigation Module
ISO/IEC/IEEE 29148:2011 Risk Mitigation Implementation
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
        logging.FileHandler("risk_mitigation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RiskMitigation:
    """Main class for risk mitigation"""
    
    def __init__(self, config_file: str):
        """
        Initialize risk mitigation
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.strategies = []
        self.statuses = []
        self.actions = []
        self.storage_file = "risk_mitigation_actions.json"
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the risk mitigation"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            # Load configuration data
            self.strategies = self.config["riskManagement"]["mitigationStrategies"]
            self.statuses = self.config["riskManagement"]["mitigationStatuses"]
            
            # Load existing actions if available
            self._load_actions()
            
            self.is_initialized = True
            logger.info("Risk mitigation initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize risk mitigation: {str(e)}")
            self.is_initialized = False
    
    def _load_actions(self) -> None:
        """Load existing mitigation actions"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    self.actions = json.load(f)
                logger.info(f"Loaded {len(self.actions)} mitigation actions")
            except Exception as e:
                logger.error(f"Failed to load mitigation actions: {str(e)}")
                self.actions = []
        else:
            self.actions = []
    
    def _save_actions(self) -> None:
        """Save mitigation actions to storage"""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.actions, f, indent=2)
            logger.info(f"Saved {len(self.actions)} mitigation actions")
        except Exception as e:
            logger.error(f"Failed to save mitigation actions: {str(e)}")
    
    def create_action(self, action_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new mitigation action
        
        Args:
            action_data: Mitigation action data
            
        Returns:
            Dict[str, Any]: Created mitigation action
        """
        # Validate required fields
        required_fields = ["related_risk", "description"]
        for field in required_fields:
            if field not in action_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Generate action ID
        action_id = f"ACT-{str(uuid.uuid4())[:8]}"
        
        # Create action with default values
        action = {
            "id": action_id,
            "related_risk": action_data["related_risk"],
            "description": action_data["description"],
            "strategy": action_data.get("strategy", "mitigate"),
            "owner": action_data.get("owner", ""),
            "due_date": action_data.get("due_date", ""),
            "status": action_data.get("status", "open"),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "notes": action_data.get("notes", "")
        }
        
        # Add action to list
        self.actions.append(action)
        
        # Save actions
        self._save_actions()
        
        logger.info(f"Created mitigation action {action_id} for risk {action['related_risk']}")
        return action
    
    def update_action(self, action_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing mitigation action
        
        Args:
            action_id: ID of the action to update
            update_data: Updated action data
            
        Returns:
            Dict[str, Any]: Updated mitigation action
        """
        # Find action by ID
        action = self.get_action(action_id)
        
        if not action:
            raise ValueError(f"Action not found: {action_id}")
        
        # Update fields
        for key, value in update_data.items():
            if key in action and key not in ["id", "created_at"]:
                action[key] = value
        
        # Update timestamp
        action["updated_at"] = datetime.now().isoformat()
        
        # Save actions
        self._save_actions()
        
        logger.info(f"Updated mitigation action {action_id}")
        return action
    
    def get_action(self, action_id: str) -> Optional[Dict[str, Any]]:
        """
        Get mitigation action by ID
        
        Args:
            action_id: ID of the action to get
            
        Returns:
            Optional[Dict[str, Any]]: Mitigation action or None if not found
        """
        for action in self.actions:
            if action["id"] == action_id:
                return action
        return None
    
    def get_actions_by_risk(self, risk_id: str) -> List[Dict[str, Any]]:
        """
        Get mitigation actions for a specific risk
        
        Args:
            risk_id: ID of the risk to get actions for
            
        Returns:
            List[Dict[str, Any]]: List of mitigation actions
        """
        return [action for action in self.actions if action["related_risk"] == risk_id]
    
    def get_actions_by_status(self, status: str) -> List[Dict[str, Any]]:
        """
        Get mitigation actions by status
        
        Args:
            status: Status to filter by
            
        Returns:
            List[Dict[str, Any]]: List of mitigation actions
        """
        return [action for action in self.actions if action["status"] == status]
    
    def get_actions_by_owner(self, owner: str) -> List[Dict[str, Any]]:
        """
        Get mitigation actions by owner
        
        Args:
            owner: Owner to filter by
            
        Returns:
            List[Dict[str, Any]]: List of mitigation actions
        """
        return [action for action in self.actions if action["owner"] == owner]
    
    def get_overdue_actions(self) -> List[Dict[str, Any]]:
        """
        Get overdue mitigation actions
        
        Returns:
            List[Dict[str, Any]]: List of overdue mitigation actions
        """
        today = datetime.now().date()
        overdue_actions = []
        
        for action in self.actions:
            # Skip completed actions
            if action["status"] == "completed":
                continue
            
            # Check if due date exists and is in the past
            if action["due_date"]:
                try:
                    due_date = datetime.strptime(action["due_date"], "%Y-%m-%d").date()
                    if due_date < today:
                        overdue_actions.append(action)
                except ValueError:
                    # Skip actions with invalid date format
                    continue
        
        return overdue_actions
    
    def get_upcoming_actions(self, days: int = 7) -> List[Dict[str, Any]]:
        """
        Get upcoming mitigation actions
        
        Args:
            days: Number of days to look ahead
            
        Returns:
            List[Dict[str, Any]]: List of upcoming mitigation actions
        """
        today = datetime.now().date()
        upcoming_date = today + timedelta(days=days)
        upcoming_actions = []
        
        for action in self.actions:
            # Skip completed actions
            if action["status"] == "completed":
                continue
            
            # Check if due date exists and is in the upcoming period
            if action["due_date"]:
                try:
                    due_date = datetime.strptime(action["due_date"], "%Y-%m-%d").date()
                    if today <= due_date <= upcoming_date:
                        upcoming_actions.append(action)
                except ValueError:
                    # Skip actions with invalid date format
                    continue
        
        return upcoming_actions
    
    def get_action_status_counts(self) -> Dict[str, int]:
        """
        Get counts of actions by status
        
        Returns:
            Dict[str, int]: Counts of actions by status
        """
        counts = {}
        
        for status in self.statuses:
            status_id = status["id"]
            counts[status_id] = len(self.get_actions_by_status(status_id))
        
        return counts
    
    def delete_action(self, action_id: str) -> bool:
        """
        Delete a mitigation action
        
        Args:
            action_id: ID of the action to delete
            
        Returns:
            bool: True if action was deleted, False otherwise
        """
        action = self.get_action(action_id)
        
        if not action:
            return False
        
        self.actions.remove(action)
        self._save_actions()
        
        logger.info(f"Deleted mitigation action {action_id}")
        return True
    
    def get_available_strategies(self) -> List[Dict[str, str]]:
        """
        Get available mitigation strategies
        
        Returns:
            List[Dict[str, str]]: List of available strategies
        """
        return [{"id": s["id"], "name": s["name"], "description": s["description"]} for s in self.strategies]
    
    def get_available_statuses(self) -> List[Dict[str, str]]:
        """
        Get available mitigation action statuses
        
        Returns:
            List[Dict[str, str]]: List of available statuses
        """
        return [{"id": s["id"], "name": s["name"], "description": s["description"]} for s in self.statuses]
    
    def get_all_actions(self) -> List[Dict[str, Any]]:
        """
        Get all mitigation actions
        
        Returns:
            List[Dict[str, Any]]: List of all mitigation actions
        """
        return self.actions
    
    def clear_completed_actions(self, days: int = 90) -> int:
        """
        Clear old completed actions
        
        Args:
            days: Number of days to keep completed actions
            
        Returns:
            int: Number of actions cleared
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        old_count = len(self.actions)
        
        self.actions = [action for action in self.actions if not (
            action["status"] == "completed" and 
            datetime.fromisoformat(action["updated_at"]) < cutoff_date
        )]
        
        cleared_count = old_count - len(self.actions)
        
        if cleared_count > 0:
            self._save_actions()
            logger.info(f"Cleared {cleared_count} old completed actions")
        
        return cleared_count


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python risk_mitigation.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    mitigation = RiskMitigation(config_file)
    
    if not mitigation.is_initialized:
        print("Failed to initialize risk mitigation")
        sys.exit(1)
    
    print("Risk mitigation initialized successfully.")
    
    # Example usage
    action_data = {
        "related_risk": "REQ-TEST-001",
        "description": "Implement third-party biometric authentication library",
        "strategy": "mitigate",
        "owner": "John Smith",
        "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    }
    
    action = mitigation.create_action(action_data)
    
    print(f"Created mitigation action {action['id']} for risk {action['related_risk']}")
    print(f"  Description: {action['description']}")
    print(f"  Strategy: {action['strategy']}")
    print(f"  Owner: {action['owner']}")
    print(f"  Due Date: {action['due_date']}")
    print(f"  Status: {action['status']}")
