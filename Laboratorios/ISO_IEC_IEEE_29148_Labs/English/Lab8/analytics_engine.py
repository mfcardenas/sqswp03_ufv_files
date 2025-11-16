#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Analytics Engine Module
----------------------
This module implements the analytics processing engine for requirements metrics.
It provides advanced analytics, trend analysis, and data processing capabilities
following ISO/IEC/IEEE 29148:2011 standards.

Functions:
- Process metrics data for analytics
- Calculate trends and patterns
- Generate insights from metrics
- Provide data for dashboards and reports
"""

import json
import logging
import datetime
import math
import os
from typing import Dict, List, Any, Optional, Union, Tuple

# Try to import advanced analytics libraries
try:
    import numpy as np
    import pandas as pd
    ADVANCED_ANALYTICS = True
except ImportError:
    ADVANCED_ANALYTICS = False
    logging.warning("Advanced analytics libraries not available. Using basic analytics.")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("analytics_engine.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("AnalyticsEngine")

class AnalyticsEngine:
    """
    Analytics Engine for Requirements Metrics
    
    This class provides functionality to:
    - Process metrics data for analytics
    - Calculate trends and patterns
    - Generate insights from metrics
    - Provide data for dashboards and reports
    """
    
    def __init__(self, metrics_collector=None):
        """
        Initialize the analytics engine
        
        Args:
            metrics_collector: Optional metrics collector instance
        """
        logger.info("Initializing AnalyticsEngine")
        
        self.metrics_collector = metrics_collector
        self.data_dir = os.path.join("data", "metrics")
        self.advanced_analytics = ADVANCED_ANALYTICS
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        logger.info("AnalyticsEngine initialized successfully")
    
    def analyze_metrics(self, metric_names: List[str] = None, 
                       start_date: str = None, 
                       end_date: str = None) -> Dict[str, Any]:
        """
        Analyze metrics data with optional filtering
        
        Args:
            metric_names: List of metric names to analyze (None for all)
            start_date: Start date for filtering (ISO format)
            end_date: End date for filtering (ISO format)
            
        Returns:
            Dict containing analytics results
        """
        logger.info(f"Analyzing metrics: {metric_names}")
        
        # Get historical data for analysis
        if self.metrics_collector:
            historical_data = self.metrics_collector.get_historical_metrics(
                metric_names=metric_names,
                start_date=start_date,
                end_date=end_date,
                limit=1000  # Increased limit for better analysis
            )
        else:
            # If no collector provided, load from files
            historical_data = self._load_historical_data(start_date, end_date)
        
        # Prepare result structure
        result = {
            "timestamp": datetime.datetime.now().isoformat(),
            "period": {
                "start": start_date,
                "end": end_date
            },
            "metrics_analyzed": metric_names if metric_names else "all",
            "analyses": {}
        }
        
        # Process with advanced analytics if available
        if self.advanced_analytics and len(historical_data) > 0:
            result["analyses"] = self._analyze_with_advanced(historical_data, metric_names)
        else:
            result["analyses"] = self._analyze_with_basic(historical_data, metric_names)
        
        logger.info(f"Completed metrics analysis: {len(result['analyses'])} metrics analyzed")
        return result
    
    def _load_historical_data(self, start_date: str = None, end_date: str = None) -> List[Dict[str, Any]]:
        """
        Load historical metrics data from files
        
        Args:
            start_date: Start date for filtering (ISO format)
            end_date: End date for filtering (ISO format)
            
        Returns:
            List of historical metrics data
        """
        # In a real implementation, this would load from actual files
        # For this lab, we'll generate sample data
        import random
        
        if not start_date:
            start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()
        
        if not end_date:
            end_date = datetime.datetime.now().isoformat()
        
        # Parse dates
        start_dt = datetime.datetime.fromisoformat(start_date)
        end_dt = datetime.datetime.fromisoformat(end_date)
        
        # Generate sample data points
        historical_data = []
        current_dt = start_dt
        
        metrics = [
            "requirements_quality",
            "review_efficiency",
            "defect_density",
            "requirements_completeness"
        ]
        
        while current_dt <= end_dt:
            data_point = {
                "timestamp": current_dt.isoformat(),
                "metrics": {}
            }
            
            # Days factor for trend simulation
            days_factor = (current_dt - start_dt).days / max(1, (end_dt - start_dt).days)
            
            # Generate values with realistic trends
            data_point["metrics"]["requirements_quality"] = round(75 + (days_factor * 10) + random.uniform(-5, 5), 2)
            data_point["metrics"]["review_efficiency"] = round(max(5, 60 - (days_factor * 20) + random.uniform(-5, 5)), 1)
            data_point["metrics"]["defect_density"] = round(max(0.01, 0.3 - (days_factor * 0.15) + random.uniform(-0.05, 0.05)), 3)
            data_point["metrics"]["requirements_completeness"] = round(min(100, 60 + (days_factor * 30) + random.uniform(-5, 5)), 2)
            
            historical_data.append(data_point)
            current_dt += datetime.timedelta(days=1)
        
        return historical_data
    
    def _analyze_with_basic(self, historical_data: List[Dict[str, Any]], 
                           metric_names: List[str] = None) -> Dict[str, Any]:
        """
        Analyze metrics using basic statistical methods
        
        Args:
            historical_data: List of historical metrics data points
            metric_names: List of metric names to analyze
            
        Returns:
            Dict containing analytics results
        """
        logger.info("Using basic analytics methods")
        
        if len(historical_data) == 0:
            return {}
        
        # Determine which metrics to analyze
        if not metric_names:
            # Get all available metrics from the first data point
            first_point = historical_data[0]
            metric_names = list(first_point["metrics"].keys())
        
        # Prepare results
        analyses = {}
        
        for metric_name in metric_names:
            # Extract values for this metric
            values = []
            timestamps = []
            
            for point in historical_data:
                if metric_name in point["metrics"]:
                    values.append(point["metrics"][metric_name])
                    timestamps.append(point["timestamp"])
            
            # Skip if no data
            if not values:
                continue
            
            # Basic statistics
            count = len(values)
            mean = sum(values) / count if count > 0 else 0
            sorted_values = sorted(values)
            median = sorted_values[count // 2] if count % 2 == 1 else (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
            minimum = min(values) if values else 0
            maximum = max(values) if values else 0
            
            # Calculate variance and standard deviation
            variance = sum((x - mean) ** 2 for x in values) / count if count > 0 else 0
            std_dev = math.sqrt(variance)
            
            # Basic trend analysis
            if count >= 2:
                first_value = values[0]
                last_value = values[-1]
                change = last_value - first_value
                percent_change = (change / abs(first_value)) * 100 if first_value != 0 else 0
                
                # Simple linear regression for trend line
                n = len(values)
                indices = list(range(n))
                
                sum_x = sum(indices)
                sum_y = sum(values)
                sum_xy = sum(i * v for i, v in zip(indices, values))
                sum_xx = sum(i * i for i in indices)
                
                # Calculate slope and intercept
                slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x) if n * sum_xx - sum_x * sum_x != 0 else 0
                intercept = (sum_y - slope * sum_x) / n
                
                # Project trend
                next_value = intercept + slope * n
                
                trend = {
                    "direction": "up" if slope > 0 else "down",
                    "slope": round(slope, 4),
                    "change": round(change, 2),
                    "percent_change": round(percent_change, 2),
                    "projected_next": round(next_value, 2)
                }
            else:
                trend = None
            
            # Store analysis
            analyses[metric_name] = {
                "count": count,
                "statistics": {
                    "mean": round(mean, 2),
                    "median": round(median, 2),
                    "min": round(minimum, 2),
                    "max": round(maximum, 2),
                    "std_dev": round(std_dev, 2)
                },
                "trend": trend,
                "data_points": list(zip(timestamps, values))
            }
        
        return analyses
    
    def _analyze_with_advanced(self, historical_data: List[Dict[str, Any]], 
                              metric_names: List[str] = None) -> Dict[str, Any]:
        """
        Analyze metrics using advanced statistical methods with NumPy/Pandas
        
        Args:
            historical_data: List of historical metrics data points
            metric_names: List of metric names to analyze
            
        Returns:
            Dict containing analytics results
        """
        logger.info("Using advanced analytics methods with NumPy/Pandas")
        
        if len(historical_data) == 0:
            return {}
        
        # Convert to DataFrame for easier analysis
        rows = []
        for point in historical_data:
            row = {"timestamp": point["timestamp"]}
            row.update(point["metrics"])
            rows.append(row)
        
        df = pd.DataFrame(rows)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.set_index("timestamp", inplace=True)
        
        # Determine which metrics to analyze
        if not metric_names:
            metric_names = [col for col in df.columns if col != "timestamp"]
        
        # Prepare results
        analyses = {}
        
        for metric_name in metric_names:
            if metric_name not in df.columns:
                continue
            
            # Get series for this metric
            series = df[metric_name]
            
            # Skip if no data
            if series.empty:
                continue
            
            # Advanced statistics
            stats = series.describe()
            
            # Linear regression for trend analysis
            x = np.arange(len(series))
            y = series.values
            
            if len(x) >= 2:
                # Use NumPy's polyfit for linear regression
                slope, intercept = np.polyfit(x, y, 1)
                
                # Calculate trend line
                trend_line = intercept + slope * x
                
                # Calculate R-squared
                y_mean = np.mean(y)
                ss_total = sum((y - y_mean) ** 2)
                ss_residual = sum((y - trend_line) ** 2)
                r_squared = 1 - (ss_residual / ss_total) if ss_total != 0 else 0
                
                # Project next value
                next_value = intercept + slope * len(series)
                
                # Calculate change
                first_value = series.iloc[0]
                last_value = series.iloc[-1]
                change = last_value - first_value
                percent_change = (change / abs(first_value)) * 100 if first_value != 0 else 0
                
                trend = {
                    "direction": "up" if slope > 0 else "down",
                    "slope": round(float(slope), 4),
                    "intercept": round(float(intercept), 4),
                    "r_squared": round(float(r_squared), 4),
                    "change": round(float(change), 2),
                    "percent_change": round(float(percent_change), 2),
                    "projected_next": round(float(next_value), 2)
                }
                
                # Detect seasonality (if enough data points)
                if len(series) >= 14:
                    try:
                        # Check for 7-day seasonality
                        autocorr = pd.Series(series).autocorr(lag=7)
                        has_seasonality = abs(autocorr) > 0.3
                        
                        trend["seasonality"] = {
                            "detected": bool(has_seasonality),
                            "autocorrelation": round(float(autocorr), 2)
                        }
                    except Exception as e:
                        logger.warning(f"Error detecting seasonality: {str(e)}")
            else:
                trend = None
            
            # Store analysis with data points
            analyses[metric_name] = {
                "count": int(stats["count"]),
                "statistics": {
                    "mean": round(float(stats["mean"]), 2),
                    "median": round(float(series.median()), 2),
                    "min": round(float(stats["min"]), 2),
                    "max": round(float(stats["max"]), 2),
                    "std_dev": round(float(stats["std"]), 2),
                    "25%": round(float(stats["25%"]), 2),
                    "75%": round(float(stats["75%"]), 2)
                },
                "trend": trend,
                "data_points": [(str(idx), round(float(val), 2)) 
                               for idx, val in zip(series.index, series.values)]
            }
        
        return analyses
    
    def analyze_trends(self, metric_name: str, 
                      period: str = "30d",
                      forecast_days: int = 7) -> Dict[str, Any]:
        """
        Perform trend analysis on a specific metric
        
        Args:
            metric_name: Name of the metric to analyze
            period: Time period for analysis (e.g., "7d", "30d", "90d")
            forecast_days: Number of days to forecast
            
        Returns:
            Dict containing trend analysis results
        """
        logger.info(f"Analyzing trends for metric: {metric_name}, period: {period}")
        
        # Parse period
        days = int(period[:-1]) if period.endswith("d") else 30
        
        # Calculate date range
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days)
        
        # Get historical data
        if self.metrics_collector:
            historical_data = self.metrics_collector.get_historical_metrics(
                metric_names=[metric_name],
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat(),
                limit=1000
            )
        else:
            # If no collector provided, load from files
            historical_data = self._load_historical_data(
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat()
            )
        
        # Extract values and timestamps
        values = []
        timestamps = []
        
        for point in historical_data:
            if metric_name in point["metrics"]:
                values.append(point["metrics"][metric_name])
                timestamps.append(point["timestamp"])
        
        # Check if we have enough data
        if len(values) < 2:
            logger.warning(f"Not enough data points for trend analysis: {len(values)}")
            return {
                "metric": metric_name,
                "period": period,
                "error": "Not enough data points for trend analysis"
            }
        
        # Perform trend analysis
        if self.advanced_analytics:
            return self._advanced_trend_analysis(metric_name, timestamps, values, forecast_days)
        else:
            return self._basic_trend_analysis(metric_name, timestamps, values, forecast_days)
    
    def _basic_trend_analysis(self, metric_name: str, timestamps: List[str], 
                             values: List[float], forecast_days: int) -> Dict[str, Any]:
        """
        Perform basic trend analysis
        
        Args:
            metric_name: Name of the metric
            timestamps: List of timestamps
            values: List of metric values
            forecast_days: Number of days to forecast
            
        Returns:
            Dict containing trend analysis results
        """
        # Convert timestamps to days from start for linear regression
        start_dt = datetime.datetime.fromisoformat(timestamps[0])
        days = [(datetime.datetime.fromisoformat(ts) - start_dt).days for ts in timestamps]
        
        # Simple linear regression
        n = len(values)
        sum_x = sum(days)
        sum_y = sum(values)
        sum_xy = sum(d * v for d, v in zip(days, values))
        sum_xx = sum(d * d for d in days)
        
        # Calculate slope and intercept
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x) if n * sum_xx - sum_x * sum_x != 0 else 0
        intercept = (sum_y - slope * sum_x) / n
        
        # Calculate trend line
        trend_line = [intercept + slope * d for d in days]
        
        # Calculate R-squared
        y_mean = sum(values) / n
        ss_total = sum((y - y_mean) ** 2 for y in values)
        ss_residual = sum((y - yhat) ** 2 for y, yhat in zip(values, trend_line))
        r_squared = 1 - (ss_residual / ss_total) if ss_total != 0 else 0
        
        # Generate forecast
        forecast = []
        last_day = days[-1]
        
        for i in range(1, forecast_days + 1):
            forecast_day = last_day + i
            forecast_value = intercept + slope * forecast_day
            forecast_date = (start_dt + datetime.timedelta(days=forecast_day)).isoformat()
            forecast.append({"date": forecast_date, "value": round(forecast_value, 2)})
        
        # Calculate change rate
        first_value = values[0]
        last_value = values[-1]
        change = last_value - first_value
        percent_change = (change / abs(first_value)) * 100 if first_value != 0 else 0
        
        # Determine trend quality based on R-squared
        trend_quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "weak"
        
        return {
            "metric": metric_name,
            "data_points": list(zip(timestamps, values)),
            "trend_line": list(zip(timestamps, trend_line)),
            "statistics": {
                "slope": round(slope, 4),
                "intercept": round(intercept, 4),
                "r_squared": round(r_squared, 4),
                "change": round(change, 2),
                "percent_change": round(percent_change, 2)
            },
            "trend": {
                "direction": "up" if slope > 0 else "down",
                "strength": trend_quality,
                "interpretation": self._interpret_trend(metric_name, slope, r_squared)
            },
            "forecast": forecast
        }
    
    def _advanced_trend_analysis(self, metric_name: str, timestamps: List[str], 
                                values: List[float], forecast_days: int) -> Dict[str, Any]:
        """
        Perform advanced trend analysis using NumPy/Pandas
        
        Args:
            metric_name: Name of the metric
            timestamps: List of timestamps
            values: List of metric values
            forecast_days: Number of days to forecast
            
        Returns:
            Dict containing trend analysis results
        """
        # Convert to DataFrame
        df = pd.DataFrame({
            "timestamp": pd.to_datetime(timestamps),
            "value": values
        })
        df.set_index("timestamp", inplace=True)
        
        # Resample to ensure regular intervals (daily)
        df_daily = df.resample("D").mean().interpolate(method="linear")
        
        # Linear regression
        x = np.arange(len(df_daily))
        y = df_daily["value"].values
        
        # Use NumPy's polyfit for linear regression
        slope, intercept = np.polyfit(x, y, 1)
        
        # Calculate trend line
        trend_line = intercept + slope * x
        
        # Calculate R-squared
        y_mean = np.mean(y)
        ss_total = sum((y - y_mean) ** 2)
        ss_residual = sum((y - trend_line) ** 2)
        r_squared = 1 - (ss_residual / ss_total) if ss_total != 0 else 0
        
        # Check for seasonality
        has_seasonality = False
        seasonality_period = None
        
        if len(df_daily) >= 14:
            try:
                # Check autocorrelations at different lags
                autocorrs = [df_daily["value"].autocorr(lag=i) for i in range(2, 8)]
                max_autocorr = max(autocorrs)
                max_lag = autocorrs.index(max_autocorr) + 2
                
                has_seasonality = max_autocorr > 0.3
                seasonality_period = max_lag if has_seasonality else None
            except Exception as e:
                logger.warning(f"Error detecting seasonality: {str(e)}")
        
        # Generate forecast
        forecast = []
        last_date = df_daily.index[-1]
        
        for i in range(1, forecast_days + 1):
            forecast_date = last_date + pd.Timedelta(days=i)
            forecast_day = len(df_daily) + i - 1
            forecast_value = intercept + slope * forecast_day
            
            # Add seasonality if detected
            if has_seasonality and seasonality_period:
                try:
                    season_index = (forecast_day % seasonality_period) - 1
                    if 0 <= season_index < len(df_daily):
                        seasonal_component = df_daily["value"].iloc[season_index] - trend_line[season_index]
                        forecast_value += seasonal_component
                except Exception as e:
                    logger.warning(f"Error applying seasonality to forecast: {str(e)}")
            
            forecast.append({
                "date": forecast_date.isoformat(),
                "value": round(float(forecast_value), 2)
            })
        
        # Calculate change rate
        first_value = df_daily["value"].iloc[0]
        last_value = df_daily["value"].iloc[-1]
        change = last_value - first_value
        percent_change = (change / abs(first_value)) * 100 if first_value != 0 else 0
        
        # Determine trend quality based on R-squared
        trend_quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "weak"
        
        # Format data for response
        data_points = [(str(idx), round(float(val), 2)) 
                     for idx, val in zip(df_daily.index, df_daily["value"])]
        
        trend_line_points = [(str(idx), round(float(val), 2)) 
                           for idx, val in zip(df_daily.index, trend_line)]
        
        return {
            "metric": metric_name,
            "data_points": data_points,
            "trend_line": trend_line_points,
            "statistics": {
                "slope": round(float(slope), 4),
                "intercept": round(float(intercept), 4),
                "r_squared": round(float(r_squared), 4),
                "change": round(float(change), 2),
                "percent_change": round(float(percent_change), 2)
            },
            "trend": {
                "direction": "up" if slope > 0 else "down",
                "strength": trend_quality,
                "interpretation": self._interpret_trend(metric_name, slope, r_squared),
                "seasonality": {
                    "detected": has_seasonality,
                    "period": seasonality_period
                }
            },
            "forecast": forecast
        }
    
    def _interpret_trend(self, metric_name: str, slope: float, r_squared: float) -> str:
        """
        Generate a human-readable interpretation of the trend
        
        Args:
            metric_name: Name of the metric
            slope: Slope of the trend line
            r_squared: R-squared value for the trend line
            
        Returns:
            String containing trend interpretation
        """
        # Define interpretation based on metric type
        if metric_name == "requirements_quality":
            if slope > 0.1:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Requirements quality shows a {quality} improving trend"
            elif slope < -0.1:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Requirements quality shows a {quality} declining trend - attention needed"
            else:
                return "Requirements quality remains stable"
            
        elif metric_name == "review_efficiency":
            # Lower is better for review time
            if slope < -0.1:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Review efficiency shows a {quality} improving trend (shorter reviews)"
            elif slope > 0.1:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Reviews are taking longer - {quality} declining efficiency"
            else:
                return "Review efficiency remains stable"
            
        elif metric_name == "defect_density":
            # Lower is better for defect density
            if slope < -0.001:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Defect density shows a {quality} improving trend (fewer defects)"
            elif slope > 0.001:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Defect density shows a {quality} increasing trend - attention needed"
            else:
                return "Defect density remains stable"
            
        elif metric_name == "requirements_completeness":
            if slope > 0.1:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Requirements completeness shows a {quality} improving trend"
            elif slope < -0.1:
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"Requirements completeness shows a {quality} declining trend - attention needed"
            else:
                return "Requirements completeness remains stable"
            
        else:
            # Generic interpretation
            if abs(slope) < 0.01:
                return f"{metric_name} shows a stable trend"
            else:
                direction = "increasing" if slope > 0 else "decreasing"
                quality = "strong" if r_squared > 0.7 else "moderate" if r_squared > 0.4 else "slight"
                return f"{metric_name} shows a {quality} {direction} trend"
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """
        Get comprehensive data for the analytics dashboard
        
        Returns:
            Dict containing dashboard data
        """
        logger.info("Generating dashboard data")
        
        # Get metrics summary
        if self.metrics_collector:
            metrics_summary = self.metrics_collector.get_metrics_summary()
        else:
            # Generate sample summary if no collector
            metrics_summary = self._generate_sample_summary()
        
        # Get trend analysis for each metric
        trends = {}
        for metric_name in metrics_summary["metrics"].keys():
            try:
                trends[metric_name] = self.analyze_trends(metric_name, period="30d")
            except Exception as e:
                logger.error(f"Error analyzing trends for {metric_name}: {str(e)}")
                trends[metric_name] = {"error": str(e)}
        
        # Generate insights
        insights = self.generate_insights(metrics_summary, trends)
        
        # Compile dashboard data
        dashboard_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "summary": metrics_summary,
            "trends": trends,
            "insights": insights,
            "recommendations": self.generate_recommendations(metrics_summary, trends)
        }
        
        return dashboard_data
    
    def _generate_sample_summary(self) -> Dict[str, Any]:
        """
        Generate a sample metrics summary when no collector is available
        
        Returns:
            Dict containing sample metrics summary
        """
        import random
        
        timestamp = datetime.datetime.now().isoformat()
        
        return {
            "timestamp": timestamp,
            "metrics": {
                "requirements_quality": {
                    "current": round(random.uniform(70, 90), 2),
                    "trend": {
                        "change": round(random.uniform(1, 5), 2),
                        "percent": round(random.uniform(1, 7), 2),
                        "direction": "up",
                        "positive": True
                    },
                    "unit": ""
                },
                "review_efficiency": {
                    "current": round(random.uniform(30, 60), 1),
                    "trend": {
                        "change": round(random.uniform(-10, -2), 2),
                        "percent": round(random.uniform(-15, -5), 2),
                        "direction": "down",
                        "positive": True
                    },
                    "unit": "hours"
                },
                "defect_density": {
                    "current": round(random.uniform(0.1, 0.3), 3),
                    "trend": {
                        "change": round(random.uniform(-0.05, -0.01), 3),
                        "percent": round(random.uniform(-20, -5), 2),
                        "direction": "down",
                        "positive": True
                    },
                    "unit": "defects/req"
                },
                "requirements_completeness": {
                    "current": round(random.uniform(75, 95), 2),
                    "trend": {
                        "change": round(random.uniform(3, 8), 2),
                        "percent": round(random.uniform(3, 10), 2),
                        "direction": "up",
                        "positive": True
                    },
                    "unit": "%"
                }
            }
        }
    
    def generate_insights(self, metrics_summary: Dict[str, Any],
                         trends: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate actionable insights from metrics data
        
        Args:
            metrics_summary: Dict containing metrics summary
            trends: Dict containing trend analyses
            
        Returns:
            List of insight objects
        """
        logger.info("Generating insights from metrics data")
        
        insights = []
        
        # Check for quality insights
        if "requirements_quality" in metrics_summary["metrics"]:
            quality = metrics_summary["metrics"]["requirements_quality"]
            
            if quality["current"] < 70:
                insights.append({
                    "type": "risk",
                    "priority": "high",
                    "title": "Low Requirements Quality",
                    "description": f"Requirements quality score is {quality['current']}, which is below the acceptable threshold of 70.",
                    "recommendation": "Review requirements quality criteria and conduct additional quality checks."
                })
            elif quality["current"] < 80:
                insights.append({
                    "type": "quality",
                    "priority": "medium",
                    "title": "Moderate Requirements Quality",
                    "description": f"Requirements quality score is {quality['current']}, which is acceptable but could be improved.",
                    "recommendation": "Focus on areas with lower quality scores for improvement."
                })
            
            # Check trend
            if quality.get("trend") and quality["trend"].get("direction") == "down" and not quality["trend"].get("positive", False):
                insights.append({
                    "type": "risk",
                    "priority": "medium",
                    "title": "Declining Quality Trend",
                    "description": f"Requirements quality shows a decline of {abs(quality['trend']['change'])} points ({abs(quality['trend']['percent'])}%).",
                    "recommendation": "Investigate recent process changes that might have affected quality."
                })
        
        # Check for efficiency insights
        if "review_efficiency" in metrics_summary["metrics"]:
            efficiency = metrics_summary["metrics"]["review_efficiency"]
            
            if efficiency["current"] > 60:
                insights.append({
                    "type": "efficiency",
                    "priority": "high",
                    "title": "Long Review Times",
                    "description": f"Average review time is {efficiency['current']} hours, which exceeds the target of 48 hours.",
                    "recommendation": "Streamline the review process or allocate additional resources."
                })
            
            # Check trend
            if efficiency.get("trend") and efficiency["trend"].get("direction") == "up" and not efficiency["trend"].get("positive", False):
                insights.append({
                    "type": "efficiency",
                    "priority": "medium",
                    "title": "Increasing Review Times",
                    "description": f"Review efficiency is declining with times increasing by {efficiency['trend']['change']} hours ({efficiency['trend']['percent']}%).",
                    "recommendation": "Analyze review bottlenecks and optimize the review process."
                })
        
        # Check for defect insights
        if "defect_density" in metrics_summary["metrics"]:
            defects = metrics_summary["metrics"]["defect_density"]
            
            if defects["current"] > 0.2:
                insights.append({
                    "type": "risk",
                    "priority": "high",
                    "title": "High Defect Density",
                    "description": f"Defect density is {defects['current']} defects per requirement, which exceeds the acceptable threshold of 0.2.",
                    "recommendation": "Implement additional quality control measures and review requirement authoring guidelines."
                })
            
            # Check trend
            if defects.get("trend") and defects["trend"].get("direction") == "up" and not defects["trend"].get("positive", False):
                insights.append({
                    "type": "risk",
                    "priority": "medium",
                    "title": "Increasing Defect Density",
                    "description": f"Defect density is increasing by {defects['trend']['change']} ({defects['trend']['percent']}%).",
                    "recommendation": "Investigate recent changes in requirements specification process."
                })
        
        # Check for completeness insights
        if "requirements_completeness" in metrics_summary["metrics"]:
            completeness = metrics_summary["metrics"]["requirements_completeness"]
            
            if completeness["current"] < 70:
                insights.append({
                    "type": "risk",
                    "priority": "high",
                    "title": "Low Requirements Completeness",
                    "description": f"Requirements completeness is at {completeness['current']}%, which is below the acceptable threshold of 70%.",
                    "recommendation": "Review incomplete requirements and ensure all required information is captured."
                })
            
            # Check trend
            if completeness.get("trend") and completeness["trend"].get("direction") == "down" and not completeness["trend"].get("positive", False):
                insights.append({
                    "type": "risk",
                    "priority": "medium",
                    "title": "Declining Completeness",
                    "description": f"Requirements completeness is declining by {abs(completeness['trend']['change'])}% ({abs(completeness['trend']['percent'])}%).",
                    "recommendation": "Review the requirements elicitation process for gaps."
                })
        
        # Add positive insights for balance
        positive_trends = []
        
        for metric_name, metric_data in metrics_summary["metrics"].items():
            if metric_data.get("trend") and metric_data["trend"].get("positive", False):
                if metric_data["trend"]["percent"] > 5:  # Significant improvement
                    positive_trends.append((metric_name, metric_data))
        
        # Add up to 2 positive insights
        for metric_name, metric_data in positive_trends[:2]:
            # Format the metric name for display
            display_name = metric_name.replace("_", " ").title()
            
            insights.append({
                "type": "success",
                "priority": "low",
                "title": f"Improving {display_name}",
                "description": f"{display_name} shows a positive trend with a {metric_data['trend']['percent']}% improvement.",
                "recommendation": "Continue with current best practices and document the successful approach."
            })
        
        # Check for cross-metric insights
        if "requirements_quality" in metrics_summary["metrics"] and "defect_density" in metrics_summary["metrics"]:
            quality = metrics_summary["metrics"]["requirements_quality"]
            defects = metrics_summary["metrics"]["defect_density"]
            
            # Correlation between quality and defects
            if quality["current"] < 80 and defects["current"] > 0.15:
                insights.append({
                    "type": "quality",
                    "priority": "high",
                    "title": "Quality-Defect Correlation",
                    "description": "There's a correlation between lower requirements quality and higher defect density.",
                    "recommendation": "Focus on improving requirements quality to reduce defects."
                })
        
        return insights
    
    def generate_recommendations(self, metrics_summary: Dict[str, Any],
                               trends: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on metrics data
        
        Args:
            metrics_summary: Dict containing metrics summary
            trends: Dict containing trend analyses
            
        Returns:
            List of recommendation objects
        """
        logger.info("Generating recommendations from metrics data")
        
        recommendations = []
        
        # Process improvement recommendations
        if "review_efficiency" in metrics_summary["metrics"]:
            efficiency = metrics_summary["metrics"]["review_efficiency"]
            
            if efficiency["current"] > 48:  # Target is 48 hours
                recommendations.append({
                    "area": "process",
                    "title": "Optimize Review Process",
                    "description": "Implement a streamlined review process to reduce review time.",
                    "actions": [
                        "Reduce the number of reviewers for smaller changes",
                        "Implement parallel reviews where appropriate",
                        "Set up automated pre-reviews to catch common issues"
                    ],
                    "priority": "high" if efficiency["current"] > 72 else "medium"
                })
        
        # Quality improvement recommendations
        quality_issues = False
        
        if "requirements_quality" in metrics_summary["metrics"]:
            quality = metrics_summary["metrics"]["requirements_quality"]
            
            if quality["current"] < 80:
                quality_issues = True
                recommendations.append({
                    "area": "quality",
                    "title": "Improve Requirements Quality",
                    "description": "Implement measures to improve overall requirements quality.",
                    "actions": [
                        "Provide additional training on requirements authoring",
                        "Implement quality checklists for requirements",
                        "Conduct regular quality audits"
                    ],
                    "priority": "high" if quality["current"] < 70 else "medium"
                })
        
        # Defect reduction recommendations
        if "defect_density" in metrics_summary["metrics"]:
            defects = metrics_summary["metrics"]["defect_density"]
            
            if defects["current"] > 0.1:
                recommendations.append({
                    "area": "quality",
                    "title": "Reduce Requirement Defects",
                    "description": "Implement measures to reduce defects in requirements.",
                    "actions": [
                        "Enhance requirements validation processes",
                        "Implement peer reviews before formal reviews",
                        "Use automated tools to detect common issues"
                    ],
                    "priority": "high" if defects["current"] > 0.2 else "medium"
                })
        
        # Completeness recommendations
        if "requirements_completeness" in metrics_summary["metrics"]:
            completeness = metrics_summary["metrics"]["requirements_completeness"]
            
            if completeness["current"] < 90:
                recommendations.append({
                    "area": "completeness",
                    "title": "Improve Requirements Completeness",
                    "description": "Ensure requirements capture all necessary information.",
                    "actions": [
                        "Implement completeness checklists",
                        "Review requirements templates for completeness",
                        "Provide training on comprehensive requirements"
                    ],
                    "priority": "high" if completeness["current"] < 70 else "medium"
                })
        
        # If no specific issues, add general improvement recommendation
        if not quality_issues and len(recommendations) < 2:
            recommendations.append({
                "area": "process",
                "title": "Continuous Improvement",
                "description": "Implement continuous improvement for requirements engineering.",
                "actions": [
                    "Conduct regular process retrospectives",
                    "Benchmark against industry standards",
                    "Implement regular training and skill development"
                ],
                "priority": "medium"
            })
        
        # Add automation recommendation if appropriate
        if "review_efficiency" in metrics_summary["metrics"] or "defect_density" in metrics_summary["metrics"]:
            recommendations.append({
                "area": "automation",
                "title": "Increase Automation",
                "description": "Implement additional automation in the requirements process.",
                "actions": [
                    "Automate quality checks and validation",
                    "Implement automated metrics collection and reporting",
                    "Develop automated compliance checking tools"
                ],
                "priority": "medium"
            })
        
        return recommendations
    
    def generate_report_data(self, report_type: str) -> Dict[str, Any]:
        """
        Generate data for a specific report type
        
        Args:
            report_type: Type of report to generate
            
        Returns:
            Dict containing report data
        """
        logger.info(f"Generating report data for type: {report_type}")
        
        # Get base data
        if self.metrics_collector:
            metrics_summary = self.metrics_collector.get_metrics_summary()
        else:
            metrics_summary = self._generate_sample_summary()
        
        # Common report data
        report_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "report_type": report_type,
            "metrics_summary": metrics_summary
        }
        
        # Add report-specific data
        if report_type == "quality":
            # Quality report focuses on quality metrics and trends
            report_data["quality_analysis"] = self.analyze_trends("requirements_quality", period="90d")
            report_data["defect_analysis"] = self.analyze_trends("defect_density", period="90d")
            report_data["quality_insights"] = [
                insight for insight in self.generate_insights(metrics_summary, {})
                if insight["type"] in ["quality", "risk"]
            ]
            report_data["quality_recommendations"] = [
                rec for rec in self.generate_recommendations(metrics_summary, {})
                if rec["area"] in ["quality", "completeness"]
            ]
            
        elif report_type == "efficiency":
            # Efficiency report focuses on process metrics
            report_data["efficiency_analysis"] = self.analyze_trends("review_efficiency", period="90d")
            report_data["efficiency_insights"] = [
                insight for insight in self.generate_insights(metrics_summary, {})
                if insight["type"] in ["efficiency"]
            ]
            report_data["efficiency_recommendations"] = [
                rec for rec in self.generate_recommendations(metrics_summary, {})
                if rec["area"] in ["process", "automation"]
            ]
            
        elif report_type == "compliance":
            # Compliance report (using completeness as a proxy)
            report_data["completeness_analysis"] = self.analyze_trends("requirements_completeness", period="90d")
            report_data["compliance_insights"] = [
                insight for insight in self.generate_insights(metrics_summary, {})
                if insight["type"] in ["risk", "quality"]
            ]
            report_data["compliance_recommendations"] = [
                rec for rec in self.generate_recommendations(metrics_summary, {})
                if rec["area"] in ["completeness", "quality"]
            ]
            
        elif report_type == "executive":
            # Executive summary with high-level metrics
            for metric_name in metrics_summary["metrics"]:
                report_data[f"{metric_name}_analysis"] = self.analyze_trends(metric_name, period="90d")
            
            report_data["key_insights"] = self.generate_insights(metrics_summary, {})[:5]
            report_data["key_recommendations"] = [
                rec for rec in self.generate_recommendations(metrics_summary, {})
                if rec["priority"] == "high"
            ]
            
        else:
            # Generic comprehensive report
            for metric_name in metrics_summary["metrics"]:
                report_data[f"{metric_name}_analysis"] = self.analyze_trends(metric_name, period="90d")
            
            report_data["all_insights"] = self.generate_insights(metrics_summary, {})
            report_data["all_recommendations"] = self.generate_recommendations(metrics_summary, {})
        
        return report_data


# Example usage
if __name__ == "__main__":
    # Create analytics engine
    engine = AnalyticsEngine()
    
    # Analyze a specific metric
    trend_analysis = engine.analyze_trends("requirements_quality")
    print(f"Trend analysis: {json.dumps(trend_analysis, indent=2)}")
    
    # Get dashboard data
    dashboard_data = engine.get_dashboard_data()
    print(f"Dashboard data sample: {json.dumps(list(dashboard_data.keys()), indent=2)}")
    
    # Generate a report
    report_data = engine.generate_report_data("quality")
    print(f"Report data sample: {json.dumps(list(report_data.keys()), indent=2)}")
