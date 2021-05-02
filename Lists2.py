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

data_science_topics.pop()

data_science_topics.pop(3)
print(data_science_topics)

# Often, we want to create a list of consecutive numbers in our programs.
# Suppose we want a list containing the numbers 0 through 9:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Python gives us an easy way of creating these types of lists using a built-in function called range().
# The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.
# So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

my_range = range(10)
print(my_range)  # Would output: range(0, 10)

# The range() function is unique in that it creates a range object.
# It is not a typical list like the ones we have been working with.
# In order to use this object as a list, we have to first convert it using another built-in function called list().
# The list() function takes in a single input for the object you want to convert.
# We use the list() function on our range object like this:

print(list(my_range))  # Would output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# By default, range() creates a list starting at 0.
# However, if we call range() with two inputs, we can create a list that starts at a different number.

# For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

my_list = range(2, 9)
print(list(my_list))  # Would output: [2, 3, 4, 5, 6, 7, 8]

# If we use a third input, we can create a list that “skips” numbers.
# For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

my_range2 = range(2, 9, 2)
print(list(my_range2))  # Would output: [2, 4, 6, 8]

range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)

# Often, we’ll need to find the number of items in a list, usually called its length.
# We can do this using a built-in function called len().
# When we apply len() to a list, we get the number of elements in that list:

my_list = [1, 2, 3, 4, 5]

print(len(my_list))  # Would output: 5

# Range objects do not need to be converted to lists in order to determine their length

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that",
             "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list = range(2, 3000, 100)

long_list_len = len(long_list)
print(long_list_len)

range_list_length = len(range_list)
print(range_list_length)
