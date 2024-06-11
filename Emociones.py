from flask import Flask, request, jsonify
from .nlp import analyze_emotion  # Importar la función de análisis desde nlp.py

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Emotion Detection App'

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    emotions = analyze_emotion(text)
    
    formatted_response = {
        'status': 'success',
        'emotions': emotions
    }

    return jsonify(formatted_response)

if __name__ == '__main__':
    app.run(debug=True)
