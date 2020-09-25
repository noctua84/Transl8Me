"""some bot commands"""
import discord


class Commands:
    """class supplying methods for each command and one controlling method"""

    def __init__(self):
        pass

    @staticmethod
    def get_help():
        """applies help response"""
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

        return {"embed": help_text}

    @staticmethod
    def trigger_translation(translation_state):
        """triggers translation"""
        if not translation_state:
            state = discord.Embed(
                colour=discord.Colour(0x7ED321), description="start translation.."
            )
            translation_state = True
        else:
            state = discord.Embed(
                colour=discord.Colour(0xD0021B), description="translation stopped.."
            )
            translation_state = False

        return {"embed": state, "status": translation_state}

    @staticmethod
    def get_status(translation_state):
        """applies status response"""
        if translation_state:
            cur_status = "translation running."
        else:
            cur_status = "translation not running."

        status_embed = discord.Embed(
            colour=discord.Colour(0xF5A623), description=f"{cur_status}"
        )

        return {"embed": status_embed}
