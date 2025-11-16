#!/usr/bin/env python3
"""
Requirements Risk Reporting Module
ISO/IEC/IEEE 29148:2011 Risk Reporting Implementation
"""

import json
import os
import sys
import logging
import argparse
from datetime import datetime
from typing import List, Dict, Any, Optional, Union
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from jinja2 import Environment, FileSystemLoader

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("risk_reporting.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RiskReporting:
    """Main class for risk reporting"""
    
    def __init__(self, config_file: str, risks_file: str, mitigations_file: str):
        """
        Initialize risk reporting
        
        Args:
            config_file: Path to configuration file
            risks_file: Path to risks data file
            mitigations_file: Path to mitigations data file
        """
        self.config_file = config_file
        self.risks_file = risks_file
        self.mitigations_file = mitigations_file
        self.config = {}
        self.risks = []
        self.mitigations = []
        self.is_initialized = False
        self.risk_levels = []
        self.risk_categories = []
        self.output_dir = "reports"
        self.initialize()
    
    def initialize(self) -> None:
        """Initialize the risk reporting"""
        try:
            # Ensure output directory exists
            os.makedirs(self.output_dir, exist_ok=True)
            
            # Load configuration
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            # Extract risk levels and categories
            self.risk_levels = self.config["riskManagement"]["riskLevels"]
            self.risk_categories = self.config["riskManagement"]["riskCategories"]
            
            # Load risks data
            with open(self.risks_file, 'r') as f:
                self.risks = json.load(f)
            
            # Load mitigations data
            with open(self.mitigations_file, 'r') as f:
                self.mitigations = json.load(f)
            
            self.is_initialized = True
            logger.info("Risk reporting initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize risk reporting: {str(e)}")
            self.is_initialized = False
    
    def generate_risk_summary(self) -> Dict[str, Any]:
        """
        Generate a summary of risks
        
        Returns:
            Dict[str, Any]: Risk summary data
        """
        total_risks = len(self.risks)
        
        # Count risks by level
        level_counts = {}
        for level in self.risk_levels:
            level_id = level["id"]
            level_counts[level_id] = len([r for r in self.risks if r["level"] == level_id])
        
        # Count risks by category
        category_counts = {}
        for category in self.risk_categories:
            category_id = category["id"]
            category_counts[category_id] = len([r for r in self.risks if r["category"] == category_id])
        
        # Count mitigations by status
        mitigation_status = {}
        status_list = set([m["status"] for m in self.mitigations])
        for status in status_list:
            mitigation_status[status] = len([m for m in self.mitigations if m["status"] == status])
        
        # Calculate risk exposure
        high_risks = len([r for r in self.risks if r["level"] in ["high", "critical"]])
        
        summary = {
            "total_risks": total_risks,
            "by_level": level_counts,
            "by_category": category_counts,
            "high_risk_percentage": (high_risks / total_risks * 100) if total_risks > 0 else 0,
            "mitigations": {
                "total": len(self.mitigations),
                "by_status": mitigation_status
            },
            "timestamp": datetime.now().isoformat()
        }
        
        return summary
    
    def plot_risk_distribution(self, output_file: str = "risk_distribution.png") -> str:
        """
        Generate a plot of risk distribution by level and category
        
        Args:
            output_file: Path to output file
            
        Returns:
            str: Path to generated plot
        """
        output_path = os.path.join(self.output_dir, output_file)
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
        
        # Count risks by level
        level_counts = {}
        for level in self.risk_levels:
            level_id = level["id"]
            level_name = level["name"]
            level_counts[level_name] = len([r for r in self.risks if r["level"] == level_id])
        
        # Count risks by category
        category_counts = {}
        for category in self.risk_categories:
            category_id = category["id"]
            category_name = category["name"]
            category_counts[category_name] = len([r for r in self.risks if r["category"] == category_id])
        
        # Plot distribution by level
        colors1 = plt.cm.Reds(np.linspace(0.4, 0.8, len(level_counts)))
        ax1.bar(level_counts.keys(), level_counts.values(), color=colors1)
        ax1.set_title('Risks by Level')
        ax1.set_ylabel('Number of Risks')
        ax1.set_xlabel('Risk Level')
        
        # Plot distribution by category
        colors2 = plt.cm.Blues(np.linspace(0.4, 0.8, len(category_counts)))
        ax2.bar(category_counts.keys(), category_counts.values(), color=colors2)
        ax2.set_title('Risks by Category')
        ax2.set_ylabel('Number of Risks')
        ax2.set_xlabel('Risk Category')
        
        # Rotate x-labels for better readability
        plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
        plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        
        logger.info(f"Generated risk distribution plot: {output_path}")
        return output_path
    
    def plot_mitigation_status(self, output_file: str = "mitigation_status.png") -> str:
        """
        Generate a plot of mitigation action statuses
        
        Args:
            output_file: Path to output file
            
        Returns:
            str: Path to generated plot
        """
        output_path = os.path.join(self.output_dir, output_file)
        
        # Count mitigations by status
        status_counts = {}
        for mitigation in self.mitigations:
            status = mitigation["status"]
            status_counts[status] = status_counts.get(status, 0) + 1
        
        # Create pie chart
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Define colors for different statuses
        status_colors = {
            "open": "#ffcc00",
            "in_progress": "#66b3ff",
            "completed": "#66cc99",
            "cancelled": "#ff6666",
            "on_hold": "#cccccc"
        }
        
        # Get colors for each status in the data
        colors = [status_colors.get(status, "#999999") for status in status_counts.keys()]
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            status_counts.values(), 
            labels=status_counts.keys(),
            autopct='%1.1f%%',
            startangle=90,
            colors=colors
        )
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        ax.set_title('Mitigation Actions by Status')
        
        # Set font size and style for labels and percentages
        plt.setp(autotexts, size=10, weight='bold')
        plt.setp(texts, size=12)
        
        plt.savefig(output_path)
        plt.close()
        
        logger.info(f"Generated mitigation status plot: {output_path}")
        return output_path
    
    def plot_risk_trend(self, trend_data: List[Dict[str, Any]], output_file: str = "risk_trend.png") -> str:
        """
        Generate a plot of risk trends over time
        
        Args:
            trend_data: List of risk data points over time
            output_file: Path to output file
            
        Returns:
            str: Path to generated plot
        """
        output_path = os.path.join(self.output_dir, output_file)
        
        # Create DataFrame from trend data
        df = pd.DataFrame(trend_data)
        
        # Convert dates to datetime objects
        df['date'] = pd.to_datetime(df['date'])
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot trend lines for each risk level
        for level in self.risk_levels:
            level_id = level["id"]
            level_name = level["name"]
            
            # Skip if column doesn't exist
            if level_id not in df.columns:
                continue
                
            # Plot line
            ax.plot(df['date'], df[level_id], label=level_name, marker='o', linewidth=2)
        
        # Set labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Risks')
        ax.set_title('Risk Trend Over Time')
        
        # Add legend and grid
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Format date axis
        plt.gcf().autofmt_xdate()
        
        # Save figure
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        
        logger.info(f"Generated risk trend plot: {output_path}")
        return output_path
    
    def generate_html_report(self, output_file: str = "risk_report.html") -> str:
        """
        Generate an HTML report of risks and mitigations
        
        Args:
            output_file: Path to output file
            
        Returns:
            str: Path to generated report
        """
        output_path = os.path.join(self.output_dir, output_file)
        
        # Generate summary data
        summary = self.generate_risk_summary()
        
        # Generate plots
        distribution_plot = os.path.basename(self.plot_risk_distribution())
        mitigation_plot = os.path.basename(self.plot_mitigation_status())
        
        # Create sample trend data
        trend_data = [
            {"date": (datetime.now().replace(day=1) - pd.DateOffset(months=i)).strftime("%Y-%m-%d"),
             "low": np.random.randint(5, 15),
             "medium": np.random.randint(10, 20),
             "high": np.random.randint(5, 15),
             "critical": np.random.randint(0, 5)
            } for i in range(6, 0, -1)
        ]
        trend_plot = os.path.basename(self.plot_risk_trend(trend_data))
        
        # Prepare data for template
        template_data = {
            "summary": summary,
            "risks": sorted(self.risks, key=lambda x: x.get("level", ""), reverse=True),
            "mitigations": self.mitigations,
            "distribution_plot": distribution_plot,
            "mitigation_plot": mitigation_plot,
            "trend_plot": trend_plot,
            "risk_levels": {level["id"]: level for level in self.risk_levels},
            "risk_categories": {cat["id"]: cat for cat in self.risk_categories},
            "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Create Jinja2 environment
        env = Environment(loader=FileSystemLoader("."))
        
        # Create basic template if it doesn't exist
        template_file = "risk_report_template.html"
        if not os.path.exists(template_file):
            with open(template_file, "w") as f:
                f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Requirements Risk Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .header {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .summary-box {
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .plot-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin-bottom: 20px;
        }
        .plot {
            margin: 10px;
            text-align: center;
        }
        .plot img {
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f8f8f8;
        }
        .risk-critical {
            background-color: #ffdddd;
        }
        .risk-high {
            background-color: #ffe6cc;
        }
        .risk-medium {
            background-color: #ffffcc;
        }
        .risk-low {
            background-color: #e6ffe6;
        }
        .footer {
            margin-top: 30px;
            text-align: center;
            font-size: 0.8em;
            color: #777;
            border-top: 1px solid #ddd;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Requirements Risk Report</h1>
        <p>ISO/IEC/IEEE 29148:2011 Risk Assessment</p>
    </div>

    <div class="summary-box">
        <h2>Executive Summary</h2>
        <p>Total Risks: {{ summary.total_risks }}</p>
        <p>Risk Breakdown:</p>
        <ul>
            {% for level, count in summary.by_level.items() %}
            <li>{{ risk_levels[level].name }}: {{ count }}</li>
            {% endfor %}
        </ul>
        <p>High Risk Percentage: {{ "%.1f"|format(summary.high_risk_percentage) }}%</p>
        <p>Total Mitigation Actions: {{ summary.mitigations.total }}</p>
        <ul>
            {% for status, count in summary.mitigations.by_status.items() %}
            <li>{{ status|capitalize }}: {{ count }}</li>
            {% endfor %}
        </ul>
    </div>

    <h2>Risk Analysis</h2>
    <div class="plot-container">
        <div class="plot">
            <h3>Risk Distribution</h3>
            <img src="{{ distribution_plot }}" alt="Risk Distribution">
        </div>
        <div class="plot">
            <h3>Mitigation Status</h3>
            <img src="{{ mitigation_plot }}" alt="Mitigation Status">
        </div>
    </div>
    <div class="plot">
        <h3>Risk Trend</h3>
        <img src="{{ trend_plot }}" alt="Risk Trend">
    </div>

    <h2>Detailed Risk Register</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Description</th>
                <th>Category</th>
                <th>Level</th>
                <th>Probability</th>
                <th>Impact</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for risk in risks %}
            <tr class="risk-{{ risk.level }}">
                <td>{{ risk.id }}</td>
                <td>{{ risk.description }}</td>
                <td>{{ risk_categories[risk.category].name }}</td>
                <td>{{ risk_levels[risk.level].name }}</td>
                <td>{{ risk.probability }}</td>
                <td>{{ risk.impact }}</td>
                <td>{{ risk.status }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>Mitigation Actions</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Related Risk</th>
                <th>Description</th>
                <th>Strategy</th>
                <th>Owner</th>
                <th>Due Date</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for action in mitigations %}
            <tr>
                <td>{{ action.id }}</td>
                <td>{{ action.related_risk }}</td>
                <td>{{ action.description }}</td>
                <td>{{ action.strategy }}</td>
                <td>{{ action.owner }}</td>
                <td>{{ action.due_date }}</td>
                <td>{{ action.status }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <div class="footer">
        <p>Generated on {{ generated_on }} | ISO/IEC/IEEE 29148:2011 Requirements Risk Report</p>
    </div>
</body>
</html>""")
        
        # Load template and render
        template = env.get_template(template_file)
        output = template.render(**template_data)
        
        # Write output
        with open(output_path, "w") as f:
            f.write(output)
        
        logger.info(f"Generated HTML report: {output_path}")
        return output_path
    
    def generate_csv_report(self, output_file: str = "risk_report.csv") -> str:
        """
        Generate a CSV report of risks
        
        Args:
            output_file: Path to output file
            
        Returns:
            str: Path to generated report
        """
        output_path = os.path.join(self.output_dir, output_file)
        
        # Convert risks to DataFrame
        df = pd.DataFrame(self.risks)
        
        # Add level and category names
        def get_level_name(level_id):
            for level in self.risk_levels:
                if level["id"] == level_id:
                    return level["name"]
            return level_id
        
        def get_category_name(category_id):
            for category in self.risk_categories:
                if category["id"] == category_id:
                    return category["name"]
            return category_id
        
        # Add columns with names
        df["level_name"] = df["level"].apply(get_level_name)
        df["category_name"] = df["category"].apply(get_category_name)
        
        # Save to CSV
        df.to_csv(output_path, index=False)
        
        logger.info(f"Generated CSV report: {output_path}")
        return output_path
    
    def generate_all_reports(self) -> Dict[str, str]:
        """
        Generate all available reports
        
        Returns:
            Dict[str, str]: Dictionary of report types and paths
        """
        reports = {}
        
        # Generate HTML report
        reports["html"] = self.generate_html_report()
        
        # Generate CSV report
        reports["csv"] = self.generate_csv_report()
        
        # Generate plots
        reports["distribution"] = self.plot_risk_distribution()
        reports["mitigation"] = self.plot_mitigation_status()
        
        # Create sample trend data for demonstration
        trend_data = [
            {"date": (datetime.now().replace(day=1) - pd.DateOffset(months=i)).strftime("%Y-%m-%d"),
             "low": np.random.randint(5, 15),
             "medium": np.random.randint(10, 20),
             "high": np.random.randint(5, 15),
             "critical": np.random.randint(0, 5)
            } for i in range(6, 0, -1)
        ]
        reports["trend"] = self.plot_risk_trend(trend_data)
        
        return reports


if __name__ == '__main__':
    """Main entry point for standalone execution"""
    parser = argparse.ArgumentParser(description='Generate risk reports')
    parser.add_argument('config_file', help='Path to configuration file')
    parser.add_argument('risks_file', help='Path to risks data file')
    parser.add_argument('mitigations_file', help='Path to mitigations data file')
    parser.add_argument('--output-dir', help='Output directory for reports', default='reports')
    parser.add_argument('--format', choices=['html', 'csv', 'all'], default='all', help='Report format')
    
    args = parser.parse_args()
    
    reporting = RiskReporting(args.config_file, args.risks_file, args.mitigations_file)
    reporting.output_dir = args.output_dir
    
    if not reporting.is_initialized:
        print("Failed to initialize risk reporting")
        sys.exit(1)
    
    print("Risk reporting initialized successfully.")
    
    if args.format == 'html' or args.format == 'all':
        html_report = reporting.generate_html_report()
        print(f"HTML report generated: {html_report}")
    
    if args.format == 'csv' or args.format == 'all':
        csv_report = reporting.generate_csv_report()
        print(f"CSV report generated: {csv_report}")
    
    if args.format == 'all':
        distribution_plot = reporting.plot_risk_distribution()
        mitigation_plot = reporting.plot_mitigation_status()
        print(f"Plots generated: {distribution_plot}, {mitigation_plot}")
