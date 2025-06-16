EmoTranslator is a simple yet unique NLP project that detects the dominant emotion in an English sentence and translates the text into another language (e.g., Hindi) with added emotional context using appropriate emotion tags. It leverages text2emotion for emotion detection and Hugging Face's MarianMT model for translation.

Features
Detects emotions such as Happy, Sad, Angry, Fear, and Surprise

Adds an emotional flair to the original sentence

Translates the emotionally enhanced sentence into a target language (default: Hindi)

Lightweight and runs quickly

Great as a beginner-friendly NLP project and a strong GitHub portfolio addition

Tech Stack
Python

Text2Emotion

Transformers (Hugging Face)

MarianMT for machine translation

NLTK

Setup
bash
Copy
Edit
pip install -r requirements.txt
Note: You must install emoji==1.6.3 to ensure compatibility with text2emotion.

Example
Input:
I am very sad today.
Detected Emotion: Sad
Translated Output: मैं आज बहुत दुखी हूं।

Why This Project?
Combines two core NLP capabilities: Emotion Detection and Machine Translation

Perfect for enhancing your portfolio, building a proof-of-concept, or submitting as a class or competition project

Designed to be simple, expressive, and uniquely creative
