from abc import abstractmethod, ABC
from receiver import Light, GarageDoor


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class GarageDoorCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()


