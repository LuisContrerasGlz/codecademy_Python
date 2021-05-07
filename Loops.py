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
