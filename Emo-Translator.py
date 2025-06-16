import text2emotion as te
from transformers import MarianMTModel, MarianTokenizer

def detect_emotion(text):
    emotions = te.get_emotion(text)
    # Pick the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    return dominant_emotion

def get_translation_model(src_lang="en", tgt_lang="hi"):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text, tokenizer, model):
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translation = model.generate(**tokens)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translated_text

def add_emotion_flair(emotion, text):
    flair_map = {
        'Happy': "😊",
        'Angry': "😠",
        'Surprise': "😲",
        'Sad': "😢",
        'Fear': "😨"
    }
    emoji = flair_map.get(emotion, "")
    return f"{emoji} {text}"

def main():
    print("🔤 EmoTranslator - Emotion Aware Translator (English ➡ Hindi)")
    user_input = input("Enter an English sentence: ")

    # Step 1: Detect Emotion
    emotion = detect_emotion(user_input)
    print(f"Detected Emotion: {emotion}")

    # Step 2: Add Flair (Optional)
    emotionally_tagged_text = add_emotion_flair(emotion, user_input)

    # Step 3: Load translation model
    tokenizer, model = get_translation_model("en", "hi")

    # Step 4: Translate
    translation = translate_text(emotionally_tagged_text, tokenizer, model)
    print(f"Translated Output (Hindi): {translation}")

if __name__ == "__main__":
    main()
