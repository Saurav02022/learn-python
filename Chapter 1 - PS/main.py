import pyjokes
import pyttsx3
import os


# Problem 1:
# Write a program to print Twinkle Twinkle Little Star poem in Python.

print('''

Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.

''')


# Problem 2:
# Use REPL and print the table of 5 using it.
#
# >>> 5 * 1
# 5
# >>> 5 * 2
# 10
# >>> 5 * 3
# 15
# ...
# >>> 5 * 10
# 50


# Problem 3:
# Install an external module and use it to perform an operation of your interest.

joke = pyjokes.get_joke()

print(joke)

engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()


# Problem 4:
# Write a Python program to print the contents of a directory using the os module.

# Get the contents of the current directory
contents = os.listdir(".")

# Print each item
for item in contents:
    print(item)