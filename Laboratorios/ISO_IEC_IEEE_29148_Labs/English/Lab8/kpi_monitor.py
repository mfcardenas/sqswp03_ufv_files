#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
KPI Monitoring Module
--------------------
This module implements a KPI monitoring system for requirements metrics.
It handles threshold monitoring, alerting, and KPI tracking for requirements analytics.

Functions:
- Define and manage KPIs
- Track KPI performance
- Monitor thresholds and generate alerts
- Calculate KPI trends and forecasts
"""

import json
import logging
import time
import datetime
import threading
import os
from typing import Dict, List, Any, Optional, Union, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("kpi_monitor.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("KPIMonitor")

class KPIMonitor:
    """
    KPI Monitoring System for Requirements Analytics
    
    This class provides functionality to:
    - Define and track key performance indicators
    - Monitor KPI thresholds and generate alerts
    - Calculate KPI trends and forecasts
    - Provide KPI dashboards and status reports
    """
    
    def __init__(self, config_path: str = 'metrics_config.json', metrics_collector=None):
        """
        Initialize the KPI monitor with configuration
        
        Args:
            config_path: Path to metrics configuration file
            metrics_collector: Optional metrics collector instance
        """
        logger.info(f"Initializing KPIMonitor with config: {config_path}")
        self.config_path = config_path
        self.config = self._load_config()
        self.metrics_collector = metrics_collector
        self.kpis = self.config.get("kpis", {})
        self.alert_handlers = []
        self.monitoring_thread = None
        self.is_monitoring = False
        self.data_dir = os.path.join("data", "kpis")
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Initialize default KPIs if none defined
        if not self.kpis:
            self._initialize_default_kpis()
        
        logger.info(f"KPIMonitor initialized with {len(self.kpis)} KPIs")
    
    def _load_config(self) -> Dict[str, Any]:
        """
        Load KPI configuration from JSON file
        
        Returns:
            Dict containing KPI configuration
        """
        try:
            with open(self.config_path, 'r') as config_file:
                config = json.load(config_file)
                return config
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {self.config_path}")
            return {"kpis": {}}
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in configuration file: {self.config_path}")
            return {"kpis": {}}
    
    def _initialize_default_kpis(self) -> None:
        """
        Initialize default KPIs if none are defined in the configuration
        """
        logger.info("Initializing default KPIs")
        
        self.kpis = {
            "requirements_quality": {
                "name": "Requirements Quality Score",
                "description": "Average quality score across all requirements",
                "source": "requirements_quality",
                "target": 85.0,
                "thresholds": {
                    "excellent": 90.0,
                    "good": 80.0,
                    "acceptable": 70.0,
                    "poor": 60.0
                },
                "trend": "increasing",
                "unit": "",
                "alert_threshold": "poor"
            },
            "review_efficiency": {
                "name": "Review Efficiency",
                "description": "Average time to complete requirement reviews",
                "source": "review_efficiency",
                "target": 48.0,
                "thresholds": {
                    "excellent": 24.0,
                    "good": 36.0,
                    "acceptable": 48.0,
                    "poor": 72.0
                },
                "trend": "decreasing",
                "unit": "hours",
                "alert_threshold": "poor"
            },
            "defect_density": {
                "name": "Defect Density",
                "description": "Average number of defects per requirement",
                "source": "defect_density",
                "target": 0.1,
                "thresholds": {
                    "excellent": 0.05,
                    "good": 0.1,
                    "acceptable": 0.2,
                    "poor": 0.3
                },
                "trend": "decreasing",
                "unit": "defects/req",
                "alert_threshold": "poor"
            },
            "requirements_completeness": {
                "name": "Requirements Completeness",
                "description": "Percentage of requirements with complete information",
                "source": "requirements_completeness",
                "target": 90.0,
                "thresholds": {
                    "excellent": 95.0,
                    "good": 85.0,
                    "acceptable": 75.0,
                    "poor": 60.0
                },
                "trend": "increasing",
                "unit": "%",
                "alert_threshold": "poor"
            }
        }
        
        # Save to configuration
        self.config["kpis"] = self.kpis
        self._save_config()
    
    def _save_config(self) -> None:
        """
        Save the current configuration to the config file
        """
        try:
            with open(self.config_path, 'w') as config_file:
                json.dump(self.config, config_file, indent=4)
            logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            logger.error(f"Error saving configuration: {str(e)}")
    
    def add_kpi(self, kpi_id: str, kpi_config: Dict[str, Any]) -> None:
        """
        Add or update a KPI definition
        
        Args:
            kpi_id: Unique identifier for the KPI
            kpi_config: KPI configuration dictionary
        """
        logger.info(f"Adding/updating KPI: {kpi_id}")
        
        # Validate KPI configuration
        required_fields = ["name", "description", "source", "target"]
        for field in required_fields:
            if field not in kpi_config:
                logger.error(f"Missing required field '{field}' in KPI configuration")
                raise ValueError(f"Missing required field '{field}' in KPI configuration")
        
        # Add KPI to configuration
        self.kpis[kpi_id] = kpi_config
        self.config["kpis"] = self.kpis
        
        # Save updated configuration
        self._save_config()
        
        logger.info(f"KPI {kpi_id} added successfully")
    
    def remove_kpi(self, kpi_id: str) -> None:
        """
        Remove a KPI definition
        
        Args:
            kpi_id: Unique identifier for the KPI to remove
        """
        logger.info(f"Removing KPI: {kpi_id}")
        
        if kpi_id in self.kpis:
            del self.kpis[kpi_id]
            self.config["kpis"] = self.kpis
            
            # Save updated configuration
            self._save_config()
            
            logger.info(f"KPI {kpi_id} removed successfully")
        else:
            logger.warning(f"KPI {kpi_id} not found")
    
    def register_alert_handler(self, handler_func) -> None:
        """
        Register a function to handle KPI alerts
        
        Args:
            handler_func: Function that accepts an alert dictionary
        """
        logger.info(f"Registering alert handler: {handler_func.__name__}")
        self.alert_handlers.append(handler_func)
    
    def start_monitoring(self, interval: int = 3600) -> None:
        """
        Start automated KPI monitoring
        
        Args:
            interval: Monitoring interval in seconds (default: 1 hour)
        """
        if self.is_monitoring:
            logger.warning("KPI monitoring already running")
            return
        
        self.is_monitoring = True
        logger.info(f"Starting KPI monitoring with interval: {interval} seconds")
        
        def monitoring_worker():
            while self.is_monitoring:
                try:
                    self.check_all_kpis()
                    time.sleep(interval)
                except Exception as e:
                    logger.error(f"Error in KPI monitoring: {str(e)}")
                    time.sleep(60)  # Wait a minute before retrying
        
        self.monitoring_thread = threading.Thread(target=monitoring_worker)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
    
    def stop_monitoring(self) -> None:
        """
        Stop the automated KPI monitoring
        """
        logger.info("Stopping KPI monitoring")
        self.is_monitoring = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=10)
    
    def check_all_kpis(self) -> Dict[str, Any]:
        """
        Check all defined KPIs against current metrics
        
        Returns:
            Dict containing KPI status information
        """
        logger.info("Checking all KPIs")
        
        timestamp = datetime.datetime.now().isoformat()
        
        # Get latest metrics
        if self.metrics_collector:
            latest_metrics = self.metrics_collector.get_latest_metrics()
        else:
            # Generate sample metrics if no collector
            latest_metrics = self._generate_sample_metrics()
        
        kpi_statuses = {}
        alerts = []
        
        # Process each KPI
        for kpi_id, kpi_config in self.kpis.items():
            source = kpi_config.get("source")
            
            # Skip if source not in metrics
            if source not in latest_metrics["metrics"]:
                logger.warning(f"Metric source '{source}' not found for KPI {kpi_id}")
                continue
            
            # Get current value
            current_value = latest_metrics["metrics"][source]
            
            # Calculate status
            status = self._calculate_kpi_status(kpi_id, current_value)
            
            # Check for alerts
            if self._should_alert(kpi_id, status):
                alert = self._create_alert(kpi_id, status, current_value)
                alerts.append(alert)
                
                # Send alert to handlers
                for handler in self.alert_handlers:
                    try:
                        handler(alert)
                    except Exception as e:
                        logger.error(f"Error in alert handler: {str(e)}")
            
            # Store KPI status
            kpi_statuses[kpi_id] = status
        
        # Store KPI check results
        result = {
            "timestamp": timestamp,
            "kpi_statuses": kpi_statuses,
            "alerts": alerts
        }
        
        self._store_kpi_check(result)
        
        logger.info(f"Checked {len(kpi_statuses)} KPIs, generated {len(alerts)} alerts")
        return result
    
    def _generate_sample_metrics(self) -> Dict[str, Any]:
        """
        Generate sample metrics when no collector is available
        
        Returns:
            Dict containing sample metrics
        """
        import random
        
        timestamp = datetime.datetime.now().isoformat()
        
        return {
            "timestamp": timestamp,
            "metrics": {
                "requirements_quality": round(random.uniform(70, 90), 2),
                "review_efficiency": round(random.uniform(30, 60), 1),
                "defect_density": round(random.uniform(0.1, 0.3), 3),
                "requirements_completeness": round(random.uniform(75, 95), 2)
            }
        }
    
    def _calculate_kpi_status(self, kpi_id: str, current_value: float) -> Dict[str, Any]:
        """
        Calculate status for a specific KPI
        
        Args:
            kpi_id: KPI identifier
            current_value: Current metric value
            
        Returns:
            Dict containing KPI status information
        """
        kpi_config = self.kpis[kpi_id]
        
        # Get target and thresholds
        target = kpi_config.get("target")
        thresholds = kpi_config.get("thresholds", {})
        trend_direction = kpi_config.get("trend", "increasing")
        unit = kpi_config.get("unit", "")
        
        # Determine performance level
        performance_level = "unknown"
        
        if trend_direction == "increasing":
            # Higher is better
            for level, threshold in sorted(thresholds.items(), key=lambda x: float(x[1]), reverse=True):
                if current_value >= threshold:
                    performance_level = level
                    break
        else:
            # Lower is better
            for level, threshold in sorted(thresholds.items(), key=lambda x: float(x[1])):
                if current_value <= threshold:
                    performance_level = level
                    break
        
        # Calculate target gap
        target_gap = current_value - target
        target_gap_percent = (target_gap / abs(target)) * 100 if target != 0 else 0
        
        # Determine if on target
        on_target = (trend_direction == "increasing" and current_value >= target) or \
                   (trend_direction == "decreasing" and current_value <= target)
        
        return {
            "kpi_id": kpi_id,
            "name": kpi_config.get("name", kpi_id),
            "current_value": current_value,
            "target": target,
            "unit": unit,
            "performance_level": performance_level,
            "target_gap": round(target_gap, 3),
            "target_gap_percent": round(target_gap_percent, 2),
            "on_target": on_target
        }
    
    def _should_alert(self, kpi_id: str, status: Dict[str, Any]) -> bool:
        """
        Determine if an alert should be generated for a KPI
        
        Args:
            kpi_id: KPI identifier
            status: KPI status information
            
        Returns:
            True if alert should be generated, False otherwise
        """
        kpi_config = self.kpis[kpi_id]
        
        # Get alert threshold
        alert_threshold = kpi_config.get("alert_threshold")
        
        if not alert_threshold:
            return False
        
        # Check if performance level is at or below alert threshold
        performance_levels = list(kpi_config.get("thresholds", {}).keys())
        
        if status["performance_level"] == alert_threshold:
            return True
        
        # Check if we need to alert based on threshold ordering
        if kpi_config.get("trend") == "increasing":
            # For increasing metrics, alert if performance is lower than threshold
            threshold_index = performance_levels.index(alert_threshold) if alert_threshold in performance_levels else -1
            level_index = performance_levels.index(status["performance_level"]) if status["performance_level"] in performance_levels else -1
            
            return level_index >= threshold_index and level_index >= 0 and threshold_index >= 0
            
        else:
            # For decreasing metrics, alert if performance is higher than threshold
            threshold_index = performance_levels.index(alert_threshold) if alert_threshold in performance_levels else -1
            level_index = performance_levels.index(status["performance_level"]) if status["performance_level"] in performance_levels else -1
            
            return level_index <= threshold_index and level_index >= 0 and threshold_index >= 0
    
    def _create_alert(self, kpi_id: str, status: Dict[str, Any], current_value: float) -> Dict[str, Any]:
        """
        Create an alert for a KPI
        
        Args:
            kpi_id: KPI identifier
            status: KPI status information
            current_value: Current metric value
            
        Returns:
            Dict containing alert information
        """
        kpi_config = self.kpis[kpi_id]
        
        # Format current value with appropriate precision
        if isinstance(current_value, float):
            if current_value < 0.1:
                formatted_value = f"{current_value:.3f}"
            elif current_value < 10:
                formatted_value = f"{current_value:.2f}"
            else:
                formatted_value = f"{current_value:.1f}"
        else:
            formatted_value = str(current_value)
        
        # Generate alert message
        message = f"{kpi_config.get('name', kpi_id)} is at {formatted_value} {kpi_config.get('unit', '')}, "
        
        if status["on_target"]:
            message += "which meets the target."
        else:
            gap_abs = abs(status["target_gap"])
            gap_percent = abs(status["target_gap_percent"])
            
            if kpi_config.get("trend") == "increasing":
                direction = "below"
            else:
                direction = "above"
            
            message += f"which is {direction} the target by {gap_abs:.2f} ({gap_percent:.1f}%)."
        
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "kpi_id": kpi_id,
            "name": kpi_config.get("name", kpi_id),
            "level": status["performance_level"],
            "current_value": current_value,
            "target": kpi_config.get("target"),
            "unit": kpi_config.get("unit", ""),
            "message": message,
            "on_target": status["on_target"]
        }
    
    def _store_kpi_check(self, check_result: Dict[str, Any]) -> None:
        """
        Store KPI check results
        
        Args:
            check_result: KPI check result to store
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        file_path = os.path.join(self.data_dir, f"kpi_checks_{timestamp}.json")
        
        # Read existing data if file exists
        if os.path.isfile(file_path):
            with open(file_path, 'r') as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {"checks": []}
        else:
            data = {"checks": []}
        
        # Append new check
        data["checks"].append(check_result)
        
        # Write updated data
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
        
        logger.info(f"Stored KPI check results to: {file_path}")
    
    def get_kpi_status(self, kpi_id: str = None) -> Dict[str, Any]:
        """
        Get current status for a specific KPI or all KPIs
        
        Args:
            kpi_id: Optional KPI identifier (None for all KPIs)
            
        Returns:
            Dict containing KPI status information
        """
        logger.info(f"Getting KPI status for: {kpi_id if kpi_id else 'all KPIs'}")
        
        # Get latest metrics
        if self.metrics_collector:
            latest_metrics = self.metrics_collector.get_latest_metrics()
        else:
            latest_metrics = self._generate_sample_metrics()
        
        timestamp = latest_metrics["timestamp"]
        result = {"timestamp": timestamp}
        
        if kpi_id:
            # Get status for specific KPI
            if kpi_id not in self.kpis:
                logger.error(f"KPI not found: {kpi_id}")
                raise ValueError(f"KPI not found: {kpi_id}")
            
            source = self.kpis[kpi_id].get("source")
            
            if source not in latest_metrics["metrics"]:
                logger.warning(f"Metric source '{source}' not found for KPI {kpi_id}")
                result["status"] = None
            else:
                current_value = latest_metrics["metrics"][source]
                result["status"] = self._calculate_kpi_status(kpi_id, current_value)
        else:
            # Get status for all KPIs
            statuses = {}
            
            for kpi_id, kpi_config in self.kpis.items():
                source = kpi_config.get("source")
                
                if source not in latest_metrics["metrics"]:
                    logger.warning(f"Metric source '{source}' not found for KPI {kpi_id}")
                    continue
                
                current_value = latest_metrics["metrics"][source]
                statuses[kpi_id] = self._calculate_kpi_status(kpi_id, current_value)
            
            result["statuses"] = statuses
        
        return result
    
    def get_kpi_history(self, kpi_id: str, 
                       start_date: str = None, 
                       end_date: str = None,
                       limit: int = 30) -> List[Dict[str, Any]]:
        """
        Get historical status for a specific KPI
        
        Args:
            kpi_id: KPI identifier
            start_date: Optional start date (ISO format)
            end_date: Optional end date (ISO format)
            limit: Maximum number of records to retrieve
            
        Returns:
            List of historical KPI status records
        """
        logger.info(f"Getting KPI history for: {kpi_id}")
        
        if kpi_id not in self.kpis:
            logger.error(f"KPI not found: {kpi_id}")
            raise ValueError(f"KPI not found: {kpi_id}")
        
        # In a real implementation, this would query stored KPI check results
        # For this lab, we'll generate sample historical data
        import random
        
        if not start_date:
            start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()
        
        if not end_date:
            end_date = datetime.datetime.now().isoformat()
        
        # Parse dates
        start_dt = datetime.datetime.fromisoformat(start_date)
        end_dt = datetime.datetime.fromisoformat(end_date)
        
        # Get KPI configuration
        kpi_config = self.kpis[kpi_id]
        target = kpi_config.get("target")
        trend = kpi_config.get("trend", "increasing")
        
        # Generate sample data points
        history = []
        current_dt = start_dt
        
        while current_dt <= end_dt and len(history) < limit:
            # Generate realistic trend
            days_factor = (current_dt - start_dt).days / max(1, (end_dt - start_dt).days)
            
            if trend == "increasing":
                # Start below target, improve over time
                base_value = target * 0.8 + (target * 0.3 * days_factor)
                current_value = round(base_value + random.uniform(-target * 0.05, target * 0.05), 2)
            else:
                # Start above target, improve over time
                base_value = target * 1.5 - (target * 0.6 * days_factor)
                current_value = round(base_value + random.uniform(-target * 0.05, target * 0.05), 2)
            
            # Calculate status
            status = self._calculate_kpi_status(kpi_id, current_value)
            
            # Add to history
            history.append({
                "timestamp": current_dt.isoformat(),
                "kpi_id": kpi_id,
                "value": current_value,
                "status": status["performance_level"],
                "on_target": status["on_target"]
            })
            
            current_dt += datetime.timedelta(days=1)
        
        return history
    
    def get_kpi_forecast(self, kpi_id: str, days: int = 30) -> Dict[str, Any]:
        """
        Generate a forecast for a specific KPI
        
        Args:
            kpi_id: KPI identifier
            days: Number of days to forecast
            
        Returns:
            Dict containing forecast information
        """
        logger.info(f"Generating forecast for KPI: {kpi_id}, days: {days}")
        
        if kpi_id not in self.kpis:
            logger.error(f"KPI not found: {kpi_id}")
            raise ValueError(f"KPI not found: {kpi_id}")
        
        # Get historical data
        history = self.get_kpi_history(kpi_id, limit=90)
        
        if not history:
            logger.warning(f"No historical data for KPI: {kpi_id}")
            return {
                "kpi_id": kpi_id,
                "error": "No historical data available for forecasting"
            }
        
        # Extract values
        values = [item["value"] for item in history]
        timestamps = [item["timestamp"] for item in history]
        
        # Simple linear regression for trend
        n = len(values)
        indices = list(range(n))
        
        sum_x = sum(indices)
        sum_y = sum(values)
        sum_xy = sum(i * v for i, v in zip(indices, values))
        sum_xx = sum(i * i for i in indices)
        
        # Calculate slope and intercept
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x) if n * sum_xx - sum_x * sum_x != 0 else 0
        intercept = (sum_y - slope * sum_x) / n
        
        # Generate forecast
        forecast = []
        last_dt = datetime.datetime.fromisoformat(timestamps[-1])
        
        for i in range(1, days + 1):
            forecast_day = n + i - 1
            forecast_value = intercept + slope * forecast_day
            forecast_date = (last_dt + datetime.timedelta(days=i)).isoformat()
            
            # Calculate status at forecasted value
            status = self._calculate_kpi_status(kpi_id, forecast_value)
            
            forecast.append({
                "timestamp": forecast_date,
                "value": round(forecast_value, 2),
                "status": status["performance_level"],
                "on_target": status["on_target"]
            })
        
        # Determine when target will be met
        kpi_config = self.kpis[kpi_id]
        target = kpi_config.get("target")
        trend = kpi_config.get("trend", "increasing")
        
        target_day = None
        if slope != 0:
            if trend == "increasing" and slope > 0:
                # Calculate days until target is reached
                if values[-1] < target:
                    days_to_target = (target - intercept) / slope - n
                    if days_to_target > 0:
                        target_day = int(days_to_target) + 1
            elif trend == "decreasing" and slope < 0:
                # Calculate days until target is reached
                if values[-1] > target:
                    days_to_target = (target - intercept) / slope - n
                    if days_to_target > 0:
                        target_day = int(days_to_target) + 1
        
        # Prepare result
        result = {
            "kpi_id": kpi_id,
            "name": kpi_config.get("name", kpi_id),
            "current_value": values[-1],
            "target": target,
            "trend": {
                "direction": "up" if slope > 0 else "down",
                "slope": round(slope, 4)
            },
            "forecast": forecast,
            "days_to_target": target_day
        }
        
        return result
    
    def get_kpi_dashboard(self) -> Dict[str, Any]:
        """
        Get comprehensive KPI dashboard data
        
        Returns:
            Dict containing dashboard data for all KPIs
        """
        logger.info("Generating KPI dashboard data")
        
        # Get current status for all KPIs
        current_status = self.get_kpi_status()
        
        # Get forecast for each KPI
        forecasts = {}
        
        for kpi_id in self.kpis:
            try:
                forecasts[kpi_id] = self.get_kpi_forecast(kpi_id)
            except Exception as e:
                logger.error(f"Error generating forecast for {kpi_id}: {str(e)}")
                forecasts[kpi_id] = {"error": str(e)}
        
        # Calculate overall health score
        health_score = self._calculate_health_score(current_status)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(current_status, forecasts)
        
        # Compile dashboard data
        dashboard = {
            "timestamp": datetime.datetime.now().isoformat(),
            "overall_health": health_score,
            "kpi_status": current_status,
            "forecasts": forecasts,
            "recommendations": recommendations
        }
        
        return dashboard
    
    def _calculate_health_score(self, status_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate overall health score based on KPI statuses
        
        Args:
            status_data: KPI status data
            
        Returns:
            Dict containing health score information
        """
        if "statuses" not in status_data:
            return {"score": 0, "level": "unknown"}
        
        statuses = status_data["statuses"]
        
        # Define scores for performance levels
        level_scores = {
            "excellent": 100,
            "good": 80,
            "acceptable": 60,
            "poor": 30,
            "unknown": 0
        }
        
        # Calculate weighted score
        total_weight = 0
        weighted_sum = 0
        
        for kpi_id, status in statuses.items():
            kpi_config = self.kpis.get(kpi_id, {})
            weight = kpi_config.get("weight", 1.0)
            
            level = status["performance_level"]
            score = level_scores.get(level, 0)
            
            weighted_sum += score * weight
            total_weight += weight
        
        # Calculate final score
        if total_weight > 0:
            final_score = weighted_sum / total_weight
        else:
            final_score = 0
        
        # Determine health level
        if final_score >= 90:
            health_level = "excellent"
        elif final_score >= 75:
            health_level = "good"
        elif final_score >= 50:
            health_level = "acceptable"
        else:
            health_level = "poor"
        
        return {
            "score": round(final_score, 1),
            "level": health_level,
            "kpis_on_target": sum(1 for s in statuses.values() if s["on_target"]),
            "total_kpis": len(statuses)
        }
    
    def _generate_recommendations(self, status_data: Dict[str, Any], 
                                forecasts: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on KPI statuses and forecasts
        
        Args:
            status_data: KPI status data
            forecasts: KPI forecast data
            
        Returns:
            List of recommendation objects
        """
        recommendations = []
        
        if "statuses" not in status_data:
            return recommendations
        
        statuses = status_data["statuses"]
        
        # Generate recommendations for KPIs below target
        for kpi_id, status in statuses.items():
            if not status["on_target"]:
                kpi_config = self.kpis.get(kpi_id, {})
                
                # Get forecast information
                forecast = forecasts.get(kpi_id, {})
                days_to_target = forecast.get("days_to_target")
                
                # Determine priority based on performance level
                priority = "medium"
                if status["performance_level"] == "poor":
                    priority = "high"
                
                # Create recommendation
                recommendation = {
                    "kpi_id": kpi_id,
                    "name": kpi_config.get("name", kpi_id),
                    "priority": priority,
                    "gap": abs(status["target_gap"]),
                    "gap_percent": abs(status["target_gap_percent"]),
                    "days_to_target": days_to_target
                }
                
                # Add appropriate actions based on KPI
                if kpi_id == "requirements_quality":
                    recommendation["actions"] = [
                        "Review quality criteria and standards",
                        "Provide additional training on requirements authoring",
                        "Implement peer reviews before formal reviews"
                    ]
                elif kpi_id == "review_efficiency":
                    recommendation["actions"] = [
                        "Streamline the review process",
                        "Reduce the number of reviewers for smaller changes",
                        "Implement parallel reviews where appropriate"
                    ]
                elif kpi_id == "defect_density":
                    recommendation["actions"] = [
                        "Enhance requirements validation processes",
                        "Improve requirements templates",
                        "Implement automated quality checks"
                    ]
                elif kpi_id == "requirements_completeness":
                    recommendation["actions"] = [
                        "Implement completeness checklists",
                        "Review requirements templates",
                        "Provide training on comprehensive requirements"
                    ]
                else:
                    recommendation["actions"] = [
                        "Review processes related to this KPI",
                        "Identify specific improvement areas",
                        "Implement targeted improvement actions"
                    ]
                
                recommendations.append(recommendation)
        
        # Sort recommendations by priority
        recommendations.sort(key=lambda x: 0 if x["priority"] == "high" else 1 if x["priority"] == "medium" else 2)
        
        return recommendations


# Example usage
if __name__ == "__main__":
    # Create KPI monitor
    monitor = KPIMonitor()
    
    # Add a custom KPI
    monitor.add_kpi("stakeholder_satisfaction", {
        "name": "Stakeholder Satisfaction",
        "description": "Average satisfaction score from stakeholders",
        "source": "stakeholder_satisfaction",
        "target": 4.2,
        "thresholds": {
            "excellent": 4.5,
            "good": 4.0,
            "acceptable": 3.5,
            "poor": 3.0
        },
        "trend": "increasing",
        "unit": "/5",
        "alert_threshold": "poor",
        "weight": 1.5
    })
    
    # Get KPI status
    status = monitor.get_kpi_status()
    print(f"KPI Status: {json.dumps(status, indent=2)}")
    
    # Get KPI history
    history = monitor.get_kpi_history("requirements_quality", limit=5)
    print(f"KPI History: {json.dumps(history, indent=2)}")
    
    # Get KPI forecast
    forecast = monitor.get_kpi_forecast("requirements_quality", days=7)
    print(f"KPI Forecast: {json.dumps(forecast, indent=2)}")
    
    # Get KPI dashboard
    dashboard = monitor.get_kpi_dashboard()
    print(f"KPI Dashboard: {json.dumps(list(dashboard.keys()), indent=2)}")
    
    # Check all KPIs
    check_result = monitor.check_all_kpis()
    print(f"KPI Check Result: {json.dumps(list(check_result.keys()), indent=2)}")
