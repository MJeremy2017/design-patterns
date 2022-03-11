from command import Command


# noinspection PyTypeChecker
class SimpleRemoteControl:
    def __init__(self):
        self.slot: Command = None

    def set_command(self, command: Command):
        self.slot = command

    def button_pressed(self):
        self.slot.execute()
