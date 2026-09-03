# Hiding the implementation details of a class and only showing the essential features to the user is known as abstraction. 
# In Python, we can achieve abstraction by using abstract classes and methods.

class Car:

    def __init__(self):
        self.acc = False
        self.brk = True
        self.clutch = False
    

    def start(self):
        self.acc = True
        self.brk = False
        self.clutch = True
        print("Car is starting...")

car1 = Car()
car1.start()
