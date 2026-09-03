# INHERITANCE TYPES

# Definition:
# Inheritance lets a child class reuse features from a parent class.
# Single, multilevel, and multiple inheritance are common types.

# Use:
# Use inheritance for an is-a relationship, such as a ToyotaCar is a Car.

class Car:
    def start(self):
        print("Car started")


class ToyotaCar(Car):  # Single inheritance
    pass


class Fortuner(ToyotaCar):  # Multilevel inheritance
    pass


class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def make_call(self):
        print("Calling")


class Smartphone(Camera, Phone):  # Multiple inheritance
    pass


Fortuner().start()
smartphone1 = Smartphone()
smartphone1.take_photo()
smartphone1.make_call()

# Expected output:
# Car started
# Photo taken
# Calling

# Common mistake:
# Do not use inheritance for a has-a relationship. A Car has an Engine.

# Practice:
# Add a stop() method to Car and use it through Fortuner.
