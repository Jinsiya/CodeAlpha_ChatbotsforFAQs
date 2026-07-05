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


## 🚀 Installation

### Step 1: Clone Repository

bash```
git clone https://github.com/Jinsiya/CodeAlpha_ChatbotsforFAQs.git
cd CodeAlpha_ChatbotsforFAQs
Step 2: Create Virtual Environment
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Download NLTK Data
bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
Step 5: Run Application
bash
python app.py

 ## Troubleshooting
NLTK Data Missing
bash
python -c "import nltk; nltk.download('all')"
Import Errors
bash
pip install -r requirements.txt --force-reinstall
