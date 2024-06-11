from flask import Flask, request, jsonify
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# Configuración de la autenticación de Watson NLP
authenticator = IAMAuthenticator('YOUR_API_KEY')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('YOUR_SERVICE_URL')

@app.route('/')
def index():
    return 'Welcome to the Emotion Detection App'

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    return jsonify(response['emotion']['document']['emotion'])

if __name__ == '__main__':
    app.run(debug=True)
    
