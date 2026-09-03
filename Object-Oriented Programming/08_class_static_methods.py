# CLASS METHODS AND STATIC METHODS

# Definition:
# An instance method receives self, the current object.
# A class method receives cls, the current class.
# A static method receives neither automatically.

# Use:
# Use instance methods for object data.
# Use class methods for class data or alternative constructors.
# Use static methods for related functions needing no object or class data.

class Student:
    school = "Python School"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    @classmethod
    def show_school(cls):
        print(cls.school)

    @staticmethod
    def show_subject():
        print("Python")


student1 = Student("Saurav")
student1.show_name()
Student.show_school()
Student.show_subject()

# @classmethod and @staticmethod are decorators.
# Expected output:
# Saurav
# Python School
# Python

# Common mistake:
# Do not use self when a method is meant to be a class or static method.

# Practice:
# Add a class method that changes school using cls.
