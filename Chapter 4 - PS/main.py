# 1. Write a program to store seven fruits in a list entered by the user.

store_fruits = []

store_fruits.append(str(input('Enter Fruit 1:- ')))
store_fruits.append(str(input('Enter Fruit 2:- ')))
store_fruits.append(str(input('Enter Fruit 3:- ')))
store_fruits.append(str(input('Enter Fruit 4:- ')))
store_fruits.append(str(input('Enter Fruit 5:- ')))
store_fruits.append(str(input('Enter Fruit 5:- ')))
store_fruits.append(str(input('Enter Fruit 6:- ')))
store_fruits.append(str(input('Enter Fruit 67:- ')))

print(store_fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

student_marks = []

student_marks.append(int(input('Enter Student marks:- ')))
student_marks.append(int(input('Enter Student marks:- ')))
student_marks.append(int(input('Enter Student marks:- ')))
student_marks.append(int(input('Enter Student marks:- ')))
student_marks.append(int(input('Enter Student marks:- ')))
student_marks.append(int(input('Enter Student marks:- ')))

student_marks.sort()

print(student_marks)

# 3. Check that a tuple type cannot be changed in python.


# 4. Write a program to sum a list with 4 numbers.

l = [10,32,42,92]

print(sum(l))

# 5. Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)

result = a.count(0)

print(result)