"""
Main application module for emotion detection using Flask and Watson NLP.
"""

from flask import Flask, request, jsonify
from .nlp import analyze_emotion  # Importar la función de análisis desde nlp.py

app = Flask(__name__)

@app.route('/')
def index():
    """
    Home route.
    """
    return 'Welcome to the Emotion Detection App'

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotion from text.
    """
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    emotions = analyze_emotion(text)
    
    modified_emotions = {
        'sadness': emotions.get('sadness', 0) * 0.5,
        'joy': emotions.get('joy', 0) * 1.5,
        'fear': emotions.get('fear', 0) * 2,
        'disgust': emotions.get('disgust', 0) * 0.8,
        'anger': emotions.get('anger', 0) * 1.2
    }

    formatted_response = {
        'status': 'success',
        'emotions': modified_emotions
    }

    return jsonify(formatted_response)

if __name__ == '__main__':
    app.run(debug=True)
