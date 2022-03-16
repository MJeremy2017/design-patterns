from abc import abstractmethod, ABC
from receiver import Light, GarageDoor, CeilingFan
from typing import List


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NilCommand(Command):
    def undo(self):
        pass

    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoorUpCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorDownCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan: CeilingFan = ceiling_fan
        self.prev_speed: int = ceiling_fan.OFF

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan: CeilingFan = ceiling_fan
        self.prev_speed: int = ceiling_fan.OFF

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class MacroCommand(Command):
    def __init__(self, commands: List[Command]):
        self.commands: List[Command] = commands

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def undo(self):
        for cmd in self.commands:
            cmd.undo()

