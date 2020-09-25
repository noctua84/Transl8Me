"""this is a module docstring"""
from textblob import TextBlob
from googletrans import Translator
from datadog import initialize, statsd
import discord


class TranslateMe:
    """Class supplying translation related methods"""

    def __init__(self, config):
        self.count_de = 0
        self.count_fr = 0
        self.count_en = 0
        self.count_other = 0
        self.src_lang = ""
        self.config = config

        # metrics
        if self.config["datadog_metrics"]:
            options = {"statsd_host": "127.0.0.1", "statsd_port": 8125}
            initialize(**options)

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
            statsd.increment("language_de", tags=["environment:develop"])

        elif lang == "en":
            trans_message_prime = self.translate_text(message.content, "de")
            trans_message_second = self.translate_text(message.content, "fr")
            self.count_en = self.count_en + 1
            statsd.increment("language_en", tags=["environment:develop"])

        elif lang == "fr":
            trans_message_prime = self.translate_text(message.content, "de")
            trans_message_second = self.translate_text(message.content, "en")
            self.count_fr = self.count_fr + 1
            statsd.increment("language_fr", tags=["environment:develop"])

        else:
            self.count_other = self.count_other + 1

        if trans_message_prime != "" and trans_message_second != "":
            statsd.increment("translated_msg", tags=["environment:develop"])
            translate_embed = discord.Embed(
                colour=discord.Colour(0x4A90E2),
                description=f"{trans_message_prime.text} \n{trans_message_second.text}",
            )

            result = {
                "embed": translate_embed,
            }
        else:
            result = {
                "embed": None,
            }

        return result

    def get_language_counts(self):
        """Method to acquire language counts and other language usage related params"""

        return {
            "count_de": self.count_de,
            "count_en": self.count_en,
            "count_fr": self.count_fr,
            "count_other": self.count_other,
        }
