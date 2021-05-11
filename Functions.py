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
