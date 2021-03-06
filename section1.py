# First section of Python program codecademy

my_name = "Luis Contreras"
print("Hello and welcome " + my_name + "!")
print('Luis Contreras')

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "Lunch"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Dinner:")
print(meal)

# You might encounter a SyntaxError if you open a string with double quotes and end it with a single quote. Update the string so that it starts and ends with the same punctuation.

# You might encounter a NameError if you try to print a single word string but fail to put any quotes around it. Python expects the word of your string to be defined elsewhere but can’t find where it’s defined. Add quotes to either side of the string to squash this bug.

# Update the malformed strings in the workspace to all be strings.

print("This message has mismatched quote marks!")
print("Abracadabra")

# Define the release and runtime integer variables below:
release_year = 2019
runtime = 150


# Define the rating_out_of_10 float variable below:
rating_out_of_10 = 9.5

# Print out the result of this equation: 25 * 68 + 13 / 28
print(25 * 68 + 13 / 28)

# You’ve decided to get into quilting!
# To calculate the number of squares you’ll need for your first quilt let’s create two variables: quilt_width and quilt_length.
# Let’s make this first quilt 8 squares wide and 12 squares long.

quilt_width = 8
quilt_length = 12

# Print out the number of squares you’ll need to create the quilt!

print(quilt_width * quilt_length)

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)

# 7x7 quilt
print(7 ** 2)

# 8x8 quilt
print(8 ** 2)

# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 4)

# The modulo operator is useful in programming when we want to perform an action every nth-time the code is run.
# Can the result of a modulo operation be larger than the divisor? Why or why not?

# You’re trying to divide a group into four teams. All of you count off, and you get number 27.

# Find out your team by computing 27 modulo 4. Save the value to my_team.

my_team = 27 % 4

# Print out my_team. What number team are you on?

print(my_team)

# If you want to concatenate a string with a number you will need to make the number a string first, using the str() function.
# If you’re trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.
# Using str() we can convert variables that are not strings to strings and then concatenate them.
# But we don’t need to convert a number to a string for it to be an argument to a print statement.

# Concatenate the strings and save the message they form in the variable message.
# Now uncomment the print statement and run your code to see the result in the terminal!

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

print(message)

# Python offers a shorthand for updating variables. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.
# The plus-equals operator also can be used for string concatenation

# We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

# Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.

# The prices (also included in the workspace) are:

# new_sneakers = 50.00
# nice_sweater = 39.00
# fun_books = 20.00

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater
total_price += fun_books

print("The total price is", total_price)

# Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError.
# Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote.
# This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.
# If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.

# Assign the string here
to_you = """ Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you? """


print(to_you)

# We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street.
# With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.
# In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. """

lovely_loveseat_price = 254.00

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

stylish_settee_price = 180.50

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. """

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization = "lovely_loveseat"

customer_one_total += luxurious_lamp_price

customer_one_itemization = "lovely_loveseat, luxurious_lamp"

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print(customer_one_itemization)
print(customer_one_total)

# So far, we’ve covered how to assign variables values directly in a Python file. However, we often want a user of a program to enter new information into the program.

# How can we do this? As it turns out, another way to assign a value to a variable is through user input.

# While we output a variable’s value using print(), we assign information to a variable using input().
# The input() function requires a prompt message, which it will print out for the user before they enter the new information.
# For example:

likes_snakes = input("Do you like snakes? ")

# In the example above, the following would occur:

# The program would print "Do you like snakes? " for the user.
# The user would enter an answer (e.g., "Yes! I have seven pythons as pets!") and press enter.
# The variable likes_snakes would be assigned a value of the user’s answer.

# Not only can input() be used for collecting all sorts of different information from a user, but once you have that information stored as a variable you can use it to simulate interaction:

favorite_fruit = input("What is your favorite fruit? ")
# What is your favorite fruit? mango

print("Oh cool! I like " + favorite_fruit +
      " too, but I think my favorite fruit is apple.")
# Oh yeah! I like mango too, but I think my favorite fruit is apple.
