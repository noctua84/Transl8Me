"""Module used to validate access to certain actions and roles."""
import discord
from discord import Member


class ValidateRoles:
    """Class to supply validation methods for role-checks."""

    def __init__(self):
        pass

    @staticmethod
    def validate_admin_role(message) -> bool:
        """validates if message-author is admin."""
        author = message.author.name
        member: Member = discord.utils.find(
            lambda m: author in m.name, message.guild.members)
        
        for role in member.roles:
            if role.name == "Admin":
                return True

        return False

    def validate_something_else(self):
        """dummy method."""
