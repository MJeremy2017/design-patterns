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

        ceiling_fan: CeilingFan = CeilingFan("")
        ceiling_fan_high: Command = CeilingFanHighCommand(ceiling_fan)
        ceiling_fan_off: Command = CeilingFanOffCommand(ceiling_fan)

        remote = SimpleRemoteControl()  # this is the invoker

        remote.set_command(0, living_room_light_on, living_room_light_off)
        remote.set_command(1, kitchen_light_on, kitchen_light_off)
        remote.set_command(2, garage_door_up, garage_door_down)

        remote.on_button_pressed(0)
        remote.on_button_pressed(1)
        remote.off_button_pressed(1)
        remote.off_button_pressed(0)

        print("Test undo button ================================== ")
        remote.on_button_pressed(0)
        remote.off_button_pressed(0)
        remote.undo_button_pressed()
        remote.off_button_pressed(0)

        print("Test ceiling fan ================================== ")
        remote.set_command(0, ceiling_fan_high, ceiling_fan_off)
        remote.on_button_pressed(0)
        remote.off_button_pressed(0)
        remote.undo_button_pressed()
        remote.off_button_pressed(0)

        print("Test Macro ========================================= ")
        commands_on: List[Command] = [living_room_light_on, kitchen_light_on, garage_door_up]
        commands_off: List[Command] = [living_room_light_off, kitchen_light_off, garage_door_down]
        macro_on: Command = MacroCommand(commands_on)
        macro_off: Command = MacroCommand(commands_off)

        remote.set_command(3, macro_on, macro_off)
        remote.on_button_pressed(3)
        remote.undo_button_pressed(3)


if __name__ == '__main__':
    RemoteControlTest.main()
