"""Module processors"""
from handler.translation import TranslateMe
from handler.commands import Commands


class MessageController:
    """class controlling what to be done with a message"""

    def __init__(self, config):
        self.translation = TranslateMe(config)

    def commands(self, command, enable_translate):
        """process bot commands"""
        return {
            "help": Commands.get_help(),
            "start": Commands.trigger_translation(enable_translate),
            "stop": Commands.trigger_translation(enable_translate),
            "status": Commands.get_status(enable_translate),
            "stats": Commands.get_stats(
                language_stats=self.translation.get_language_counts()
            ),
        }[command]

    def translate_message(self, message):
        """process translation"""
        lang = self.translation.get_language(message.content)
        translated_message = self.translation.translated_message(message, lang)
        return translated_message
