# Learn how to build control flow into your python code by including if, else, and elif statements as well as try and except statements.
# Expect to learn all you need to know about boolean variables and logical operators.

# In order to build control flow into our program, we want to be able to check if something is true or not. A boolean expression is a statement that can either be True or False.

# "Dogs are mammals"
import math
import random
statement_one = "Yes"

# My dog is named Pavel.
statement_two = "Yes"

# Dogs make the best pets.
statement_three = "No"

# Cats are female dogs.
statement_four = "Yes"

# Relational operators compare two items and return either True or False.
# For this reason, you will sometimes hear them called comparators.
# The two relational operators we’ll cover first are:

# Equals: ==
# Not equals: !=
# These operators compare two items and return True or False if they are equal or not.

statement_one = (5 * 2) - 1 == 8 + 1

statement_two = 13 - 6 != (3 * 2) + 1

statement_three = 3 * (2 - 1) == 4 - 1

my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))

# Enter a user name here, make sure to make it a string
user_name = "Dave"

if user_name == "Dave":
    print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
    print("I know it is you, Dave! Go away!")

x = 20
y = 20

# Write the first if statement here:
if x == y:
    print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120:
    print("You have enough credits to graduate!")

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
    print("You meet the requirements to graduate!")

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate!")

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate!")

grade = 86

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


name = "Luis"
question = "Will I be a good programmer?"
answer = ""

random_number = random.randint(1, 9)

# print(random_number)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "IBetter not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error."

print(name + " " + "asks: " + "question")
print("Magic 8-Ball's answer: " + answer)

# Python refers to the mistakes within the program as errors and will point to the location where an error occurred with a ^ character.
# When programs throw errors that we didn’t expect to encounter, we call those errors bugs.
# Programmers call the process of updating the program so that it no longer produces bugs debugging.

# In Python, there are many different ways of classifying errors, but here are some common ones:

# SyntaxError: Error caused by not following the proper structure (syntax) of the language.
# NameError: Errors reported when the interpreter detects a variable that is unknown.
# TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.

# Here’s an example of a SyntaxError error message:

# File "script.py", line 1
#  print(Hello world!)
#                  ^
# SyntaxError: invalid syntax

# Some common syntax errors are:

# Misspelling a Python keyword.
# Missing colon :.
# Missing closing parenthesis ), square bracket ], or curly brace }.


fortune = random.randint(0, 4)

if fortune == 0:
    print("May you one day be carbon neutral")
elif fortune == 1:
    print("You have rice in your teeth")
elif fortune == 2:
    print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
    print("You can only connect the dots looking backwards")
elif fortune == 4:
    print("The fortune you seek is in another cookie")

# Who Wants To Be A Millionaire 💰

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = "LBJ"
option4 = 'A&W'

print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)

answer = 'a'

if answer == 'A' or answer == 'a':
    score += 100
    print("\nCorrect!")
else:
    print("\nNope, sorry!")

# Area Calculator 📏


base = 20
height = 30
area = base * height / 2

print("The triangle area is", area)

length = 2
width = 12
area = length * width

print("The rectangle area is", area)

radius = 36
area = math.pi * radius * radius

print("The circle area is", area)

# There is also another type of error that doesn’t have error messages that we will cover down the line:

# Logic errors: Errors found by the programmer when the program isn’t doing what it is intending to do.
