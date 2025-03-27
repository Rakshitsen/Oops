from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass  # Abstract method (must be implemented in child classes)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(f"Area of the rectangle is {self.length * self.width}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        print(f"Area of the circle is {3.14 * (self.radius ** 2)}")

# Creating objects and calling the abstract method
r1 = Rectangle(5, 6)
r1.calculate_area()  # Output: Area of the rectangle is 30

c1 = Circle(7)
c1.calculate_area()  # Output: Area of the circle is 153.86

