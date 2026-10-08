# Emotion Detector

## Description
This project is a Flask-based web application for detecting emotions in text using the IBM Watson NLP Emotion Detection service. It processes user input and returns the confidence scores for various emotions (anger, disgust, fear, joy, sadness) and identifies the dominant emotion. It was built for the IBM Skills Network final project.

## Features
- Provides an easy-to-use web interface for entering text.
- Analyzes text via IBM Watson NLP.
- Handles empty or invalid inputs gracefully.
- Displays scores for anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.

## Installation Instructions
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
Start the Flask application by running:
```bash
python server.py
```
Then navigate to `http://127.0.0.1:5000` in your web browser.

## Running Tests
To execute unit tests:
```bash
python -m unittest -v
```

## Configuring the IBM NLP Service
The service uses the `EmotionPredict` endpoint. By default, it expects the `sn-watson-emotion.labs.skills.network` endpoint. If you have your own credentials or a different URL, please update `url` and `headers` inside `emotion_detection.py`.

## Limitations and Troubleshooting
- The IBM Skills Network service endpoint might be restricted to lab environments or might require VPN/tokens. If the API cannot be reached, the system will return `None` for all values or time out.
- Ensure your internet connection is stable.
- If Pylint warns about missing docstrings, refer to `server.py` which has been formatted to achieve a 10/10 score.
