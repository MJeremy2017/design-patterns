class Light:
    def __init__(self, name: str):
        self.name: str = name

    def on(self):
        print(self.name, "light is on!")

    def off(self):
        print(self.name, "light is off")


class GarageDoor:
    def __init__(self, name: str):
        self.name: str = name

    def up(self):
        print(self.name, "garage door is up!")

    def down(self):
        print(self.name, "garage door is down!")


class CeilingFan:
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __init__(self, name: str):
        self.name: str = name
        self.speed = self.OFF

    def off(self):
        self.speed = self.OFF
        print("speed is off")

    def low(self):
        self.speed = self.LOW
        print("speed is low")

    def medium(self):
        self.speed = self.MEDIUM
        print("speed is medium")

    def high(self):
        self.speed = self.HIGH
        print("speed is high")

    def get_speed(self):
        return self.speed




