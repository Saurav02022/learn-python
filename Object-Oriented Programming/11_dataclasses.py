# DATACLASSES

# Definition:
# A dataclass is a class mainly used to store data.
# Python creates common methods such as __init__ for us.

# Why use it?
# Use a dataclass when an object mostly contains values.
# It avoids writing repeated setup code.

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int


student1 = Student("Saurav", 27)
student2 = Student("Aman", 25)

print(student1)
print(student2)

# @dataclass creates an __init__ method and a useful display method.
# Expected output:
# Student(name='Saurav', age=27)
# Student(name='Aman', age=25)

# Common mistake:
# Use a normal class when the object needs complex behavior.

# Practice:
# Add a marks field and create another Student.
