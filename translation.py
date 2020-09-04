"""this is a module docstring"""
from textblob import TextBlob
from googletrans import Translator


class TranslateMe:
    """Class supplying translation related methods"""
    def __init__(self):
        pass

    @staticmethod
    def get_language(text):
        """method to extract the language of a given text"""
        lang = TextBlob(text)
        result = lang.detect_language()
        return result

    @staticmethod
    def translate_text(text, dest_language):
        """method to translate a given text based on the supplied language code"""
        translate = Translator()
        result = translate.translate(text, dest_language)
        return result
