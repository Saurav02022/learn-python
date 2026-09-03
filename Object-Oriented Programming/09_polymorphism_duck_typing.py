# POLYMORPHISM AND DUCK TYPING

# Definition:
# Polymorphism means the same method call can behave differently for different objects.
# Duck typing checks what an object can do instead of checking its class.

# Use:
# Use polymorphism when different objects share an action.

class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# The same animal.sound() call gives different results.
# Expected output:
# Bark
# Meow

# Common mistake:
# Every object used in the loop must have the method being called.

# Practice:
# Add a Bird class with sound() and put it in animals.
