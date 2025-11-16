"""
Predictive Analytics Module for Requirements Engineering
Based on ISO/IEC/IEEE 29148:2011 Standards

This module implements predictive analytics capabilities for requirements
engineering, including success prediction, risk assessment, and effort estimation.
"""

import json
import os
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.preprocessing import StandardScaler
from joblib import dump, load

class PredictiveAnalyzer:
    """Predictive analytics engine for requirements engineering."""
    
    def __init__(self, config_path=None):
        """
        Initialize the predictive analytics engine.
        
        Args:
            config_path (str): Path to the configuration file
        """
        self.config = {}
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        
        # Initialize models
        self.success_model = None
        self.risk_model = None
        self.effort_model = None
        self.feature_importance = {}
        
        # Define model storage paths
        self.models_dir = os.path.join(os.path.dirname(__file__), 'models')
        os.makedirs(self.models_dir, exist_ok=True)
        
        # Initialize scaler for feature normalization
        self.scaler = StandardScaler()
    
    def load_models(self):
        """Load trained predictive models from disk."""
        try:
            self.success_model = load(os.path.join(self.models_dir, 'success_model.joblib'))
            self.risk_model = load(os.path.join(self.models_dir, 'risk_model.joblib'))
            self.effort_model = load(os.path.join(self.models_dir, 'effort_model.joblib'))
            self.scaler = load(os.path.join(self.models_dir, 'scaler.joblib'))
            
            print("Models loaded successfully")
            return True
        except Exception as e:
            print(f"Error loading models: {e}")
            return False
    
    def save_models(self):
        """Save trained predictive models to disk."""
        try:
            if self.success_model:
                dump(self.success_model, os.path.join(self.models_dir, 'success_model.joblib'))
            if self.risk_model:
                dump(self.risk_model, os.path.join(self.models_dir, 'risk_model.joblib'))
            if self.effort_model:
                dump(self.effort_model, os.path.join(self.models_dir, 'effort_model.joblib'))
            if hasattr(self.scaler, 'mean_'):
                dump(self.scaler, os.path.join(self.models_dir, 'scaler.joblib'))
                
            print("Models saved successfully")
            return True
        except Exception as e:
            print(f"Error saving models: {e}")
            return False
    
    def prepare_features(self, requirements_data):
        """
        Prepare and normalize features for prediction.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            numpy.ndarray: Normalized feature matrix
        """
        # Extract features into a DataFrame
        df = pd.DataFrame(requirements_data)
        
        # Define core features based on ISO/IEC/IEEE 29148:2011
        core_features = [
            'completeness_score', 'clarity_score', 'consistency_score',
            'verifiability_score', 'traceability_score', 'feasibility_score',
            'word_count', 'complexity_score', 'priority_level', 'stakeholder_count'
        ]
        
        # Ensure all required features exist
        for feature in core_features:
            if feature not in df.columns:
                df[feature] = 0.0
        
        # Normalize features
        X = self.scaler.fit_transform(df[core_features])
        return X
    
    def train_success_model(self, training_data):
        """
        Train the success prediction model.
        
        Args:
            training_data (dict): Dictionary with 'features' and 'success_labels'
            
        Returns:
            float: Model accuracy score
        """
        X = self.prepare_features(training_data['features'])
        y = np.array(training_data['success_labels'])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.success_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.success_model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.success_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Store feature importance
        feature_names = [
            'completeness', 'clarity', 'consistency',
            'verifiability', 'traceability', 'feasibility',
            'word_count', 'complexity', 'priority', 'stakeholders'
        ]
        self.feature_importance['success'] = dict(zip(
            feature_names, 
            self.success_model.feature_importances_
        ))
        
        print(f"Success prediction model trained - Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred))
        
        return accuracy
    
    def train_risk_model(self, training_data):
        """
        Train the risk prediction model.
        
        Args:
            training_data (dict): Dictionary with 'features' and 'risk_levels'
            
        Returns:
            float: Model accuracy score
        """
        X = self.prepare_features(training_data['features'])
        y = np.array(training_data['risk_levels'])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.risk_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.risk_model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.risk_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Store feature importance
        feature_names = [
            'completeness', 'clarity', 'consistency',
            'verifiability', 'traceability', 'feasibility',
            'word_count', 'complexity', 'priority', 'stakeholders'
        ]
        self.feature_importance['risk'] = dict(zip(
            feature_names, 
            self.risk_model.feature_importances_
        ))
        
        print(f"Risk prediction model trained - Accuracy: {accuracy:.4f}")
        
        return accuracy
    
    def train_effort_model(self, training_data):
        """
        Train the effort estimation model.
        
        Args:
            training_data (dict): Dictionary with 'features' and 'effort_hours'
            
        Returns:
            float: Root mean squared error
        """
        X = self.prepare_features(training_data['features'])
        y = np.array(training_data['effort_hours'])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.effort_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.effort_model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.effort_model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        # Store feature importance
        feature_names = [
            'completeness', 'clarity', 'consistency',
            'verifiability', 'traceability', 'feasibility',
            'word_count', 'complexity', 'priority', 'stakeholders'
        ]
        self.feature_importance['effort'] = dict(zip(
            feature_names, 
            self.effort_model.feature_importances_
        ))
        
        print(f"Effort estimation model trained - RMSE: {rmse:.4f}")
        
        return rmse
    
    def predict_success(self, requirements_data):
        """
        Predict the success probability for requirements.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            list: List of success probability dictionaries
        """
        if not self.success_model:
            raise ValueError("Success prediction model not trained or loaded")
        
        X = self.prepare_features(requirements_data)
        probabilities = self.success_model.predict_proba(X)
        predictions = self.success_model.predict(X)
        
        results = []
        for i, req in enumerate(requirements_data):
            results.append({
                'requirement_id': req.get('id', f'REQ-{i+1:04d}'),
                'success_probability': float(probabilities[i][1]),
                'prediction': bool(predictions[i]),
                'timestamp': datetime.now().isoformat()
            })
        
        return results
    
    def predict_risk(self, requirements_data):
        """
        Predict the risk level for requirements.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            list: List of risk level dictionaries
        """
        if not self.risk_model:
            raise ValueError("Risk prediction model not trained or loaded")
        
        X = self.prepare_features(requirements_data)
        risk_levels = self.risk_model.predict(X)
        probabilities = self.risk_model.predict_proba(X)
        
        # Map numeric risk levels to labels
        risk_labels = ['Low', 'Medium', 'High']
        
        results = []
        for i, req in enumerate(requirements_data):
            # Get the highest probability risk class
            risk_class = int(risk_levels[i])
            risk_label = risk_labels[risk_class] if risk_class < len(risk_labels) else f"Level-{risk_class}"
            
            results.append({
                'requirement_id': req.get('id', f'REQ-{i+1:04d}'),
                'risk_level': risk_label,
                'risk_score': float(max(probabilities[i])),
                'risk_factors': self._get_risk_factors(req),
                'timestamp': datetime.now().isoformat()
            })
        
        return results
    
    def predict_effort(self, requirements_data):
        """
        Predict the effort required for requirements implementation.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            list: List of effort estimation dictionaries
        """
        if not self.effort_model:
            raise ValueError("Effort estimation model not trained or loaded")
        
        X = self.prepare_features(requirements_data)
        effort_predictions = self.effort_model.predict(X)
        
        results = []
        for i, req in enumerate(requirements_data):
            # Calculate confidence interval (using prediction std if available)
            effort_hours = float(effort_predictions[i])
            
            results.append({
                'requirement_id': req.get('id', f'REQ-{i+1:04d}'),
                'effort_hours': effort_hours,
                'effort_days': round(effort_hours / 8, 1),
                'confidence_level': self._calculate_confidence_level(req),
                'timestamp': datetime.now().isoformat()
            })
        
        return results
    
    def get_feature_importance(self, model_type='all'):
        """
        Get feature importance for prediction models.
        
        Args:
            model_type (str): Type of model ('success', 'risk', 'effort', or 'all')
            
        Returns:
            dict: Feature importance dictionary
        """
        if model_type == 'all':
            return self.feature_importance
        elif model_type in self.feature_importance:
            return {model_type: self.feature_importance[model_type]}
        else:
            return {}
    
    def generate_insights(self, requirements_data):
        """
        Generate predictive insights from requirements data.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            dict: Dictionary with predictive insights
        """
        # Run all predictions
        success_predictions = self.predict_success(requirements_data)
        risk_predictions = self.predict_risk(requirements_data)
        effort_predictions = self.predict_effort(requirements_data)
        
        # Combine results
        combined_insights = {}
        for i, req in enumerate(requirements_data):
            req_id = req.get('id', f'REQ-{i+1:04d}')
            combined_insights[req_id] = {
                'requirement': req,
                'success': success_predictions[i],
                'risk': risk_predictions[i],
                'effort': effort_predictions[i]
            }
        
        # Generate aggregate insights
        aggregate_insights = {
            'overall_success_rate': self._calculate_overall_success_rate(success_predictions),
            'risk_distribution': self._calculate_risk_distribution(risk_predictions),
            'total_effort': self._calculate_total_effort(effort_predictions),
            'high_risk_requirements': self._identify_high_risk_requirements(risk_predictions),
            'timestamp': datetime.now().isoformat()
        }
        
        return {
            'requirement_insights': combined_insights,
            'aggregate_insights': aggregate_insights
        }
    
    def _get_risk_factors(self, requirement):
        """
        Identify specific risk factors for a requirement.
        
        Args:
            requirement (dict): Requirement dictionary with features
            
        Returns:
            list: List of risk factor strings
        """
        risk_factors = []
        
        # Check for quality issues
        for metric in ['completeness_score', 'clarity_score', 'consistency_score',
                       'verifiability_score', 'traceability_score', 'feasibility_score']:
            if metric in requirement and requirement[metric] < 0.7:
                risk_factors.append(f"Low {metric.replace('_score', '')}")
        
        # Check complexity
        if 'complexity_score' in requirement and requirement['complexity_score'] > 0.8:
            risk_factors.append("High complexity")
        
        # Check stakeholder count
        if 'stakeholder_count' in requirement and requirement['stakeholder_count'] > 5:
            risk_factors.append("Multiple stakeholders")
        
        # Add more risk factors as needed
        
        return risk_factors
    
    def _calculate_confidence_level(self, requirement):
        """
        Calculate confidence level for effort estimation.
        
        Args:
            requirement (dict): Requirement dictionary with features
            
        Returns:
            float: Confidence level between 0.0 and 1.0
        """
        # Simple heuristic based on quality metrics
        quality_metrics = [
            requirement.get('completeness_score', 0),
            requirement.get('clarity_score', 0),
            requirement.get('consistency_score', 0),
            requirement.get('verifiability_score', 0)
        ]
        
        # Higher quality generally means higher confidence
        avg_quality = sum(quality_metrics) / len(quality_metrics) if quality_metrics else 0
        
        # Adjust based on complexity (higher complexity = lower confidence)
        complexity_factor = 1.0 - (requirement.get('complexity_score', 0) * 0.5)
        
        # Calculate final confidence
        confidence = avg_quality * complexity_factor
        
        return min(max(confidence, 0.0), 1.0)  # Clamp between 0 and 1
    
    def _calculate_overall_success_rate(self, success_predictions):
        """
        Calculate overall success rate from predictions.
        
        Args:
            success_predictions (list): List of success prediction dictionaries
            
        Returns:
            float: Overall success rate
        """
        if not success_predictions:
            return 0.0
        
        success_count = sum(1 for pred in success_predictions if pred['prediction'])
        return success_count / len(success_predictions)
    
    def _calculate_risk_distribution(self, risk_predictions):
        """
        Calculate risk level distribution.
        
        Args:
            risk_predictions (list): List of risk prediction dictionaries
            
        Returns:
            dict: Distribution of risk levels
        """
        if not risk_predictions:
            return {}
        
        distribution = {'Low': 0, 'Medium': 0, 'High': 0}
        
        for pred in risk_predictions:
            risk_level = pred['risk_level']
            if risk_level in distribution:
                distribution[risk_level] += 1
            else:
                distribution[risk_level] = 1
        
        # Convert to percentages
        total = len(risk_predictions)
        for level in distribution:
            distribution[level] = round(distribution[level] / total * 100, 1)
        
        return distribution
    
    def _calculate_total_effort(self, effort_predictions):
        """
        Calculate total effort hours from predictions.
        
        Args:
            effort_predictions (list): List of effort prediction dictionaries
            
        Returns:
            dict: Total effort information
        """
        if not effort_predictions:
            return {'hours': 0, 'days': 0, 'weeks': 0}
        
        total_hours = sum(pred['effort_hours'] for pred in effort_predictions)
        
        return {
            'hours': total_hours,
            'days': round(total_hours / 8, 1),
            'weeks': round(total_hours / 40, 1)
        }
    
    def _identify_high_risk_requirements(self, risk_predictions):
        """
        Identify high risk requirements.
        
        Args:
            risk_predictions (list): List of risk prediction dictionaries
            
        Returns:
            list: List of high risk requirement IDs
        """
        return [pred['requirement_id'] for pred in risk_predictions 
                if pred['risk_level'] == 'High']


# Main execution
if __name__ == "__main__":
    analyzer = PredictiveAnalyzer('analytics_config.json')
    
    # Sample data for demonstration
    sample_requirements = [
        {
            'id': 'REQ-0001',
            'completeness_score': 0.85,
            'clarity_score': 0.75,
            'consistency_score': 0.82,
            'verifiability_score': 0.78,
            'traceability_score': 0.65,
            'feasibility_score': 0.80,
            'word_count': 120,
            'complexity_score': 0.65,
            'priority_level': 2,
            'stakeholder_count': 3
        },
        {
            'id': 'REQ-0002',
            'completeness_score': 0.65,
            'clarity_score': 0.55,
            'consistency_score': 0.70,
            'verifiability_score': 0.60,
            'traceability_score': 0.55,
            'feasibility_score': 0.75,
            'word_count': 85,
            'complexity_score': 0.80,
            'priority_level': 1,
            'stakeholder_count': 5
        }
    ]
    
    # Check if models exist, otherwise train with sample data
    if not analyzer.load_models():
        print("Training new models with sample data...")
        
        # Generate synthetic training data
        np.random.seed(42)
        n_samples = 1000
        
        synthetic_features = []
        success_labels = []
        risk_levels = []
        effort_hours = []
        
        for i in range(n_samples):
            # Generate random feature values
            completeness = np.random.uniform(0.4, 1.0)
            clarity = np.random.uniform(0.3, 1.0)
            consistency = np.random.uniform(0.5, 1.0)
            verifiability = np.random.uniform(0.4, 1.0)
            traceability = np.random.uniform(0.3, 0.9)
            feasibility = np.random.uniform(0.5, 1.0)
            
            word_count = np.random.randint(20, 500)
            complexity = np.random.uniform(0.1, 1.0)
            priority = np.random.randint(1, 4)
            stakeholders = np.random.randint(1, 10)
            
            # Create feature dictionary
            feature = {
                'id': f'REQ-{i+1:04d}',
                'completeness_score': completeness,
                'clarity_score': clarity,
                'consistency_score': consistency,
                'verifiability_score': verifiability,
                'traceability_score': traceability,
                'feasibility_score': feasibility,
                'word_count': word_count,
                'complexity_score': complexity,
                'priority_level': priority,
                'stakeholder_count': stakeholders
            }
            
            synthetic_features.append(feature)
            
            # Generate labels (simple heuristics for demo)
            # Success: higher quality scores and lower complexity → higher success
            quality_avg = (completeness + clarity + consistency + verifiability + traceability + feasibility) / 6
            success_prob = quality_avg * (1 - complexity * 0.3)
            success = 1 if np.random.random() < success_prob else 0
            success_labels.append(success)
            
            # Risk: lower quality, higher complexity, more stakeholders → higher risk
            risk_score = (1 - quality_avg) * 0.7 + complexity * 0.2 + (stakeholders / 10) * 0.1
            if risk_score < 0.4:
                risk = 0  # Low
            elif risk_score < 0.7:
                risk = 1  # Medium
            else:
                risk = 2  # High
            risk_levels.append(risk)
            
            # Effort: based on complexity, word count, and number of stakeholders
            base_hours = 20 + word_count / 10
            complexity_factor = 1 + complexity * 2
            stakeholder_factor = 1 + stakeholders * 0.1
            effort = base_hours * complexity_factor * stakeholder_factor
            effort_hours.append(effort)
        
        # Train models
        training_data = {
            'features': synthetic_features,
            'success_labels': success_labels,
            'risk_levels': risk_levels,
            'effort_hours': effort_hours
        }
        
        analyzer.train_success_model(training_data)
        analyzer.train_risk_model(training_data)
        analyzer.train_effort_model(training_data)
        
        # Save models
        analyzer.save_models()
    
    # Run predictions on sample data
    print("\nGenerating predictions for sample requirements...")
    
    success_predictions = analyzer.predict_success(sample_requirements)
    risk_predictions = analyzer.predict_risk(sample_requirements)
    effort_predictions = analyzer.predict_effort(sample_requirements)
    
    print("\nSuccess Predictions:")
    for pred in success_predictions:
        print(f"  {pred['requirement_id']}: {pred['success_probability']:.2f} ({pred['prediction']})")
    
    print("\nRisk Predictions:")
    for pred in risk_predictions:
        print(f"  {pred['requirement_id']}: {pred['risk_level']} (Score: {pred['risk_score']:.2f})")
        print(f"    Risk factors: {', '.join(pred['risk_factors'])}")
    
    print("\nEffort Predictions:")
    for pred in effort_predictions:
        print(f"  {pred['requirement_id']}: {pred['effort_hours']:.1f} hours ({pred['effort_days']:.1f} days)")
        print(f"    Confidence: {pred['confidence_level']:.2f}")
    
    print("\nFeature Importance:")
    feature_importance = analyzer.get_feature_importance()
    for model_type, importance in feature_importance.items():
        print(f"  {model_type.capitalize()} model:")
        sorted_features = sorted(importance.items(), key=lambda x: x[1], reverse=True)
        for feature, imp in sorted_features:
            print(f"    {feature}: {imp:.4f}")
