# What is a List?
# In programming, it is common to want to work with collections of data.
# In Python, a list is one of the many built-in data structures that allows us to work with a collection of data in sequential order.

heights = [61, 70, 67, 64]

ints_and_strings = [1, 2, 3, "four", "five", "Cool"]
sam_height_and_testscore = ["Sam", 67, 85.5,  True]

# Empty Lists
# A list doesn’t have to contain anything. You can create an empty list like this:

empty_list = []

# Usually, it’s because we’re planning on filling it up later based on some other input.

# In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data.
# We call this built-in functionality a method.

# For lists, methods will follow the form of list_name.method().
# Some methods will require an input value that will go between the parenthesis of the method ( ).

# An example of a popular list method is .append(), which allows us to add an element to the end of a list.

append_example = ['This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)

# Will output: ['This', 'is', 'an', 'example', 'list']

example_list = [1, 2, 3, 4]

# Using Append
example_list.append(5)
# print(example_list)

# Using Remove
example_list.remove(5)
# print(example_list)

# We can add a single element to a list using the .append() Python method.
# Suppose we have an empty list called garden:

garden = []

# We can add the element "Tomatoes" by using the .append() method:
garden.append("Tomatoes")

print(garden)

# Will output:['Tomatoes']

# When we use .append() on a list that already has elements, our new element is added to the end of the list.

orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)

# When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
# We can only use + with other lists.
# If we want to add a single element using +, we have to put it into a list with brackets ([])

my_list = [1, 2, 3]
my_list + [4]

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders


broken_prices = [5, 3, 4, 5, 4] + [4]
