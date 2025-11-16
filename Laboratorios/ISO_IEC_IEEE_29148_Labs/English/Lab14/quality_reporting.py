"""
Quality Reporting Module for ISO/IEC/IEEE 29148:2011 
Requirements Quality Assurance System

This module implements quality reporting features for requirements
based on ISO/IEC/IEEE 29148:2011 standards.
"""

import json
import os
import re
import datetime
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict, Counter
from io import BytesIO
import base64

from quality_metrics import QualityAssessor
from quality_gates import QualityGateSystem


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('quality_reporting')


class QualityReport:
    """Base class for quality reports"""
    
    def __init__(self, name, description, assessor=None, gate_system=None):
        """
        Initialize a quality report
        
        Args:
            name (str): Name of the report
            description (str): Description of the report
            assessor (QualityAssessor): Quality assessor instance
            gate_system (QualityGateSystem): Quality gate system instance
        """
        self.name = name
        self.description = description
        self.assessor = assessor
        self.gate_system = gate_system
        self.data = {}
        self.charts = {}
        self.timestamp = datetime.datetime.now().isoformat()
    
    def generate(self, assessment_results=None, gate_results=None):
        """
        Generate the report
        
        Args:
            assessment_results (dict): Assessment results to include in the report
            gate_results (dict): Gate results to include in the report
            
        Returns:
            dict: Report data
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def save(self, output_file=None, format='json'):
        """
        Save the report to a file
        
        Args:
            output_file (str): Path to output file
            format (str): Output format ('json', 'html', or 'pdf')
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        if not self.data:
            logger.warning("No report data to save")
            return False
        
        if not output_file:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"{self.name.replace(' ', '_')}_{timestamp}.{format}"
        
        try:
            if format.lower() == 'json':
                with open(output_file, 'w') as f:
                    json.dump(self.data, f, indent=2)
                return True
            
            elif format.lower() == 'html':
                html = self._generate_html()
                with open(output_file, 'w') as f:
                    f.write(html)
                return True
            
            elif format.lower() == 'pdf':
                # This would require a PDF generation library like ReportLab
                logger.warning("PDF export not implemented")
                return False
            
            else:
                logger.warning(f"Unsupported export format: {format}")
                return False
                
        except Exception as e:
            logger.error(f"Error saving report: {e}")
            return False
    
    def _generate_html(self):
        """
        Generate HTML representation of the report
        
        Returns:
            str: HTML content
        """
        # Start with a basic HTML template
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.name}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2, h3, h4 {{
                    color: #2c3e50;
                }}
                .report-header {{
                    border-bottom: 2px solid #eee;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }}
                .report-section {{
                    margin-bottom: 40px;
                }}
                .chart-container {{
                    margin: 20px 0;
                    text-align: center;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                }}
                th, td {{
                    padding: 12px 15px;
                    border-bottom: 1px solid #ddd;
                    text-align: left;
                }}
                th {{
                    background-color: #f8f9fa;
                }}
                tr:hover {{
                    background-color: #f5f5f5;
                }}
                .metric-good {{
                    color: #28a745;
                }}
                .metric-warning {{
                    color: #ffc107;
                }}
                .metric-poor {{
                    color: #dc3545;
                }}
                .summary-box {{
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    padding: 20px;
                    margin-bottom: 20px;
                    background-color: #f8f9fa;
                }}
                .recommendation {{
                    background-color: #e7f4ff;
                    border-left: 4px solid #4a6de5;
                    padding: 15px;
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <div class="report-header">
                <h1>{self.name}</h1>
                <p>{self.description}</p>
                <p><strong>Generated:</strong> {datetime.datetime.fromisoformat(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        """
        
        # Add report-specific HTML content
        html += self._generate_report_html()
        
        # Close HTML tags
        html += """
        </body>
        </html>
        """
        
        return html
    
    def _generate_report_html(self):
        """
        Generate HTML content specific to this report
        
        Returns:
            str: HTML content
        """
        return "<p>Report content not implemented</p>"
    
    def _create_chart(self, chart_type, data, options=None):
        """
        Create a chart for the report
        
        Args:
            chart_type (str): Type of chart ('bar', 'pie', 'line', etc.)
            data (dict): Chart data
            options (dict): Chart options
            
        Returns:
            str: Base64-encoded chart image
        """
        # Set up matplotlib figure
        plt.figure(figsize=(10, 6))
        
        # Use seaborn style
        sns.set_style("whitegrid")
        
        try:
            if chart_type == 'bar':
                self._create_bar_chart(data, options)
            elif chart_type == 'pie':
                self._create_pie_chart(data, options)
            elif chart_type == 'line':
                self._create_line_chart(data, options)
            elif chart_type == 'heatmap':
                self._create_heatmap(data, options)
            else:
                logger.warning(f"Unsupported chart type: {chart_type}")
                return None
            
            # Save chart to a bytes buffer
            buffer = BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format='png', dpi=100)
            buffer.seek(0)
            
            # Encode as base64
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close()
            
            return image_base64
            
        except Exception as e:
            logger.error(f"Error creating chart: {e}")
            plt.close()
            return None
    
    def _create_bar_chart(self, data, options=None):
        """
        Create a bar chart
        
        Args:
            data (dict): Chart data with keys 'x' and 'y'
            options (dict): Chart options
        """
        options = options or {}
        
        # Extract data
        x = data.get('x', [])
        y = data.get('y', [])
        
        if not x or not y or len(x) != len(y):
            logger.warning("Invalid data for bar chart")
            return
        
        # Create chart
        ax = sns.barplot(x=x, y=y, palette=options.get('palette', 'Blues_d'))
        
        # Set labels and title
        plt.xlabel(options.get('xlabel', ''))
        plt.ylabel(options.get('ylabel', ''))
        plt.title(options.get('title', ''))
        
        # Rotate x-axis labels if specified
        if options.get('rotate_xlabels'):
            plt.xticks(rotation=options.get('rotate_xlabels'))
        
        # Add value labels on bars
        if options.get('show_values', True):
            for i, v in enumerate(y):
                ax.text(i, v * 1.01, f"{v:.2f}" if isinstance(v, float) else str(v), 
                      ha='center', fontsize=10)
    
    def _create_pie_chart(self, data, options=None):
        """
        Create a pie chart
        
        Args:
            data (dict): Chart data with keys 'labels' and 'values'
            options (dict): Chart options
        """
        options = options or {}
        
        # Extract data
        labels = data.get('labels', [])
        values = data.get('values', [])
        
        if not labels or not values or len(labels) != len(values):
            logger.warning("Invalid data for pie chart")
            return
        
        # Create chart
        plt.pie(values, labels=None, autopct='%1.1f%%', 
              shadow=options.get('shadow', False), 
              startangle=options.get('startangle', 90),
              colors=options.get('colors', None))
        
        # Add legend
        plt.legend(labels, loc=options.get('legend_loc', 'best'))
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        plt.axis('equal')
        
        # Set title
        plt.title(options.get('title', ''))
    
    def _create_line_chart(self, data, options=None):
        """
        Create a line chart
        
        Args:
            data (dict): Chart data with keys 'x' and 'y' (or 'y_series' for multiple lines)
            options (dict): Chart options
        """
        options = options or {}
        
        # Extract data
        x = data.get('x', [])
        y = data.get('y', [])
        y_series = data.get('y_series', {})
        
        if not x:
            logger.warning("Invalid x data for line chart")
            return
        
        if y:
            # Single line
            if len(x) != len(y):
                logger.warning("X and Y data lengths don't match for line chart")
                return
            
            plt.plot(x, y, marker=options.get('marker', 'o'), 
                   linestyle=options.get('linestyle', '-'),
                   color=options.get('color', 'blue'),
                   linewidth=options.get('linewidth', 2),
                   markersize=options.get('markersize', 6),
                   label=options.get('label', None))
            
        elif y_series:
            # Multiple lines
            for label, y_data in y_series.items():
                if len(x) != len(y_data):
                    logger.warning(f"X and Y data lengths don't match for series {label}")
                    continue
                
                plt.plot(x, y_data, marker=options.get('marker', 'o'), 
                       linestyle=options.get('linestyle', '-'),
                       linewidth=options.get('linewidth', 2),
                       markersize=options.get('markersize', 6),
                       label=label)
            
            plt.legend(loc=options.get('legend_loc', 'best'))
        
        # Set labels and title
        plt.xlabel(options.get('xlabel', ''))
        plt.ylabel(options.get('ylabel', ''))
        plt.title(options.get('title', ''))
        
        # Set grid
        plt.grid(options.get('grid', True), linestyle='--', alpha=0.7)
        
        # Rotate x-axis labels if specified
        if options.get('rotate_xlabels'):
            plt.xticks(rotation=options.get('rotate_xlabels'))
    
    def _create_heatmap(self, data, options=None):
        """
        Create a heatmap
        
        Args:
            data (dict): Chart data with key 'matrix'
            options (dict): Chart options
        """
        options = options or {}
        
        # Extract data
        matrix = data.get('matrix', [])
        
        if not matrix:
            logger.warning("Invalid data for heatmap")
            return
        
        # Convert to numpy array if it's not already
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
        
        # Create heatmap
        ax = sns.heatmap(
            matrix,
            annot=options.get('annot', True),
            fmt=options.get('fmt', '.2f'),
            cmap=options.get('cmap', 'Blues'),
            linewidths=options.get('linewidths', 0.5),
            xticklabels=options.get('xticklabels', True),
            yticklabels=options.get('yticklabels', True)
        )
        
        # Set labels and title
        plt.xlabel(options.get('xlabel', ''))
        plt.ylabel(options.get('ylabel', ''))
        plt.title(options.get('title', ''))
        
        # Rotate tick labels if specified
        if options.get('rotate_xlabels'):
            plt.xticks(rotation=options.get('rotate_xlabels'))
        if options.get('rotate_ylabels'):
            plt.yticks(rotation=options.get('rotate_ylabels'))


class QualitySummaryReport(QualityReport):
    """Summary report of quality assessment and gate results"""
    
    def __init__(self, assessor=None, gate_system=None):
        """Initialize the summary report"""
        super().__init__(
            name="Requirements Quality Summary Report",
            description="Summary of requirements quality assessment and gate results",
            assessor=assessor,
            gate_system=gate_system
        )
    
    def generate(self, assessment_results=None, gate_results=None):
        """
        Generate the summary report
        
        Args:
            assessment_results (dict): Assessment results
            gate_results (dict): Gate results
            
        Returns:
            dict: Report data
        """
        # Initialize report data
        self.data = {
            'name': self.name,
            'description': self.description,
            'timestamp': self.timestamp,
            'summary': {},
            'assessment': {},
            'gates': {},
            'recommendations': []
        }
        
        # Add assessment summary if available
        if assessment_results and 'summary' in assessment_results:
            summary = assessment_results['summary']
            
            self.data['assessment'] = {
                'average_score': summary.get('average_score', 0.0),
                'total_requirements': summary.get('total_requirements', 0),
                'total_passing': summary.get('total_passing', 0),
                'passing_ratio': summary.get('total_passing', 0) / summary.get('total_requirements', 1),
                'metrics_summary': summary.get('metrics_summary', {})
            }
            
            # Create metrics chart
            if 'metrics_summary' in summary:
                metrics = []
                scores = []
                thresholds = []
                
                for metric, data in summary['metrics_summary'].items():
                    metrics.append(metric)
                    scores.append(data.get('average_score', 0.0))
                    thresholds.append(data.get('threshold', 0.7))
                
                # Create bar chart for metrics
                chart_data = {
                    'x': metrics,
                    'y': scores
                }
                
                chart_options = {
                    'title': 'Quality Metrics Summary',
                    'xlabel': 'Metrics',
                    'ylabel': 'Average Score',
                    'rotate_xlabels': 45,
                    'palette': 'Blues_d'
                }
                
                metrics_chart = self._create_chart('bar', chart_data, chart_options)
                if metrics_chart:
                    self.charts['metrics_summary'] = metrics_chart
                
                # Create pie chart for passing requirements
                pie_data = {
                    'labels': ['Passing', 'Failing'],
                    'values': [
                        summary.get('total_passing', 0),
                        summary.get('total_requirements', 0) - summary.get('total_passing', 0)
                    ]
                }
                
                pie_options = {
                    'title': 'Requirements Pass/Fail',
                    'colors': ['#28a745', '#dc3545']
                }
                
                passing_chart = self._create_chart('pie', pie_data, pie_options)
                if passing_chart:
                    self.charts['passing_ratio'] = passing_chart
        
        # Add gate results if available
        if gate_results and 'phase_results' in gate_results:
            phase_results = gate_results['phase_results']
            
            self.data['gates'] = {
                'all_phases_passing': gate_results.get('all_phases_passing', False),
                'phases': []
            }
            
            for phase in phase_results:
                phase_data = {
                    'name': phase.get('name', ''),
                    'status': phase.get('status', ''),
                    'gates': []
                }
                
                for gate in phase.get('gates', []):
                    gate_data = {
                        'name': gate.get('name', ''),
                        'status': gate.get('status', ''),
                        'status_reason': gate.get('status_reason', '')
                    }
                    phase_data['gates'].append(gate_data)
                
                self.data['gates']['phases'].append(phase_data)
            
            # Create gate status chart
            gate_statuses = ['passed', 'failed', 'waived', 'pending']
            status_counts = [0, 0, 0, 0]
            
            for phase in phase_results:
                for gate in phase.get('gates', []):
                    status = gate.get('status', '')
                    if status == 'passed':
                        status_counts[0] += 1
                    elif status == 'failed':
                        status_counts[1] += 1
                    elif status == 'waived':
                        status_counts[2] += 1
                    elif status == 'pending':
                        status_counts[3] += 1
            
            gate_chart_data = {
                'labels': gate_statuses,
                'values': status_counts
            }
            
            gate_chart_options = {
                'title': 'Gate Status Summary',
                'colors': ['#28a745', '#dc3545', '#ffc107', '#6c757d']
            }
            
            gate_chart = self._create_chart('pie', gate_chart_data, gate_chart_options)
            if gate_chart:
                self.charts['gate_status'] = gate_chart
        
        # Add overall summary
        self.data['summary'] = {
            'quality_score': self.data['assessment'].get('average_score', 0.0) if 'assessment' in self.data else 0.0,
            'quality_rating': self._get_quality_rating(
                self.data['assessment'].get('average_score', 0.0) if 'assessment' in self.data else 0.0
            ),
            'passing_requirements': self.data['assessment'].get('passing_ratio', 0.0) if 'assessment' in self.data else 0.0,
            'passing_gates': self.data['gates'].get('all_phases_passing', False) if 'gates' in self.data else False
        }
        
        # Generate recommendations
        if self.assessor:
            recommendations = self.assessor.get_improvement_recommendations()
            
            if recommendations:
                # Add overall recommendations
                for rec in recommendations.get('overall', []):
                    self.data['recommendations'].append({
                        'type': 'overall',
                        'recommendation': rec
                    })
                
                # Add metric-specific recommendations
                for metric, recs in recommendations.get('by_metric', {}).items():
                    for rec in recs:
                        self.data['recommendations'].append({
                            'type': 'metric',
                            'metric': metric,
                            'recommendation': rec
                        })
        
        return self.data
    
    def _get_quality_rating(self, score):
        """
        Get a textual rating based on quality score
        
        Args:
            score (float): Quality score (0.0-1.0)
            
        Returns:
            str: Quality rating
        """
        if score >= 0.9:
            return "Excellent"
        elif score >= 0.8:
            return "Good"
        elif score >= 0.7:
            return "Satisfactory"
        elif score >= 0.6:
            return "Needs Improvement"
        else:
            return "Poor"
    
    def _generate_report_html(self):
        """
        Generate HTML content for the summary report
        
        Returns:
            str: HTML content
        """
        html = ""
        
        # Add summary section
        if 'summary' in self.data:
            summary = self.data['summary']
            
            html += """
            <div class="report-section">
                <h2>Quality Overview</h2>
                <div class="summary-box">
            """
            
            quality_score = summary.get('quality_score', 0.0)
            quality_class = "metric-poor"
            if quality_score >= 0.7:
                quality_class = "metric-good"
            elif quality_score >= 0.6:
                quality_class = "metric-warning"
            
            html += f"""
                    <h3>Overall Quality: <span class="{quality_class}">{summary.get('quality_rating', 'Unknown')}</span></h3>
                    <p><strong>Quality Score:</strong> {quality_score:.2f}</p>
                    <p><strong>Passing Requirements:</strong> {summary.get('passing_requirements', 0.0)*100:.1f}%</p>
                    <p><strong>Quality Gates:</strong> {'All Passed' if summary.get('passing_gates', False) else 'Some Failed'}</p>
                </div>
            """
            
            # Add charts
            if 'metrics_summary' in self.charts and 'passing_ratio' in self.charts:
                html += """
                <div class="chart-container" style="display: flex; flex-wrap: wrap; justify-content: space-around;">
                """
                
                # Add metrics chart
                html += f"""
                    <div style="flex: 1; min-width: 400px; margin: 10px;">
                        <h3>Quality Metrics</h3>
                        <img src="data:image/png;base64,{self.charts['metrics_summary']}" alt="Quality Metrics Chart" style="max-width: 100%;">
                    </div>
                """
                
                # Add passing ratio chart
                html += f"""
                    <div style="flex: 1; min-width: 400px; margin: 10px;">
                        <h3>Requirements Passing</h3>
                        <img src="data:image/png;base64,{self.charts['passing_ratio']}" alt="Requirements Passing Chart" style="max-width: 100%;">
                    </div>
                """
                
                html += """
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add assessment section
        if 'assessment' in self.data:
            assessment = self.data['assessment']
            metrics_summary = assessment.get('metrics_summary', {})
            
            html += """
            <div class="report-section">
                <h2>Quality Assessment</h2>
            """
            
            if metrics_summary:
                html += """
                <h3>Metric Scores</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Score</th>
                            <th>Threshold</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                """
                
                for metric, data in metrics_summary.items():
                    score = data.get('average_score', 0.0)
                    threshold = data.get('threshold', 0.7)
                    passing = score >= threshold
                    
                    status_class = "metric-good" if passing else "metric-poor"
                    status_text = "PASS" if passing else "FAIL"
                    
                    html += f"""
                        <tr>
                            <td>{metric}</td>
                            <td>{score:.2f}</td>
                            <td>{threshold:.2f}</td>
                            <td class="{status_class}">{status_text}</td>
                        </tr>
                    """
                
                html += """
                    </tbody>
                </table>
                """
            
            html += """
            </div>
            """
        
        # Add gates section
        if 'gates' in self.data:
            gates = self.data['gates']
            phases = gates.get('phases', [])
            
            html += """
            <div class="report-section">
                <h2>Quality Gates</h2>
            """
            
            # Add gate status chart if available
            if 'gate_status' in self.charts:
                html += f"""
                <div class="chart-container">
                    <h3>Gate Status Summary</h3>
                    <img src="data:image/png;base64,{self.charts['gate_status']}" alt="Gate Status Chart" style="max-width: 100%;">
                </div>
                """
            
            if phases:
                for phase in phases:
                    phase_name = phase.get('name', '')
                    phase_status = phase.get('status', '')
                    gates = phase.get('gates', [])
                    
                    status_class = "metric-good" if phase_status == "passed" else "metric-poor"
                    
                    html += f"""
                    <h3>Phase: {phase_name} <span class="{status_class}">({phase_status.upper()})</span></h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Gate</th>
                                <th>Status</th>
                                <th>Details</th>
                            </tr>
                        </thead>
                        <tbody>
                    """
                    
                    for gate in gates:
                        gate_name = gate.get('name', '')
                        gate_status = gate.get('status', '')
                        gate_reason = gate.get('status_reason', '')
                        
                        status_class = "metric-good"
                        if gate_status == "failed":
                            status_class = "metric-poor"
                        elif gate_status == "waived" or gate_status == "pending":
                            status_class = "metric-warning"
                        
                        html += f"""
                            <tr>
                                <td>{gate_name}</td>
                                <td class="{status_class}">{gate_status.upper()}</td>
                                <td>{gate_reason}</td>
                            </tr>
                        """
                    
                    html += """
                        </tbody>
                    </table>
                    """
            
            html += """
            </div>
            """
        
        # Add recommendations section
        if 'recommendations' in self.data and self.data['recommendations']:
            html += """
            <div class="report-section">
                <h2>Improvement Recommendations</h2>
            """
            
            for rec in self.data['recommendations']:
                rec_type = rec.get('type', '')
                rec_text = rec.get('recommendation', '')
                
                if rec_type == 'metric':
                    metric = rec.get('metric', '')
                    html += f"""
                    <div class="recommendation">
                        <h4>{metric}</h4>
                        <p>{rec_text}</p>
                    </div>
                    """
                else:
                    html += f"""
                    <div class="recommendation">
                        <p>{rec_text}</p>
                    </div>
                    """
            
            html += """
            </div>
            """
        
        return html


class QualityTrendReport(QualityReport):
    """Report showing quality trends over time"""
    
    def __init__(self, assessor=None, gate_system=None):
        """Initialize the trend report"""
        super().__init__(
            name="Requirements Quality Trend Report",
            description="Analysis of quality trends over time",
            assessor=assessor,
            gate_system=gate_system
        )
    
    def generate(self, history_file=None, assessment_results=None, gate_results=None):
        """
        Generate the trend report
        
        Args:
            history_file (str): Path to quality history file
            assessment_results (dict): Current assessment results
            gate_results (dict): Current gate results
            
        Returns:
            dict: Report data
        """
        # Initialize report data
        self.data = {
            'name': self.name,
            'description': self.description,
            'timestamp': self.timestamp,
            'trends': {},
            'current': {}
        }
        
        # Load history data
        history = []
        if history_file and os.path.exists(history_file):
            try:
                with open(history_file, 'r') as f:
                    history = json.load(f)
            except Exception as e:
                logger.error(f"Error loading history file: {e}")
        
        # Add current results to history if available
        if assessment_results and 'summary' in assessment_results:
            summary = assessment_results['summary']
            
            current_summary = {
                'timestamp': summary.get('timestamp', self.timestamp),
                'average_score': summary.get('average_score', 0.0),
                'total_requirements': summary.get('total_requirements', 0),
                'total_passing': summary.get('total_passing', 0),
                'metrics': {}
            }
            
            # Add metrics data
            for metric, data in summary.get('metrics_summary', {}).items():
                current_summary['metrics'][metric] = data.get('average_score', 0.0)
            
            # Add to history
            history.append(current_summary)
            
            # Save current assessment data
            self.data['current'] = {
                'average_score': summary.get('average_score', 0.0),
                'passing_ratio': summary.get('total_passing', 0) / summary.get('total_requirements', 1),
                'metrics': {
                    metric: data.get('average_score', 0.0)
                    for metric, data in summary.get('metrics_summary', {}).items()
                }
            }
        
        # Generate trend data
        if history:
            # Sort history by timestamp
            history.sort(key=lambda x: x.get('timestamp', ''))
            
            # Extract timestamps and overall scores
            timestamps = []
            overall_scores = []
            passing_ratios = []
            metric_scores = defaultdict(list)
            
            for entry in history:
                # Convert timestamp to readable date
                try:
                    dt = datetime.datetime.fromisoformat(entry.get('timestamp', '')).strftime('%Y-%m-%d')
                except:
                    dt = entry.get('timestamp', '')
                
                timestamps.append(dt)
                overall_scores.append(entry.get('average_score', 0.0))
                
                # Calculate passing ratio
                total = entry.get('total_requirements', 0)
                passing = entry.get('total_passing', 0)
                passing_ratio = passing / total if total > 0 else 0.0
                passing_ratios.append(passing_ratio)
                
                # Collect metric scores
                for metric, score in entry.get('metrics', {}).items():
                    metric_scores[metric].append(score)
            
            # Store trend data
            self.data['trends'] = {
                'timestamps': timestamps,
                'overall_scores': overall_scores,
                'passing_ratios': passing_ratios,
                'metric_scores': dict(metric_scores)
            }
            
            # Create trend charts
            
            # Overall quality trend
            line_data = {
                'x': timestamps,
                'y_series': {
                    'Overall Score': overall_scores,
                    'Passing Ratio': passing_ratios
                }
            }
            
            line_options = {
                'title': 'Quality Trends Over Time',
                'xlabel': 'Date',
                'ylabel': 'Score',
                'rotate_xlabels': 45,
                'grid': True
            }
            
            trend_chart = self._create_chart('line', line_data, line_options)
            if trend_chart:
                self.charts['quality_trend'] = trend_chart
            
            # Metrics trend
            if metric_scores:
                metrics_data = {
                    'x': timestamps,
                    'y_series': metric_scores
                }
                
                metrics_options = {
                    'title': 'Metrics Trends Over Time',
                    'xlabel': 'Date',
                    'ylabel': 'Score',
                    'rotate_xlabels': 45,
                    'grid': True
                }
                
                metrics_chart = self._create_chart('line', metrics_data, metrics_options)
                if metrics_chart:
                    self.charts['metrics_trend'] = metrics_chart
            
            # Calculate trend analysis
            self.data['trend_analysis'] = self._calculate_trends(
                timestamps, overall_scores, passing_ratios, metric_scores
            )
        
        return self.data
    
    def _calculate_trends(self, timestamps, overall_scores, passing_ratios, metric_scores):
        """
        Calculate trend analysis
        
        Args:
            timestamps (list): List of timestamps
            overall_scores (list): List of overall scores
            passing_ratios (list): List of passing ratios
            metric_scores (dict): Dictionary of metric scores
            
        Returns:
            dict: Trend analysis
        """
        analysis = {
            'overall': self._calculate_trend(overall_scores),
            'passing_ratio': self._calculate_trend(passing_ratios),
            'metrics': {}
        }
        
        for metric, scores in metric_scores.items():
            analysis['metrics'][metric] = self._calculate_trend(scores)
        
        return analysis
    
    def _calculate_trend(self, values):
        """
        Calculate trend from a series of values
        
        Args:
            values (list): List of numerical values
            
        Returns:
            dict: Trend information
        """
        if not values or len(values) < 2:
            return {'direction': 'stable', 'change': 0.0}
        
        # Calculate simple linear regression
        n = len(values)
        x = list(range(n))
        y = values
        
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
        
        if denominator == 0:
            slope = 0
        else:
            slope = numerator / denominator
        
        # Determine direction
        if abs(slope) < 0.01:
            direction = 'stable'
        elif slope > 0:
            direction = 'improving'
        else:
            direction = 'declining'
        
        # Calculate percent change from first to last
        if values[0] == 0:
            percent_change = 0
        else:
            percent_change = (values[-1] - values[0]) / values[0] * 100
        
        return {
            'direction': direction,
            'change': percent_change,
            'slope': slope,
            'current': values[-1],
            'previous': values[-2] if len(values) > 1 else values[-1]
        }
    
    def _generate_report_html(self):
        """
        Generate HTML content for the trend report
        
        Returns:
            str: HTML content
        """
        html = ""
        
        # Add current quality section
        if 'current' in self.data:
            current = self.data['current']
            
            html += """
            <div class="report-section">
                <h2>Current Quality Status</h2>
                <div class="summary-box">
            """
            
            quality_score = current.get('average_score', 0.0)
            quality_class = "metric-poor"
            if quality_score >= 0.7:
                quality_class = "metric-good"
            elif quality_score >= 0.6:
                quality_class = "metric-warning"
            
            html += f"""
                    <h3>Current Overall Score: <span class="{quality_class}">{quality_score:.2f}</span></h3>
                    <p><strong>Passing Requirements:</strong> {current.get('passing_ratio', 0.0)*100:.1f}%</p>
                </div>
            </div>
            """
        
        # Add trend charts section
        if 'quality_trend' in self.charts:
            html += """
            <div class="report-section">
                <h2>Quality Trends</h2>
            """
            
            html += f"""
                <div class="chart-container">
                    <h3>Quality Over Time</h3>
                    <img src="data:image/png;base64,{self.charts['quality_trend']}" alt="Quality Trends Chart" style="max-width: 100%;">
                </div>
            """
            
            if 'metrics_trend' in self.charts:
                html += f"""
                <div class="chart-container">
                    <h3>Metrics Over Time</h3>
                    <img src="data:image/png;base64,{self.charts['metrics_trend']}" alt="Metrics Trends Chart" style="max-width: 100%;">
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add trend analysis section
        if 'trend_analysis' in self.data:
            analysis = self.data['trend_analysis']
            
            html += """
            <div class="report-section">
                <h2>Trend Analysis</h2>
                
                <h3>Overall Quality Trend</h3>
            """
            
            overall = analysis.get('overall', {})
            direction = overall.get('direction', 'stable')
            change = overall.get('change', 0.0)
            
            direction_class = "metric-warning"
            if direction == "improving":
                direction_class = "metric-good"
            elif direction == "declining":
                direction_class = "metric-poor"
            
            html += f"""
                <div class="summary-box">
                    <p><strong>Direction:</strong> <span class="{direction_class}">{direction.capitalize()}</span></p>
                    <p><strong>Change:</strong> {change:.1f}%</p>
                    <p><strong>Current Value:</strong> {overall.get('current', 0.0):.2f}</p>
                    <p><strong>Previous Value:</strong> {overall.get('previous', 0.0):.2f}</p>
                </div>
            """
            
            # Add metrics trends
            if 'metrics' in analysis:
                html += """
                <h3>Metrics Trends</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Direction</th>
                            <th>Change</th>
                            <th>Current</th>
                            <th>Previous</th>
                        </tr>
                    </thead>
                    <tbody>
                """
                
                for metric, metric_analysis in analysis['metrics'].items():
                    direction = metric_analysis.get('direction', 'stable')
                    change = metric_analysis.get('change', 0.0)
                    current = metric_analysis.get('current', 0.0)
                    previous = metric_analysis.get('previous', 0.0)
                    
                    direction_class = "metric-warning"
                    if direction == "improving":
                        direction_class = "metric-good"
                    elif direction == "declining":
                        direction_class = "metric-poor"
                    
                    html += f"""
                        <tr>
                            <td>{metric}</td>
                            <td class="{direction_class}">{direction.capitalize()}</td>
                            <td>{change:.1f}%</td>
                            <td>{current:.2f}</td>
                            <td>{previous:.2f}</td>
                        </tr>
                    """
                
                html += """
                    </tbody>
                </table>
                """
            
            html += """
            </div>
            """
        
        return html


class QualityComplianceReport(QualityReport):
    """Report showing compliance with quality standards"""
    
    def __init__(self, assessor=None, gate_system=None):
        """Initialize the compliance report"""
        super().__init__(
            name="Requirements Quality Compliance Report",
            description="Analysis of compliance with quality standards",
            assessor=assessor,
            gate_system=gate_system
        )
    
    def generate(self, assessment_results=None, gate_results=None, standards_file=None):
        """
        Generate the compliance report
        
        Args:
            assessment_results (dict): Assessment results
            gate_results (dict): Gate results
            standards_file (str): Path to standards file
            
        Returns:
            dict: Report data
        """
        # Initialize report data
        self.data = {
            'name': self.name,
            'description': self.description,
            'timestamp': self.timestamp,
            'compliance': {},
            'standards': {},
            'recommendations': []
        }
        
        # Load standards if provided
        standards = {}
        if standards_file and os.path.exists(standards_file):
            try:
                with open(standards_file, 'r') as f:
                    standards = json.load(f)
                self.data['standards'] = standards
            except Exception as e:
                logger.error(f"Error loading standards file: {e}")
        
        # Generate compliance data from assessment results
        if assessment_results and 'summary' in assessment_results:
            summary = assessment_results['summary']
            metrics_summary = summary.get('metrics_summary', {})
            
            compliance_results = {}
            overall_compliance = 0.0
            total_weight = 0.0
            
            # Check compliance for each metric
            for metric, data in metrics_summary.items():
                score = data.get('average_score', 0.0)
                threshold = data.get('threshold', 0.7)
                
                # Get standard definition if available
                standard = {}
                if 'metrics' in standards:
                    for std in standards['metrics']:
                        if std.get('name', '') == metric:
                            standard = std
                            break
                
                weight = standard.get('weight', 1.0)
                requirement = standard.get('requirement', 'Must meet minimum threshold')
                
                # Check if metric meets standard
                compliant = score >= threshold
                
                compliance_results[metric] = {
                    'score': score,
                    'threshold': threshold,
                    'compliant': compliant,
                    'weight': weight,
                    'requirement': requirement
                }
                
                # Add to weighted compliance
                if compliant:
                    overall_compliance += weight
                total_weight += weight
            
            # Calculate overall compliance percentage
            overall_compliance_pct = 0.0
            if total_weight > 0:
                overall_compliance_pct = overall_compliance / total_weight
            
            # Store compliance data
            self.data['compliance'] = {
                'metrics': compliance_results,
                'overall_compliance': overall_compliance_pct,
                'total_metrics': len(metrics_summary),
                'compliant_metrics': sum(1 for m in compliance_results.values() if m['compliant'])
            }
            
            # Create compliance chart
            chart_data = {
                'labels': ['Compliant', 'Non-Compliant'],
                'values': [
                    self.data['compliance']['compliant_metrics'],
                    self.data['compliance']['total_metrics'] - self.data['compliance']['compliant_metrics']
                ]
            }
            
            chart_options = {
                'title': 'Metrics Compliance',
                'colors': ['#28a745', '#dc3545']
            }
            
            compliance_chart = self._create_chart('pie', chart_data, chart_options)
            if compliance_chart:
                self.charts['compliance'] = compliance_chart
            
            # Create metrics compliance chart
            metrics = []
            scores = []
            thresholds = []
            
            for metric, data in compliance_results.items():
                metrics.append(metric)
                scores.append(data['score'])
                thresholds.append(data['threshold'])
            
            metrics_data = {
                'x': metrics,
                'y': scores
            }
            
            metrics_options = {
                'title': 'Metrics vs. Thresholds',
                'xlabel': 'Metrics',
                'ylabel': 'Score',
                'rotate_xlabels': 45
            }
            
            metrics_chart = self._create_chart('bar', metrics_data, metrics_options)
            if metrics_chart:
                self.charts['metrics_compliance'] = metrics_chart
            
            # Generate recommendations for non-compliant metrics
            for metric, data in compliance_results.items():
                if not data['compliant']:
                    self.data['recommendations'].append({
                        'metric': metric,
                        'score': data['score'],
                        'threshold': data['threshold'],
                        'recommendation': f"Improve {metric} score to meet threshold of {data['threshold']:.2f}"
                    })
        
        return self.data
    
    def _generate_report_html(self):
        """
        Generate HTML content for the compliance report
        
        Returns:
            str: HTML content
        """
        html = ""
        
        # Add compliance summary section
        if 'compliance' in self.data:
            compliance = self.data['compliance']
            
            html += """
            <div class="report-section">
                <h2>Compliance Summary</h2>
                <div class="summary-box">
            """
            
            compliance_pct = compliance.get('overall_compliance', 0.0) * 100
            compliance_class = "metric-poor"
            if compliance_pct >= 90:
                compliance_class = "metric-good"
            elif compliance_pct >= 70:
                compliance_class = "metric-warning"
            
            html += f"""
                    <h3>Overall Compliance: <span class="{compliance_class}">{compliance_pct:.1f}%</span></h3>
                    <p><strong>Compliant Metrics:</strong> {compliance.get('compliant_metrics', 0)} of {compliance.get('total_metrics', 0)}</p>
                </div>
            """
            
            # Add compliance charts
            if 'compliance' in self.charts and 'metrics_compliance' in self.charts:
                html += """
                <div class="chart-container" style="display: flex; flex-wrap: wrap; justify-content: space-around;">
                """
                
                html += f"""
                    <div style="flex: 1; min-width: 400px; margin: 10px;">
                        <h3>Metrics Compliance</h3>
                        <img src="data:image/png;base64,{self.charts['compliance']}" alt="Compliance Chart" style="max-width: 100%;">
                    </div>
                    
                    <div style="flex: 1; min-width: 400px; margin: 10px;">
                        <h3>Metrics vs. Thresholds</h3>
                        <img src="data:image/png;base64,{self.charts['metrics_compliance']}" alt="Metrics Compliance Chart" style="max-width: 100%;">
                    </div>
                """
                
                html += """
                </div>
                """
            
            html += """
            </div>
            """
        
        # Add detailed compliance section
        if 'compliance' in self.data and 'metrics' in self.data['compliance']:
            metrics_compliance = self.data['compliance']['metrics']
            
            html += """
            <div class="report-section">
                <h2>Detailed Compliance</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Score</th>
                            <th>Threshold</th>
                            <th>Status</th>
                            <th>Requirement</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            
            for metric, data in metrics_compliance.items():
                status_class = "metric-good" if data['compliant'] else "metric-poor"
                status_text = "COMPLIANT" if data['compliant'] else "NON-COMPLIANT"
                
                html += f"""
                    <tr>
                        <td>{metric}</td>
                        <td>{data['score']:.2f}</td>
                        <td>{data['threshold']:.2f}</td>
                        <td class="{status_class}">{status_text}</td>
                        <td>{data['requirement']}</td>
                    </tr>
                """
            
            html += """
                    </tbody>
                </table>
            </div>
            """
        
        # Add standards section
        if 'standards' in self.data and 'metrics' in self.data['standards']:
            standards = self.data['standards']['metrics']
            
            html += """
            <div class="report-section">
                <h2>Quality Standards</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Description</th>
                            <th>Threshold</th>
                            <th>Weight</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            
            for standard in standards:
                html += f"""
                    <tr>
                        <td>{standard.get('name', '')}</td>
                        <td>{standard.get('description', '')}</td>
                        <td>{standard.get('threshold', 0.0):.2f}</td>
                        <td>{standard.get('weight', 1.0):.1f}</td>
                    </tr>
                """
            
            html += """
                    </tbody>
                </table>
            </div>
            """
        
        # Add recommendations section
        if 'recommendations' in self.data and self.data['recommendations']:
            html += """
            <div class="report-section">
                <h2>Compliance Recommendations</h2>
            """
            
            for rec in self.data['recommendations']:
                html += f"""
                <div class="recommendation">
                    <h4>{rec.get('metric', '')}</h4>
                    <p><strong>Current Score:</strong> {rec.get('score', 0.0):.2f} / <strong>Threshold:</strong> {rec.get('threshold', 0.0):.2f}</p>
                    <p>{rec.get('recommendation', '')}</p>
                </div>
                """
            
            html += """
            </div>
            """
        
        return html


class QualityReportingSystem:
    """Main class for managing quality reports"""
    
    def __init__(self, config_file=None, assessor=None, gate_system=None):
        """
        Initialize the quality reporting system
        
        Args:
            config_file (str): Path to configuration file
            assessor (QualityAssessor): Quality assessor instance
            gate_system (QualityGateSystem): Quality gate system instance
        """
        self.assessor = assessor
        self.gate_system = gate_system
        self.config = {}
        self.reports = []
        
        # Load configuration if provided
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = json.load(f)
    
    def create_report(self, report_type, assessment_results=None, gate_results=None, **kwargs):
        """
        Create a quality report
        
        Args:
            report_type (str): Type of report to create
            assessment_results (dict): Assessment results
            gate_results (dict): Gate results
            **kwargs: Additional arguments for specific report types
            
        Returns:
            QualityReport: The created report
        """
        report = None
        
        if report_type.lower() == 'summary':
            report = QualitySummaryReport(self.assessor, self.gate_system)
            report.generate(assessment_results, gate_results)
        
        elif report_type.lower() == 'trend':
            report = QualityTrendReport(self.assessor, self.gate_system)
            report.generate(kwargs.get('history_file'), assessment_results, gate_results)
        
        elif report_type.lower() == 'compliance':
            report = QualityComplianceReport(self.assessor, self.gate_system)
            report.generate(assessment_results, gate_results, kwargs.get('standards_file'))
        
        if report:
            self.reports.append(report)
        
        return report
    
    def create_all_reports(self, assessment_results=None, gate_results=None, **kwargs):
        """
        Create all types of reports
        
        Args:
            assessment_results (dict): Assessment results
            gate_results (dict): Gate results
            **kwargs: Additional arguments for specific report types
            
        Returns:
            list: List of created reports
        """
        # Clear existing reports
        self.reports = []
        
        # Create each report type
        summary_report = self.create_report('summary', assessment_results, gate_results)
        trend_report = self.create_report('trend', assessment_results, gate_results, 
                                        history_file=kwargs.get('history_file'))
        compliance_report = self.create_report('compliance', assessment_results, gate_results, 
                                             standards_file=kwargs.get('standards_file'))
        
        return self.reports
    
    def save_reports(self, output_dir=None, format='html'):
        """
        Save all reports to files
        
        Args:
            output_dir (str): Directory to save reports
            format (str): Output format ('json', 'html', or 'pdf')
            
        Returns:
            bool: True if all reports were saved successfully, False otherwise
        """
        if not self.reports:
            logger.warning("No reports to save")
            return False
        
        # Create output directory if it doesn't exist
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save each report
        success = True
        for report in self.reports:
            # Create output file path
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{report.name.replace(' ', '_')}_{timestamp}.{format}"
            
            if output_dir:
                output_file = os.path.join(output_dir, filename)
            else:
                output_file = filename
            
            # Save report
            if not report.save(output_file, format):
                success = False
        
        return success
    
    def create_dashboard_data(self):
        """
        Create data for a quality dashboard
        
        Returns:
            dict: Dashboard data
        """
        dashboard = {
            'timestamp': datetime.datetime.now().isoformat(),
            'summary': {},
            'metrics': {},
            'trends': {},
            'compliance': {},
            'recommendations': []
        }
        
        # Extract data from reports
        for report in self.reports:
            if isinstance(report, QualitySummaryReport):
                # Extract summary data
                if 'summary' in report.data:
                    dashboard['summary'] = report.data['summary']
                
                # Extract metrics data
                if 'assessment' in report.data and 'metrics_summary' in report.data['assessment']:
                    dashboard['metrics'] = report.data['assessment']['metrics_summary']
                
                # Extract recommendations
                if 'recommendations' in report.data:
                    dashboard['recommendations'] = report.data['recommendations']
            
            elif isinstance(report, QualityTrendReport):
                # Extract trend data
                if 'trends' in report.data:
                    dashboard['trends'] = report.data['trends']
                
                # Extract trend analysis
                if 'trend_analysis' in report.data:
                    dashboard['trend_analysis'] = report.data['trend_analysis']
            
            elif isinstance(report, QualityComplianceReport):
                # Extract compliance data
                if 'compliance' in report.data:
                    dashboard['compliance'] = report.data['compliance']
        
        # Add chart data
        dashboard['charts'] = {}
        
        for report in self.reports:
            for chart_name, chart_data in report.charts.items():
                dashboard['charts'][chart_name] = chart_data
        
        return dashboard
    
    def save_dashboard_data(self, output_file=None):
        """
        Save dashboard data to a file
        
        Args:
            output_file (str): Path to output file
            
        Returns:
            bool: True if dashboard data was saved successfully, False otherwise
        """
        dashboard_data = self.create_dashboard_data()
        
        if not dashboard_data:
            logger.warning("No dashboard data to save")
            return False
        
        if not output_file:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"quality_dashboard_data_{timestamp}.json"
        
        try:
            with open(output_file, 'w') as f:
                json.dump(dashboard_data, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error saving dashboard data: {e}")
            return False


# Run as standalone module
if __name__ == "__main__":
    import argparse
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    
    parser = argparse.ArgumentParser(description='Requirements Quality Reporting Tool')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--assessment', help='Path to assessment results file')
    parser.add_argument('--gates', help='Path to gate results file')
    parser.add_argument('--history', help='Path to quality history file')
    parser.add_argument('--standards', help='Path to standards file')
    parser.add_argument('--output-dir', help='Directory to save reports')
    parser.add_argument('--report-type', choices=['summary', 'trend', 'compliance', 'all'],
                        default='all', help='Type of report to generate')
    parser.add_argument('--format', choices=['json', 'html', 'pdf'],
                        default='html', help='Output format')
    parser.add_argument('--dashboard', action='store_true',
                        help='Generate dashboard data')
    
    args = parser.parse_args()
    
    # Load assessment results if provided
    assessment_results = None
    if args.assessment and os.path.exists(args.assessment):
        try:
            with open(args.assessment, 'r') as f:
                assessment_results = json.load(f)
            print(f"Loaded assessment results from {args.assessment}")
        except Exception as e:
            print(f"Error loading assessment results: {e}")
    
    # Load gate results if provided
    gate_results = None
    if args.gates and os.path.exists(args.gates):
        try:
            with open(args.gates, 'r') as f:
                gate_results = json.load(f)
            print(f"Loaded gate results from {args.gates}")
        except Exception as e:
            print(f"Error loading gate results: {e}")
    
    # Create reporting system
    reporting_system = QualityReportingSystem(args.config)
    
    # Generate reports
    if args.report_type == 'all':
        reports = reporting_system.create_all_reports(
            assessment_results=assessment_results,
            gate_results=gate_results,
            history_file=args.history,
            standards_file=args.standards
        )
        print(f"Generated {len(reports)} reports")
    else:
        report = reporting_system.create_report(
            args.report_type,
            assessment_results=assessment_results,
            gate_results=gate_results,
            history_file=args.history,
            standards_file=args.standards
        )
        print(f"Generated {args.report_type} report")
    
    # Save reports
    if reporting_system.save_reports(args.output_dir, args.format):
        print(f"Reports saved to {args.output_dir or 'current directory'}")
    
    # Generate dashboard data if requested
    if args.dashboard:
        dashboard_file = "quality_dashboard_data.json"
        if reporting_system.save_dashboard_data(dashboard_file):
            print(f"Dashboard data saved to {dashboard_file}")
