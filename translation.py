from textblob import TextBlob
from googletrans import Translator


class TranslateMe:
    def __init__(self):
        pass

    @staticmethod
    def get_language(text):
        lang = TextBlob(text)
        result = lang.detect_language()
        return result

    @staticmethod
    def translate_text(text, dest_language):
        translate = Translator()
        result = translate.translate(text, dest_language)
        return result
