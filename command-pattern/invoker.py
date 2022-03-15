from command import Command, NilCommand
from typing import List


# noinspection PyTypeChecker
class SimpleRemoteControl:
    def __init__(self):
        self.on_commands: List[Command] = [NilCommand] * 7
        self.off_commands: List[Command] = [NilCommand] * 7
        self.undo_command: Command = NilCommand

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_pressed(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_pressed(self):
        self.undo_command.undo()
