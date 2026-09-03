# METHOD OVERRIDING, super(), AND MRO

# Definition:
# Overriding means a child writes its own version of a parent method.
# super() calls the parent version.
# MRO is the order Python follows to find a method.

# Use:
# Use overriding for different child behavior.
# Use super() to reuse parent behavior.
# Learn MRO when multiple inheritance is involved.

class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):
        super().show()
        print("Child method")


child1 = Child()
child1.show()
print([class_name.__name__ for class_name in Child.mro()])

# Child.show() overrides Parent.show().
# super().show() still calls Parent.show().
# Expected output:
# Parent method
# Child method
# ['Child', 'Parent', 'object']

# Common mistake:
# self.show() inside Child.show() would call Child.show() again.

# Practice:
# Create a GrandChild class and observe its MRO.
