from textblob import TextBlob

class EmotionAI:
    def add_emotion(self, text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return f"{text} 🙂"
        elif analysis.sentiment.polarity < 0:
            return f"{text} 🙁"
        else:
            return f"{text} 😐"
