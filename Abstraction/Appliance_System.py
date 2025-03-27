from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass  # Abstract method (must be implemented in child classes)

class Fan(Appliance):
    def turn_on(self):
        print("Fan is now running.")

class Light(Appliance):
    def turn_on(self):
        print("Light is now on.")

# Creating objects and calling the abstract method
f = Fan()
f.turn_on()  # Output: Fan is now running.

l = Light()
l.turn_on()  # Output: Light is now on.

