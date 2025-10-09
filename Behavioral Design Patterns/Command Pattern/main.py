from abc import ABC, abstractmethod

class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")   

class Fan:
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class LightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class FanCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

    def undo(self):
        self.fan.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

if __name__ == "__main__":
    light = Light()
    fan = Fan()

    light_command = LightCommand(light)
    fan_command = FanCommand(fan)

    remote = RemoteControl()

    remote.set_command(light_command)
    remote.press_button()
    remote.press_undo()

    remote.set_command(fan_command)
    remote.press_button()
    remote.press_undo()