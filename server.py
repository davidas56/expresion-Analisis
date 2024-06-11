"""
Server module for running the Flask application.
"""

from emotion_detector.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
