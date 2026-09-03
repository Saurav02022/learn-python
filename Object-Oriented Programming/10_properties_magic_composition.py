# PROPERTIES, MAGIC METHODS, AND COMPOSITION

# Definition:
# A property lets a method act like an attribute.
# A magic method gives Python operations meaning for our objects.
# Composition means one object contains another object: a has-a relationship.

# Use:
# Use properties to validate data.
# Use magic methods for operations such as str(), len(), and +.
# Use composition when an object is made of other objects.

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, speed):
        self.engine = Engine()
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value >= 0:
            self._speed = value

    def __str__(self):
        return f"Car at {self.speed} km/h"

    def __add__(self, other):
        return self.speed + other.speed

    def start(self):
        self.engine.start()


car1 = Car(40)
car2 = Car(60)
car1.speed = 50
car1.start()
print(car1)
print(car1 + car2)

# car1 has an Engine, so this is composition.
# car1 + car2 calls __add__().
# Expected output:
# Engine started
# Car at 50 km/h
# 110

# Common mistake:
# A property is used without parentheses: car1.speed, not car1.speed().

# Practice:
# Add __eq__ to compare two cars by speed.
