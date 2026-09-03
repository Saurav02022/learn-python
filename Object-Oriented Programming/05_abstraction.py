# ABSTRACTION AND ABSTRACT CLASSES

# Definition:
# Abstraction hides complex steps behind a simple method.
# An abstract class gives child classes a required plan.

# Use:
# Use abstraction when users should call a simple method.
# Use an abstract class when every child must provide a method.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


square1 = Square(5)
print(square1.area())

# Shape gives the rule: every shape must have area().
# Square hides the calculation inside area().
# Expected output:
# 25

# Common mistake:
# An abstract child cannot be created until it implements every abstract method.

# Practice:
# Create a Circle class with an area() method.
