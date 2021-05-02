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

# Python gives us a method to remove elements at a specific index using a method called .pop().
# The .pop() method takes an optional single input: The index for the element you want to remove.

cs_topics = ["Python", "Data Structures",
             "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop()

# Would output: ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is.
# .pop() is unique in that it will return the value that was removed. If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method.

cs_topics.pop(2)

# Would output: ['Python', 'Data Structures', 'Algorithms']
# The method can be called with an optional specific index to remove. In our case, the index 2 removes the value of "Balloon Making".
# We don’t have to save the removed value to any variable if we don’t care to use it later.
# Note: Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError.

data_science_topics = ["Machine Learning", "SQL",
                       "Pandas", "Algorithms", "Statistics", "Python 3"]


# Your code below:
data_science_topics.pop()


data_science_topics.pop(3)
print(data_science_topics)
