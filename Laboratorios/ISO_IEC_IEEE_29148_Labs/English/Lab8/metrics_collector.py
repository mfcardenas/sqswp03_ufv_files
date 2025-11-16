#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Metrics Collector Module
------------------------
This module implements the metrics collection engine for requirements analytics.
It handles automated collection, calculation, and aggregation of requirements metrics
following ISO/IEC/IEEE 29148:2011 standards.

Functions:
- Collect metrics from multiple data sources
- Process and normalize metrics data
- Store historical metrics
- Schedule automated collection intervals
"""

import json
import logging
import time
import datetime
import threading
import os
import csv
from typing import Dict, List, Any, Optional, Union, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("metrics_collector.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("MetricsCollector")

class MetricsCollector:
    """
    Metrics Collection Engine for Requirements Analytics
    
    This class provides functionality to:
    - Collect metrics from multiple sources
    - Process metrics in real-time
    - Store historical metrics data
    - Schedule automated collection intervals
    """
    
    def __init__(self, config_path: str = 'metrics_config.json'):
        """
        Initialize the metrics collector with configuration
        
        Args:
            config_path: Path to metrics configuration file
        """
        logger.info(f"Initializing MetricsCollector with config: {config_path}")
        self.config_path = config_path
        self.config = self._load_config()
        self.metrics_data = {}
        self.collection_thread = None
        self.is_collecting = False
        self.data_dir = os.path.join("data", "metrics")
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        logger.info("MetricsCollector initialized successfully")
    
    def _load_config(self) -> Dict[str, Any]:
        """
        Load metrics configuration from JSON file
        
        Returns:
            Dict containing metrics configuration
        """
        try:
            with open(self.config_path, 'r') as config_file:
                config = json.load(config_file)
                logger.info(f"Loaded configuration with {len(config['metrics'])} metrics")
                return config
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {self.config_path}")
            # Create default configuration
            default_config = {
                "collection_interval": 3600,  # Default: hourly collection
                "metrics": {
                    "requirements_quality": {
                        "enabled": True,
                        "source": "quality_analysis",
                        "aggregation": "average"
                    },
                    "review_efficiency": {
                        "enabled": True,
                        "source": "review_data",
                        "aggregation": "average",
                        "unit": "hours"
                    },
                    "defect_density": {
                        "enabled": True,
                        "source": "defect_tracking",
                        "aggregation": "count_per_item"
                    },
                    "requirements_completeness": {
                        "enabled": True,
                        "source": "requirements_db",
                        "aggregation": "percentage"
                    }
                },
                "data_sources": {
                    "quality_analysis": {
                        "type": "database",
                        "connection_string": "sqlite:///data/quality.db",
                        "query": "SELECT * FROM quality_scores"
                    },
                    "review_data": {
                        "type": "file",
                        "path": "data/reviews.csv"
                    },
                    "defect_tracking": {
                        "type": "api",
                        "url": "http://localhost:8080/api/defects"
                    },
                    "requirements_db": {
                        "type": "database",
                        "connection_string": "sqlite:///data/requirements.db"
                    }
                },
                "storage": {
                    "type": "file",
                    "format": "csv",
                    "retention_days": 365
                }
            }
            
            # Save default configuration
            with open(self.config_path, 'w') as config_file:
                json.dump(default_config, config_file, indent=4)
            
            logger.warning(f"Created default configuration file: {self.config_path}")
            return default_config
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in configuration file: {self.config_path}")
            raise
    
    def start_collection(self) -> None:
        """
        Start automated metrics collection based on configured interval
        """
        if self.is_collecting:
            logger.warning("Metrics collection already running")
            return
        
        self.is_collecting = True
        interval = self.config.get("collection_interval", 3600)  # Default: hourly
        
        logger.info(f"Starting metrics collection with interval: {interval} seconds")
        
        def collection_worker():
            while self.is_collecting:
                try:
                    self.collect_all_metrics()
                    time.sleep(interval)
                except Exception as e:
                    logger.error(f"Error in metrics collection: {str(e)}")
                    time.sleep(60)  # Wait a minute before retrying
        
        self.collection_thread = threading.Thread(target=collection_worker)
        self.collection_thread.daemon = True
        self.collection_thread.start()
    
    def stop_collection(self) -> None:
        """
        Stop the automated metrics collection
        """
        logger.info("Stopping metrics collection")
        self.is_collecting = False
        if self.collection_thread:
            self.collection_thread.join(timeout=10)
    
    def collect_all_metrics(self) -> Dict[str, Any]:
        """
        Collect all enabled metrics from configured sources
        
        Returns:
            Dict containing collected metrics data
        """
        logger.info("Collecting all metrics")
        timestamp = datetime.datetime.now().isoformat()
        
        metrics_result = {
            "timestamp": timestamp,
            "metrics": {}
        }
        
        for metric_name, metric_config in self.config["metrics"].items():
            if metric_config.get("enabled", True):
                try:
                    value = self.collect_metric(metric_name)
                    metrics_result["metrics"][metric_name] = value
                except Exception as e:
                    logger.error(f"Error collecting metric {metric_name}: {str(e)}")
        
        # Store collected metrics
        self._store_metrics(metrics_result)
        
        logger.info(f"Collected {len(metrics_result['metrics'])} metrics")
        return metrics_result
    
    def collect_metric(self, metric_name: str) -> Union[float, int, Dict]:
        """
        Collect a specific metric from its data source
        
        Args:
            metric_name: Name of the metric to collect
            
        Returns:
            Collected metric value
        """
        logger.info(f"Collecting metric: {metric_name}")
        
        if metric_name not in self.config["metrics"]:
            logger.error(f"Unknown metric: {metric_name}")
            raise ValueError(f"Unknown metric: {metric_name}")
        
        metric_config = self.config["metrics"][metric_name]
        source_name = metric_config.get("source")
        
        if not source_name or source_name not in self.config["data_sources"]:
            logger.error(f"Invalid data source for metric {metric_name}")
            raise ValueError(f"Invalid data source for metric {metric_name}")
        
        source_config = self.config["data_sources"][source_name]
        source_type = source_config.get("type")
        
        # Simulate data collection based on source type
        if source_type == "database":
            return self._collect_from_database(source_config, metric_config)
        elif source_type == "file":
            return self._collect_from_file(source_config, metric_config)
        elif source_type == "api":
            return self._collect_from_api(source_config, metric_config)
        else:
            logger.error(f"Unsupported data source type: {source_type}")
            raise ValueError(f"Unsupported data source type: {source_type}")
    
    def _collect_from_database(self, source_config: Dict, metric_config: Dict) -> float:
        """
        Collect metrics from a database source
        
        Args:
            source_config: Database source configuration
            metric_config: Metric configuration
            
        Returns:
            Calculated metric value
        """
        # In a real implementation, this would use database connection
        # For simulation, we'll generate sample data
        import random
        
        # Simulate query execution time
        time.sleep(0.1)
        
        # Generate random metric value based on metric type
        if metric_config.get("aggregation") == "average":
            return round(random.uniform(60, 95), 2)
        elif metric_config.get("aggregation") == "percentage":
            return round(random.uniform(50, 100), 2)
        elif metric_config.get("aggregation") == "count":
            return random.randint(10, 500)
        else:
            return round(random.uniform(0, 100), 2)
    
    def _collect_from_file(self, source_config: Dict, metric_config: Dict) -> float:
        """
        Collect metrics from a file source
        
        Args:
            source_config: File source configuration
            metric_config: Metric configuration
            
        Returns:
            Calculated metric value
        """
        # In a real implementation, this would read from the file
        # For simulation, we'll generate sample data
        import random
        
        # Simulate file reading time
        time.sleep(0.05)
        
        # Generate random metric value
        if metric_config.get("unit") == "hours":
            return round(random.uniform(1, 72), 1)
        elif metric_config.get("aggregation") == "percentage":
            return round(random.uniform(0, 100), 2)
        else:
            return round(random.uniform(0, 100), 2)
    
    def _collect_from_api(self, source_config: Dict, metric_config: Dict) -> float:
        """
        Collect metrics from an API source
        
        Args:
            source_config: API source configuration
            metric_config: Metric configuration
            
        Returns:
            Calculated metric value
        """
        # In a real implementation, this would make API requests
        # For simulation, we'll generate sample data
        import random
        
        # Simulate API response time
        time.sleep(0.2)
        
        # Generate random metric value
        if metric_config.get("aggregation") == "count_per_item":
            return round(random.uniform(0.01, 0.5), 3)
        else:
            return round(random.uniform(0, 100), 2)
    
    def _store_metrics(self, metrics_data: Dict[str, Any]) -> None:
        """
        Store collected metrics data
        
        Args:
            metrics_data: Metrics data to store
        """
        storage_config = self.config.get("storage", {"type": "file", "format": "csv"})
        storage_type = storage_config.get("type")
        
        if storage_type == "file":
            self._store_to_file(metrics_data, storage_config)
        elif storage_type == "database":
            self._store_to_database(metrics_data, storage_config)
        else:
            logger.warning(f"Unsupported storage type: {storage_type}, using file storage")
            self._store_to_file(metrics_data, {"format": "csv"})
    
    def _store_to_file(self, metrics_data: Dict[str, Any], storage_config: Dict) -> None:
        """
        Store metrics data to a file
        
        Args:
            metrics_data: Metrics data to store
            storage_config: Storage configuration
        """
        format_type = storage_config.get("format", "csv")
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        
        if format_type == "csv":
            # Store to CSV
            file_path = os.path.join(self.data_dir, f"metrics_{timestamp}.csv")
            
            # Check if file exists to determine if we need to write headers
            file_exists = os.path.isfile(file_path)
            
            with open(file_path, 'a', newline='') as csv_file:
                fieldnames = ["timestamp"] + list(metrics_data["metrics"].keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                row_data = {"timestamp": metrics_data["timestamp"]}
                row_data.update(metrics_data["metrics"])
                writer.writerow(row_data)
            
            logger.info(f"Stored metrics to CSV: {file_path}")
        
        elif format_type == "json":
            # Store to JSON
            file_path = os.path.join(self.data_dir, f"metrics_{timestamp}.json")
            
            # Read existing data if file exists
            if os.path.isfile(file_path):
                with open(file_path, 'r') as json_file:
                    try:
                        data = json.load(json_file)
                    except json.JSONDecodeError:
                        data = {"metrics": []}
            else:
                data = {"metrics": []}
            
            # Append new metrics
            data["metrics"].append(metrics_data)
            
            # Write updated data
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=2)
            
            logger.info(f"Stored metrics to JSON: {file_path}")
        
        else:
            logger.error(f"Unsupported file format: {format_type}")
    
    def _store_to_database(self, metrics_data: Dict[str, Any], storage_config: Dict) -> None:
        """
        Store metrics data to a database
        
        Args:
            metrics_data: Metrics data to store
            storage_config: Storage configuration
        """
        # In a real implementation, this would store to a database
        # For this lab example, we'll just log it
        logger.info(f"Simulated database storage of metrics: {metrics_data['timestamp']}")
    
    def get_latest_metrics(self) -> Dict[str, Any]:
        """
        Get the latest collected metrics
        
        Returns:
            Dict containing the latest metrics data
        """
        # In a real implementation, this would fetch from storage
        # For this lab, we'll generate a sample of latest metrics
        timestamp = datetime.datetime.now().isoformat()
        
        latest_metrics = {
            "timestamp": timestamp,
            "metrics": {}
        }
        
        for metric_name, metric_config in self.config["metrics"].items():
            if metric_config.get("enabled", True):
                try:
                    latest_metrics["metrics"][metric_name] = self.collect_metric(metric_name)
                except Exception as e:
                    logger.error(f"Error getting latest metric {metric_name}: {str(e)}")
        
        return latest_metrics
    
    def get_historical_metrics(self, 
                              metric_names: List[str] = None, 
                              start_date: str = None, 
                              end_date: str = None,
                              limit: int = 100) -> List[Dict[str, Any]]:
        """
        Get historical metrics data with optional filtering
        
        Args:
            metric_names: List of metric names to retrieve (None for all)
            start_date: Start date for filtering (ISO format)
            end_date: End date for filtering (ISO format)
            limit: Maximum number of records to retrieve
            
        Returns:
            List of historical metrics data
        """
        # In a real implementation, this would query the storage
        # For this lab, we'll generate sample historical data
        import random
        
        if not metric_names:
            metric_names = list(self.config["metrics"].keys())
        
        if not start_date:
            start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()
        
        if not end_date:
            end_date = datetime.datetime.now().isoformat()
        
        # Parse dates
        start_dt = datetime.datetime.fromisoformat(start_date)
        end_dt = datetime.datetime.fromisoformat(end_date)
        
        # Generate sample data points (one per day)
        historical_data = []
        current_dt = start_dt
        
        while current_dt <= end_dt and len(historical_data) < limit:
            data_point = {
                "timestamp": current_dt.isoformat(),
                "metrics": {}
            }
            
            for metric_name in metric_names:
                if metric_name in self.config["metrics"]:
                    metric_config = self.config["metrics"][metric_name]
                    
                    # Generate appropriate sample value based on metric type
                    if metric_name == "requirements_quality":
                        # Gradually improving trend
                        days_factor = (current_dt - start_dt).days / max(1, (end_dt - start_dt).days)
                        base_value = 75 + (days_factor * 10)
                        data_point["metrics"][metric_name] = round(base_value + random.uniform(-5, 5), 2)
                    
                    elif metric_name == "review_efficiency":
                        # Decreasing hours (improvement)
                        days_factor = (current_dt - start_dt).days / max(1, (end_dt - start_dt).days)
                        base_value = 60 - (days_factor * 20)
                        data_point["metrics"][metric_name] = round(max(5, base_value + random.uniform(-5, 5)), 1)
                    
                    elif metric_name == "defect_density":
                        # Decreasing defects (improvement)
                        days_factor = (current_dt - start_dt).days / max(1, (end_dt - start_dt).days)
                        base_value = 0.3 - (days_factor * 0.15)
                        data_point["metrics"][metric_name] = round(max(0.01, base_value + random.uniform(-0.05, 0.05)), 3)
                    
                    elif metric_name == "requirements_completeness":
                        # Increasing completeness
                        days_factor = (current_dt - start_dt).days / max(1, (end_dt - start_dt).days)
                        base_value = 60 + (days_factor * 30)
                        data_point["metrics"][metric_name] = round(min(100, base_value + random.uniform(-5, 5)), 2)
                    
                    else:
                        # Generic random value
                        data_point["metrics"][metric_name] = round(random.uniform(50, 100), 2)
            
            historical_data.append(data_point)
            current_dt += datetime.timedelta(days=1)
        
        return historical_data
    
    def process_metrics_batch(self, data_batch: List[Dict]) -> Dict[str, Any]:
        """
        Process a batch of metrics data for performance testing
        
        Args:
            data_batch: List of metrics data points to process
            
        Returns:
            Dict with processing results
        """
        start_time = time.time()
        processed_count = 0
        
        for data_point in data_batch:
            # Simulate processing each data point
            time.sleep(0.001)  # 1ms per item simulation
            processed_count += 1
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        logger.info(f"Processed {processed_count} metrics in {processing_time:.2f} seconds")
        
        return {
            "processed_count": processed_count,
            "processing_time": processing_time,
            "items_per_second": processed_count / max(0.001, processing_time)
        }
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """
        Get a summary of all metrics with current values and trends
        
        Returns:
            Dict containing metrics summary
        """
        # Get latest metrics
        latest = self.get_latest_metrics()
        
        # Get historical data for trend calculation (last 7 days)
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=7)
        historical = self.get_historical_metrics(
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat()
        )
        
        # Calculate trends
        summary = {
            "timestamp": latest["timestamp"],
            "metrics": {}
        }
        
        for metric_name, current_value in latest["metrics"].items():
            # Extract historical values for this metric
            historical_values = [
                point["metrics"].get(metric_name) 
                for point in historical 
                if metric_name in point["metrics"]
            ]
            
            # Calculate trend if we have enough data
            trend = None
            if len(historical_values) >= 2:
                first_value = historical_values[0]
                trend_change = current_value - first_value
                trend_percent = (trend_change / abs(first_value)) * 100 if first_value != 0 else 0
                
                # Determine if trend is positive based on metric type
                metric_config = self.config["metrics"].get(metric_name, {})
                trend_direction = metric_config.get("trend", "increasing")
                
                is_positive = (trend_change > 0 and trend_direction == "increasing") or \
                             (trend_change < 0 and trend_direction == "decreasing")
                
                trend = {
                    "change": round(trend_change, 2),
                    "percent": round(trend_percent, 2),
                    "direction": "up" if trend_change > 0 else "down",
                    "positive": is_positive
                }
            
            # Add to summary
            summary["metrics"][metric_name] = {
                "current": current_value,
                "trend": trend,
                "unit": self.config["metrics"].get(metric_name, {}).get("unit", "")
            }
        
        return summary


# Example usage
if __name__ == "__main__":
    # Create collector
    collector = MetricsCollector()
    
    # Start collection
    collector.start_collection()
    
    # Get latest metrics
    latest = collector.get_latest_metrics()
    print(f"Latest metrics: {json.dumps(latest, indent=2)}")
    
    # Get historical data
    historical = collector.get_historical_metrics(limit=5)
    print(f"Historical data sample: {json.dumps(historical, indent=2)}")
    
    # Get metrics summary
    summary = collector.get_metrics_summary()
    print(f"Metrics summary: {json.dumps(summary, indent=2)}")
    
    # Performance test with large dataset
    large_dataset = [{"data": i} for i in range(10000)]
    result = collector.process_metrics_batch(large_dataset)
    print(f"Performance test result: {json.dumps(result, indent=2)}")
    
    # Stop collection
    collector.stop_collection()
