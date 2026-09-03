# SELF AND CONSTRUCTOR

# Definition:
# self means the current object.
# A constructor initializes an object when it is created.
# In Python, __init__ is used to initialize the object.

# Use:
# Use self to save and use data belonging to one object.
# Use __init__ to give every new object its starting data.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name, self.age)


student1 = Student("Saurav", 27)
student2 = Student("Aman", 25)
student1.show_details()
student2.show_details()

# Python sends student1 as self in student1.show_details().
# Expected output:
# Saurav 27
# Aman 25

# Common mistake:
# self is written in the method definition but is not passed manually when calling it.

# Practice:
# Add a city argument and print it for both students.
