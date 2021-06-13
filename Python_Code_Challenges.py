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
