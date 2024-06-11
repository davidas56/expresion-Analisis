from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Configuración de la autenticación de Watson NLP
authenticator = IAMAuthenticator('YOUR_API_KEY')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('YOUR_SERVICE_URL')

def analyze_emotion(text):
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    
    return response['emotion']['document']['emotion']
