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

# In Python, often we want to extract only a portion of a list.
# Dividing a list in such a manner is referred to as slicing.

letters = ["a", "b", "c", "d", "e", "f", "g"]

# Suppose we want to select from "b" through "f"
# We can do this using the following syntax: letters[start:end], where:
# start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
# end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.

sliced_list = letters[1:6]
print(sliced_list)  # Would output: ["b", "c", "d", "e", "f"]

# Notice that the element at index 6 (which is "g") is not included in our selection.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

print(beginning)

middle = suitcase[2:4]

# Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing.
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]

# If we want to select the first n elements of a list, we could use the following code:
fruits[:n]

# The following code would start slicing from index 0 and up to index 3. Note that the fruit at index 3 (orange) is not included in the results.

print(fruits[:3])  # Would output: ['apple', 'cherry', 'pineapple']

# We can do something similar when we want to slice the last n elements in a list:
fruits[-n:]

# This code slices from the element at index -2 up through the last index.
print(fruits[-2:])  # Would output: ['orange', 'mango']

# Negative indices can also accomplish taking all but n last elements of a list.

fruits[:-n]

# This example starts counting from the 0 index up to the element at index -1
print(fruits[:-1])  # Would output: ['apple', 'cherry', 'pineapple', 'orange']

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# In Python, it is common to want to count occurrences of an item in a list.

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]

# If we want to know how many times i appears in this word, we can use the list method called .count():
num_i = letters.count("i")
print(num_i)  # Would output: 4

# Notice that since .count() returns a value, we must assign it to a variable to use it.
# We can even use .count() to count element appearances in a two-dimensional list.

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

# If we wanted to know how often the sublist [100, 200] appears:

num_pairs = number_collection.count([100, 200])
print(num_pairs)  # Would output: 2

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie",
         "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)

# Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.
# We can sort a list using the method .sort().

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

names.sort()
print(names)  # Would output: ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

# As we can see, the .sort() method sorted our list of names in alphabetical order.
# .sort() also provides us the option to go in reverse.
# Instead of sorting in ascending order like we just saw, we can do so in descending order.

names.sort(reverse=True)
print(names)  # Would output: ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

# Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly.
# If we do assign the result of the method, it would assign the value of None to the variable.

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place",
             "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses)

names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)

# A second way of sorting a list in Python is to use the built-in function sorted().
# The sorted() function is different from the .sort() method in two ways:
# It comes before a list, instead of after as all built-in functions do.
# It generates a new list rather than modifying the one that already exists.

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

# Using sorted(), we can create a new list, called sorted_names:

sorted_names = sorted(names)
print(sorted_names)

# This yields the list sorted alphabetically:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)

print(games)
print(games_sorted)
