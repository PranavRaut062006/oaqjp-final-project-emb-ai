import sys
import os

# Ensure the root project directory is in sys.path so emotion_detection can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emotion_detection import emotion_detector
