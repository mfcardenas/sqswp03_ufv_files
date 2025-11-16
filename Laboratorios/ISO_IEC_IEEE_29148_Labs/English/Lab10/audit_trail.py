#!/usr/bin/env python3
"""
Audit Trail Module for Requirements Compliance & Audit
ISO/IEC/IEEE 29148:2011 Compliance Auditing
"""

import json
import os
import sys
import time
import logging
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Union
from uuid import uuid4

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("audit_trail.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AuditEvent:
    """Class representing an audit event entry"""
    
    def __init__(self, user_id: str, action: str, object_type: str, object_id: str, 
                 details: str = '', ip_address: str = '', metadata: Dict[str, Any] = None):
        """Initialize audit event"""
        self.entry_id = str(uuid4())
        self.timestamp = datetime.now().isoformat()
        self.user_id = user_id
        self.action = action
        self.object_type = object_type
        self.object_id = object_id
        self.details = details
        self.ip_address = ip_address
        self.metadata = metadata or {}
        self.previous_hash = ""  # Will be set by AuditTrail
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            'entry_id': self.entry_id,
            'timestamp': self.timestamp,
            'user_id': self.user_id,
            'action': self.action,
            'object_type': self.object_type,
            'object_id': self.object_id,
            'details': self.details,
            'ip_address': self.ip_address,
            'metadata': self.metadata,
            'previous_hash': self.previous_hash
        }
    
    def calculate_hash(self) -> str:
        """Calculate hash of audit event"""
        event_data = {k: v for k, v in self.to_dict().items() if k != 'previous_hash'}
        event_json = json.dumps(event_data, sort_keys=True)
        return hashlib.sha256(event_json.encode()).hexdigest()


