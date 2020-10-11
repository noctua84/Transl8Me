"""Module used to validate access to certain actions and roles"""


class Validations:
    """Class supplying validation methods for admin-role and command restrictions"""

    def __init__(self, config: dict):
        self.config = config
        self.restricted = []
        self.open = []

        if len(config["restricted"]) > 0:
            self.restricted = [
                command
                for command in config["implemented"]
                if command in config["restricted"]
            ]
            self.open = [
                command
                for command in config["implemented"]
                if command not in config["restricted"]
            ]

        else:
            for command in config["implemented"]:
                self.open.append(command)

        print(self.restricted)
        print(self.open)

    @staticmethod
    def validate_admin_role(message, client) -> bool:
        """validates if message-author is admin"""
        cur_member = ""

        for member in client.get_all_members():
            if member == message.author:
                cur_member = member

        for role in cur_member.roles:
            if role.name == "Admin":
                return True

        return False

    def validate_restrictions(self, context, is_admin) -> bool:
        """validates if command has restrictions or not and if these are met"""
        if context in self.restricted and is_admin:
            return True
        if context in self.open:
            return True
        return False
