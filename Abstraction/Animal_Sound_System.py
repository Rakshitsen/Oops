from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (must be implemented in child classes)

class Dog(Animal):
    def make_sound(self):
        print("Barking")

class Cat(Animal):
    def make_sound(self):
        print("Meowing")

class Cow(Animal):
    def make_sound(self):
        print("Mooing")

# Creating objects and calling the abstract method
d1 = Dog()
d1.make_sound()  # Output: Barking

c1 = Cat()
c1.make_sound()  # Output: Meowing

c2 = Cow()
c2.make_sound()  # Output: Mooing

