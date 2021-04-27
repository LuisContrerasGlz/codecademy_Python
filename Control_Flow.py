# Learn how to build control flow into your python code by including if, else, and elif statements as well as try and except statements.
# Expect to learn all you need to know about boolean variables and logical operators.

# In order to build control flow into our program, we want to be able to check if something is true or not. A boolean expression is a statement that can either be True or False.

# "Dogs are mammals"
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
