# Variables

a = 1
b = 2

sum = a + b

print(sum)

name = 'Saurav Kumar'

# Data types

'''
Primarily these are the following data types in Python:
1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. None
'''



m = 3 # Integers
n = 0.10 # Floating point number
s = 'gupta' # String
t = True # boolean
u = None # None


# Rules for identifiers 

'''
A variable name can contain alphabets, digits, and underscores.
A variable name can only start with an alphabet and underscores.
A variable name can’t start with a digit.
No white space is allowed to be used inside a variable name.

'''

# Operators

'''
1. Arithmetic operators: +, -, *, / etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not.

'''

#  Arithmetic operators

print(7 + 4)
print(11 - 3)
print(10 * 2)
  
# Assignment operators

first = 10 * 9

first += 3

first -= 3

print(first)



# Comparison operators

a = 10

b  = 10

result = a == b

result2 = a > b

result3 = a < b

result4 = a != b

result5 = a >= b

result6 = a <= b

# Logical operators


print(result ==  result2 or result2 > result3)
print(result ==  result2 and result2 > result3)
print(not(True))


# type() and typecasting


print(type(a))

# input()

store_input = input('Please tell me your age?')

print(store_input)