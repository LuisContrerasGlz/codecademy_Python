# Create a function named every_other_letter that takes a string named word as a parameter.
# The function should return a string containing every other letter in word.

def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

# Write a function named reverse_string that has a string named word as a parameter.
# The function should return word in reverse.


def reverse_string(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse

# Create a function named add_exclamation that has one parameter named word.
# This function should add exclamation points to the end of word until word is 20 characters long.
# If word is already at least 20 characters long, just return word.


def add_exclamation(word):
    while(len(word) < 20):
        word += "!"
    return word


print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

# A function that counts the number of values in a dictionary that are above a given number


def greater_than_ten(my_dictionary, number):
    count = 0
    for value in my_dictionary.values():
        if value > number:
            count += 1
    return count

# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
# The function should return the sum of the values of the dictionary


def sum_values(my_dictionary):
    total = 0
    for value in my_dictionary.values():
        total += value
    return total


print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter.
# This function should return the sum of the values of all even keys.


def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            total += my_dictionary[key]
    return total


print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
# This function should return a list of all values in the dictionary that are also keys.


def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys


print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]

# A function that counts the number of values in a dictionary that are above a given number


def greater_than_ten(my_dictionary, number):
    count = 0
    for value in my_dictionary.values():
        if value > number:
            count += 1
    return count

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter.
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.


def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths

# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter.
# The function should return the number of unique values in the dictionary.


def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)
