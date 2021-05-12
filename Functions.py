# In programming, as we start to write bigger and more complex programs, one thing we will start to notice is we will often have to repeat the same set of steps in many different places in our program.
#  1. Establish your origin and destination
#  2. Calculate the distance/route
#  3. Return the best route to the user

# We will perform these three steps every time users have to travel between two points using our trip application.
# In our programs, we could rewrite the same procedures over and over (and over) for each time we want to travel, but there’s a better way! Python gives us a useful concept called functions.
# Functions are a convenient way to group our code into reusable blocks.
# A function contains a sequence of steps that can be performed repeatedly throughout a program without having to repeat the process of writing the same code again.

# If we were to convert our steps into Python code, a very simple version that plans a trip between two popular New York tourist destinations might look like this:

print("Setting the Empire State Building as the starting point and Time Square as our destination.")

print("Calculating the total distance between our points.")

print("The best route is by train and will take approximately 10 minutes.")

# First user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Time Square as our destination.")
print("Calculating the total distance between our points.")
print("The best route is by train and will take approximately 10 minutes.")

# Second user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Time Square as our destination.")
print("Calculating the total distance between our points.")
print("The best route is by train and will take approximately 10 minutes.")


# Third user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Time Square as our destination.")
print("Calculating the total distance between our points.")
print("The best route is by train and will take approximately 10 minutes.")

# Fourth user wants to travel between these two points!

print("Setting the Empire State Building as the starting point and Time Square as our destination.")
print("Calculating the total distance between our points.")
print("The best route is by train and will take approximately 10 minutes.")

# A function consists of many parts, so let’s first get familiar with its core - a function definition.


def function_name():
  # functions tasks go here

    # The def keyword indicates the beginning of a function (also known as a function header).
    # The function header is followed by a name in snake_case format that describes the task the function performs.
    # It’s best practice to give your functions a descriptive yet concise name.

    # Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters.
    # In this example function, we have no parameters.

    # A colon : to mark the end of the function header.

    # Lastly, we have one or more valid python statements that make up the function body
    # Like loops and conditionals, code inside a function must be indented to show that they are part of the function.


def trip_welcome():
    print("Welcome to Tripcademy!")
    print("Let's get you to your destination.")


def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")

# The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”).
# To call a function in Python, type out its name followed by parentheses ( ).


directions_to_timesSq()

# Calling the function will execute the print statements within the body (from the top statement to the bottom statement)
