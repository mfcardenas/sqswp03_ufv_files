"""
Natural Language Processing (NLP) Module for Requirements Engineering
Based on ISO/IEC/IEEE 29148:2011 Standards

This module implements NLP capabilities for requirements engineering,
including text analysis, sentiment detection, and requirements classification.
"""

import json
import os
import re
import numpy as np
import pandas as pd
from datetime import datetime
from collections import Counter, defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load
import spacy

# Download NLTK resources (if not already downloaded)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

class NLPProcessor:
    """Natural Language Processing engine for requirements engineering."""
    
    def __init__(self, config_path=None):
        """
        Initialize the NLP processor.
        
        Args:
            config_path (str): Path to the configuration file
        """
        self.config = {}
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        
        # Initialize NLP components
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
        # Add domain-specific stopwords
        domain_stopwords = {'shall', 'should', 'must', 'will', 'the', 'system', 'user'}
        self.stop_words.update(domain_stopwords)
        
        # Initialize models
        self.classifier_model = None
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.label_encoder = LabelEncoder()
        
        # Load spaCy model
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            # If the model is not installed, download it
            os.system('python -m spacy download en_core_web_sm')
            self.nlp = spacy.load('en_core_web_sm')
        
        # Define model storage paths
        self.models_dir = os.path.join(os.path.dirname(__file__), 'models')
        os.makedirs(self.models_dir, exist_ok=True)
        
        # Quality attributes patterns from ISO/IEC/IEEE 29148:2011
        self.quality_patterns = {
            'ambiguity': [
                r'\b(?:may|might|could|possibly|probably|likely|unlikely)\b',
                r'\b(?:and/or|etc\.)\b',
                r'\b(?:various|appropriate|some|many|few)\b'
            ],
            'incomplete': [
                r'\b(?:tbd|tbs|tbr|tba|not defined|not specified|unknown)\b',
                r'\b(?:for example|such as|e\.g\.)\b'
            ],
            'inconsistent': [
                r'\b(?:but|however|although|though|whereas|otherwise)\b'
            ],
            'unverifiable': [
                r'\b(?:user-friendly|easy to use|efficient|fast|reliable|flexible)\b'
            ]
        }
    
    def load_models(self):
        """Load trained NLP models from disk."""
        try:
            self.classifier_model = load(os.path.join(self.models_dir, 'classifier_model.joblib'))
            self.vectorizer = load(os.path.join(self.models_dir, 'vectorizer.joblib'))
            self.label_encoder = load(os.path.join(self.models_dir, 'label_encoder.joblib'))
            
            print("NLP models loaded successfully")
            return True
        except Exception as e:
            print(f"Error loading NLP models: {e}")
            return False
    
    def save_models(self):
        """Save trained NLP models to disk."""
        try:
            if self.classifier_model:
                dump(self.classifier_model, os.path.join(self.models_dir, 'classifier_model.joblib'))
            if hasattr(self.vectorizer, 'vocabulary_'):
                dump(self.vectorizer, os.path.join(self.models_dir, 'vectorizer.joblib'))
            if hasattr(self.label_encoder, 'classes_'):
                dump(self.label_encoder, os.path.join(self.models_dir, 'label_encoder.joblib'))
                
            print("NLP models saved successfully")
            return True
        except Exception as e:
            print(f"Error saving NLP models: {e}")
            return False
    
    def preprocess_text(self, text):
        """
        Preprocess text for NLP analysis.
        
        Args:
            text (str): Raw text to preprocess
            
        Returns:
            list: List of preprocessed tokens
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words and len(token) > 2]
        
        return tokens
    
    def analyze_text(self, text):
        """
        Perform comprehensive text analysis on requirements text.
        
        Args:
            text (str): Requirements text to analyze
            
        Returns:
            dict: Analysis results
        """
        # Basic text statistics
        word_count = len(text.split())
        sentence_count = len(sent_tokenize(text))
        avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count > 0 else 0
        
        # Readability (Flesch-Kincaid Grade Level)
        readability_score = self._calculate_readability(text)
        
        # Preprocessing
        preprocessed_tokens = self.preprocess_text(text)
        
        # Keyword extraction
        keywords = self._extract_keywords(preprocessed_tokens)
        
        # Entity recognition using spaCy
        entities = self._extract_entities(text)
        
        # Quality analysis based on ISO/IEC/IEEE 29148:2011
        quality_issues = self._detect_quality_issues(text)
        
        # Complexity metrics
        complexity = self._calculate_complexity(text)
        
        return {
            'statistics': {
                'word_count': word_count,
                'sentence_count': sentence_count,
                'avg_word_length': avg_word_length,
                'readability_score': readability_score
            },
            'keywords': keywords,
            'entities': entities,
            'quality_issues': quality_issues,
            'complexity': complexity,
            'timestamp': datetime.now().isoformat()
        }
    
    def _calculate_readability(self, text):
        """
        Calculate readability metrics.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            float: Readability score
        """
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        
        if not sentences or not words:
            return 0.0
        
        # Count syllables (approximation)
        syllable_count = 0
        for word in words:
            word = word.lower()
            if len(word) <= 3:
                syllable_count += 1
                continue
            
            # Count vowel groups as syllables
            vowels = "aeiouy"
            temp_word = word.lower()
            if temp_word[0] in vowels:
                syllable_count += 1
            for index in range(1, len(temp_word)):
                if temp_word[index] in vowels and temp_word[index - 1] not in vowels:
                    syllable_count += 1
            if temp_word.endswith('e'):
                syllable_count -= 1
            if temp_word.endswith('le') and len(temp_word) > 2 and temp_word[-3] not in vowels:
                syllable_count += 1
            if syllable_count == 0:
                syllable_count += 1
        
        # Calculate Flesch-Kincaid Grade Level
        if len(sentences) == 0 or len(words) == 0:
            return 0
        
        avg_sentence_length = len(words) / len(sentences)
        avg_syllables_per_word = syllable_count / len(words)
        
        fk_grade = 0.39 * avg_sentence_length + 11.8 * avg_syllables_per_word - 15.59
        
        return max(0, min(fk_grade, 18))  # Clamp between 0 and 18
    
    def _extract_keywords(self, tokens, top_n=10):
        """
        Extract keywords from preprocessed tokens.
        
        Args:
            tokens (list): Preprocessed tokens
            top_n (int): Number of top keywords to return
            
        Returns:
            list: List of keyword dictionaries
        """
        # Count word frequencies
        word_freq = Counter(tokens)
        
        # Get top N keywords
        keywords = word_freq.most_common(top_n)
        
        # Format as list of dictionaries
        return [{'word': word, 'frequency': freq} for word, freq in keywords]
    
    def _extract_entities(self, text):
        """
        Extract named entities using spaCy.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            list: List of entity dictionaries
        """
        doc = self.nlp(text)
        
        entities = []
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'type': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            })
        
        return entities
    
    def _detect_quality_issues(self, text):
        """
        Detect quality issues based on ISO/IEC/IEEE 29148:2011 patterns.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Dictionary of quality issues
        """
        text_lower = text.lower()
        issues = {}
        
        for quality_type, patterns in self.quality_patterns.items():
            matches = []
            for pattern in patterns:
                for match in re.finditer(pattern, text_lower, re.IGNORECASE):
                    # Get some context around the match
                    start = max(0, match.start() - 20)
                    end = min(len(text), match.end() + 20)
                    context = text[start:end]
                    
                    matches.append({
                        'text': match.group(),
                        'start': match.start(),
                        'end': match.end(),
                        'context': context
                    })
            
            if matches:
                issues[quality_type] = matches
        
        return issues
    
    def _calculate_complexity(self, text):
        """
        Calculate complexity metrics for requirements text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Complexity metrics
        """
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        
        if not sentences or not words:
            return {
                'lexical_diversity': 0,
                'sentence_complexity': 0,
                'cognitive_complexity': 0
            }
        
        # Lexical diversity (unique words / total words)
        unique_words = set(word.lower() for word in words)
        lexical_diversity = len(unique_words) / len(words) if words else 0
        
        # Sentence complexity (average words per sentence)
        avg_words_per_sentence = len(words) / len(sentences) if sentences else 0
        
        # Cognitive complexity (heuristic based on sentence length, word length, etc.)
        long_words = sum(1 for word in words if len(word) > 6)
        long_word_ratio = long_words / len(words) if words else 0
        
        cognitive_complexity = (avg_words_per_sentence * 0.5) + (long_word_ratio * 0.5)
        
        return {
            'lexical_diversity': lexical_diversity,
            'sentence_complexity': avg_words_per_sentence,
            'cognitive_complexity': cognitive_complexity
        }
    
    def detect_sentiment(self, text):
        """
        Detect sentiment in requirements text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Sentiment analysis results
        """
        # Use spaCy's textcat for sentiment analysis
        doc = self.nlp(text)
        
        # Define default sentiment lexicon for requirements
        positive_words = {
            'clear', 'complete', 'consistent', 'effective', 'efficient',
            'reliable', 'robust', 'simple', 'usable', 'verifiable'
        }
        
        negative_words = {
            'ambiguous', 'complex', 'difficult', 'incomplete', 'inconsistent',
            'slow', 'unstable', 'unreliable', 'unverifiable', 'vague'
        }
        
        # Count positive and negative words
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        positive_count = sum(1 for token in tokens if token in positive_words)
        negative_count = sum(1 for token in tokens if token in negative_words)
        
        # Calculate sentiment score (-1 to 1)
        total = positive_count + negative_count
        if total == 0:
            sentiment_score = 0.0
        else:
            sentiment_score = (positive_count - negative_count) / total
        
        # Determine sentiment label
        if sentiment_score > 0.2:
            sentiment = 'positive'
        elif sentiment_score < -0.2:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'sentiment_score': sentiment_score,
            'positive_count': positive_count,
            'negative_count': negative_count,
            'timestamp': datetime.now().isoformat()
        }
    
    def extract_topics(self, requirements_texts, num_topics=5, num_words=10):
        """
        Extract topics from a collection of requirements texts.
        
        Args:
            requirements_texts (list): List of requirements texts
            num_topics (int): Number of topics to extract
            num_words (int): Number of words per topic
            
        Returns:
            dict: Topic modeling results
        """
        if not requirements_texts:
            return {'topics': [], 'document_topics': []}
        
        # Create document-term matrix
        vectorizer = CountVectorizer(
            max_features=1000,
            stop_words=self.stop_words,
            max_df=0.85,
            min_df=2
        )
        
        try:
            dtm = vectorizer.fit_transform(requirements_texts)
            
            # Apply LDA for topic modeling
            lda_model = LatentDirichletAllocation(
                n_components=num_topics,
                random_state=42,
                max_iter=50
            )
            
            lda_model.fit(dtm)
            
            # Get feature names (words)
            feature_names = vectorizer.get_feature_names_out()
            
            # Extract topics
            topics = []
            for topic_idx, topic in enumerate(lda_model.components_):
                top_words_idx = topic.argsort()[:-num_words-1:-1]
                top_words = [feature_names[i] for i in top_words_idx]
                topics.append({
                    'id': topic_idx,
                    'words': top_words,
                    'weights': topic[top_words_idx].tolist()
                })
            
            # Determine document-topic distribution
            document_topics = []
            topic_distribution = lda_model.transform(dtm)
            
            for idx, dist in enumerate(topic_distribution):
                dominant_topic = dist.argmax()
                document_topics.append({
                    'document_id': idx,
                    'dominant_topic': int(dominant_topic),
                    'distribution': dist.tolist()
                })
            
            return {
                'topics': topics,
                'document_topics': document_topics,
                'timestamp': datetime.now().isoformat()
            }
        
        except ValueError as e:
            print(f"Error in topic extraction: {e}")
            return {'topics': [], 'document_topics': [], 'error': str(e)}
    
    def train_classifier(self, training_data):
        """
        Train a requirements classifier.
        
        Args:
            training_data (dict): Dictionary with 'texts' and 'categories'
            
        Returns:
            float: Model accuracy score
        """
        X = training_data['texts']
        y = training_data['categories']
        
        # Encode labels
        y_encoded = self.label_encoder.fit_transform(y)
        
        # Create document vectors
        X_vectorized = self.vectorizer.fit_transform(X)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y_encoded, test_size=0.2, random_state=42)
        
        # Train model
        self.classifier_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.classifier_model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.classifier_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Requirements classifier trained - Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred, target_names=self.label_encoder.classes_))
        
        return accuracy
    
    def classify_requirements(self, requirements_texts):
        """
        Classify requirements into categories.
        
        Args:
            requirements_texts (list): List of requirements texts
            
        Returns:
            list: List of classification dictionaries
        """
        if not self.classifier_model:
            raise ValueError("Classifier model not trained or loaded")
        
        # Create document vectors
        X_vectorized = self.vectorizer.transform(requirements_texts)
        
        # Predict categories
        predictions = self.classifier_model.predict(X_vectorized)
        probabilities = self.classifier_model.predict_proba(X_vectorized)
        
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
    
    def cluster_requirements(self, requirements_texts, n_clusters=5):
        """
        Cluster requirements into groups based on similarity.
        
        Args:
            requirements_texts (list): List of requirements texts
            n_clusters (int): Number of clusters
            
        Returns:
            dict: Clustering results
        """
        if not requirements_texts:
            return {'clusters': [], 'cluster_assignments': []}
        
        # Create document vectors
        X_vectorized = self.vectorizer.fit_transform(requirements_texts)
        
        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=min(n_clusters, len(requirements_texts)), random_state=42)
        cluster_labels = kmeans.fit_predict(X_vectorized)
        
        # Get cluster centers and convert to dense arrays
        centers = kmeans.cluster_centers_.tolist()
        
        # Extract top terms per cluster
        feature_names = self.vectorizer.get_feature_names_out()
        
        clusters = []
        for i, center in enumerate(centers):
            # Convert center to dense array and get top indices
            center_dense = np.array(center)
            sorted_indices = center_dense.argsort()[::-1][:10]  # Top 10 words
            top_terms = [feature_names[idx] for idx in sorted_indices]
            
            # Count documents in this cluster
            cluster_size = np.sum(cluster_labels == i)
            
            clusters.append({
                'id': i,
                'size': int(cluster_size),
                'top_terms': top_terms
            })
        
        # Create cluster assignments
        cluster_assignments = []
        for i, label in enumerate(cluster_labels):
            text_snippet = requirements_texts[i][:100] + '...' if len(requirements_texts[i]) > 100 else requirements_texts[i]
            cluster_assignments.append({
                'text_id': i,
                'text_snippet': text_snippet,
                'cluster': int(label)
            })
        
        return {
            'clusters': clusters,
            'cluster_assignments': cluster_assignments,
            'timestamp': datetime.now().isoformat()
        }


# Main execution
if __name__ == "__main__":
    processor = NLPProcessor('analytics_config.json')
    
    # Sample requirements for demonstration
    sample_requirements = [
        "The system shall provide users with the ability to log in using their username and password.",
        "The system must process customer orders within 5 seconds under normal load conditions.",
        "The application should be user-friendly and easy to navigate.",
        "The database will store customer information securely and prevent unauthorized access.",
        "The product may include various reporting capabilities as deemed appropriate by the project team.",
        "The system performance should be fast and efficient for all operations."
    ]
    
    # Analyze a sample requirement
    print("\nText Analysis:")
    analysis = processor.analyze_text(sample_requirements[0])
    print(f"  Statistics: {analysis['statistics']}")
    print(f"  Keywords: {', '.join(kw['word'] for kw in analysis['keywords'])}")
    print(f"  Entities: {analysis['entities']}")
    print(f"  Quality Issues: {list(analysis['quality_issues'].keys())}")
    print(f"  Complexity: {analysis['complexity']}")
    
    # Sentiment analysis
    print("\nSentiment Analysis:")
    for req in sample_requirements[:3]:
        sentiment = processor.detect_sentiment(req)
        print(f"  '{req[:50]}...': {sentiment['sentiment']} ({sentiment['sentiment_score']:.2f})")
    
    # Topic extraction
    print("\nTopic Extraction:")
    topics_result = processor.extract_topics(sample_requirements)
    for topic in topics_result['topics']:
        print(f"  Topic {topic['id']}: {', '.join(topic['words'])}")
    
    # Train classifier with sample data
    print("\nTraining Classifier:")
    # Define more sample data for training
    np.random.seed(42)
    n_samples = 100
    
    training_texts = []
    training_categories = []
    
    # Functional requirements
    for i in range(n_samples // 4):
        training_texts.append(f"The system shall allow users to {np.random.choice(['view', 'create', 'update', 'delete'])} {np.random.choice(['user accounts', 'products', 'orders', 'payments'])}.")
        training_categories.append('Functional')
    
    # Non-functional requirements
    for i in range(n_samples // 4):
        training_texts.append(f"The system must be {np.random.choice(['secure', 'fast', 'reliable', 'scalable'])} and {np.random.choice(['efficient', 'robust', 'maintainable', 'user-friendly'])}.")
        training_categories.append('Non-Functional')
    
    # Interface requirements
    for i in range(n_samples // 4):
        training_texts.append(f"The system shall interface with {np.random.choice(['the database', 'the payment gateway', 'the CRM system', 'the ERP system'])} using {np.random.choice(['REST API', 'SOAP', 'GraphQL', 'Web Services'])}.")
        training_categories.append('Interface')
    
    # Data requirements
    for i in range(n_samples // 4):
        training_texts.append(f"The system shall store {np.random.choice(['user', 'product', 'order', 'payment'])} data including {np.random.choice(['ID', 'name', 'date', 'status'])} and {np.random.choice(['address', 'price', 'quantity', 'amount'])}.")
        training_categories.append('Data')
    
    training_data = {
        'texts': training_texts,
        'categories': training_categories
    }
    
    accuracy = processor.train_classifier(training_data)
    processor.save_models()
    
    # Classification
    print("\nRequirements Classification:")
    classifications = processor.classify_requirements(sample_requirements)
    for cls in classifications:
        print(f"  '{cls['text']}': {cls['category']} (Confidence: {cls['confidence']:.2f})")
    
    # Clustering
    print("\nRequirements Clustering:")
    clustering = processor.cluster_requirements(sample_requirements)
    for cluster in clustering['clusters']:
        print(f"  Cluster {cluster['id']} (Size: {cluster['size']}):")
        print(f"    Top terms: {', '.join(cluster['top_terms'])}")
        
    print("\nCluster Assignments:")
    for assignment in clustering['cluster_assignments']:
        print(f"  '{assignment['text_snippet']}': Cluster {assignment['cluster']}")
