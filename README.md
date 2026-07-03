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

🚀 Installation
Step 1: Clone Repository
bash
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot
Step 2: Create Virtual Environment
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Download NLP Data
bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
Step 5: Run Application
bash
python app.py
Step 6: Open Browser
Navigate to: http://127.0.0.1:5000

📖 Usage Guide
Chat Interface
Type your question in the input box

Press Enter or click Send button

View response with confidence score

Click suggestion chips for quick questions

Toggle dark/light mode with moon/sun icon

Sample Questions
Category	Example Questions
Returns	"What is your return policy?"
Shipping	"How long does shipping take?"
Payments	"What payment methods do you accept?"
Orders	"How can I track my order?"
Support	"How do I contact customer service?"
API Endpoints
Endpoint	Method	Description
/	GET	Chat interface
/api/chat	POST	Send message, get response
/api/faqs	GET	Get all FAQs
/api/faqs	POST	Add new FAQ
⚙️ How It Works
Matching Pipeline
text
User Question → Preprocess → TF-IDF Vectorize → Cosine Similarity → Best Match
Preprocessing

Lowercase conversion

Remove special characters

Tokenization

Stopword removal

Stemming/Lemmatization

Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency)

N-gram support (1-3 words)

Feature extraction

Matching

Cosine similarity calculation

Multiple question variations

Threshold filtering

Partial matching fallback

Response

Best match FAQ answer

Confidence score

Status indicator
