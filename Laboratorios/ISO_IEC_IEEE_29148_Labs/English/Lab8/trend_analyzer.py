#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Trend Analyzer Module
-------------------
This module implements trend analysis and predictive analytics for requirements metrics.
It provides historical trend identification, forecasting, and anomaly detection.

Functions:
- Analyze historical trends
- Generate forecasts and predictions
- Detect anomalies in metrics data
- Provide visualizations of trends
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
    from scipy import stats
    import statsmodels.api as sm
    from statsmodels.tsa.arima.model import ARIMA
    ADVANCED_ANALYTICS = True
except ImportError:
    ADVANCED_ANALYTICS = False
    logging.warning("Advanced analytics libraries not available. Using basic analytics.")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("trend_analyzer.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("TrendAnalyzer")

class TrendAnalyzer:
    """
    Trend Analyzer for Requirements Metrics
    
    This class provides functionality to:
    - Analyze historical trends in metrics data
    - Generate forecasts and predictions
    - Detect anomalies in metrics data
    - Provide visualizations of trends
    """
    
    def __init__(self, analytics_engine=None):
        """
        Initialize the trend analyzer
        
        Args:
            analytics_engine: Optional analytics engine instance
        """
        logger.info("Initializing TrendAnalyzer")
        
        self.analytics_engine = analytics_engine
        self.data_dir = os.path.join("data", "trends")
        self.advanced_analytics = ADVANCED_ANALYTICS
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        logger.info(f"TrendAnalyzer initialized with advanced analytics: {self.advanced_analytics}")
    
    def analyze_metric_trend(self, metric_name: str, 
                            period: str = "90d",
                            seasonality_check: bool = True,
                            anomaly_detection: bool = True) -> Dict[str, Any]:
        """
        Analyze trends for a specific metric
        
        Args:
            metric_name: Name of the metric to analyze
            period: Time period for analysis (e.g., "30d", "90d", "1y")
            seasonality_check: Whether to check for seasonality
            anomaly_detection: Whether to detect anomalies
            
        Returns:
            Dict containing trend analysis results
        """
        logger.info(f"Analyzing trends for metric: {metric_name}, period: {period}")
        
        # Get historical data
        historical_data = self._get_historical_data(metric_name, period)
        
        # Check if we have enough data
        if len(historical_data) < 2:
            logger.warning(f"Not enough data points for trend analysis: {len(historical_data)}")
            return {
                "metric": metric_name,
                "period": period,
                "error": "Not enough data points for trend analysis"
            }
        
        # Extract timestamps and values
        timestamps = [point["timestamp"] for point in historical_data]
        values = [point["value"] for point in historical_data]
        
        # Perform basic trend analysis
        basic_trend = self._analyze_basic_trend(metric_name, timestamps, values)
        
        # Add result object
        result = {
            "metric": metric_name,
            "period": period,
            "data_points": len(historical_data),
            "start_date": timestamps[0],
            "end_date": timestamps[-1],
            "trend": basic_trend["trend"]
        }
        
        # Add seasonality analysis if requested and we have enough data
        if seasonality_check and len(historical_data) >= 14:
            result["seasonality"] = self._analyze_seasonality(timestamps, values)
        
        # Add anomaly detection if requested
        if anomaly_detection:
            result["anomalies"] = self._detect_anomalies(timestamps, values)
        
        # Add forecast
        result["forecast"] = self._generate_forecast(metric_name, timestamps, values, basic_trend["trend"])
        
        # Add interpretation
        result["interpretation"] = self._generate_interpretation(metric_name, result)
        
        return result
    
    def _get_historical_data(self, metric_name: str, period: str) -> List[Dict[str, Any]]:
        """
        Get historical data for a metric
        
        Args:
            metric_name: Name of the metric
            period: Time period for analysis
            
        Returns:
            List of data points
        """
        # Parse period
        if period.endswith("d"):
            days = int(period[:-1])
        elif period.endswith("w"):
            days = int(period[:-1]) * 7
        elif period.endswith("m"):
            days = int(period[:-1]) * 30
        elif period.endswith("y"):
            days = int(period[:-1]) * 365
        else:
            days = 90  # Default to 90 days
        
        # Calculate date range
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days)
        
        # Get data from analytics engine if available
        if self.analytics_engine:
            # In a real implementation, this would call the analytics engine
            # For this lab, we'll generate sample data
            return self._generate_sample_data(metric_name, start_date, end_date)
        else:
            # Generate sample data
            return self._generate_sample_data(metric_name, start_date, end_date)
    
    def _generate_sample_data(self, metric_name: str, 
                             start_date: datetime.datetime,
                             end_date: datetime.datetime) -> List[Dict[str, Any]]:
        """
        Generate sample historical data
        
        Args:
            metric_name: Name of the metric
            start_date: Start date for data
            end_date: End date for data
            
        Returns:
            List of data points
        """
        import random
        
        # Generate one data point per day
        data_points = []
        current_date = start_date
        
        # Different metrics have different patterns
        if metric_name == "requirements_quality":
            # Start at 75, gradually improve to 85
            base = 75
            slope = 10 / max(1, (end_date - start_date).days)
            
            while current_date <= end_date:
                days = (current_date - start_date).days
                value = base + (slope * days)
                
                # Add some random noise
                value += random.uniform(-3, 3)
                
                # Add seasonal pattern (slight dip every 7 days)
                day_of_week = current_date.weekday()
                if day_of_week == 5 or day_of_week == 6:  # Weekend
                    value -= 2
                
                # Add an anomaly around the middle
                mid_point = start_date + (end_date - start_date) / 2
                if abs((current_date - mid_point).days) < 2:
                    value -= 8  # Significant drop
                
                data_points.append({
                    "timestamp": current_date.isoformat(),
                    "value": round(max(0, value), 2)
                })
                
                current_date += datetime.timedelta(days=1)
        
        elif metric_name == "review_efficiency":
            # Start at 60 hours, improve to 40 hours (lower is better)
            base = 60
            slope = -20 / max(1, (end_date - start_date).days)
            
            while current_date <= end_date:
                days = (current_date - start_date).days
                value = base + (slope * days)
                
                # Add some random noise
                value += random.uniform(-5, 5)
                
                # Add seasonal pattern (higher on Mondays)
                day_of_week = current_date.weekday()
                if day_of_week == 0:  # Monday
                    value += 8
                
                # Add an anomaly around 1/3 of the way
                third_point = start_date + (end_date - start_date) / 3
                if abs((current_date - third_point).days) < 2:
                    value += 15  # Significant spike
                
                data_points.append({
                    "timestamp": current_date.isoformat(),
                    "value": round(max(1, value), 1)
                })
                
                current_date += datetime.timedelta(days=1)
                
        elif metric_name == "defect_density":
            # Start at 0.25, improve to 0.1 (lower is better)
            base = 0.25
            slope = -0.15 / max(1, (end_date - start_date).days)
            
            while current_date <= end_date:
                days = (current_date - start_date).days
                value = base + (slope * days)
                
                # Add some random noise
                value += random.uniform(-0.02, 0.02)
                
                # Add subtle bi-weekly pattern
                day_in_cycle = days % 14
                if day_in_cycle < 7:
                    value += 0.01
                
                # Add an anomaly around 2/3 of the way
                two_thirds = start_date + 2 * (end_date - start_date) / 3
                if abs((current_date - two_thirds).days) < 2:
                    value += 0.08  # Significant spike
                
                data_points.append({
                    "timestamp": current_date.isoformat(),
                    "value": round(max(0.01, value), 3)
                })
                
                current_date += datetime.timedelta(days=1)
                
        else:
            # Generic increasing trend
            base = 50
            slope = 30 / max(1, (end_date - start_date).days)
            
            while current_date <= end_date:
                days = (current_date - start_date).days
                value = base + (slope * days)
                
                # Add some random noise
                value += random.uniform(-5, 5)
                
                # Add monthly pattern
                day_in_month = current_date.day
                if day_in_month < 5:
                    value -= 3
                elif day_in_month > 25:
                    value += 3
                
                # Add an anomaly
                if random.random() < 0.03:  # 3% chance per day
                    value += random.choice([-15, 15])  # Random spike or dip
                
                data_points.append({
                    "timestamp": current_date.isoformat(),
                    "value": round(max(0, value), 2)
                })
                
                current_date += datetime.timedelta(days=1)
        
        return data_points
    
    def _analyze_basic_trend(self, metric_name: str, 
                            timestamps: List[str], 
                            values: List[float]) -> Dict[str, Any]:
        """
        Perform basic trend analysis
        
        Args:
            metric_name: Name of the metric
            timestamps: List of timestamp strings
            values: List of metric values
            
        Returns:
            Dict containing basic trend analysis
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
        denominator = n * sum_xx - sum_x * sum_x
        if denominator == 0:
            slope = 0
        else:
            slope = (n * sum_xy - sum_x * sum_y) / denominator
        
        intercept = (sum_y - slope * sum_x) / n
        
        # Calculate trend line
        trend_line = [intercept + slope * d for d in days]
        
        # Calculate R-squared
        y_mean = sum(values) / n
        ss_total = sum((y - y_mean) ** 2 for y in values)
        ss_residual = sum((y - yhat) ** 2 for y, yhat in zip(values, trend_line))
        
        if ss_total == 0:
            r_squared = 0
        else:
            r_squared = 1 - (ss_residual / ss_total)
        
        # Calculate basic statistics
        first_value = values[0]
        last_value = values[-1]
        min_value = min(values)
        max_value = max(values)
        
        # Calculate change
        change = last_value - first_value
        if first_value == 0:
            percent_change = 0
        else:
            percent_change = (change / abs(first_value)) * 100
        
        # Determine trend direction and strength
        if abs(slope) < 0.0001:
            direction = "flat"
        else:
            direction = "up" if slope > 0 else "down"
        
        if r_squared < 0.3:
            strength = "weak"
        elif r_squared < 0.7:
            strength = "moderate"
        else:
            strength = "strong"
        
        # Determine if trend is good or bad based on metric
        is_good = None
        if metric_name == "requirements_quality":
            is_good = slope > 0  # Higher is better
        elif metric_name == "review_efficiency":
            is_good = slope < 0  # Lower is better (hours)
        elif metric_name == "defect_density":
            is_good = slope < 0  # Lower is better
        elif metric_name == "requirements_completeness":
            is_good = slope > 0  # Higher is better
        
        # Return trend information
        return {
            "trend": {
                "direction": direction,
                "strength": strength,
                "slope": round(slope, 6),
                "intercept": round(intercept, 2),
                "r_squared": round(r_squared, 4),
                "change": round(change, 3),
                "percent_change": round(percent_change, 2),
                "is_good": is_good,
                "first_value": round(first_value, 3),
                "last_value": round(last_value, 3),
                "min_value": round(min_value, 3),
                "max_value": round(max_value, 3)
            },
            "trend_line": list(zip(timestamps, [round(v, 3) for v in trend_line]))
        }
    
    def _analyze_seasonality(self, timestamps: List[str], 
                            values: List[float]) -> Dict[str, Any]:
        """
        Analyze seasonality patterns in the data
        
        Args:
            timestamps: List of timestamp strings
            values: List of metric values
            
        Returns:
            Dict containing seasonality analysis
        """
        # Convert timestamps to datetime objects
        dates = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
        
        # Check for common seasonality patterns
        patterns = {
            "daily": False,
            "weekly": False,
            "monthly": False,
            "detected_period": None,
            "confidence": 0
        }
        
        # If we have advanced analytics libraries, use autocorrelation
        if self.advanced_analytics and len(values) >= 14:
            try:
                # Detrend the data
                x = np.array(range(len(values)))
                y = np.array(values)
                
                # Linear regression to remove trend
                slope, intercept, _, _, _ = stats.linregress(x, y)
                trend = slope * x + intercept
                detrended = y - trend
                
                # Calculate autocorrelation
                autocorr = sm.tsa.acf(detrended, nlags=min(14, len(detrended) // 2))
                
                # Check for weekly pattern (lag 7)
                if len(autocorr) > 7 and autocorr[7] > 0.3:
                    patterns["weekly"] = True
                    patterns["detected_period"] = 7
                    patterns["confidence"] = round(autocorr[7], 2)
                
                # Check for monthly pattern (lag ~30)
                monthly_lag = min(30, len(autocorr) - 1)
                if len(autocorr) > monthly_lag and autocorr[monthly_lag] > 0.3:
                    patterns["monthly"] = True
                    patterns["detected_period"] = monthly_lag
                    patterns["confidence"] = round(autocorr[monthly_lag], 2)
                
                # Check for other strong autocorrelations
                if not patterns["weekly"] and not patterns["monthly"]:
                    # Skip lag 0 (always 1.0)
                    max_corr = max(autocorr[1:]) if len(autocorr) > 1 else 0
                    max_lag = list(autocorr).index(max_corr) if max_corr > 0.3 else None
                    
                    if max_lag:
                        patterns["detected_period"] = max_lag
                        patterns["confidence"] = round(max_corr, 2)
                
                # Store autocorrelation values
                patterns["autocorrelation"] = [round(float(a), 3) for a in autocorr]
                
            except Exception as e:
                logger.error(f"Error in advanced seasonality analysis: {str(e)}")
                # Fall back to basic analysis
        
        # Basic pattern detection using day of week
        if not patterns["detected_period"] and len(dates) >= 14:
            # Group values by day of week
            day_of_week_values = [[] for _ in range(7)]
            
            for date, value in zip(dates, values):
                day_of_week_values[date.weekday()].append(value)
            
            # Calculate average value for each day of week
            day_averages = [sum(values) / len(values) if values else 0 for values in day_of_week_values]
            
            # Calculate overall average
            overall_avg = sum(values) / len(values)
            
            # Check for significant variation by day of week
            variations = [abs(avg - overall_avg) / overall_avg if overall_avg != 0 else 0 for avg in day_averages]
            max_variation = max(variations)
            
            if max_variation > 0.1:  # >10% variation suggests weekly pattern
                patterns["weekly"] = True
                patterns["detected_period"] = 7
                patterns["confidence"] = round(min(max_variation * 5, 0.99), 2)  # Scale to confidence
                patterns["day_of_week_pattern"] = [round(avg, 3) for avg in day_averages]
        
        # Check for month-end patterns
        if len(dates) >= 60:  # Need enough data to detect monthly patterns
            # Group values by day of month
            day_of_month_values = [[] for _ in range(31)]
            
            for date, value in zip(dates, values):
                if date.day <= 31:
                    day_of_month_values[date.day - 1].append(value)
            
            # Calculate average value for each day of month
            day_averages = [sum(values) / len(values) if values else 0 for values in day_of_month_values]
            
            # Calculate overall average
            overall_avg = sum(values) / len(values)
            
            # Check for significant variation in month-end (last 5 days)
            month_end_avg = sum(day_averages[-5:]) / 5 if all(day_averages[-5:]) else 0
            month_end_variation = abs(month_end_avg - overall_avg) / overall_avg if overall_avg != 0 else 0
            
            if month_end_variation > 0.1:  # >10% variation suggests monthly pattern
                if not patterns["detected_period"] or patterns["confidence"] < month_end_variation * 5:
                    patterns["monthly"] = True
                    patterns["detected_period"] = 30
                    patterns["confidence"] = round(min(month_end_variation * 5, 0.99), 2)
        
        return patterns
    
    def _detect_anomalies(self, timestamps: List[str], 
                         values: List[float]) -> List[Dict[str, Any]]:
        """
        Detect anomalies in the data
        
        Args:
            timestamps: List of timestamp strings
            values: List of metric values
            
        Returns:
            List of detected anomalies
        """
        anomalies = []
        
        # Need enough data for meaningful anomaly detection
        if len(values) < 7:
            return anomalies
        
        # If we have advanced analytics libraries, use more sophisticated methods
        if self.advanced_analytics:
            try:
                # Use Z-score method for anomaly detection
                y = np.array(values)
                
                # Calculate moving average and standard deviation with window size 7
                window = 7
                weights = np.ones(window) / window
                y_smooth = np.convolve(y, weights, mode='same')
                
                # For the edges, use smaller windows
                for i in range(window // 2):
                    # Left edge
                    left_weights = np.ones(i + window // 2 + 1) / (i + window // 2 + 1)
                    y_smooth[i] = np.sum(y[:i + window // 2 + 1] * left_weights)
                    
                    # Right edge
                    right_weights = np.ones(i + window // 2 + 1) / (i + window // 2 + 1)
                    y_smooth[-(i+1)] = np.sum(y[-(i + window // 2 + 1):] * right_weights)
                
                # Calculate residuals
                residuals = y - y_smooth
                
                # Calculate standard deviation of residuals
                std_residuals = np.std(residuals)
                
                # Identify anomalies as points with residuals > 2.5 standard deviations
                z_scores = residuals / std_residuals if std_residuals > 0 else np.zeros_like(residuals)
                anomaly_indices = np.where(np.abs(z_scores) > 2.5)[0]
                
                # Create anomaly objects
                for idx in anomaly_indices:
                    anomalies.append({
                        "timestamp": timestamps[idx],
                        "value": round(float(values[idx]), 3),
                        "expected_value": round(float(y_smooth[idx]), 3),
                        "z_score": round(float(z_scores[idx]), 2),
                        "severity": "high" if abs(z_scores[idx]) > 4 else "medium"
                    })
                    
            except Exception as e:
                logger.error(f"Error in advanced anomaly detection: {str(e)}")
                # Fall back to basic method
        
        # Basic anomaly detection using moving average
        if not anomalies:
            window_size = min(7, len(values) // 2)
            if window_size < 2:
                return anomalies
            
            for i in range(len(values)):
                # Calculate local average (excluding the current point)
                if i < window_size:
                    # For beginning points, use forward window
                    local_values = values[i+1:i+window_size+1]
                    if not local_values:
                        continue
                    local_avg = sum(local_values) / len(local_values)
                elif i >= len(values) - window_size:
                    # For end points, use backward window
                    local_values = values[i-window_size:i]
                    if not local_values:
                        continue
                    local_avg = sum(local_values) / len(local_values)
                else:
                    # For middle points, use surrounding window
                    surrounding = values[i-window_size:i] + values[i+1:i+window_size+1]
                    local_avg = sum(surrounding) / len(surrounding)
                
                # Calculate deviation
                deviation = abs(values[i] - local_avg)
                relative_deviation = deviation / local_avg if local_avg != 0 else 0
                
                # Identify significant deviations
                if relative_deviation > 0.25:  # >25% deviation
                    anomalies.append({
                        "timestamp": timestamps[i],
                        "value": round(values[i], 3),
                        "expected_value": round(local_avg, 3),
                        "deviation": round(relative_deviation, 2),
                        "severity": "high" if relative_deviation > 0.5 else "medium"
                    })
        
        return anomalies
    
    def _generate_forecast(self, metric_name: str, 
                          timestamps: List[str], 
                          values: List[float],
                          trend: Dict[str, Any],
                          forecast_days: int = 30) -> Dict[str, Any]:
        """
        Generate forecast for future values
        
        Args:
            metric_name: Name of the metric
            timestamps: List of timestamp strings
            values: List of metric values
            trend: Trend information
            forecast_days: Number of days to forecast
            
        Returns:
            Dict containing forecast information
        """
        # Get last date
        last_date = datetime.datetime.fromisoformat(timestamps[-1])
        
        # Basic linear extrapolation
        slope = trend["slope"]
        intercept = trend["intercept"]
        
        # Convert timestamps to days from start for extrapolation
        start_dt = datetime.datetime.fromisoformat(timestamps[0])
        max_days = (last_date - start_dt).days
        
        # Generate forecast points
        forecast_points = []
        
        for i in range(1, forecast_days + 1):
            forecast_day = max_days + i
            forecast_date = last_date + datetime.timedelta(days=i)
            
            # Basic forecast using trend line
            forecast_value = intercept + slope * forecast_day
            
            # Ensure reasonable bounds
            if metric_name == "requirements_quality":
                forecast_value = min(100, max(0, forecast_value))
            elif metric_name == "review_efficiency":
                forecast_value = max(1, forecast_value)
            elif metric_name == "defect_density":
                forecast_value = max(0, forecast_value)
            
            forecast_points.append({
                "timestamp": forecast_date.isoformat(),
                "value": round(forecast_value, 3)
            })
        
        # Calculate time to reach significant milestones
        milestones = {}
        
        if metric_name == "requirements_quality":
            # Milestones for quality: 80, 90, 95
            thresholds = [80, 90, 95]
            for threshold in thresholds:
                if slope > 0 and trend["last_value"] < threshold:
                    days_to_threshold = (threshold - intercept) / slope - max_days if slope != 0 else float('inf')
                    if days_to_threshold > 0:
                        milestones[str(threshold)] = round(days_to_threshold)
                        
        elif metric_name == "review_efficiency":
            # Milestones for efficiency: 48, 36, 24 hours (lower is better)
            thresholds = [48, 36, 24]
            for threshold in thresholds:
                if slope < 0 and trend["last_value"] > threshold:
                    days_to_threshold = (threshold - intercept) / slope - max_days if slope != 0 else float('inf')
                    if days_to_threshold > 0:
                        milestones[str(threshold)] = round(days_to_threshold)
                        
        elif metric_name == "defect_density":
            # Milestones for defect density: 0.2, 0.1, 0.05 (lower is better)
            thresholds = [0.2, 0.1, 0.05]
            for threshold in thresholds:
                if slope < 0 and trend["last_value"] > threshold:
                    days_to_threshold = (threshold - intercept) / slope - max_days if slope != 0 else float('inf')
                    if days_to_threshold > 0:
                        milestones[str(threshold)] = round(days_to_threshold)
        
        # Prepare forecast result
        forecast_result = {
            "points": forecast_points,
            "confidence": round(trend["r_squared"] * 100),
            "method": "linear_extrapolation",
            "milestones": milestones
        }
        
        # Add advanced forecast if available
        if self.advanced_analytics and len(values) >= 14:
            try:
                # Use ARIMA for advanced forecasting
                y = np.array(values)
                
                # Fit ARIMA model
                model = ARIMA(y, order=(1, 1, 0))
                model_fit = model.fit()
                
                # Generate forecast
                arima_forecast = model_fit.forecast(steps=forecast_days)
                
                # Create forecast points
                arima_points = []
                
                for i in range(forecast_days):
                    forecast_date = last_date + datetime.timedelta(days=i+1)
                    forecast_value = arima_forecast[i]
                    
                    # Ensure reasonable bounds
                    if metric_name == "requirements_quality":
                        forecast_value = min(100, max(0, forecast_value))
                    elif metric_name == "review_efficiency":
                        forecast_value = max(1, forecast_value)
                    elif metric_name == "defect_density":
                        forecast_value = max(0, forecast_value)
                    
                    arima_points.append({
                        "timestamp": forecast_date.isoformat(),
                        "value": round(float(forecast_value), 3)
                    })
                
                # Add ARIMA forecast
                forecast_result["advanced_forecast"] = {
                    "points": arima_points,
                    "method": "ARIMA(1,1,0)"
                }
                
            except Exception as e:
                logger.error(f"Error in advanced forecasting: {str(e)}")
        
        return forecast_result
    
    def _generate_interpretation(self, metric_name: str, 
                               analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate human-readable interpretation of the analysis
        
        Args:
            metric_name: Name of the metric
            analysis: Analysis results
            
        Returns:
            Dict containing interpretation
        """
        trend = analysis["trend"]
        
        # Base interpretation on trend direction and strength
        if trend["direction"] == "flat":
            trend_text = f"{metric_name.replace('_', ' ').title()} has remained stable"
        elif trend["direction"] == "up":
            trend_text = f"{metric_name.replace('_', ' ').title()} has been increasing at a {trend['strength']} rate"
        else:
            trend_text = f"{metric_name.replace('_', ' ').title()} has been decreasing at a {trend['strength']} rate"
        
        # Add context about whether this is good or bad
        if trend["is_good"] is not None:
            if trend["is_good"]:
                quality_text = "This is a positive trend"
            else:
                quality_text = "This is a negative trend that requires attention"
        else:
            quality_text = ""
        
        # Add quantification
        if trend["direction"] != "flat":
            change_text = f"with a change of {abs(trend['change'])} ({abs(trend['percent_change'])}%) over the period"
        else:
            change_text = ""
        
        # Add seasonality interpretation if available
        seasonality_text = ""
        if "seasonality" in analysis and analysis["seasonality"]["detected_period"]:
            period = analysis["seasonality"]["detected_period"]
            confidence = analysis["seasonality"]["confidence"]
            
            if period == 7:
                seasonality_text = f"There is a weekly pattern in the data with {confidence * 100:.0f}% confidence"
            elif period > 25 and period < 32:
                seasonality_text = f"There is a monthly pattern in the data with {confidence * 100:.0f}% confidence"
            else:
                seasonality_text = f"There is a cyclical pattern every {period} days with {confidence * 100:.0f}% confidence"
        
        # Add anomaly interpretation if available
        anomaly_text = ""
        if "anomalies" in analysis and analysis["anomalies"]:
            anomaly_count = len(analysis["anomalies"])
            high_severity = sum(1 for a in analysis["anomalies"] if a["severity"] == "high")
            
            if high_severity > 0:
                anomaly_text = f"Detected {anomaly_count} anomalies, including {high_severity} high-severity anomalies that require investigation"
            else:
                anomaly_text = f"Detected {anomaly_count} moderate anomalies in the data"
        
        # Add forecast interpretation
        forecast_text = ""
        if "forecast" in analysis and analysis["forecast"]["points"]:
            confidence = analysis["forecast"]["confidence"]
            
            if confidence < 50:
                forecast_text = f"The forecast has low confidence ({confidence}%) due to high variability in the data"
            else:
                forecast_text = f"Based on the current trend, the forecast has {confidence}% confidence"
                
                # Add milestone information
                milestones = analysis["forecast"]["milestones"]
                if milestones:
                    milestone_texts = []
                    
                    for threshold, days in milestones.items():
                        if metric_name == "requirements_quality":
                            milestone_texts.append(f"quality score of {threshold} in approximately {days} days")
                        elif metric_name == "review_efficiency":
                            milestone_texts.append(f"review time of {threshold} hours in approximately {days} days")
                        elif metric_name == "defect_density":
                            milestone_texts.append(f"defect density of {threshold} in approximately {days} days")
                    
                    if milestone_texts:
                        milestone_text = "The metric is projected to reach " + ", ".join(milestone_texts)
                        forecast_text += ". " + milestone_text
        
        # Combine all interpretations
        summary = f"{trend_text} {change_text}. {quality_text}."
        
        if seasonality_text:
            details = f"{seasonality_text}. {anomaly_text}."
        else:
            details = anomaly_text
        
        # Prepare interpretation result
        interpretation = {
            "summary": summary.strip(),
            "details": details.strip(),
            "forecast": forecast_text.strip()
        }
        
        return interpretation
    
    def analyze_cross_metric_trends(self, metric_names: List[str], 
                                  period: str = "90d") -> Dict[str, Any]:
        """
        Analyze relationships between multiple metrics
        
        Args:
            metric_names: List of metrics to analyze
            period: Time period for analysis
            
        Returns:
            Dict containing cross-metric analysis
        """
        logger.info(f"Analyzing cross-metric trends for: {metric_names}")
        
        if len(metric_names) < 2:
            return {"error": "Need at least two metrics for cross-metric analysis"}
        
        # Get individual metric analyses
        metric_analyses = {}
        for metric_name in metric_names:
            metric_analyses[metric_name] = self.analyze_metric_trend(
                metric_name=metric_name,
                period=period,
                seasonality_check=False,
                anomaly_detection=False
            )
        
        # Prepare result
        result = {
            "metrics": metric_names,
            "period": period,
            "individual_analyses": metric_analyses,
            "correlations": {},
            "relationships": [],
            "insights": []
        }
        
        # Calculate correlations between metrics
        correlations = {}
        
        for i, metric1 in enumerate(metric_names):
            for j, metric2 in enumerate(metric_names):
                if i >= j:
                    continue  # Skip self-correlations and duplicates
                
                # Get data points for both metrics
                data1 = metric_analyses[metric1].get("data_points", [])
                data2 = metric_analyses[metric2].get("data_points", [])
                
                if not data1 or not data2:
                    continue
                
                # Ensure we have the same timestamps
                timestamps1 = [datetime.datetime.fromisoformat(point["timestamp"]) for point in data1]
                timestamps2 = [datetime.datetime.fromisoformat(point["timestamp"]) for point in data2]
                
                # Find common date range
                common_dates = []
                for ts in timestamps1:
                    if ts in timestamps2:
                        common_dates.append(ts)
                
                if len(common_dates) < 7:
                    # Not enough common data points
                    correlations[f"{metric1}_{metric2}"] = {"correlation": 0, "significance": "insufficient_data"}
                    continue
                
                # Extract values for common dates
                values1 = []
                values2 = []
                
                for date in common_dates:
                    idx1 = timestamps1.index(date)
                    idx2 = timestamps2.index(date)
                    
                    if idx1 < len(data1) and idx2 < len(data2):
                        values1.append(data1[idx1]["value"])
                        values2.append(data2[idx2]["value"])
                
                # Calculate correlation
                if self.advanced_analytics:
                    try:
                        correlation, p_value = stats.pearsonr(values1, values2)
                        
                        # Determine significance
                        if p_value < 0.01:
                            significance = "strong"
                        elif p_value < 0.05:
                            significance = "moderate"
                        else:
                            significance = "weak"
                        
                        correlations[f"{metric1}_{metric2}"] = {
                            "correlation": round(float(correlation), 3),
                            "p_value": round(float(p_value), 3),
                            "significance": significance
                        }
                        
                    except Exception as e:
                        logger.error(f"Error calculating correlation: {str(e)}")
                        # Fall back to basic correlation
                
                # If advanced analytics failed or not available, use basic correlation
                if f"{metric1}_{metric2}" not in correlations:
                    # Calculate basic correlation
                    n = len(values1)
                    sum_x = sum(values1)
                    sum_y = sum(values2)
                    sum_xy = sum(x * y for x, y in zip(values1, values2))
                    sum_xx = sum(x * x for x in values1)
                    sum_yy = sum(y * y for y in values2)
                    
                    denominator = (n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)
                    if denominator <= 0:
                        correlation = 0
                    else:
                        correlation = (n * sum_xy - sum_x * sum_y) / math.sqrt(denominator)
                    
                    # Determine significance based on correlation strength
                    if abs(correlation) > 0.7:
                        significance = "strong"
                    elif abs(correlation) > 0.4:
                        significance = "moderate"
                    else:
                        significance = "weak"
                    
                    correlations[f"{metric1}_{metric2}"] = {
                        "correlation": round(correlation, 3),
                        "significance": significance
                    }
        
        # Add correlations to result
        result["correlations"] = correlations
        
        # Generate relationship insights
        relationships = []
        
        for pair, corr_info in correlations.items():
            metrics = pair.split("_")
            metric1 = metrics[0]
            metric2 = metrics[1]
            
            correlation = corr_info["correlation"]
            significance = corr_info["significance"]
            
            if significance == "insufficient_data":
                continue
            
            if abs(correlation) < 0.3:
                continue  # Skip weak correlations
            
            # Format metric names for display
            metric1_display = metric1.replace("_", " ").title()
            metric2_display = metric2.replace("_", " ").title()
            
            # Determine relationship type
            if correlation > 0:
                relationship_type = "positive"
                relationship_desc = f"As {metric1_display} increases, {metric2_display} tends to increase"
            else:
                relationship_type = "negative"
                relationship_desc = f"As {metric1_display} increases, {metric2_display} tends to decrease"
            
            # Create relationship object
            relationship = {
                "metrics": [metric1, metric2],
                "correlation": correlation,
                "significance": significance,
                "type": relationship_type,
                "description": relationship_desc
            }
            
            relationships.append(relationship)
        
        # Add relationships to result
        result["relationships"] = relationships
        
        # Generate insights based on relationships
        insights = []
        
        for relationship in relationships:
            if relationship["significance"] != "strong":
                continue
            
            metrics = relationship["metrics"]
            metric1 = metrics[0]
            metric2 = metrics[1]
            
            # Format metric names for display
            metric1_display = metric1.replace("_", " ").title()
            metric2_display = metric2.replace("_", " ").title()
            
            # Generate insight based on specific metric pairs
            if metric1 == "requirements_quality" and metric2 == "defect_density" and relationship["type"] == "negative":
                insights.append({
                    "type": "correlation",
                    "title": "Quality Reduces Defects",
                    "description": f"There is a strong negative correlation between Requirements Quality and Defect Density. Improving quality directly reduces defects.",
                    "recommendation": "Continue focusing on requirements quality improvements to further reduce defects."
                })
                
            elif metric1 == "requirements_quality" and metric2 == "review_efficiency" and relationship["type"] == "negative":
                insights.append({
                    "type": "correlation",
                    "title": "Quality Improves Review Efficiency",
                    "description": f"Higher Requirements Quality correlates with shorter review times. Better requirements require less review effort.",
                    "recommendation": "Improve initial requirements quality to reduce review bottlenecks."
                })
                
            elif metric1 == "review_efficiency" and metric2 == "defect_density" and relationship["type"] == "positive":
                insights.append({
                    "type": "correlation",
                    "title": "Rushed Reviews Miss Defects",
                    "description": f"Shorter review times correlate with higher defect density. Thorough reviews are essential for defect detection.",
                    "recommendation": "Ensure review processes are thorough even when optimizing for efficiency."
                })
                
            else:
                # Generic insight
                insights.append({
                    "type": "correlation",
                    "title": f"{metric1_display} - {metric2_display} Correlation",
                    "description": f"There is a {relationship['significance']} {relationship['type']} correlation between {metric1_display} and {metric2_display}.",
                    "recommendation": f"Consider this relationship when planning improvements."
                })
        
        # Add insights to result
        result["insights"] = insights
        
        return result
    
    def generate_predictive_insights(self, metric_names: List[str] = None) -> List[Dict[str, Any]]:
        """
        Generate predictive insights based on trend analysis
        
        Args:
            metric_names: Optional list of metrics to analyze (default: all main metrics)
            
        Returns:
            List of predictive insights
        """
        logger.info("Generating predictive insights")
        
        if not metric_names:
            metric_names = ["requirements_quality", "review_efficiency", "defect_density", "requirements_completeness"]
        
        insights = []
        
        # Analyze each metric
        for metric_name in metric_names:
            analysis = self.analyze_metric_trend(
                metric_name=metric_name,
                period="90d",  # Use 90 days for better predictions
                seasonality_check=True,
                anomaly_detection=True
            )
            
            # Skip if error in analysis
            if "error" in analysis:
                continue
            
            # Extract key information
            trend = analysis["trend"]
            forecast = analysis["forecast"]
            
            # Format metric name for display
            metric_display = metric_name.replace("_", " ").title()
            
            # Generate trend-based insight
            if trend["direction"] != "flat":
                if trend["is_good"]:
                    trend_quality = "positive"
                    if trend["strength"] == "strong":
                        priority = "low"  # Good trend that's strong is low priority
                    else:
                        priority = "medium"  # Good trend that's moderate/weak could be improved
                else:
                    trend_quality = "negative"
                    if trend["strength"] == "strong":
                        priority = "high"  # Bad trend that's strong is high priority
                    else:
                        priority = "medium"  # Bad trend that's moderate/weak is medium priority
                
                # Create insight
                direction_text = "increasing" if trend["direction"] == "up" else "decreasing"
                
                insights.append({
                    "type": "trend",
                    "metric": metric_name,
                    "title": f"{metric_display} {direction_text.title()} Trend",
                    "description": f"{metric_display} shows a {trend['strength']} {direction_text} trend ({trend['percent_change']}% over the period).",
                    "impact": trend_quality,
                    "priority": priority,
                    "confidence": round(trend["r_squared"] * 100)
                })
            
            # Generate forecast-based insight
            if "milestones" in forecast and forecast["milestones"]:
                # Get nearest milestone
                nearest_milestone = min(forecast["milestones"].items(), key=lambda x: int(x[1]))
                threshold, days = nearest_milestone
                
                # Determine priority based on milestone
                if metric_name == "requirements_quality":
                    if float(threshold) >= 90:
                        priority = "low"
                        milestone_quality = "positive"
                    elif float(threshold) >= 80:
                        priority = "medium"
                        milestone_quality = "positive"
                    else:
                        priority = "high"
                        milestone_quality = "negative"
                        
                elif metric_name == "review_efficiency":
                    if float(threshold) <= 24:
                        priority = "low"
                        milestone_quality = "positive"
                    elif float(threshold) <= 48:
                        priority = "medium"
                        milestone_quality = "positive"
                    else:
                        priority = "high"
                        milestone_quality = "negative"
                        
                elif metric_name == "defect_density":
                    if float(threshold) <= 0.05:
                        priority = "low"
                        milestone_quality = "positive"
                    elif float(threshold) <= 0.1:
                        priority = "medium"
                        milestone_quality = "positive"
                    else:
                        priority = "high"
                        milestone_quality = "negative"
                else:
                    priority = "medium"
                    milestone_quality = "neutral"
                
                # Create insight
                if metric_name == "requirements_quality":
                    insights.append({
                        "type": "forecast",
                        "metric": metric_name,
                        "title": f"{metric_display} Milestone Forecast",
                        "description": f"{metric_display} is projected to reach {threshold}% in approximately {days} days.",
                        "impact": milestone_quality,
                        "priority": priority,
                        "confidence": forecast["confidence"]
                    })
                elif metric_name == "review_efficiency":
                    insights.append({
                        "type": "forecast",
                        "metric": metric_name,
                        "title": f"{metric_display} Milestone Forecast",
                        "description": f"{metric_display} is projected to reach {threshold} hours in approximately {days} days.",
                        "impact": milestone_quality,
                        "priority": priority,
                        "confidence": forecast["confidence"]
                    })
                elif metric_name == "defect_density":
                    insights.append({
                        "type": "forecast",
                        "metric": metric_name,
                        "title": f"{metric_display} Milestone Forecast",
                        "description": f"{metric_display} is projected to reach {threshold} defects per requirement in approximately {days} days.",
                        "impact": milestone_quality,
                        "priority": priority,
                        "confidence": forecast["confidence"]
                    })
                else:
                    insights.append({
                        "type": "forecast",
                        "metric": metric_name,
                        "title": f"{metric_display} Milestone Forecast",
                        "description": f"{metric_display} is projected to reach {threshold} in approximately {days} days.",
                        "impact": milestone_quality,
                        "priority": priority,
                        "confidence": forecast["confidence"]
                    })
            
            # Generate seasonality-based insight
            if "seasonality" in analysis and analysis["seasonality"]["detected_period"]:
                period = analysis["seasonality"]["detected_period"]
                confidence = analysis["seasonality"]["confidence"]
                
                if period == 7:
                    period_text = "weekly"
                elif period > 25 and period < 32:
                    period_text = "monthly"
                else:
                    period_text = f"{period}-day"
                
                insights.append({
                    "type": "seasonality",
                    "metric": metric_name,
                    "title": f"{metric_display} {period_text.title()} Pattern",
                    "description": f"{metric_display} shows a {period_text} cyclical pattern.",
                    "impact": "neutral",
                    "priority": "medium",
                    "confidence": round(confidence * 100)
                })
            
            # Generate anomaly-based insight
            if "anomalies" in analysis and analysis["anomalies"]:
                high_severity = [a for a in analysis["anomalies"] if a["severity"] == "high"]
                
                if high_severity:
                    # Get the most recent high-severity anomaly
                    latest_anomaly = max(high_severity, key=lambda x: x["timestamp"])
                    
                    insights.append({
                        "type": "anomaly",
                        "metric": metric_name,
                        "title": f"{metric_display} Significant Anomaly",
                        "description": f"Detected a significant anomaly in {metric_display} on {latest_anomaly['timestamp'][:10]} with value {latest_anomaly['value']} (expected: {latest_anomaly['expected_value']}).",
                        "impact": "negative",
                        "priority": "high",
                        "confidence": 90
                    })
        
        # If we have multiple metrics, add cross-metric analysis
        if len(metric_names) >= 2:
            cross_analysis = self.analyze_cross_metric_trends(metric_names)
            
            # Add relationship insights
            for insight in cross_analysis.get("insights", []):
                if "title" in insight and "description" in insight:
                    insights.append({
                        "type": "relationship",
                        "title": insight["title"],
                        "description": insight["description"],
                        "impact": "neutral",
                        "priority": "medium",
                        "confidence": 80
                    })
        
        return insights


# Example usage
if __name__ == "__main__":
    # Create trend analyzer
    analyzer = TrendAnalyzer()
    
    # Analyze a single metric
    trend_analysis = analyzer.analyze_metric_trend("requirements_quality")
    print(f"Trend analysis: {json.dumps(trend_analysis['trend'], indent=2)}")
    
    # Analyze cross-metric trends
    cross_analysis = analyzer.analyze_cross_metric_trends(
        ["requirements_quality", "defect_density"]
    )
    print(f"Cross-metric analysis: {len(cross_analysis['relationships'])} relationships found")
    
    # Generate predictive insights
    insights = analyzer.generate_predictive_insights()
    print(f"Generated {len(insights)} predictive insights")
