from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from utils.matcher import FAQMatcher
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FAQ matcher
matcher = FAQMatcher()

try:
    matcher.load_faqs()
    logger.info("FAQs loaded successfully!")
except Exception as e:
    logger.error(f"Error loading FAQs: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'error': 'Please enter a message',
                'status': 'error'
            }), 400
        
        # Get best match
        best_faq, confidence = matcher.get_best_match(user_message)
        
        if best_faq:
            response = {
                'answer': best_faq['answer'],
                'confidence': float(confidence),
                'status': 'success'
            }
        else:
            response = {
                'answer': "I'm not sure about that. Please contact our support team for more information.",
                'confidence': float(confidence),
                'status': 'not_found'
            }
        
        logger.info(f"User: {user_message} | Confidence: {confidence:.2f}")
        return jsonify(response)
    
    except Exception as e:
        logger.error(f"Error processing chat: {e}")
        return jsonify({
            'error': 'An error occurred while processing your request',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)