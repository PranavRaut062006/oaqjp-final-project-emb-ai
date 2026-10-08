import unittest
from unittest.mock import patch
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    @patch('emotion_detection.requests.post')
    def test_emotion_detector_joy(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.9, 'sadness': 0.0}}]
        }
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        
    @patch('emotion_detection.requests.post')
    def test_emotion_detector_anger(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.9, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0}}]
        }
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        
    @patch('emotion_detection.requests.post')
    def test_emotion_detector_disgust(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.0, 'disgust': 0.9, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0}}]
        }
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    @patch('emotion_detection.requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.9}}]
        }
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    @patch('emotion_detection.requests.post')
    def test_emotion_detector_fear(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{'emotion': {'anger': 0.0, 'disgust': 0.0, 'fear': 0.9, 'joy': 0.0, 'sadness': 0.0}}]
        }
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    @patch('emotion_detection.requests.post')
    def test_emotion_detector_400(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 400
        result = emotion_detector(" ")
        self.assertIsNone(result['dominant_emotion'])

    @patch('emotion_detection.requests.post')
    def test_emotion_detector_network_error(self, mock_post):
        import requests
        mock_post.side_effect = requests.exceptions.RequestException
        result = emotion_detector("Some text")
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()
