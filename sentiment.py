from transformers import pipeline

# ==========================
# NLP TASKS
# ==========================

# 1. Sentiment Analysis
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

text = "I love learning Artificial Intelligence."

print("\n===== SENTIMENT ANALYSIS =====")
print(sentiment(text))

# 2. Text Summarization
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

long_text = """
Artificial Intelligence is one of the fastest growing technologies.
It is used in healthcare, education, finance, transportation,
and many other industries. AI helps automate tasks and improve
decision making while reducing manual effort.
"""

print("\n===== TEXT SUMMARIZATION =====")
summary = summarizer(long_text, max_length=30, min_length=10)
print(summary[0]["summary_text"])

# 3. Translation
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

print("\n===== TRANSLATION =====")
translation = translator("Hello, how are you?")
print(translation[0]["translation_text"])

# ==========================
# MULTIMODAL TASKS
# ==========================

# 4. Image Captioning
try:
    image_captioner = pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-base"
    )

    print("\n===== IMAGE CAPTIONING =====")
    caption = image_captioner("image.jpg")
    print(caption[0]["generated_text"])

except Exception as e:
    print("Image Error:", e)

# 5. Speech Recognition
try:
    speech_recognizer = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-base"
    )

    print("\n===== SPEECH TO TEXT =====")
    transcription = speech_recognizer("audio.wav")
    print(transcription["text"])

except Exception as e:
    print("Audio Error:", e)

print("\n===== ALL TASKS COMPLETED =====")