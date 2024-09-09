"""
This module contains the Flask web application for the Emotion Detector.

It defines two routes:
- /emotionDetector: Takes input text, processes it using the emotion_detector function,
  and returns the detected emotions along with the dominant emotion.
- /: Renders the index.html page.

The application is designed to run on host 0.0.0.0, port 5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Handles requests to detect emotion from the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
