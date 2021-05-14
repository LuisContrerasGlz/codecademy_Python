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

# In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function.
# The execution of a program always begins on the first line.
# The code is then executed one line at a time from top to bottom.
# This is known as execution flow and is the order a program in python executes code.

print("Checking the weather for you!")


def weather_check():
    print("Looks great outside! Enjoy your trip.")
    print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")


weather_check()


def trip_welcome():
    print("Welcome to Tripcademy!")
    print("Looks like you're going to Times Square today.")


trip_welcome()

# Function parameters allow our function to accept data as an input value.
# We list the parameters a function takes as input between the parentheses of a function ( ).


def my_function(single_parameter)  # function that defines a single parameter


def trip_welcome(destination):
    print("Welcome to Tripcademy!")
    print("Looks like you're going to " + destination + " today.")

# In the above example, we define a single parameter called destination and apply it in our function body in the second print statement.
# We are telling our function it should expect some data passed in for destination that it can apply to any statements in the function body.
# Our parameter of destination is used by passing in an argument to the function when we call it.


trip_welcome("Times Square")

# Would output:

# Welcome to Tripcademy!
# Looks like you're going to Times Square today.

# The parameter is the name defined in the parenthesis of the function and can be used in the function body.
# The argument is the data that is passed in when we call the function and assigned to the parameter name.


def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


generate_trip_instructions("Grand Central Station")

# Using a single parameter is useful but functions let us use as many parameters as we want! That way, we can pass in more than one input to our functions.
# We can write a function that takes in more than one parameter by using commas:


def my_function(parameter1, parameter2, parameter3):
  # Some code

    # When we call our function, we will need to provide arguments for each of the parameters we assigned in our function definition.


def trip_welcome(origin, destination):
    print("Welcome to Tripcademy")
    print("Looks like you are traveling from " + origin)
    print("And you are heading to " + destination)

# The ordering of your parameters is important as their position will map to the position of the arguments and will determine their assigned value in the function body


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print(car_rental_total + hotel_total + plane_ticket_price)


calculate_expenses(200, 100, 100, 5)
