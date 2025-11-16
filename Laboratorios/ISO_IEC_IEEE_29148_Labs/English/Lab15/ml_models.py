"""
Machine Learning Models for Requirements Engineering
Based on ISO/IEC/IEEE 29148:2011 Standards

This module implements machine learning models for requirements engineering,
including categorization, quality prediction, and similarity analysis.
"""

import json
import os
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from joblib import dump, load
import re

class MLModels:
    """Machine learning models for requirements engineering."""
    
    def __init__(self, config_path=None):
        """
        Initialize the ML models.
        
        Args:
            config_path (str): Path to the configuration file
        """
        self.config = {}
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        
        # Initialize models
        self.categorization_model = None
        self.quality_model = None
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
        # Define model storage paths
        self.models_dir = os.path.join(os.path.dirname(__file__), 'models')
        os.makedirs(self.models_dir, exist_ok=True)
        
        # Quality metrics from ISO/IEC/IEEE 29148:2011
        self.quality_metrics = [
            'completeness', 'clarity', 'consistency', 'verifiability',
            'traceability', 'feasibility', 'correctness'
        ]
    
    def load_models(self):
        """Load trained ML models from disk."""
        try:
            self.categorization_model = load(os.path.join(self.models_dir, 'categorization_model.joblib'))
            self.quality_model = load(os.path.join(self.models_dir, 'quality_model.joblib'))
            self.vectorizer = load(os.path.join(self.models_dir, 'ml_vectorizer.joblib'))
            self.scaler = load(os.path.join(self.models_dir, 'ml_scaler.joblib'))
            self.label_encoder = load(os.path.join(self.models_dir, 'ml_label_encoder.joblib'))
            
            print("ML models loaded successfully")
            return True
        except Exception as e:
            print(f"Error loading ML models: {e}")
            return False
    
    def save_models(self):
        """Save trained ML models to disk."""
        try:
            if self.categorization_model:
                dump(self.categorization_model, os.path.join(self.models_dir, 'categorization_model.joblib'))
            if self.quality_model:
                dump(self.quality_model, os.path.join(self.models_dir, 'quality_model.joblib'))
            if hasattr(self.vectorizer, 'vocabulary_'):
                dump(self.vectorizer, os.path.join(self.models_dir, 'ml_vectorizer.joblib'))
            if hasattr(self.scaler, 'mean_'):
                dump(self.scaler, os.path.join(self.models_dir, 'ml_scaler.joblib'))
            if hasattr(self.label_encoder, 'classes_'):
                dump(self.label_encoder, os.path.join(self.models_dir, 'ml_label_encoder.joblib'))
                
            print("ML models saved successfully")
            return True
        except Exception as e:
            print(f"Error saving ML models: {e}")
            return False
    
    def preprocess_text(self, text):
        """
        Preprocess text for ML analysis.
        
        Args:
            text (str): Raw text to preprocess
            
        Returns:
            str: Preprocessed text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def extract_text_features(self, requirements_texts):
        """
        Extract text features for ML models.
        
        Args:
            requirements_texts (list): List of requirements texts
            
        Returns:
            scipy.sparse.csr_matrix: Document-term matrix
        """
        # Preprocess texts
        preprocessed_texts = [self.preprocess_text(text) for text in requirements_texts]
        
        # Create document vectors
        X_vectorized = self.vectorizer.fit_transform(preprocessed_texts)
        
        return X_vectorized
    
    def extract_quality_features(self, requirements_data):
        """
        Extract quality features for ML models.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            numpy.ndarray: Feature matrix
        """
        # Convert to DataFrame
        df = pd.DataFrame(requirements_data)
        
        # Ensure all required features exist
        feature_columns = []
        for metric in self.quality_metrics:
            column_name = f"{metric}_score"
            if column_name not in df.columns:
                df[column_name] = 0.0
            feature_columns.append(column_name)
        
        # Add additional features if available
        additional_features = ['word_count', 'sentence_count', 'complexity_score']
        for feature in additional_features:
            if feature in df.columns:
                feature_columns.append(feature)
            else:
                df[feature] = 0.0
        
        # Normalize features
        X = self.scaler.fit_transform(df[feature_columns])
        
        return X
    
    def train_categorization_model(self, training_data):
        """
        Train the requirements categorization model.
        
        Args:
            training_data (dict): Dictionary with 'texts' and 'categories'
            
        Returns:
            float: Model accuracy score
        """
        X_texts = training_data['texts']
        y = training_data['categories']
        
        # Encode labels
        y_encoded = self.label_encoder.fit_transform(y)
        
        # Extract text features
        X_vectorized = self.extract_text_features(X_texts)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y_encoded, test_size=0.2, random_state=42)
        
        # Train model
        self.categorization_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.categorization_model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.categorization_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Requirements categorization model trained - Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred, target_names=self.label_encoder.classes_))
        
        return accuracy
    
    def train_quality_model(self, training_data):
        """
        Train the requirements quality prediction model.
        
        Args:
            training_data (dict): Dictionary with 'features' and 'quality_scores'
            
        Returns:
            float: Root mean squared error
        """
        X = self.extract_quality_features(training_data['features'])
        y = np.array(training_data['quality_scores'])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.quality_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.quality_model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.quality_model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        print(f"Quality prediction model trained - RMSE: {rmse:.4f}")
        
        return rmse
    
    def categorize_requirements(self, requirements_texts):
        """
        Categorize requirements into predefined categories.
        
        Args:
            requirements_texts (list): List of requirements texts
            
        Returns:
            list: List of categorization dictionaries
        """
        if not self.categorization_model:
            raise ValueError("Categorization model not trained or loaded")
        
        # Preprocess texts
        preprocessed_texts = [self.preprocess_text(text) for text in requirements_texts]
        
        # Create document vectors (using existing vocabulary)
        X_vectorized = self.vectorizer.transform(preprocessed_texts)
        
        # Predict categories
        predictions = self.categorization_model.predict(X_vectorized)
        probabilities = self.categorization_model.predict_proba(X_vectorized)
        
        # Decode predictions
        categories = self.label_encoder.inverse_transform(predictions)
        
        results = []
        for i, (text, category) in enumerate(zip(requirements_texts, categories)):
            # Get probability for predicted class
            category_idx = self.label_encoder.transform([category])[0]
            confidence = probabilities[i][category_idx]
            
            results.append({
                'text': text[:100] + '...' if len(text) > 100 else text,
                'category': category,
                'confidence': float(confidence),
                'timestamp': datetime.now().isoformat()
            })
        
        return results
    
    def predict_quality(self, requirements_data):
        """
        Predict quality scores for requirements.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            
        Returns:
            list: List of quality prediction dictionaries
        """
        if not self.quality_model:
            raise ValueError("Quality prediction model not trained or loaded")
        
        X = self.extract_quality_features(requirements_data)
        quality_predictions = self.quality_model.predict(X)
        
        results = []
        for i, req in enumerate(requirements_data):
            # Get the requirement ID
            req_id = req.get('id', f'REQ-{i+1:04d}')
            
            # Predict overall quality
            quality_score = float(quality_predictions[i])
            
            # Quality level based on score
            if quality_score >= 0.85:
                quality_level = 'Excellent'
            elif quality_score >= 0.70:
                quality_level = 'Good'
            elif quality_score >= 0.50:
                quality_level = 'Acceptable'
            else:
                quality_level = 'Poor'
            
            # Identify areas for improvement
            improvement_areas = self._identify_improvement_areas(req)
            
            results.append({
                'requirement_id': req_id,
                'quality_score': quality_score,
                'quality_level': quality_level,
                'improvement_areas': improvement_areas,
                'timestamp': datetime.now().isoformat()
            })
        
        return results
    
    def analyze_similarity(self, requirements_texts, threshold=0.7):
        """
        Analyze similarity between requirements.
        
        Args:
            requirements_texts (list): List of requirements texts
            threshold (float): Similarity threshold (0.0 to 1.0)
            
        Returns:
            dict: Similarity analysis results
        """
        if not requirements_texts:
            return {'similarity_pairs': [], 'clusters': []}
        
        # Preprocess texts
        preprocessed_texts = [self.preprocess_text(text) for text in requirements_texts]
        
        # Create document vectors
        X_vectorized = self.vectorizer.fit_transform(preprocessed_texts)
        
        # Calculate similarity matrix
        similarity_matrix = cosine_similarity(X_vectorized)
        
        # Find similar pairs
        similar_pairs = []
        n = len(requirements_texts)
        
        for i in range(n):
            for j in range(i+1, n):
                similarity = similarity_matrix[i, j]
                if similarity >= threshold:
                    similar_pairs.append({
                        'req1_index': i,
                        'req2_index': j,
                        'req1_text': requirements_texts[i][:100] + '...' if len(requirements_texts[i]) > 100 else requirements_texts[i],
                        'req2_text': requirements_texts[j][:100] + '...' if len(requirements_texts[j]) > 100 else requirements_texts[j],
                        'similarity': float(similarity)
                    })
        
        # Cluster similar requirements
        num_clusters = min(max(2, n // 5), n)  # Adaptive number of clusters
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(X_vectorized)
        
        # Organize requirements by cluster
        clusters = {}
        for i, label in enumerate(cluster_labels):
            label_int = int(label)
            if label_int not in clusters:
                clusters[label_int] = []
            
            clusters[label_int].append({
                'index': i,
                'text': requirements_texts[i][:100] + '...' if len(requirements_texts[i]) > 100 else requirements_texts[i]
            })
        
        # Format clusters for output
        formatted_clusters = []
        for label, items in clusters.items():
            formatted_clusters.append({
                'cluster_id': label,
                'size': len(items),
                'requirements': items
            })
        
        return {
            'similarity_pairs': similar_pairs,
            'clusters': formatted_clusters,
            'timestamp': datetime.now().isoformat()
        }
    
    def generate_insights(self, requirements_data, requirements_texts):
        """
        Generate ML-based insights for requirements.
        
        Args:
            requirements_data (list): List of requirement dictionaries with features
            requirements_texts (list): List of requirements texts
            
        Returns:
            dict: ML insights
        """
        insights = {}
        
        # Run categorization
        if self.categorization_model:
            insights['categorization'] = self.categorize_requirements(requirements_texts)
            
            # Analyze category distribution
            categories = [item['category'] for item in insights['categorization']]
            category_counts = pd.Series(categories).value_counts().to_dict()
            insights['category_distribution'] = {
                'counts': category_counts,
                'percentages': {k: v / len(categories) * 100 for k, v in category_counts.items()}
            }
        
        # Run quality prediction
        if self.quality_model:
            insights['quality_predictions'] = self.predict_quality(requirements_data)
            
            # Analyze quality distribution
            quality_levels = [item['quality_level'] for item in insights['quality_predictions']]
            quality_counts = pd.Series(quality_levels).value_counts().to_dict()
            insights['quality_distribution'] = {
                'counts': quality_counts,
                'percentages': {k: v / len(quality_levels) * 100 for k, v in quality_counts.items()}
            }
            
            # Calculate average quality
            avg_quality = sum(item['quality_score'] for item in insights['quality_predictions']) / len(insights['quality_predictions'])
            insights['average_quality'] = avg_quality
        
        # Run similarity analysis
        insights['similarity_analysis'] = self.analyze_similarity(requirements_texts)
        
        # Count potential duplicates
        if 'similarity_analysis' in insights:
            high_similarity_pairs = [pair for pair in insights['similarity_analysis']['similarity_pairs'] if pair['similarity'] > 0.8]
            insights['potential_duplicates'] = len(high_similarity_pairs)
        
        # Add timestamp
        insights['timestamp'] = datetime.now().isoformat()
        
        return insights
    
    def _identify_improvement_areas(self, requirement):
        """
        Identify areas for improvement in a requirement.
        
        Args:
            requirement (dict): Requirement dictionary with features
            
        Returns:
            list: List of improvement area dictionaries
        """
        improvement_areas = []
        
        # Check each quality metric
        for metric in self.quality_metrics:
            metric_name = f"{metric}_score"
            if metric_name in requirement:
                score = requirement[metric_name]
                
                # Determine threshold based on metric
                threshold = 0.7  # Default threshold
                if metric == 'completeness':
                    threshold = 0.8
                elif metric == 'clarity':
                    threshold = 0.75
                elif metric == 'consistency':
                    threshold = 0.8
                elif metric == 'verifiability':
                    threshold = 0.75
                
                # Add to improvement areas if below threshold
                if score < threshold:
                    improvement_areas.append({
                        'metric': metric,
                        'current_score': score,
                        'target_score': threshold,
                        'gap': threshold - score,
                        'priority': 'High' if (threshold - score) > 0.2 else 'Medium'
                    })
        
        # Sort by gap (largest first)
        improvement_areas.sort(key=lambda x: x['gap'], reverse=True)
        
        return improvement_areas


# Main execution
if __name__ == "__main__":
    ml_models = MLModels('analytics_config.json')
    
    # Sample requirements for demonstration
    sample_requirements_texts = [
        "The system shall provide users with the ability to log in using their username and password.",
        "The system must process customer orders within 5 seconds under normal load conditions.",
        "The application should be user-friendly and easy to navigate.",
        "The database will store customer information securely and prevent unauthorized access.",
        "The product may include various reporting capabilities as deemed appropriate by the project team.",
        "The system shall enable users to log in with their credentials.",
        "The system should generate reports in PDF, Excel, and CSV formats.",
        "The application must comply with GDPR data protection requirements."
    ]
    
    # Sample requirements data
    sample_requirements_data = [
        {
            'id': 'REQ-001',
            'completeness_score': 0.85,
            'clarity_score': 0.90,
            'consistency_score': 0.85,
            'verifiability_score': 0.70,
            'traceability_score': 0.65,
            'feasibility_score': 0.80,
            'correctness_score': 0.85,
            'word_count': 18,
            'sentence_count': 1,
            'complexity_score': 0.30
        },
        {
            'id': 'REQ-002',
            'completeness_score': 0.90,
            'clarity_score': 0.85,
            'consistency_score': 0.90,
            'verifiability_score': 0.95,
            'traceability_score': 0.70,
            'feasibility_score': 0.75,
            'correctness_score': 0.90,
            'word_count': 15,
            'sentence_count': 1,
            'complexity_score': 0.25
        },
        {
            'id': 'REQ-003',
            'completeness_score': 0.60,
            'clarity_score': 0.55,
            'consistency_score': 0.70,
            'verifiability_score': 0.40,
            'traceability_score': 0.50,
            'feasibility_score': 0.65,
            'correctness_score': 0.75,
            'word_count': 9,
            'sentence_count': 1,
            'complexity_score': 0.15
        },
        {
            'id': 'REQ-004',
            'completeness_score': 0.80,
            'clarity_score': 0.75,
            'consistency_score': 0.85,
            'verifiability_score': 0.70,
            'traceability_score': 0.80,
            'feasibility_score': 0.75,
            'correctness_score': 0.80,
            'word_count': 14,
            'sentence_count': 1,
            'complexity_score': 0.30
        },
        {
            'id': 'REQ-005',
            'completeness_score': 0.55,
            'clarity_score': 0.50,
            'consistency_score': 0.60,
            'verifiability_score': 0.35,
            'traceability_score': 0.45,
            'feasibility_score': 0.70,
            'correctness_score': 0.65,
            'word_count': 14,
            'sentence_count': 1,
            'complexity_score': 0.35
        },
        {
            'id': 'REQ-006',
            'completeness_score': 0.80,
            'clarity_score': 0.85,
            'consistency_score': 0.80,
            'verifiability_score': 0.65,
            'traceability_score': 0.60,
            'feasibility_score': 0.85,
            'correctness_score': 0.80,
            'word_count': 11,
            'sentence_count': 1,
            'complexity_score': 0.25
        },
        {
            'id': 'REQ-007',
            'completeness_score': 0.85,
            'clarity_score': 0.90,
            'consistency_score': 0.85,
            'verifiability_score': 0.85,
            'traceability_score': 0.70,
            'feasibility_score': 0.80,
            'correctness_score': 0.85,
            'word_count': 14,
            'sentence_count': 1,
            'complexity_score': 0.30
        },
        {
            'id': 'REQ-008',
            'completeness_score': 0.75,
            'clarity_score': 0.80,
            'consistency_score': 0.75,
            'verifiability_score': 0.70,
            'traceability_score': 0.85,
            'feasibility_score': 0.65,
            'correctness_score': 0.80,
            'word_count': 11,
            'sentence_count': 1,
            'complexity_score': 0.40
        }
    ]
    
    # Check if models exist, otherwise train with sample data
    if not ml_models.load_models():
        print("Training new models with sample data...")
        
        # Generate synthetic training data for categorization
        np.random.seed(42)
        n_samples = 200
        
        training_texts = []
        training_categories = []
        
        # Functional requirements
        for i in range(n_samples // 4):
            training_texts.append(f"The system shall {np.random.choice(['allow', 'enable', 'provide', 'support'])} users to {np.random.choice(['view', 'create', 'update', 'delete'])} {np.random.choice(['user accounts', 'products', 'orders', 'payments'])}.")
            training_categories.append('Functional')
        
        # Non-functional requirements
        for i in range(n_samples // 4):
            training_texts.append(f"The system {np.random.choice(['shall', 'must', 'should', 'will'])} be {np.random.choice(['secure', 'fast', 'reliable', 'scalable'])} and {np.random.choice(['efficient', 'robust', 'maintainable', 'user-friendly'])}.")
            training_categories.append('Non-Functional')
        
        # Interface requirements
        for i in range(n_samples // 4):
            training_texts.append(f"The system {np.random.choice(['shall', 'must', 'should', 'will'])} interface with {np.random.choice(['the database', 'the payment gateway', 'the CRM system', 'the ERP system'])} using {np.random.choice(['REST API', 'SOAP', 'GraphQL', 'Web Services'])}.")
            training_categories.append('Interface')
        
        # Data requirements
        for i in range(n_samples // 4):
            training_texts.append(f"The system {np.random.choice(['shall', 'must', 'should', 'will'])} store {np.random.choice(['user', 'product', 'order', 'payment'])} data including {np.random.choice(['ID', 'name', 'date', 'status'])} and {np.random.choice(['address', 'price', 'quantity', 'amount'])}.")
            training_categories.append('Data')
        
        categorization_training_data = {
            'texts': training_texts,
            'categories': training_categories
        }
        
        # Generate synthetic training data for quality prediction
        n_samples = 100
        synthetic_features = []
        quality_scores = []
        
        for i in range(n_samples):
            # Generate random feature values
            completeness = np.random.uniform(0.4, 1.0)
            clarity = np.random.uniform(0.3, 1.0)
            consistency = np.random.uniform(0.5, 1.0)
            verifiability = np.random.uniform(0.4, 1.0)
            traceability = np.random.uniform(0.3, 0.9)
            feasibility = np.random.uniform(0.5, 1.0)
            correctness = np.random.uniform(0.5, 1.0)
            
            word_count = np.random.randint(10, 50)
            sentence_count = np.random.randint(1, 4)
            complexity = np.random.uniform(0.1, 0.6)
            
            # Create feature dictionary
            feature = {
                'id': f'REQ-{i+1:03d}',
                'completeness_score': completeness,
                'clarity_score': clarity,
                'consistency_score': consistency,
                'verifiability_score': verifiability,
                'traceability_score': traceability,
                'feasibility_score': feasibility,
                'correctness_score': correctness,
                'word_count': word_count,
                'sentence_count': sentence_count,
                'complexity_score': complexity
            }
            
            synthetic_features.append(feature)
            
            # Generate overall quality score (weighted average)
            weights = {
                'completeness': 0.20,
                'clarity': 0.20,
                'consistency': 0.15,
                'verifiability': 0.15,
                'traceability': 0.10,
                'feasibility': 0.10,
                'correctness': 0.10
            }
            
            overall_quality = (
                completeness * weights['completeness'] +
                clarity * weights['clarity'] +
                consistency * weights['consistency'] +
                verifiability * weights['verifiability'] +
                traceability * weights['traceability'] +
                feasibility * weights['feasibility'] +
                correctness * weights['correctness']
            )
            
            # Add some noise
            overall_quality = min(1.0, max(0.0, overall_quality + np.random.normal(0, 0.05)))
            
            quality_scores.append(overall_quality)
        
        quality_training_data = {
            'features': synthetic_features,
            'quality_scores': quality_scores
        }
        
        # Train models
        ml_models.train_categorization_model(categorization_training_data)
        ml_models.train_quality_model(quality_training_data)
        
        # Save models
        ml_models.save_models()
    
    # Run ML analysis on sample data
    print("\nRequirements Categorization:")
    categorizations = ml_models.categorize_requirements(sample_requirements_texts)
    for i, cat in enumerate(categorizations):
        print(f"  REQ-{i+1:03d}: {cat['category']} (Confidence: {cat['confidence']:.2f})")
    
    print("\nQuality Predictions:")
    quality_predictions = ml_models.predict_quality(sample_requirements_data)
    for pred in quality_predictions:
        print(f"  {pred['requirement_id']}: {pred['quality_score']:.2f} - {pred['quality_level']}")
        if pred['improvement_areas']:
            print(f"    Improvement areas: {', '.join(area['metric'] for area in pred['improvement_areas'])}")
    
    print("\nSimilarity Analysis:")
    similarity = ml_models.analyze_similarity(sample_requirements_texts)
    
    print("  Similar Pairs:")
    for pair in similarity['similarity_pairs']:
        print(f"    REQ-{pair['req1_index']+1:03d} & REQ-{pair['req2_index']+1:03d}: {pair['similarity']:.2f}")
    
    print("  Clusters:")
    for cluster in similarity['clusters']:
        print(f"    Cluster {cluster['cluster_id']} (Size: {cluster['size']})")
    
    print("\nGenerating Comprehensive Insights...")
    insights = ml_models.generate_insights(sample_requirements_data, sample_requirements_texts)
    
    if 'category_distribution' in insights:
        print("  Category Distribution:")
        for category, percentage in insights['category_distribution']['percentages'].items():
            print(f"    {category}: {percentage:.1f}%")
    
    if 'quality_distribution' in insights:
        print("  Quality Distribution:")
        for level, percentage in insights['quality_distribution']['percentages'].items():
            print(f"    {level}: {percentage:.1f}%")
    
    if 'average_quality' in insights:
        print(f"  Average Quality Score: {insights['average_quality']:.2f}")
    
    if 'potential_duplicates' in insights:
        print(f"  Potential Duplicates: {insights['potential_duplicates']}")
