"""this is a module docstring"""
import discord
from textblob import TextBlob
from googletrans import Translator


class TranslateMe:
    """Class supplying translation related methods"""

    def __init__(self):
        self.count_de = 0
        self.count_fr = 0
        self.count_en = 0
        self.count_other = 0
        self.src_lang = ""

    def get_language(self, text):
        """method to extract the language of a given text"""
        lang = TextBlob(text)
        self.src_lang = lang.detect_language()
        return self.src_lang

    @staticmethod
    def translate_text(text, dest_language):
        """method to translate a given text based on the supplied language code"""
        translate = Translator()
        return translate.translate(text, dest_language)

    def translated_message(self, message, lang):
        """Method to manage the translation"""
        trans_message_prime = ""
        trans_message_second = ""

        if lang == "de":
            trans_message_prime = self.translate_text(message.content, "en")
            trans_message_second = self.translate_text(message.content, "fr")
            self.count_de = self.count_de + 1
        elif lang == "en":
            trans_message_prime = self.translate_text(message.content, "de")
            trans_message_second = self.translate_text(message.content, "fr")
            self.count_en = self.count_en + 1
        elif lang == "fr":
            trans_message_prime = self.translate_text(message.content, "de")
            trans_message_second = self.translate_text(message.content, "en")
            self.count_fr = self.count_fr + 1
        else:
            self.count_other = self.count_other + 1

        if trans_message_prime != "" and trans_message_second != "":
            translate_embed = discord.Embed(
                colour=discord.Colour(0x4A90E2),
                description=f"{trans_message_prime.text} \n{trans_message_second.text}",
            )
            print(
                f"DE: {self.count_de}, EN: {self.count_en}, FR: {self.count_fr}, other: {self.count_other}"
            )
            result = {
                "embed": translate_embed,
            }
        else:
            print(
                f"DE: {self.count_de}, EN: {self.count_en}, FR: {self.count_fr}, other: {self.count_other}"
            )
            result = {
                "embed": None,
            }

        return result

    def get_language_counts(self):
        """Method to acquire language counts and other language usage related params"""
        return {
            "detect_lang": self.src_lang,
            "count_de": self.count_de,
            "count_en": self.count_en,
            "count_fr": self.count_fr,
            "count_other": self.count_other,
        }
