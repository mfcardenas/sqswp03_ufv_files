#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reporting Engine Module
----------------------
This module implements the automated report generation system for requirements metrics.
It handles scheduled reports, multiple output formats, and custom report templates.

Functions:
- Generate reports in multiple formats
- Apply custom templates and branding
- Schedule automated reports
- Distribute reports to stakeholders
"""

import json
import logging
import datetime
import os
import time
import threading
from typing import Dict, List, Any, Optional, Union, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("reporting_engine.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ReportingEngine")

class ReportingEngine:
    """
    Reporting Engine for Requirements Analytics
    
    This class provides functionality to:
    - Generate reports in multiple formats (PDF, Excel, HTML)
    - Apply custom templates and branding
    - Schedule automated reports
    - Distribute reports to stakeholders
    """
    
    def __init__(self, analytics_engine=None, kpi_monitor=None):
        """
        Initialize the reporting engine
        
        Args:
            analytics_engine: Optional analytics engine instance
            kpi_monitor: Optional KPI monitor instance
        """
        logger.info("Initializing ReportingEngine")
        
        self.analytics_engine = analytics_engine
        self.kpi_monitor = kpi_monitor
        self.data_dir = os.path.join("data", "reports")
        self.templates_dir = os.path.join("templates", "reports")
        self.scheduled_reports = []
        self.scheduling_thread = None
        self.is_scheduling = False
        
        # Ensure directories exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.templates_dir, exist_ok=True)
        
        # Define report types
        self.report_types = {
            "quality": {
                "name": "Requirements Quality Report",
                "description": "Comprehensive quality metrics and analysis",
                "sections": ["quality_summary", "defect_analysis", "quality_trends", "recommendations"]
            },
            "efficiency": {
                "name": "Process Efficiency Report",
                "description": "Analysis of requirements engineering process efficiency",
                "sections": ["efficiency_summary", "review_metrics", "efficiency_trends", "recommendations"]
            },
            "compliance": {
                "name": "Compliance Report",
                "description": "Requirements compliance with standards and regulations",
                "sections": ["compliance_summary", "standards_adherence", "compliance_trends", "actions"]
            },
            "executive": {
                "name": "Executive Summary",
                "description": "High-level overview of requirements engineering metrics",
                "sections": ["kpi_summary", "key_trends", "insights", "recommendations"]
            },
            "comprehensive": {
                "name": "Comprehensive Requirements Report",
                "description": "Complete analysis of all requirements metrics",
                "sections": ["executive_summary", "quality_metrics", "process_metrics", 
                            "compliance_metrics", "trends", "insights", "recommendations"]
            }
        }
        
        logger.info("ReportingEngine initialized successfully")
    
    def generate_report(self, report_type: str, 
                       format_type: str = "html", 
                       template_id: str = None,
                       custom_title: str = None,
                       start_date: str = None,
                       end_date: str = None) -> Dict[str, Any]:
        """
        Generate a report of the specified type and format
        
        Args:
            report_type: Type of report to generate
            format_type: Output format (html, pdf, excel)
            template_id: Optional template identifier
            custom_title: Optional custom report title
            start_date: Optional start date for report period (ISO format)
            end_date: Optional end date for report period (ISO format)
            
        Returns:
            Dict containing report information
        """
        logger.info(f"Generating {format_type} report of type: {report_type}")
        
        # Validate report type
        if report_type not in self.report_types:
            valid_types = ", ".join(self.report_types.keys())
            logger.error(f"Invalid report type: {report_type}. Valid types: {valid_types}")
            raise ValueError(f"Invalid report type: {report_type}. Valid types: {valid_types}")
        
        # Validate format type
        valid_formats = ["html", "pdf", "excel"]
        if format_type not in valid_formats:
            valid_formats_str = ", ".join(valid_formats)
            logger.error(f"Invalid format type: {format_type}. Valid formats: {valid_formats_str}")
            raise ValueError(f"Invalid format type: {format_type}. Valid formats: {valid_formats_str}")
        
        # Set default dates if not provided
        if not end_date:
            end_date = datetime.datetime.now().isoformat()
        
        if not start_date:
            # Default to 30 days before end date
            end_dt = datetime.datetime.fromisoformat(end_date)
            start_dt = end_dt - datetime.timedelta(days=30)
            start_date = start_dt.isoformat()
        
        # Get report data
        report_data = self._collect_report_data(report_type, start_date, end_date)
        
        # Apply template if specified
        if template_id:
            report_data = self._apply_template(report_data, template_id)
        
        # Set custom title if provided
        if custom_title:
            report_data["title"] = custom_title
        
        # Generate report in specified format
        report_file = self._generate_report_file(report_data, format_type)
        
        # Log report generation
        logger.info(f"Generated {format_type} report: {report_file}")
        
        # Return report information
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "report_type": report_type,
            "format": format_type,
            "title": report_data.get("title", self.report_types[report_type]["name"]),
            "period": {
                "start": start_date,
                "end": end_date
            },
            "file_path": report_file
        }
    
    def _collect_report_data(self, report_type: str, 
                            start_date: str, 
                            end_date: str) -> Dict[str, Any]:
        """
        Collect data for the specified report type
        
        Args:
            report_type: Type of report to generate
            start_date: Start date for report period (ISO format)
            end_date: End date for report period (ISO format)
            
        Returns:
            Dict containing report data
        """
        logger.info(f"Collecting data for report type: {report_type}")
        
        # Initialize report data with metadata
        report_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "report_type": report_type,
            "title": self.report_types[report_type]["name"],
            "period": {
                "start": start_date,
                "end": end_date
            },
            "sections": []
        }
        
        # Get analytics data if analytics engine is available
        if self.analytics_engine:
            # Get data based on report type
            if report_type == "quality":
                report_data.update(self.analytics_engine.generate_report_data("quality"))
            elif report_type == "efficiency":
                report_data.update(self.analytics_engine.generate_report_data("efficiency"))
            elif report_type == "compliance":
                report_data.update(self.analytics_engine.generate_report_data("compliance"))
            elif report_type == "executive":
                report_data.update(self.analytics_engine.generate_report_data("executive"))
            else:  # comprehensive
                report_data.update(self.analytics_engine.generate_report_data("comprehensive"))
        else:
            # Generate sample data if no analytics engine
            report_data.update(self._generate_sample_report_data(report_type, start_date, end_date))
        
        # Get KPI data if KPI monitor is available
        if self.kpi_monitor:
            kpi_dashboard = self.kpi_monitor.get_kpi_dashboard()
            report_data["kpi_data"] = kpi_dashboard
        
        # Add sections based on report type
        report_data["sections"] = self.report_types[report_type]["sections"]
        
        return report_data
    
    def _generate_sample_report_data(self, report_type: str, 
                                   start_date: str, 
                                   end_date: str) -> Dict[str, Any]:
        """
        Generate sample report data when no analytics engine is available
        
        Args:
            report_type: Type of report to generate
            start_date: Start date for report period (ISO format)
            end_date: End date for report period (ISO format)
            
        Returns:
            Dict containing sample report data
        """
        import random
        
        logger.info(f"Generating sample data for report type: {report_type}")
        
        # Parse dates
        start_dt = datetime.datetime.fromisoformat(start_date)
        end_dt = datetime.datetime.fromisoformat(end_date)
        days_diff = (end_dt - start_dt).days
        
        # Common metrics
        metrics = {
            "requirements_quality": round(random.uniform(75, 90), 2),
            "review_efficiency": round(random.uniform(30, 50), 1),
            "defect_density": round(random.uniform(0.05, 0.2), 3),
            "requirements_completeness": round(random.uniform(80, 95), 2)
        }
        
        # Generate trend data
        trend_data = {}
        for metric, value in metrics.items():
            data_points = []
            for i in range(min(30, days_diff + 1)):
                day = start_dt + datetime.timedelta(days=i)
                
                # Generate value with a slight upward trend
                trend_factor = i / max(1, days_diff)
                if metric in ["requirements_quality", "requirements_completeness"]:
                    # Increasing trend is good
                    day_value = value * 0.9 + (value * 0.2 * trend_factor)
                else:
                    # Decreasing trend is good
                    day_value = value * 1.1 - (value * 0.2 * trend_factor)
                
                # Add random variation
                day_value += random.uniform(-value * 0.05, value * 0.05)
                
                data_points.append((day.isoformat(), round(day_value, 2)))
            
            trend_data[metric] = data_points
        
        # Generate insights
        insights = []
        if metrics["requirements_quality"] < 80:
            insights.append({
                "type": "quality",
                "priority": "medium",
                "title": "Quality Improvement Needed",
                "description": f"Requirements quality score is {metrics['requirements_quality']}, which is below the target of 85."
            })
        
        if metrics["defect_density"] > 0.1:
            insights.append({
                "type": "risk",
                "priority": "high",
                "title": "High Defect Density",
                "description": f"Defect density is {metrics['defect_density']} defects per requirement, which exceeds the target of 0.1."
            })
        
        # Generate recommendations
        recommendations = [
            {
                "title": "Improve Requirements Quality",
                "description": "Implement measures to improve overall requirements quality.",
                "actions": [
                    "Provide additional training on requirements authoring",
                    "Implement quality checklists for requirements",
                    "Conduct regular quality audits"
                ]
            },
            {
                "title": "Optimize Review Process",
                "description": "Streamline the review process to reduce review time.",
                "actions": [
                    "Reduce the number of reviewers for smaller changes",
                    "Implement parallel reviews where appropriate",
                    "Set up automated pre-reviews to catch common issues"
                ]
            }
        ]
        
        # Build report data based on type
        report_data = {
            "metrics_summary": metrics,
            "trend_data": trend_data,
            "insights": insights,
            "recommendations": recommendations
        }
        
        # Add report-specific data
        if report_type == "quality":
            report_data["quality_analysis"] = {
                "overall_score": metrics["requirements_quality"],
                "quality_components": {
                    "completeness": round(random.uniform(70, 95), 2),
                    "correctness": round(random.uniform(70, 95), 2),
                    "consistency": round(random.uniform(70, 95), 2),
                    "clarity": round(random.uniform(70, 95), 2),
                    "verifiability": round(random.uniform(70, 95), 2)
                },
                "defect_trends": trend_data["defect_density"]
            }
            
        elif report_type == "efficiency":
            report_data["efficiency_analysis"] = {
                "review_time": metrics["review_efficiency"],
                "efficiency_metrics": {
                    "requirements_per_day": round(random.uniform(5, 15), 1),
                    "review_cycle_time": round(random.uniform(2, 5), 1),
                    "approval_time": round(random.uniform(10, 30), 1)
                },
                "efficiency_trends": trend_data["review_efficiency"]
            }
            
        elif report_type == "compliance":
            report_data["compliance_analysis"] = {
                "compliance_score": metrics["requirements_completeness"],
                "standards_compliance": {
                    "iso_29148": round(random.uniform(80, 95), 2),
                    "internal_standards": round(random.uniform(80, 95), 2),
                    "regulatory_requirements": round(random.uniform(80, 95), 2)
                },
                "compliance_trends": trend_data["requirements_completeness"]
            }
            
        # For executive and comprehensive, include all data
        
        return report_data
    
    def _apply_template(self, report_data: Dict[str, Any], 
                       template_id: str) -> Dict[str, Any]:
        """
        Apply a template to the report data
        
        Args:
            report_data: Report data to format
            template_id: Template identifier
            
        Returns:
            Dict containing formatted report data
        """
        logger.info(f"Applying template {template_id} to report")
        
        # In a real implementation, this would load and apply a template
        # For this lab, we'll just add template information
        
        report_data["template"] = {
            "id": template_id,
            "name": f"Template {template_id}",
            "applied": True
        }
        
        return report_data
    
    def _generate_report_file(self, report_data: Dict[str, Any], 
                             format_type: str) -> str:
        """
        Generate a report file in the specified format
        
        Args:
            report_data: Report data to format
            format_type: Output format (html, pdf, excel)
            
        Returns:
            Path to the generated report file
        """
        logger.info(f"Generating report file in {format_type} format")
        
        # Create a unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_type = report_data["report_type"]
        filename = f"report_{report_type}_{timestamp}.{format_type}"
        file_path = os.path.join(self.data_dir, filename)
        
        # In a real implementation, this would generate the actual file
        # For this lab, we'll create a simple file with JSON data
        
        if format_type == "html":
            # Generate simple HTML report
            html_content = self._generate_html_report(report_data)
            
            with open(file_path, 'w') as f:
                f.write(html_content)
                
        elif format_type == "pdf":
            # In a real implementation, this would generate a PDF
            # For this lab, we'll create a text file with a note
            
            with open(file_path, 'w') as f:
                f.write(f"PDF Report for {report_data['title']}\n")
                f.write(f"Generated: {report_data['timestamp']}\n\n")
                f.write("This is a simulated PDF report. In a real implementation, this would be a PDF file.")
                
        elif format_type == "excel":
            # In a real implementation, this would generate an Excel file
            # For this lab, we'll create a text file with a note
            
            with open(file_path, 'w') as f:
                f.write(f"Excel Report for {report_data['title']}\n")
                f.write(f"Generated: {report_data['timestamp']}\n\n")
                f.write("This is a simulated Excel report. In a real implementation, this would be an Excel file.")
        
        logger.info(f"Report file generated: {file_path}")
        return file_path
    
    def _generate_html_report(self, report_data: Dict[str, Any]) -> str:
        """
        Generate HTML content for a report
        
        Args:
            report_data: Report data to format
            
        Returns:
            HTML content as a string
        """
        # This is a simplified HTML generator
        # In a real implementation, this would use a proper template engine
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{report_data['title']}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; color: #333; }}
                .report-header {{ text-align: center; margin-bottom: 30px; }}
                .report-title {{ font-size: 24px; margin-bottom: 10px; }}
                .report-subtitle {{ font-size: 16px; color: #666; margin-bottom: 5px; }}
                .report-date {{ font-size: 14px; color: #888; }}
                .section {{ margin-bottom: 30px; }}
                .section-title {{ font-size: 18px; margin-bottom: 15px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }}
                .metric-row {{ display: flex; margin-bottom: 15px; }}
                .metric-name {{ width: 200px; font-weight: bold; }}
                .metric-value {{ width: 100px; text-align: right; }}
                .metric-trend {{ width: 100px; text-align: right; }}
                .recommendation {{ background-color: #f8f8f8; padding: 15px; margin-bottom: 15px; border-left: 4px solid #4a90e2; }}
                .recommendation-title {{ font-weight: bold; margin-bottom: 10px; }}
                .recommendation-actions {{ margin-top: 10px; }}
                .recommendation-action {{ margin-bottom: 5px; }}
                .insight {{ background-color: #f8f8f8; padding: 15px; margin-bottom: 15px; }}
                .insight-high {{ border-left: 4px solid #e25a4a; }}
                .insight-medium {{ border-left: 4px solid #e2a94a; }}
                .insight-low {{ border-left: 4px solid #4a90e2; }}
                .insight-title {{ font-weight: bold; margin-bottom: 5px; }}
                .trend-chart {{ height: 200px; background-color: #f8f8f8; margin-bottom: 15px; display: flex; align-items: center; justify-content: center; }}
                .footer {{ margin-top: 50px; text-align: center; font-size: 12px; color: #888; }}
            </style>
        </head>
        <body>
            <div class="report-header">
                <div class="report-title">{report_data['title']}</div>
                <div class="report-subtitle">Report Type: {report_data['report_type']}</div>
                <div class="report-date">Period: {report_data['period']['start']} to {report_data['period']['end']}</div>
                <div class="report-date">Generated: {report_data['timestamp']}</div>
            </div>
        """
        
        # Add executive summary section
        html += """
            <div class="section">
                <div class="section-title">Executive Summary</div>
        """
        
        # Add metrics summary if available
        if "metrics_summary" in report_data:
            html += """
                <div class="metrics-summary">
            """
            
            for metric_name, metric_value in report_data["metrics_summary"].items():
                display_name = metric_name.replace("_", " ").title()
                html += f"""
                    <div class="metric-row">
                        <div class="metric-name">{display_name}</div>
                        <div class="metric-value">{metric_value}</div>
                    </div>
                """
            
            html += """
                </div>
            """
        
        html += """
            </div>
        """
        
        # Add insights section if available
        if "insights" in report_data and report_data["insights"]:
            html += """
            <div class="section">
                <div class="section-title">Key Insights</div>
            """
            
            for insight in report_data["insights"]:
                priority_class = f"insight-{insight.get('priority', 'medium')}"
                html += f"""
                <div class="insight {priority_class}">
                    <div class="insight-title">{insight.get('title', 'Insight')}</div>
                    <div>{insight.get('description', '')}</div>
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add recommendations section if available
        if "recommendations" in report_data and report_data["recommendations"]:
            html += """
            <div class="section">
                <div class="section-title">Recommendations</div>
            """
            
            for recommendation in report_data["recommendations"]:
                html += f"""
                <div class="recommendation">
                    <div class="recommendation-title">{recommendation.get('title', 'Recommendation')}</div>
                    <div>{recommendation.get('description', '')}</div>
                """
                
                if "actions" in recommendation and recommendation["actions"]:
                    html += """
                    <div class="recommendation-actions">
                    """
                    
                    for action in recommendation["actions"]:
                        html += f"""
                        <div class="recommendation-action">• {action}</div>
                        """
                    
                    html += """
                    </div>
                    """
                
                html += """
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add trend charts section if available
        if "trend_data" in report_data and report_data["trend_data"]:
            html += """
            <div class="section">
                <div class="section-title">Trend Analysis</div>
            """
            
            for metric_name, data_points in report_data["trend_data"].items():
                display_name = metric_name.replace("_", " ").title()
                html += f"""
                <div class="trend-section">
                    <div class="section-title">{display_name} Trend</div>
                    <div class="trend-chart">
                        [This would be a chart in a real implementation - {len(data_points)} data points]
                    </div>
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add report-specific sections based on type
        if report_data["report_type"] == "quality" and "quality_analysis" in report_data:
            quality = report_data["quality_analysis"]
            html += """
            <div class="section">
                <div class="section-title">Quality Analysis</div>
            """
            
            if "quality_components" in quality:
                html += """
                <div class="quality-components">
                    <div class="section-title">Quality Components</div>
                """
                
                for component, value in quality["quality_components"].items():
                    display_name = component.title()
                    html += f"""
                    <div class="metric-row">
                        <div class="metric-name">{display_name}</div>
                        <div class="metric-value">{value}</div>
                    </div>
                    """
                
                html += """
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add footer
        html += """
            <div class="footer">
                Generated by Requirements Reporting Engine<br>
                ISO/IEC/IEEE 29148:2011 Compliance Report
            </div>
        </body>
        </html>
        """
        
        return html
    
    def schedule_report(self, report_config: Dict[str, Any]) -> str:
        """
        Schedule a report for automatic generation
        
        Args:
            report_config: Report configuration
            
        Returns:
            Scheduled report ID
        """
        logger.info(f"Scheduling report: {report_config.get('report_type')}")
        
        # Validate report configuration
        required_fields = ["report_type", "format", "schedule"]
        for field in required_fields:
            if field not in report_config:
                logger.error(f"Missing required field '{field}' in report configuration")
                raise ValueError(f"Missing required field '{field}' in report configuration")
        
        # Generate a unique ID for the scheduled report
        report_id = f"report_{len(self.scheduled_reports) + 1}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Add report to scheduled reports
        scheduled_report = {
            "id": report_id,
            "config": report_config,
            "next_run": self._calculate_next_run(report_config["schedule"]),
            "last_run": None,
            "last_report": None
        }
        
        self.scheduled_reports.append(scheduled_report)
        
        # Start scheduler if not already running
        if not self.is_scheduling:
            self._start_scheduler()
        
        logger.info(f"Report scheduled with ID: {report_id}")
        return report_id
    
    def _calculate_next_run(self, schedule: Dict[str, Any]) -> str:
        """
        Calculate the next run time based on schedule
        
        Args:
            schedule: Schedule configuration
            
        Returns:
            ISO format timestamp for next run
        """
        now = datetime.datetime.now()
        
        if schedule["type"] == "daily":
            # Daily at specified time
            hour = schedule.get("hour", 0)
            minute = schedule.get("minute", 0)
            
            next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # If the time has already passed today, schedule for tomorrow
            if next_run <= now:
                next_run += datetime.timedelta(days=1)
                
        elif schedule["type"] == "weekly":
            # Weekly on specified day at specified time
            day = schedule.get("day", 0)  # 0=Monday, 6=Sunday
            hour = schedule.get("hour", 0)
            minute = schedule.get("minute", 0)
            
            # Calculate days until next specified day
            days_ahead = day - now.weekday()
            if days_ahead <= 0:  # Target day already happened this week
                days_ahead += 7
                
            next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0) + datetime.timedelta(days=days_ahead)
            
        elif schedule["type"] == "monthly":
            # Monthly on specified day at specified time
            day = schedule.get("day", 1)
            hour = schedule.get("hour", 0)
            minute = schedule.get("minute", 0)
            
            # Start with the first day of next month
            if now.month == 12:
                next_month = now.replace(year=now.year + 1, month=1, day=1)
            else:
                next_month = now.replace(month=now.month + 1, day=1)
                
            # Adjust to specified day, handling month length
            month_length = (next_month.replace(month=next_month.month % 12 + 1, day=1) - datetime.timedelta(days=1)).day
            day = min(day, month_length)
            
            next_run = next_month.replace(day=day, hour=hour, minute=minute, second=0, microsecond=0)
            
            # If the day has not yet passed this month, schedule for this month
            current_month_day = min(day, (datetime.datetime(now.year, now.month % 12 + 1, 1) - datetime.timedelta(days=1)).day)
            this_month_run = now.replace(day=current_month_day, hour=hour, minute=minute, second=0, microsecond=0)
            
            if this_month_run > now:
                next_run = this_month_run
                
        else:
            # Default to daily at midnight
            next_run = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        
        return next_run.isoformat()
    
    def _start_scheduler(self) -> None:
        """
        Start the report scheduler
        """
        if self.is_scheduling:
            logger.warning("Scheduler already running")
            return
        
        self.is_scheduling = True
        logger.info("Starting report scheduler")
        
        def scheduler_worker():
            while self.is_scheduling:
                try:
                    self._check_scheduled_reports()
                    time.sleep(60)  # Check every minute
                except Exception as e:
                    logger.error(f"Error in report scheduler: {str(e)}")
                    time.sleep(60)  # Wait a minute before retrying
        
        self.scheduling_thread = threading.Thread(target=scheduler_worker)
        self.scheduling_thread.daemon = True
        self.scheduling_thread.start()
    
    def _stop_scheduler(self) -> None:
        """
        Stop the report scheduler
        """
        logger.info("Stopping report scheduler")
        self.is_scheduling = False
        if self.scheduling_thread:
            self.scheduling_thread.join(timeout=10)
    
    def _check_scheduled_reports(self) -> None:
        """
        Check for reports that need to be generated
        """
        now = datetime.datetime.now()
        now_iso = now.isoformat()
        
        for report in self.scheduled_reports:
            next_run_iso = report["next_run"]
            
            # Check if it's time to run the report
            if next_run_iso <= now_iso:
                try:
                    # Generate the report
                    config = report["config"]
                    report_info = self.generate_report(
                        report_type=config["report_type"],
                        format_type=config["format"],
                        template_id=config.get("template_id"),
                        custom_title=config.get("title"),
                        start_date=config.get("start_date"),
                        end_date=config.get("end_date")
                    )
                    
                    # Update report status
                    report["last_run"] = now_iso
                    report["last_report"] = report_info
                    report["next_run"] = self._calculate_next_run(config["schedule"])
                    
                    logger.info(f"Generated scheduled report: {report['id']}")
                    
                    # Distribute report if configured
                    if "distribution" in config:
                        self._distribute_report(report_info, config["distribution"])
                        
                except Exception as e:
                    logger.error(f"Error generating scheduled report {report['id']}: {str(e)}")
    
    def _distribute_report(self, report_info: Dict[str, Any], 
                          distribution: Dict[str, Any]) -> None:
        """
        Distribute a report according to configuration
        
        Args:
            report_info: Information about the generated report
            distribution: Distribution configuration
        """
        logger.info(f"Distributing report: {report_info.get('file_path')}")
        
        # In a real implementation, this would send emails, upload to servers, etc.
        # For this lab, we'll just log the distribution
        
        method = distribution.get("method", "log")
        
        if method == "email":
            recipients = distribution.get("recipients", [])
            logger.info(f"Would email report to: {', '.join(recipients)}")
            
        elif method == "upload":
            destination = distribution.get("destination", "")
            logger.info(f"Would upload report to: {destination}")
            
        else:
            logger.info(f"Report distributed via {method}")
    
    def get_report_templates(self) -> List[Dict[str, Any]]:
        """
        Get list of available report templates
        
        Returns:
            List of template information
        """
        # In a real implementation, this would scan the templates directory
        # For this lab, we'll return sample templates
        
        return [
            {
                "id": "default",
                "name": "Default Template",
                "description": "Standard report template",
                "formats": ["html", "pdf", "excel"]
            },
            {
                "id": "executive",
                "name": "Executive Template",
                "description": "Simplified template for executive reports",
                "formats": ["html", "pdf"]
            },
            {
                "id": "detailed",
                "name": "Detailed Analysis Template",
                "description": "Comprehensive template with detailed charts and tables",
                "formats": ["html", "pdf", "excel"]
            },
            {
                "id": "compliance",
                "name": "Compliance Template",
                "description": "Template focused on standards compliance",
                "formats": ["html", "pdf"]
            }
        ]
    
    def get_scheduled_reports(self) -> List[Dict[str, Any]]:
        """
        Get list of scheduled reports
        
        Returns:
            List of scheduled report information
        """
        return self.scheduled_reports
    
    def cancel_scheduled_report(self, report_id: str) -> bool:
        """
        Cancel a scheduled report
        
        Args:
            report_id: ID of the scheduled report to cancel
            
        Returns:
            True if successful, False otherwise
        """
        logger.info(f"Cancelling scheduled report: {report_id}")
        
        for i, report in enumerate(self.scheduled_reports):
            if report["id"] == report_id:
                del self.scheduled_reports[i]
                logger.info(f"Scheduled report cancelled: {report_id}")
                return True
        
        logger.warning(f"Scheduled report not found: {report_id}")
        return False


# Example usage
if __name__ == "__main__":
    # Create reporting engine
    reporting_engine = ReportingEngine()
    
    # Generate a report
    report_info = reporting_engine.generate_report("quality", "html")
    print(f"Generated report: {report_info['file_path']}")
    
    # Schedule a report
    schedule_config = {
        "report_type": "executive",
        "format": "pdf",
        "title": "Weekly Executive Summary",
        "schedule": {
            "type": "weekly",
            "day": 1,  # Monday
            "hour": 8,
            "minute": 0
        },
        "distribution": {
            "method": "email",
            "recipients": ["executives@example.com"]
        }
    }
    
    report_id = reporting_engine.schedule_report(schedule_config)
    print(f"Scheduled report ID: {report_id}")
    
    # Get available templates
    templates = reporting_engine.get_report_templates()
    print(f"Available templates: {len(templates)}")
    
    # Get scheduled reports
    scheduled = reporting_engine.get_scheduled_reports()
    print(f"Scheduled reports: {len(scheduled)}")
    
    # Cancel a scheduled report
    cancelled = reporting_engine.cancel_scheduled_report(report_id)
    print(f"Report cancelled: {cancelled}")
    
    # Stop scheduler
    reporting_engine._stop_scheduler()
