"""everything needed to create the actual bot."""
import discord
from translation import TranslateMe


class Bot(discord.Client):
    """class representing the bot."""
    # target_lang = 'en'
    client = None
    lang = ""
    enable_translate = False

    def set_client(self, client):
        """method to supply the actual client-instance"""
        self.client = client

    # einloggen:
    async def on_ready(self):
        """async method called when the bot is logged in"""
        print("Bot online.")

    # wenn nachrichten gepostet werden:
    async def on_message(self, message):
        """async method called whenever a message is sent and the bot belongs to the channel."""
        # general actions:
        if message.author == self.client.user:
            return

        if message.content.startswith('hello bot'):
            await message.channel.send('hello and welcome to the channel')

        # ---------------------------------------------------------------------------------------
        # bot commands:
        # help:
        if message.content.startswith('$help'):
            help_text = discord.Embed(title="**Info**",
                                      colour=discord.Colour(0xf8e71c),
                                      description="this bot automatically translates messages "
                                                  "from english to german and vice versa")
            help_text.set_footer()
            help_text.add_field(name="**Commands**", value="```\n $start - starts translation "
                                                           "\n $stop - stops translation \n```")
            await message.channel.send(embed=help_text)

        # start translation:
        if message.content.startswith('$start'):
            self.enable_translate = True
            start = discord.Embed(colour=discord.Colour(
                0x7ed321), description="start translation..")
            await message.channel.send(embed=start)

        # stop translation:
        if message.content.startswith('$stop'):
            self.enable_translate = False
            stop = discord.Embed(colour=discord.Colour(
                0xd0021b), description="translation stopped..")
            await message.channel.send(embed=stop)

        # ---------------------------------------------------------------------------------------
        # general message reaction:
        # detect language:
        if not message.content.startswith('$') and len(message.content) > 2:
            self.lang = TranslateMe.get_language(message.content)
        else:
            pass

        # translate actual message-content:
        if self.enable_translate:
            if self.lang == "en" and not message.content.startswith('$'):
                trans_message = TranslateMe.translate_text(
                    message.content, "de")
                await message.channel.send(trans_message.text)
            elif self.lang == "de" and not message.content.startswith('$'):
                trans_message = TranslateMe.translate_text(
                    message.content, "en")
                await message.channel.send(trans_message.text)
            else:
                pass
        else:
            pass
