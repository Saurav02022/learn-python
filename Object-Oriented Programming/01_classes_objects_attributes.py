# CLASS, OBJECT, CLASS ATTRIBUTE, INSTANCE ATTRIBUTE

# Definition:
# A class is a blueprint. An object is one item made from that blueprint.
# A class attribute is shared. An instance attribute belongs to one object.

# Use:
# Use a class to keep related data together.
# Use instance attributes for data that changes from object to object.
# Use class attributes for data shared by every object.

class Student:
    school = "Python School"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute


student1 = Student("Saurav")
student2 = Student("Aman")

print(student1.school)
print(student1.name)
print(student2.name)

# Both students share school, but each has a different name.
# Expected output:
# Python School
# Saurav
# Aman

# Common mistake:
# Do not use a class attribute for data that should be different for each object.

# Practice:
# Add a class attribute called country and an instance attribute called age.
