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
