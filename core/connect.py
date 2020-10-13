from discord import LoginFailure
from sentry_sdk import capture_exception
from .bot import Bot


class Connect:
    """class handeling the connection of the bot to the server"""

    def __init__(self, config):
        self.config = config

    def connect_bot(self):
        """Function to connect the bot to the server"""
        try:
            token = self.config["global_settings"]["bot_token"]
            client = Bot(self.config)
            client.set_client(client)
            # client.loop.create_task(client.save_msg_stats())
            client.run(token)
        except TypeError as type_exception:
            capture_exception(type_exception)
        except LoginFailure as bot_token_exception:
            capture_exception(bot_token_exception)
