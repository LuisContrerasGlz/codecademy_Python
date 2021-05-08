# In programming, the process of using an initialization, repetitions, and an ending condition is called a loop.
# In a loop, we perform a process of iteration (repeating tasks).

# Programming languages like Python implement two types of iteration:

# Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.
# Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).
# Typically we will find loops being used to iterate a collection of items.

# Let’s say we have a list of ingredients and we want to print every element in the list:
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# If we only use print(), our program might look like this:

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

# The output would be:
# milk
# sugar
# vanilla extract
# dough
# chocolate

# That’s still manageable, We’re writing 5 print() statements (or copying and pasting a few times).
# Now imagine if we come back to this program and our list had 10, or 24601, or … 100,000,000 elements?
# It would take an extremely long time and by the end, we could still end up with inconsistencies and mistakes.

# Let’s start with your first type of loop, a for loop, a type of definite iteration.
# In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length.
# With for loops, on each iteration, we will be able to perform an action on each element of the collection.

# for <temporary variable> in <collection>:
#     <action>

# A for keyword indicates the start of a for loop.
# A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
# An in keyword separates the temporary variable from the collection used for iteration.
# A <collection> to loop over.
# An <action> to do anything on each iteration of the loop.

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for ingredient in ingredients:
    print(ingredient)

# ingredient is the <temporary variable>.
# ingredients is our <collection>.
# print(ingredient) was the <action> performed on every iteration using the temporary variable of ingredient.
# A temporary variable’s name is arbitrary and does not need to be defined beforehand.

for i in ingredients:
    print(i)

for item in ingredients:
    print(item)

# Notice that in all of these examples the print statement is indented.
# Everything at the same level of indentation after the for loop declaration is included in the loop body and is run on every iteration of the loop.

for ingredient in ingredients:
    # Any code at this level of indentation
    # will run on each iteration of the loop
    print(ingredient)

# If we ever forget to indent, we’ll get an IndentationError or unexpected behavior.

board_games = ["Settlers of Catan", "Carcassone",
               "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)

for sportg in sport_games:
    print(sportg)

# Often we won’t be iterating through a specific list (or any collection), but rather only want to perform a certain action multiple times.
# For example, if we wanted to print out a "Learning Loops!" message six times using a for loop, we would follow this structure:

# for <temporary variable> in <list of length 6>:
#   print("Learning Loops!")

# Notice that we need to iterate through a list with a length of six, but we don’t necessarily care what is inside of the list.
# To create arbitrary collections of any length, we can pair our for loops with the trusty Python built-in function range()

six_steps = range(6)

# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5

# We can then use the range directly in our for loops as the collection to perform a six-step iteration:

for temp in range(6):
    print("Learning Loops!")

# Would output:
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!

# Something to note is we are not using temp anywhere inside of the loop body.
# If we are curious about which loop iteration (step) we are on, we can use temp to track it.
# Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.

for temp in range(6):
    print("Loop is on iteration number " + str(temp + 1))

# Would output:

# Loop is on iteration number 1
# Loop is on iteration number 2
# Loop is on iteration number 3
# Loop is on iteration number 4
# Loop is on iteration number 5
# Loop is on iteration number 6

promise = "I will finish the python loops module!"

for temp in range(5):
    print(promise)
