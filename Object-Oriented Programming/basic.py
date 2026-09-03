# class Student:
#     name = 'Saurav Kumar'

# s1 = Student()
# print(s1.name)

# class Car:
#     color = 'blue'
#     brand = 'bmw'

# car1 = Car()
# print(car1.brand)
# print(car1.color)

# Constructor and __init__ Fuction

# class Student:
#     college_name = 'IIT Patna'

#     # default constructors
#     # def __init__(self, name, bases, dict, /, **kwds):
#     #     pass

#     # constructor with parameter
#     def __init__(self,fullname,age):
#         self.name = fullname
#         self.age = age
#         print('Adding a new data in database')


# s1 = Student('Saurav',27)
# print(s1.name) #Saurav
# print(s1.age) # 27
# print(s1.college_name) # IIT Patna
# print(Student.college_name) # IIT Patna


# practice question 
# Create student class that takes name and marks of 3 subjects as arguments in constructore. Then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def chechHealth():
        print('Stuent Class is healthy')   

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

s1 = Student('Saurav', [90, 80, 70])
print(s1.name) # Saurav
print(s1.chechHealth()) # Stuent Class is healthy
print(s1.average()) # 80.0