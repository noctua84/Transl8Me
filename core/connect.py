"""Module to handle the bot-connection and related things."""
import discord
from discord import LoginFailure
from sentry_sdk import capture_exception
from .bot import Bot


class Connect:
    """Class to handle the connection of the bot to the server."""

    def __init__(self, config):
        self.config = config

    def connect_bot(self):
        """Function to connect the bot to the server"""
        try:
            token = self.config["global_settings"]["bot_token"]
            intents = discord.Intents.all()
            client = Bot(self.config, intents=intents)
            client.set_client(client)
            # client.loop.create_task(client.save_msg_stats())
            client.run(token)
        except TypeError as type_exception:
            capture_exception(type_exception)
        except LoginFailure as bot_token_exception:
            capture_exception(bot_token_exception)

    def something_else(self):
        """A dummy method to do nothing but be there."""
