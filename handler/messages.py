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
        img_only = self.__check_img_only(message.content, message.attachments[0])
        emoji_only = self.__check_emojis_only(message.content.split(" "))

        if img_only or emoji_only:
            return False

    def get_message_count(self) -> dict:
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
        """Method to reset message counters"""
        self.message_count_img = 0
        self.message_count_emoji = 0
        self.message_count_all = 0
        self.message_count_translated = 0
        self.message_count_bot = 0
        self.message_count_command = 0

    # Helper methods
    def __check_emojis_only(self, split_message: list) -> bool:
        """Method to check if message contains only emojis"""
        emoji_count = 0

        # check if content contains only emojis:
        for item in split_message:
            if item in UNICODE_EMOJI:
                emoji_count += 1

            if len(split_message) == emoji_count:
                self.message_count_emoji += 1
                return False
            return True

    def __check_img_only(self, content, attachment) -> bool:
        """Method to check if message contains only images"""
        attachment_type = attachment.filename.split(".")
        if content == "" and attachment_type in ["jpg", "png", "gif", "jpeg"]:
            self.message_count_img += 1
            return True
