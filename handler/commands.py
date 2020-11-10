"""Module for bot commands."""
import discord


class Commands:
    """class to supply methods for each command and one controlling method."""

    def __init__(self):
        pass

    @staticmethod
    def get_help():
        """applies help response."""
        help_text = discord.Embed(
            title="**Info**",
            colour=discord.Colour(0xF8E71C),
            description="this bot automatically translates messages "
            "from english to german, french and russian and vice versa",
        )
        help_text.set_footer()
        help_text.add_field(
            name="**Commands**",
            value="```\n $start - starts translation "
            "\n $stop - stops translation "
            "\n $status - shows if translation is active or not```",
        )

        return {"embed": help_text}

    @staticmethod
    def trigger_translation(command: str, enable_translate: bool):
        """triggers translation."""

        if command == "start" and not enable_translate:
            state = discord.Embed(
                colour=discord.Colour(0x7ED321), description="start translation.."
            )

        elif command == "stop" and enable_translate:
            state = discord.Embed(
                colour=discord.Colour(0xD0021B), description="translation stopped.."
            )
        else:
            state = ""

        return {"embed": state}

    @staticmethod
    def get_status(translation_state):
        """applies status response."""
        if translation_state:
            cur_status = "translation running."
        else:
            cur_status = "translation not running."

        status_embed = discord.Embed(
            colour=discord.Colour(0xF5A623), description=f"{cur_status}"
        )

        return {"embed": status_embed}

    @staticmethod
    def get_stats(language_stats: dict, message_stats: dict):
        """renders embed for language statistics."""

        stats_embed = discord.Embed(
            colour=discord.Colour(0xF5A623),
            title="**Stats**",
            description="```"
            f"German: {language_stats['de']} Messages\n"
            f"English: {language_stats['en']} Messages\n"
            f"French: {language_stats['fr']} Messages\n"
            f"Russian: {language_stats['ru']} Messages\n"
            f"Other: {language_stats['other']} Messages\n"
            f"\n"
            f"Messages translated: {message_stats['translated']} \n"
            f"Messages not translated: {language_stats['other']} \n"
            f"\n"
            f"Emoji-Messages: {message_stats['emojis']} \n"
            f"Command-Messages: {message_stats['commands']} \n"
            f"Image-Messages: {message_stats['images']} \n"
            f"\n"
            f"Total user messages handled: {message_stats['all']} \n"
            f"Total bot messages: {message_stats['bot']} \n"
            "```",
        )

        return {"embed": stats_embed}
