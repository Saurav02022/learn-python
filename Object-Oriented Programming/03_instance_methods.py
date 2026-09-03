# METHODS AND INSTANCE METHODS

# Definition:
# A method is a function inside a class.
# An instance method receives the current object as self.

# Use:
# Use an instance method when an object needs to perform an action with its data.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def show_name(self):
        print(self.name)


student1 = Student("Saurav", [90, 80, 70])
student1.show_name()
print(student1.average())

# student1.average() is similar to Student.average(student1).
# Expected output:
# Saurav
# 80.0

# Common mistake:
# A method using object data needs self in its definition.

# Practice:
# Add a method that returns the highest mark.
