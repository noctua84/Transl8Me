"""Module for message handling"""
from emoji import UNICODE_EMOJI


class Messages:
    """
    class handling message-related tasks.
    currently checking if a message is translatable functioning as a filter
    for image-only and emoji-only messages requiring no translation.
    """

    # class vars (independent from instance):
    message_count_all = 0
    message_count_translated = 0
    message_count_emoji = 0
    message_count_img = 0
    message_count_bot = 0
    message_count_command = 0

    def __init__(self):
        pass

    def is_translatable(self, message) -> bool:
        """
        evaluates if message should be translated or not.
        filters messages containing only emojis.
        """
        if message.content == "" and message.attachments[0].filename.endswith(".jpg"):
            self.message_count_img += 1
            return False
        else:
            cur_message = message.content.split(" ")
            emoji_count = 0

            # check if content contains only emojis:
            for item in cur_message:
                if item in UNICODE_EMOJI:
                    emoji_count += 1

            if len(cur_message) == emoji_count:
                self.message_count_emoji += 1
                return False
            else:
                return True

    def get_message_count(self):
        """returns message counts"""

        return {
            "all": self.message_count_all,
            "commands": self.message_count_command,
            "translated": self.message_count_translated,
            "emojis": self.message_count_emoji,
            "images": self.message_count_img,
            "bot": self.message_count_bot,
        }

    def reset_message_count(self):
        self.message_count_img = 0
        self.message_count_emoji = 0
        self.message_count_all = 0
        self.message_count_translated = 0
        self.message_count_bot = 0
        self.message_count_command = 0
