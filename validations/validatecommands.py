"""Module to validate commands."""


class ValidateCommands:
    """class providing command validation."""

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

    def command_restrictions(self, context, is_admin) -> bool:
        """validates if command has restrictions or not and if these are met."""
        if context in self.restricted and is_admin:
            return True
        if context in self.open:
            return True
        return False

    def check_command_prefix(self):
        """check command prefix."""
        pass
