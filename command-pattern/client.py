from command import *
from invoker import SimpleRemoteControl
from receiver import Light, GarageDoor


class RemoteControlTest:
    @staticmethod
    def main():
        light: Light = Light()
        # wrap the object to a command
        light_on_command: Command = LightOnCommand(light)

        garage_door: GarageDoor = GarageDoor()
        garage_door_command: Command = GarageDoorCommand(garage_door)

        remote = SimpleRemoteControl()  # this is the invoker

        remote.set_command(light_on_command)
        remote.button_pressed()
        remote.set_command(garage_door_command)
        remote.button_pressed()


if __name__ == '__main__':
    RemoteControlTest.main()
