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

# In Python, for loops are not the only type of loops we can use.
# Another type of loop is called a while loop and is a form of indefinite iteration.
# A while loop performs a set of instructions as long as a given condition is true.

# The structure follows this pattern:

# while <conditional statement>:
#  <action>

count = 0
while count <= 3:
    # Loop Body
    print(count)
    count += 1

# Notice that in our example the code under the loop declaration is indented.
# Similar to a for loop, everything at the same level of indentation after the while loop declaration is run on every iteration of the loop while the condition is true.

while count <= 3:
    # Loop Body
    print(count)
    count += 1
    # Any other code at this level of indentation will
    # run on each iteration

# If we ever forget to indent, we’ll get an IndentationError or unexpected behavior.

# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
    # Loop Body
    # Print if the condition is still true
    print("Loop Iteration - count <= 3 is still true")
    # Print the current value of count
    print("Count is currently " + str(count))
    # Increment count
    count += 1
    print(" ----- ")
print("While Loop ended")

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1

print("We have liftoff!")

# A while loop isn’t only good for counting! Similar to how we saw for loops working with lists, we can use while loops to iterate through a list as well.

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# We know that a list has a predetermined length.
# If we use the length of the list as the basis for how long our while loop needs to run, we can iterate the exact length of the list.

# We can use the built-in Python len() function to accomplish this:

# Length would be equal to 5
length = len(ingredients)

# We can then use this length in addition to another variable to construct the while loop:

length = len(ingredients)
index = 0

while index < length:
    print(ingredients[index])
    index += 1

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1

# A loop that never terminates is called an infinite loop.
# These are very dangerous for our code because they will make our program run forever and thus consume all of your computer’s resources.
# A program that hits an infinite loop often becomes completely unusable.
# The best course of action is to avoid writing an infinite loop.

# my_favorite_numbers = [4, 8, 15, 16, 42]

# for number in my_favorite_numbers:
#   my_favorite_numbers.append(1)

items_on_sale = ["blue shirt", "striped socks",
                 "knit dress", "red headband", "dinosaur onesie"]

# What does our loop look like if we want to search for the value of "knit dress" and print out "Found it" if it did exist?

for item in items_on_sale:
    if item == "knit dress":
        print("Found it")

items_on_sale = ["blue shirt", "striped socks",
                 "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
    print(item)
    if item == "knit dress":
        break

print("End of search!")

dog_breeds_available_for_adoption = [
    "french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

# While the break control statement will come in handy, there are other situations where we don’t want to end the loop entirely.

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
    if i <= 0:
        continue
    print(i)

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
    if i < 21:
        continue
    print(i)
