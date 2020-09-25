"""everything needed to create the actual bot."""
import discord
from Bot.processors import Processors


class Bot(discord.Client):
    """class representing the bot."""

    # target_lang = 'en'
    client = None
    enable_translate = False
    processor = Processors()

    def set_client(self, client):
        """method to supply the actual client-instance"""
        self.client = client

    # einloggen:
    async def on_ready(self):
        """async method called when the bot is logged in"""
        print("Bot online.")
        print(self.user.name)

    # wenn nachrichten gepostet werden:
    async def on_message(self, message):
        """async method called whenever a message is sent and the bot belongs to the channel."""

        # general actions:
        if self.client.user == message.author:
            return

        if message.content.startswith("hello bot"):
            await message.channel.send("hello and welcome to the channel")

        # ---------------------------------------------------------------------------------------
        # bot commands:
        if message.content.startswith("$"):
            context = message.content.split("$")[1]
            # handle commands
            result = Processors.commands(context, self.enable_translate)
            if "status" in result and result["status"]:
                self.enable_translate = result["status"]

            await message.channel.send(embed=result["embed"])

        # ---------------------------------------------------------------------------------------
        # general message reaction:
        else:
            if translate_embed["embed"] is not None:
                await message.channel.send(embed=translate_embed["embed"])
            else:
                pass
