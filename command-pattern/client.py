from command import *
from invoker import SimpleRemoteControl
from receiver import Light, GarageDoor


class RemoteControlTest:
    @staticmethod
    def main():
        living_room_light: Light = Light("Living Room")
        kitchen_light: Light = Light("Kitchen")
        # wrap the object to a command
        living_room_light_on: Command = LightOnCommand(living_room_light)
        living_room_light_off: Command = LightOffCommand(living_room_light)

        kitchen_light_on: Command = LightOnCommand(kitchen_light)
        kitchen_light_off: Command = LightOffCommand(kitchen_light)

        garage_door: GarageDoor = GarageDoor("")
        garage_door_up: Command = GarageDoorUpCommand(garage_door)
        garage_door_down: Command = GarageDoorDownCommand(garage_door)

        remote = SimpleRemoteControl()  # this is the invoker

        remote.set_command(0, living_room_light_on, living_room_light_off)
        remote.set_command(1, kitchen_light_on, kitchen_light_off)
        remote.set_command(2, garage_door_up, garage_door_down)

        remote.on_button_pressed(0)
        remote.on_button_pressed(1)
        remote.off_button_pressed(1)
        remote.off_button_pressed(0)


if __name__ == '__main__':
    RemoteControlTest.main()
