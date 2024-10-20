from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of subclasses
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Calling methods
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

# shape = Shape()
# print(shape.area)