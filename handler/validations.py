"""Module used to validate access to certain actions and roles"""


class Validations:
    """Class supplying validation methods for admin-role and command restrictions"""

    def __init__(self):
        pass

    @staticmethod
    def validate_admin_role(message, client) -> bool:
        """validates if message-author is admin"""
        admin = False
        cur_members = client.get_all_members()
        for member in cur_members:
            if member == message.author:
                for role in member.roles:
                    if role.name == "Admin":
                        admin = True

        return admin

    @staticmethod
    def validate_restrictions(context, is_admin) -> bool:
        """validates if command has restrictions or not and if these are met"""
        if context in ["start", "stop", "stats"] and is_admin:
            return True
        elif context in ["help", "status"]:
            return True
        else:
            return False
