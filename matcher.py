import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from .preprocessor import TextPreprocessor

class FAQMatcher:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.faqs = []
        self.processed_questions = []
        self.original_questions = []
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),  # Use unigrams, bigrams, and trigrams
            max_features=5000,
            stop_words='english'
        )
        self.tfidf_matrix = None
        
    def load_faqs(self, filepath='data/faqs.json'):
        """Load FAQs from JSON file"""
        with open(filepath, 'r') as f:
            self.faqs = json.load(f)
        
        # Store original questions
        self.original_questions = [faq['question'] for faq in self.faqs]
        
        # Preprocess all questions with multiple variations
        self.processed_questions = []
        for faq in self.faqs:
            # Original preprocessed
            base = self.preprocessor.preprocess(faq['question'])
            # Add variations for better matching
            variations = [
                base,
                self.preprocessor.get_processed_text(faq['question']),  # Without stemming
                self.preprocessor.clean_text(faq['question'])  # Only cleaning
            ]
            # Use the base for TF-IDF, but store variations for later use
            self.processed_questions.append(base)
        
        # Create TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.processed_questions)
        
    def get_best_match(self, user_question, threshold=0.05):
        """Find the best matching FAQ for a user question with typo handling"""
        if not self.faqs:
            return None, 0
        
        # Preprocess user question
        processed_user = self.preprocessor.preprocess(user_question)
        processed_user_clean = self.preprocessor.get_processed_text(user_question)
        
        # Try multiple variations of the user question
        user_variations = [
            processed_user,
            processed_user_clean,
            self.preprocessor.clean_text(user_question)
        ]
        
        best_score = 0
        best_index = -1
        
        for user_var in user_variations:
            # Transform user question to TF-IDF
            user_vector = self.vectorizer.transform([user_var])
            
            # Calculate cosine similarities
            similarities = cosine_similarity(user_vector, self.tfidf_matrix)
            
            # Get best match for this variation
            current_score = np.max(similarities)
            current_index = np.argmax(similarities)
            
            if current_score > best_score:
                best_score = current_score
                best_index = current_index
        
        # If score is above threshold, return the match
        if best_score >= threshold and best_index >= 0:
            return self.faqs[best_index], best_score
        else:
            # Try partial matching as fallback
            partial_match = self._partial_match(user_question)
            if partial_match:
                return partial_match, 0.3
            return None, best_score
    
    def _partial_match(self, user_question):
        """Fallback: Try to find partial matches using keyword matching"""
        user_words = set(self.preprocessor.clean_text(user_question).split())
        
        if not user_words:
            return None
        
        best_match = None
        best_count = 0
        
        for faq in self.faqs:
            faq_words = set(self.preprocessor.clean_text(faq['question']).split())
            common_words = user_words.intersection(faq_words)
            
            # Check if common words are meaningful (not just stopwords)
            meaningful_common = [w for w in common_words if len(w) > 2]
            
            if len(meaningful_common) > best_count:
                best_count = len(meaningful_common)
                best_match = faq
        
        # Return if we have at least 2 meaningful common words
        if best_count >= 2:
            return best_match
        
        return None
    
    def add_faq(self, question, answer):
        """Add a new FAQ dynamically"""
        new_faq = {
            'id': len(self.faqs) + 1,
            'question': question,
            'answer': answer
        }
        self.faqs.append(new_faq)
        self.original_questions.append(question)
        
        # Update processed questions
        processed_q = self.preprocessor.preprocess(question)
        self.processed_questions.append(processed_q)
        
        # Update TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.processed_questions)