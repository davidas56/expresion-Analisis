import unittest
from emotion_detector.app import app

class EmotionDetectorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome to the Emotion Detection App')

    def test_detect_emotion_valid(self):
        response = self.app.post('/detect_emotion', json={'text': 'I am very happy today!'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'success')
        self.assertIn('emotions', json_data)

    def test_detect_emotion_no_text(self):
        response = self.app.post('/detect_emotion', json={'text': ''})
        self.assertEqual(response.status_code, 400)
        json_data = response.get_json()
        self.assertIn('error', json_data)
        self.assertEqual(json_data['error'], 'Text is required')

if __name__ == '__main__':
    unittest.main()
