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
        # help:
        if message.content.startswith("$help"):
            help_text = discord.Embed(
                title="**Info**",
                colour=discord.Colour(0xF8E71C),
                description="this bot automatically translates messages "
                "from english to german and french and vice versa",
            )
            help_text.set_footer()
            help_text.add_field(
                name="**Commands**",
                value="```\n $start - starts translation "
                "\n $stop - stops translation "
                "\n $status - shows if translation is active or not```",
            )
            await message.channel.send(embed=help_text)

        # start translation:
        if message.content.startswith("$start"):
            self.enable_translate = True
            start = discord.Embed(
                colour=discord.Colour(0x7ED321), description="start translation.."
            )
            await message.channel.send(embed=start)

        # stop translation:
        if message.content.startswith("$stop"):
            self.enable_translate = False
            stop = discord.Embed(
                colour=discord.Colour(0xD0021B), description="translation stopped.."
            )
            await message.channel.send(embed=stop)

        # translation status:
        if message.content.startswith("$status"):
            if self.enable_translate:
                cur_status = "translation running."
            else:
                cur_status = "translation not running."

            status_embed = discord.Embed(
                colour=discord.Colour(0xF5A623), description=f"{cur_status}"
            )
            await message.channel.send(embed=status_embed)

        # ---------------------------------------------------------------------------------------
        # general message reaction:
        # detect language:
        if not message.content.startswith("$") and len(message.content) > 2:
            self.lang = TranslateMe.get_language(message.content)
        else:
            pass

        # translate actual message-content:
        if self.enable_translate:
            # english
            if self.lang == "en" and not message.content.startswith("$"):
                trans_message_prime = TranslateMe.translate_text(
                    message.content, "de")
                trans_message_second = TranslateMe.translate_text(
                    message.content, "fr")
                translate_embed = discord.Embed(
                    colour=discord.Colour(0x4A90E2),
                    description=f"{trans_message_prime.text} \n{trans_message_second.text}",
                )
                await message.channel.send(embed=translate_embed)

            # german
            elif self.lang == "de" and not message.content.startswith("$"):
                trans_message_prime = TranslateMe.translate_text(
                    message.content, "en")
                trans_message_second = TranslateMe.translate_text(
                    message.content, "fr")
                translate_embed = discord.Embed(
                    colour=discord.Colour(0x4A90E2),
                    description=f"{trans_message_prime.text} \n{trans_message_second.text}",
                )
                await message.channel.send(embed=translate_embed)

            # french
            elif self.lang == "fr" and not message.content.startswith("$"):
                trans_message_prime = TranslateMe.translate_text(
                    message.content, "de")
                trans_message_second = TranslateMe.translate_text(
                    message.content, "en")
                translate_embed = discord.Embed(
                    colour=discord.Colour(0x4A90E2),
                    description=f"{trans_message_prime.text} \n{trans_message_second.text}",
                )
                await message.channel.send(embed=translate_embed)

            else:
                pass
        else:
            pass