class AuditTrail:
    """Main class for audit trail management"""
    
    def __init__(self, config_file: str, storage_path: str = None):
        """
        Initialize audit trail
        
        Args:
            config_file: Path to configuration file
            storage_path: Optional path to audit log storage
        """
        self.config_file = config_file
        self.config = {}
        self.storage_path = storage_path
        self.logs = []
        self.last_hash = None
        self.retention_period = 365  # Default to 1 year
        self.encryption_enabled = False
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the audit trail"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            self.retention_period = self.config['audit']['retention_period_days']
            self.encryption_enabled = self.config['audit']['encryption']['enabled']
            
            if not self.storage_path:
                self.storage_path = self.config['audit'].get('storage_path', 'audit_logs')
            
            # Create storage directory if it doesn't exist
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)
            
            # Load existing logs if available
            self._load_logs()
            
            self.is_initialized = True
            logger.info("Audit trail initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize audit trail: {str(e)}")
            self.is_initialized = False
    
    def _load_logs(self) -> None:
        """Load existing audit logs"""
        log_file = os.path.join(self.storage_path, 'audit_logs.json')
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r') as f:
                    log_data = json.load(f)
                
                self.logs = []
                for entry_data in log_data:
                    entry = AuditEvent(
                        user_id=entry_data['user_id'],
                        action=entry_data['action'],
                        object_type=entry_data['object_type'],
                        object_id=entry_data['object_id'],
                        details=entry_data['details'],
                        ip_address=entry_data.get('ip_address', ''),
                        metadata=entry_data.get('metadata', {})
                    )
                    entry.entry_id = entry_data['entry_id']
                    entry.timestamp = entry_data['timestamp']
                    entry.previous_hash = entry_data['previous_hash']
                    
                    self.logs.append(entry)
                
                if self.logs:
                    self.last_hash = self.logs[-1].calculate_hash()
                
                logger.info(f"Loaded {len(self.logs)} audit log entries")
            except Exception as e:
                logger.error(f"Failed to load audit logs: {str(e)}")
    
    def _save_logs(self) -> None:
        """Save audit logs to storage"""
        log_file = os.path.join(self.storage_path, 'audit_logs.json')
        
        try:
            log_data = [entry.to_dict() for entry in self.logs]
            
            with open(log_file, 'w') as f:
                json.dump(log_data, f, indent=2)
            
            logger.info(f"Saved {len(self.logs)} audit log entries")
        except Exception as e:
            logger.error(f"Failed to save audit logs: {str(e)}")
    
    def log_event(self, user_id: str, action: str, object_type: str, object_id: str, 
                  details: str = '', ip_address: str = '', metadata: Dict[str, Any] = None) -> AuditEvent:
        """
        Log an audit event
        
        Args:
            user_id: ID of the user performing the action
            action: Type of action (create, read, update, delete, etc.)
            object_type: Type of object being acted upon (requirement, rule, etc.)
            object_id: ID of the object being acted upon
            details: Additional details about the action
            ip_address: IP address of the user
            metadata: Additional metadata about the event
            
        Returns:
            AuditEvent: The created audit event
        """
        entry = AuditEvent(
            user_id=user_id,
            action=action,
            object_type=object_type,
            object_id=object_id,
            details=details,
            ip_address=ip_address,
            metadata=metadata
        )
        
        # Set hash chain
        if self.last_hash:
            entry.previous_hash = self.last_hash
        
        self.logs.append(entry)
        self.last_hash = entry.calculate_hash()
        
        # Save logs after each event
        self._save_logs()
        
        return entry
    
    def get_logs(self, user_id: str = None, action: str = None, object_type: str = None, 
                 object_id: str = None, start_date: datetime = None, end_date: datetime = None) -> List[AuditEvent]:
        """
        Get audit logs with optional filtering
        
        Args:
            user_id: Filter by user ID
            action: Filter by action type
            object_type: Filter by object type
            object_id: Filter by object ID
            start_date: Filter by start date
            end_date: Filter by end date
            
        Returns:
            List[AuditEvent]: Filtered audit logs
        """
        filtered_logs = self.logs
        
        if user_id:
            filtered_logs = [log for log in filtered_logs if log.user_id == user_id]
        
        if action:
            filtered_logs = [log for log in filtered_logs if log.action == action]
        
        if object_type:
            filtered_logs = [log for log in filtered_logs if log.object_type == object_type]
        
        if object_id:
            filtered_logs = [log for log in filtered_logs if log.object_id == object_id]
        
        if start_date:
            filtered_logs = [log for log in filtered_logs if datetime.fromisoformat(log.timestamp) >= start_date]
        
        if end_date:
            filtered_logs = [log for log in filtered_logs if datetime.fromisoformat(log.timestamp) <= end_date]
        
        return filtered_logs
    
    def verify_log_integrity(self) -> bool:
        """
        Verify integrity of the audit log chain
        
        Returns:
            bool: True if audit log chain is intact, False otherwise
        """
        if not self.logs:
            return True
        
        for i in range(len(self.logs)):
            current_entry = self.logs[i]
            current_hash = current_entry.calculate_hash()
            
            # Skip first entry
            if i == 0:
                if current_entry.previous_hash != "":
                    logger.warning("First audit log entry has non-empty previous_hash")
                    return False
                continue
            
            # Check hash chain
            previous_entry = self.logs[i-1]
            previous_hash = previous_entry.calculate_hash()
            
            if current_entry.previous_hash != previous_hash:
                logger.warning(f"Audit log integrity broken at entry {current_entry.entry_id}")
                return False
        
        return True
    
    def export_logs(self, format: str = 'json', filters: Dict[str, Any] = None) -> str:
        """
        Export audit logs to a specific format
        
        Args:
            format: Export format (json, csv)
            filters: Optional filters to apply
            
        Returns:
            str: Exported audit logs in the specified format
        """
        # Apply filters if provided
        if filters:
            filtered_logs = self.get_logs(**filters)
        else:
            filtered_logs = self.logs
        
        # Export to JSON
        if format.lower() == 'json':
            log_data = [entry.to_dict() for entry in filtered_logs]
            return json.dumps(log_data, indent=2)
        
        # Export to CSV
        elif format.lower() == 'csv':
            csv_lines = [
                "entry_id,timestamp,user_id,action,object_type,object_id,details,ip_address"
            ]
            
            for entry in filtered_logs:
                csv_lines.append(
                    f"{entry.entry_id},{entry.timestamp},{entry.user_id},{entry.action},"
                    f"{entry.object_type},{entry.object_id},\"{entry.details}\",{entry.ip_address}"
                )
            
            return "\n".join(csv_lines)
        
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def purge_old_logs(self) -> int:
        """
        Purge logs older than retention period
        
        Returns:
            int: Number of purged log entries
        """
        if not self.retention_period:
            return 0
        
        retention_date = datetime.now() - timedelta(days=self.retention_period)
        old_count = len(self.logs)
        
        self.logs = [log for log in self.logs if datetime.fromisoformat(log.timestamp) >= retention_date]
        purged_count = old_count - len(self.logs)
        
        if purged_count > 0:
            logger.info(f"Purged {purged_count} audit log entries older than {self.retention_period} days")
            self._save_logs()
        
        return purged_count


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python audit_trail.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    audit = AuditTrail(config_file)
    
    if not audit.is_initialized:
        print("Failed to initialize audit trail")
        sys.exit(1)
    
    print(f"Loaded {len(audit.logs)} audit log entries")
    
    # Verify log integrity
    if audit.verify_log_integrity():
        print("Audit log integrity verified")
    else:
        print("WARNING: Audit log integrity verification failed")
