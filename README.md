💬 FAQ Chatbot System
An intelligent FAQ chatbot that uses Natural Language Processing to answer user questions by matching them with the most relevant FAQs.

📋 Overview
This FAQ Chatbot is a smart conversational agent that understands user queries and provides accurate answers from a pre-defined FAQ database. Using NLP techniques, it matches user questions with the most similar FAQ entries and returns the best matching answer with confidence scores.

✨ Features
Core Features
Natural Language Understanding - Uses NLP to understand user queries

Intelligent Matching - TF-IDF vectorization and cosine similarity

Confidence Scoring - Shows confidence level for each answer

Dynamic FAQs - Add new FAQs on the fly

Typo Tolerance - Handles spelling mistakes and variations

UI Features
Modern chat interface with dark/light mode

Real-time typing indicators

Suggestion chips for quick questions

Confidence score display

Dark/Light theme toggle

Responsive for mobile/tablet

Keyboard shortcuts support

Technical Features
Multiple preprocessing strategies

N-gram support for phrase matching

Partial matching fallback

Stemming and lemmatization

Extensible FAQ database

🛠 Technologies
Category	Technologies
Backend	Python 3.8+, Flask, NLTK, scikit-learn
NLP	TF-IDF, Cosine Similarity, Stemming, Tokenization
Frontend	HTML5, CSS3, JavaScript, Font Awesome
Data	JSON for FAQ storage
## Project Structure
<img width="299" height="394" alt="image" src="https://github.com/user-attachments/assets/5ba21342-6df6-4dbf-b79a-664d8129c6d3" />

⚙️ How It Works
User Question → Preprocess → TF-IDF Vectorize → Cosine Similarity → Best Match
