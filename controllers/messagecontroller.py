"""Module processors"""
from handler.translation import TranslateMe
from handler.commands import Commands


class MessageController:
    """class supplying methods to process incoming messages"""

    def __init__(self, config, validation):
        self.translation = TranslateMe(config)
        self.message_stats = validation

    def commands(self, command, enable_translate):
        """process bot commands"""
        return {
            "help": Commands.get_help(),
            "start": Commands.trigger_translation(enable_translate),
            "stop": Commands.trigger_translation(enable_translate),
            "status": Commands.get_status(enable_translate),
            "stats": Commands.get_stats(
                language_stats=self.translation.get_language_counts(),
                message_stats=self.message_stats.get_message_count(),
            ),
        }[command]

    def translate_message(self, message):
        """process translation"""
        self.translation.get_language(message.content)
        translated_message = self.translation.generate_embed(message)
        return translated_message
