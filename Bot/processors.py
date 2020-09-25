from Bot.translation import TranslateMe
from Bot.commands import Commands


class Processors:
    def __init__(self):
        self.translation = TranslateMe()

    @staticmethod
    def commands(command, enable_translate):
        """process bot commands"""
        return {
            "help": Commands.get_help(),
            "start": Commands.trigger_translation(enable_translate),
            "stop": Commands.trigger_translation(enable_translate),
            "status": Commands.get_status(enable_translate),
        }[command]

    def translate_message(self, message):
        """process translation"""
        lang = self.translation.get_language(message.content)
        translated_message = self.translation.translated_message(message, lang)
        return translated_message
