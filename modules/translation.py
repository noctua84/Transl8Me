"""Translation module."""
from textblob import TextBlob
# from google.cloud import translate_v3
from googletrans import Translator
import discord

# implement google cloud translate api (not free sadly) [test]


class TranslateMe:
    """Class to translation related methods."""

    lang_counts = {}

    def __init__(self, config):
        self.src_lang = ""
        self.config = config

        # generate language-counts dict:
        self.lang_counts = {language: 0 for language in config["language"]["supported"]}
        self.lang_counts["other"] = 0
        print(self.lang_counts)
        
    def translate_message(self, message):
        """Method to process translation."""
        self.__get_language(message.content)
        return self.__generate_embed(message)

    def __get_language(self, text):
        """Method to extract the language of a given text."""
        lang = TextBlob(text)
        self.src_lang = lang.detect_language()

    def __translate_text(self, text, valid_languages: list) -> dict:
        """Method to translate a given text based on the supplied language code."""
        trans = Translator()
        translations = {}
        lang_count = 1

        self.lang_counts.update(
            {
                lang_id: value + 1
                for lang_id, value in self.lang_counts.items()
                if lang_id == self.src_lang
            }
        )

        if self.src_lang in valid_languages:
            valid_languages.remove(self.src_lang)

            for lang in valid_languages:
                result = trans.translate(text, lang)
                translations[lang_count] = result
                lang_count += 1
        else:
            self.lang_counts["other"] += 1

        return translations

    def __generate_embed(self, message):
        """Method to manage the translation."""
        valid_languages = []

        for language in self.config["language"]["supported"]:
            valid_languages.append(language)

        trans_messages = self.__translate_text(message.content, valid_languages)

        if trans_messages != {}:
            translate_embed = discord.Embed(
                colour=discord.Colour(0x4A90E2),
                description=f"{trans_messages[1].text} \n\n "
                f"{trans_messages[2].text}",
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
        """Method to acquire language counts and other language usage related params."""
        return self.lang_counts
