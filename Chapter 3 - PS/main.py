# 1. Write a python program to display a user entered name followed by Good Afternoon using
# input() function.

name = input('Enter your name:-')

print(f'Good Afternoon, {name}')

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

letter = letter.replace('<|Name|>','Saurav')
letter = letter.replace('<|Date|>','28th August 2026')

print(letter)

# 3. Write a program to detect double space in a string.

name = 'Saurav  Kumar'

print(name.find("  "))

# 4. Replace the double space from problem 3 with single spaces.

name = name.replace("  "," ")

print(name)

# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"


letter = "Dear Harry,\nthis python course is nice.\nThanks!"

print(letter)