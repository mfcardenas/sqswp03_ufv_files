#!/usr/bin/env python3
"""
Regulatory Reporting Module for Requirements Compliance & Audit
ISO/IEC/IEEE 29148:2011 Compliance Reporting
"""

import json
import os
import sys
import logging
import csv
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("regulatory_reporting.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ReportFormat:
    """Class for report format handling"""
    
    def __init__(self, format_config: Dict[str, Any]):
        """Initialize report format"""
        self.id = format_config.get('id', '')
        self.name = format_config.get('name', '')
        self.description = format_config.get('description', '')
        self.template = format_config.get('template', '')
        self.metadata = format_config.get('metadata', {})
    
    def format_report(self, data: Dict[str, Any]) -> str:
        """
        Format report data according to this format
        
        Args:
            data: Report data to format
            
        Returns:
            str: Formatted report
        """
        if self.id == 'json':
            return json.dumps(data, indent=2)
        elif self.id == 'csv':
            return self._format_as_csv(data)
        elif self.id == 'html':
            return self._format_as_html(data)
        elif self.id == 'pdf':
            return self._format_as_pdf(data)
        else:
            logger.warning(f"Unsupported report format: {self.id}")
            return json.dumps(data, indent=2)
    
    def _format_as_csv(self, data: Dict[str, Any]) -> str:
        """Format report data as CSV"""
        if 'details' not in data or 'rules' not in data['details']:
            return "No data to format as CSV"
        
        csv_lines = [
            "rule_id,standard,description,status,severity"
        ]
        
        for rule in data['details']['rules']:
            csv_lines.append(
                f"{rule['id']},{rule['standard']},\"{rule['description']}\","
                f"{rule['status']},{rule['severity']}"
            )
        
        return "\n".join(csv_lines)
    
    def _format_as_html(self, data: Dict[str, Any]) -> str:
        """Format report data as HTML"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Compliance Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #333; }
                .summary { background: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
                table { border-collapse: collapse; width: 100%; }
                th, td { text-align: left; padding: 8px; }
                th { background-color: #f2f2f2; }
                tr:nth-child(even) { background-color: #f9f9f9; }
                .compliant { color: green; }
                .non-compliant { color: red; }
            </style>
        </head>
        <body>
            <h1>Compliance Report</h1>
            
            <div class="summary">
                <h2>Summary</h2>
                <p>Compliance Score: <strong>{0}%</strong></p>
                <p>Total Rules: <strong>{1}</strong></p>
                <p>Compliant Rules: <strong>{2}</strong></p>
                <p>Non-Compliant Rules: <strong>{3}</strong></p>
                <p>Generated: <strong>{4}</strong></p>
            </div>
            
            <h2>Details</h2>
            <table>
                <tr>
                    <th>Rule ID</th>
                    <th>Standard</th>
                    <th>Description</th>
                    <th>Status</th>
                    <th>Severity</th>
                </tr>
                {5}
            </table>
        </body>
        </html>
        """.format(
            data['summary']['compliance_score'],
            data['summary']['total_rules'],
            data['summary']['compliant_rules'],
            data['summary']['non_compliant_rules'],
            data['summary'].get('timestamp', datetime.now().isoformat()),
            self._format_rules_as_html_rows(data['details'].get('rules', []))
        )
        
        return html
    
    def _format_rules_as_html_rows(self, rules: List[Dict[str, Any]]) -> str:
        """Format rules as HTML table rows"""
        rows = []
        
        for rule in rules:
            status_class = "compliant" if rule['status'] == 'compliant' else "non-compliant"
            
            row = f"""
            <tr>
                <td>{rule['id']}</td>
                <td>{rule['standard']}</td>
                <td>{rule['description']}</td>
                <td class="{status_class}">{rule['status']}</td>
                <td>{rule['severity']}</td>
            </tr>
            """
            
            rows.append(row)
        
        return "".join(rows)
    
    def _format_as_pdf(self, data: Dict[str, Any]) -> str:
        """Format report data as PDF"""
        # Note: This would typically use a PDF generation library
        # For this lab, we'll just return a placeholder
        return "PDF generation not implemented in this version"


class ReportType:
    """Class for report type handling"""
    
    def __init__(self, type_config: Dict[str, Any]):
        """Initialize report type"""
        self.id = type_config.get('id', '')
        self.name = type_config.get('name', '')
        self.description = type_config.get('description', '')
        self.template = type_config.get('template', '')
        self.required_data = type_config.get('required_data', [])
        self.metadata = type_config.get('metadata', {})
    
    def generate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate report data according to this type
        
        Args:
            data: Raw data for report generation
            
        Returns:
            Dict[str, Any]: Processed report data
        """
        # Check if required data is present
        for field in self.required_data:
            if field not in data:
                logger.warning(f"Required field '{field}' missing for report type {self.id}")
                return {"error": f"Required field '{field}' missing"}
        
        # Process data based on report type
        if self.id == 'compliance_summary':
            return self._generate_compliance_summary(data)
        elif self.id == 'non_compliance':
            return self._generate_non_compliance(data)
        elif self.id == 'standard_specific':
            return self._generate_standard_specific(data)
        elif self.id == 'historical_trends':
            return self._generate_historical_trends(data)
        else:
            logger.warning(f"Unsupported report type: {self.id}")
            return data
    
    def _generate_compliance_summary(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate compliance summary report"""
        if 'summary' not in data:
            data['summary'] = {}
        
        # Calculate compliance score if not provided
        if 'compliance_score' not in data['summary'] and 'rules' in data:
            total = len(data['rules'])
            compliant = sum(1 for r in data['rules'] if r.get('status') == 'compliant')
            data['summary']['compliance_score'] = int((compliant / total) * 100) if total > 0 else 0
            data['summary']['total_rules'] = total
            data['summary']['compliant_rules'] = compliant
            data['summary']['non_compliant_rules'] = total - compliant
        
        # Add timestamp if not provided
        if 'timestamp' not in data['summary']:
            data['summary']['timestamp'] = datetime.now().isoformat()
        
        return {
            'report_type': 'compliance_summary',
            'summary': data['summary'],
            'details': {
                'rules': data.get('rules', [])
            }
        }
    
    def _generate_non_compliance(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate non-compliance report"""
        non_compliant_rules = []
        
        if 'rules' in data:
            non_compliant_rules = [r for r in data['rules'] if r.get('status') == 'non_compliant']
        
        # Calculate non-compliance statistics
        if 'summary' not in data:
            data['summary'] = {}
        
        total = len(data.get('rules', []))
        non_compliant = len(non_compliant_rules)
        
        data['summary']['total_rules'] = total
        data['summary']['non_compliant_rules'] = non_compliant
        data['summary']['non_compliance_rate'] = int((non_compliant / total) * 100) if total > 0 else 0
        
        # Group by severity
        by_severity = {}
        for rule in non_compliant_rules:
            severity = rule.get('severity', 'medium')
            if severity not in by_severity:
                by_severity[severity] = []
            by_severity[severity].append(rule)
        
        return {
            'report_type': 'non_compliance',
            'summary': data['summary'],
            'details': {
                'rules': non_compliant_rules,
                'by_severity': by_severity
            }
        }
    
    def _generate_standard_specific(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate standard-specific report"""
        if 'standard' not in data:
            return {"error": "Standard not specified"}
        
        standard = data['standard']
        standard_rules = []
        
        if 'rules' in data:
            standard_rules = [r for r in data['rules'] if r.get('standard') == standard]
        
        # Calculate standard-specific statistics
        if 'summary' not in data:
            data['summary'] = {}
        
        total = len(standard_rules)
        compliant = sum(1 for r in standard_rules if r.get('status') == 'compliant')
        
        data['summary']['standard'] = standard
        data['summary']['total_rules'] = total
        data['summary']['compliant_rules'] = compliant
        data['summary']['non_compliant_rules'] = total - compliant
        data['summary']['compliance_score'] = int((compliant / total) * 100) if total > 0 else 0
        
        return {
            'report_type': 'standard_specific',
            'standard': standard,
            'summary': data['summary'],
            'details': {
                'rules': standard_rules
            }
        }
    
    def _generate_historical_trends(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate historical trends report"""
        if 'historical_data' not in data:
            return {"error": "Historical data not provided"}
        
        historical_data = data['historical_data']
        trend_data = []
        
        for period in historical_data:
            period_data = {
                'period': period['period'],
                'compliance_score': period.get('compliance_score', 0),
                'compliant_rules': period.get('compliant_rules', 0),
                'non_compliant_rules': period.get('non_compliant_rules', 0),
                'total_rules': period.get('total_rules', 0)
            }
            trend_data.append(period_data)
        
        # Sort by period
        trend_data.sort(key=lambda x: x['period'])
        
        # Calculate trend
        if len(trend_data) >= 2:
            first = trend_data[0]['compliance_score']
            last = trend_data[-1]['compliance_score']
            trend = last - first
        else:
            trend = 0
        
        return {
            'report_type': 'historical_trends',
            'summary': {
                'trend': trend,
                'periods': len(trend_data)
            },
            'details': {
                'trend_data': trend_data
            }
        }


class ReportEngine:
    """Main class for regulatory reporting"""
    
    def __init__(self, config_file: str):
        """
        Initialize report engine
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = {}
        self.report_types = {}
        self.formats = {}
        self.is_initialized = False
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the report engine"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            self._load_report_types()
            self._load_formats()
            
            self.is_initialized = True
            logger.info("Report engine initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize report engine: {str(e)}")
            self.is_initialized = False
    
    def _load_report_types(self) -> None:
        """Load report types from configuration"""
        self.report_types = {}
        
        try:
            for type_config in self.config['reporting']['report_types']:
                report_type = ReportType(type_config)
                self.report_types[report_type.id] = report_type
            
            logger.info(f"Loaded {len(self.report_types)} report types")
        except Exception as e:
            logger.error(f"Failed to load report types: {str(e)}")
    
    def _load_formats(self) -> None:
        """Load report formats from configuration"""
        self.formats = {}
        
        try:
            for format_config in self.config['reporting']['formats']:
                report_format = ReportFormat(format_config)
                self.formats[report_format.id] = report_format
            
            logger.info(f"Loaded {len(self.formats)} report formats")
        except Exception as e:
            logger.error(f"Failed to load report formats: {str(e)}")
    
    def generate_report(self, report_type: str, data: Dict[str, Any], format: str = 'json', 
                       standard: str = None, report_id: str = None) -> str:
        """
        Generate a regulatory report
        
        Args:
            report_type: Type of report to generate
            data: Data for report generation
            format: Format of the generated report
            standard: Optional standard for standard-specific reports
            report_id: Optional report ID
            
        Returns:
            str: Generated report in the specified format
        """
        if report_type not in self.report_types:
            logger.error(f"Unknown report type: {report_type}")
            return json.dumps({"error": f"Unknown report type: {report_type}"})
        
        if format not in self.formats:
            logger.error(f"Unknown report format: {format}")
            return json.dumps({"error": f"Unknown report format: {format}"})
        
        # Add standard to data if provided
        if standard:
            data['standard'] = standard
        
        # Add report ID to data if provided
        if report_id:
            data['report_id'] = report_id
        else:
            data['report_id'] = f"RPT-{int(time.time())}"
        
        # Generate report data
        report_data = self.report_types[report_type].generate(data)
        
        # Format report
        formatted_report = self.formats[format].format_report(report_data)
        
        return formatted_report
    
    def get_scheduled_reports(self) -> List[Dict[str, Any]]:
        """
        Get list of scheduled reports
        
        Returns:
            List[Dict[str, Any]]: List of scheduled reports
        """
        if 'reporting' not in self.config or 'scheduled_reports' not in self.config['reporting']:
            return []
        
        return self.config['reporting']['scheduled_reports'].get('schedules', [])
    
    def schedule_report(self, schedule: Dict[str, Any]) -> bool:
        """
        Schedule a report for periodic generation
        
        Args:
            schedule: Report schedule configuration
            
        Returns:
            bool: True if report was scheduled successfully, False otherwise
        """
        try:
            if 'reporting' not in self.config:
                self.config['reporting'] = {}
            
            if 'scheduled_reports' not in self.config['reporting']:
                self.config['reporting']['scheduled_reports'] = {
                    'schedules': []
                }
            
            self.config['reporting']['scheduled_reports']['schedules'].append(schedule)
            
            # Save updated configuration
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            
            logger.info(f"Scheduled report: {schedule.get('report_type')} ({schedule.get('frequency')})")
            return True
        except Exception as e:
            logger.error(f"Failed to schedule report: {str(e)}")
            return False
    
    def get_report_types(self) -> List[Dict[str, Any]]:
        """
        Get available report types
        
        Returns:
            List[Dict[str, Any]]: List of available report types
        """
        return [
            {
                'id': rt.id,
                'name': rt.name,
                'description': rt.description
            }
            for rt in self.report_types.values()
        ]
    
    def get_formats(self) -> List[Dict[str, Any]]:
        """
        Get available report formats
        
        Returns:
            List[Dict[str, Any]]: List of available report formats
        """
        return [
            {
                'id': rf.id,
                'name': rf.name,
                'description': rf.description
            }
            for rf in self.formats.values()
        ]


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    if len(sys.argv) < 2:
        print("Usage: python regulatory_reporting.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    engine = ReportEngine(config_file)
    
    if not engine.is_initialized:
        print("Failed to initialize report engine")
        sys.exit(1)
    
    print(f"Available report types: {', '.join(engine.report_types.keys())}")
    print(f"Available formats: {', '.join(engine.formats.keys())}")
