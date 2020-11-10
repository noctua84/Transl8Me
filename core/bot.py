"""everything needed to create the actual bot."""
import time
import asyncio
import discord
from sentry_sdk import capture_exception
from controllers.messagecontroller import MessageController
from validations.validatecommands import ValidateCommands
from validations.validateroles import ValidateRoles
from handler.messages import Messages
from handler.translation import TranslateMe


class Bot(discord.Client):
    """Class representing the bot."""

    client = None
    enable_translate = False

    def __init__(self, config, **options):
        super().__init__(**options)
        self.msg = Messages()
        self.val_com = ValidateCommands(config["commands"])
        self.val_role = ValidateRoles
        self.trans = TranslateMe(config)
        self.message_controller = MessageController(self.trans, self.msg)

    def set_client(self, client):
        """Method to supply the actual client-instance."""
        self.client = client

    # action on login:
    async def on_ready(self):
        """Async method called when the bot is logged in."""
        print("Bot online.")
        print(self.user.name)

    # action on message sent to channel:
    async def on_message(self, message):
        """
        Async method called whenever a message is sent
        and the bot belongs to the channel.
        """
        # general actions:
        if self.client.user == message.author:
            self.msg.message_count_bot += 1
            return

        if message.content.startswith("hello bot"):
            self.msg.message_count_all += 1
            await message.channel.send("hello and welcome to the channel")

        # ---------------------------------------------------------------------------------------
        # bot commands:
        if message.content.startswith("$"):
            self.msg.message_count_all += 1
            self.msg.message_count_command += 1
            # get command context:
            context = message.content.split("$")[1]

            # handle commands with restrictions:
            if self.val_com.command_restrictions(
                context, self.val_role.validate_admin_role(message)
            ):
                result = self.message_controller.commands(
                    context, self.enable_translate
                )

                if context == "start":
                    self.enable_translate = True

                if context == "stop":
                    self.enable_translate = False

                if result["embed"] != "":
                    await message.channel.send(embed=result["embed"])
            else:
                print("nothing to do")

        # ---------------------------------------------------------------------------------------
        # general message reaction:
        else:
            if self.msg.is_translatable(message):
                translate_embed = self.message_controller.translate_message(message)

                if translate_embed["embed"] is not None:
                    self.msg.message_count_all += 1
                    self.msg.message_count_translated += 1
                    await message.channel.send(embed=translate_embed["embed"])
                else:
                    self.msg.message_count_all += 1
            else:
                self.msg.message_count_all += 1

    # function for background task: archive stats
    async def save_msg_stats(self):
        """Save message stats."""
        await self.client.wait_until_ready()

        while not self.client.is_closed():
            cur_msg_count = self.msg.get_message_count()
            cur_translation_count = self.trans.get_language_counts()

            try:
                with open("stats.txt", "a+") as file:
                    file.write(
                        f"Time: {int(time.time())} \n"
                        f"Messages: {cur_msg_count} \n"
                        f"Translations: {cur_translation_count}\n\n"
                    )

                    self.msg.reset_message_count()

                    await asyncio.sleep(10)

            except FileNotFoundError as f_err:
                capture_exception(f_err)
                await asyncio.sleep(60)
