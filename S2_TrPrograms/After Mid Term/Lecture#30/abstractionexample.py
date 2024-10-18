from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# Creating instances of shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(4)

# Using abstraction to calculate area and perimeter without knowing the internal details
print("Circle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print("\nRectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

print("\nSquare:")
print("Area:", square.area())
print("Perimeter:", square.perimeter())
