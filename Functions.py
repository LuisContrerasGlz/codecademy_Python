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

# In Python, there are 3 different types of arguments we can give a function.

# Positional arguments: arguments that can be called by their position in the function definition.
# Keyword arguments: arguments that can be called by their name.
# Default arguments: arguments that are given default values.

# Positional Arguments are arguments we have already been using! Their assignments depend on their positions in the function call.


def calculate_taxi_price(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount)

# Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.


calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

# Lastly, sometimes we want to give our function arguments default values. We can provide a default value to an argument by using the assignment operator (=). This will happen in the function declaration rather than the function call.


def calculate_taxi_price(miles_to_travel, rate, discount=10):
    print(miles_to_travel * rate - discount)

# When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:


# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)


def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in " + first_destination, "then" +
          second_destination, "and lastly " + final_destination)


trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland",
             final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")

# There are two distinct categories for functions in the world of Python.
# What we have been writing so far in our exercises are called User Defined Functions - functions that are written by users.

# There is another category called Built-in functions - functions that come built into Python for us to use.

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# There are even more obscure ones like help() where Python will print a link to documentation for us and provide some details:
help("string")

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)

print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)

print(min_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)

# As we expand our programs with more functions, we might start to ponder, where exactly do we have access to our variables?

# To examine this, let’s revisit a modified version of the first function we built out together:


def trip_welcome(destination):
    print(" Looks like you're going to the " + destination + " today. ")

# What if we wanted to access the variable destination outside of the function? Could we use it?


def trip_welcome(destination):
    print(" Looks like you're going to the " + destination + " today. ")


print(destination)

# We call the part of a program where destination can be accessed its scope. The scope of destination is only inside the trip_welcome().
# If a variable lives outside of any function it can be accessed anywhere in the file.

favorite_locations = "Paris, Norway, Iceland"
# This function will print a hardcoded count of how many locations we have.


def print_count_locations():
    print("There are 3 locations")

# This function will print the favorite locations


def show_favorite_locations():
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations()

# At this point, our functions have been using print() to help us visualize the output in our interpreter.
# Functions can also return a value to the program so that this value can be modified or used later.
# We use the Python keyword return to do this.


def calculate_exchange_usd(us_dollars, exchange_rate):
    return us_dollars * exchange_rate


new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " +
      str(new_zealand_exchange) + " New Zealand dollars")

# Saving our values returned from a function like we did with new_zealand_exchange allows us to reuse the value (in the form of a variable) throughout the rest of the program.
# When there is a result from a function that is stored in a variable, it is called a returned function value.

current_budget = 3500.75
shirt_expense = 9


def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))


print_remaining_budget(current_budget)


def deduct_expense(budget, expense):
    return budget - expense


new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

# Sometimes we may want to return more than one value from a function.
# We can return several values by separating them with a comma.

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']


def threeday_weather_report(weather):
    first_day = " Tomorrow the weather will be " + weather[0]
    second_day = " The following day it will be " + weather[1]
    third_day = " Two days from now it will be " + weather[2]
    return first_day, second_day, third_day


monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)


def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)
