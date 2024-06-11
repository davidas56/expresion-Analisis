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
    
    # Modificar los valores de la respuesta JSON
    modified_emotions = {
        'sadness': emotions.get('sadness', 0) * 0.5,  # Ejemplo de modificación
        'joy': emotions.get('joy', 0) * 1.5,  # Ejemplo de modificación
        'fear': emotions.get('fear', 0) * 2,  # Ejemplo de modificación
        'disgust': emotions.get('disgust', 0) * 0.8,  # Ejemplo de modificación
        'anger': emotions.get('anger', 0) * 1.2  # Ejemplo de modificación
    }

    formatted_response = {
        'status': 'success',
        'emotions': modified_emotions
    }

    return jsonify(formatted_response)

if __name__ == '__main__':
    app.run(debug=True)
