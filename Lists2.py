# We will start to explore additional ways of working with lists like:

# Add and remove items from a list using a specific index.
# Create lists with continuous values.
# Get the length of a list.
# Select portions of a list (called slicing).
# Count the number of times that an element appears in a list.
# Sort a list of items.

# The Python list method .insert() allows us to add an element to a specific index in a list.
# The .insert() method takes in two inputs:

# The index you want to insert into.
# The element you want to insert at the specified index.
# The .insert() method will handle shifting over elements and can be used with negative indices.

store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
# Would output:  ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
print(store_line)

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below:

front_display_list.insert(0, "Pineapple")
print(front_display_list)
