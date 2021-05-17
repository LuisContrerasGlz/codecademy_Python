# Words and sentences are fundamental to how we communicate, so it follows that we’d want our computers to be able to work with words and sentences as well.
# In Python, the way we store something like a word, a sentence, or even a whole paragraph is as a string.
# A string is a sequence of characters contained within a pair of 'single quotes' or "double quotes".
# A string can be any length and can contain any letters, numbers, symbols, and spaces.

favorite_word = "UFC"
print(favorite_word)

# A string can be thought of as a list of characters.
# Like any other list, each character in a string has an index.

favorite_fruit = "blueberry"

# We can select specific letters from this string using the index.

print(favorite_fruit[1])
# Output: l

# Whoops, is that the first letter you expected? Notice that the letter at index 1 of "blueberry" isn’t b, it’s l.
# This is because the indices of a string start at 0. b is located at the zero index and we could select it using:

print(favorite_fruit[0])
# Output: b

# It’s important to note that indices of strings must be integers. If we were to try to select a non-integer index we would get a TypeError.

print(favorite_fruit[1.5])

my_name = "Luis"
first_initial = my_name[0]

# Not only can we select a single character from a string, but we can also select entire chunks of characters from a string. We can do this with the following syntax:
# string[first_index:last_index]
# This is called slicing a string.
# When we slice a string we are creating a brand new string that starts at (and includes) the first_index and ends at (but excludes) the last_index.

favorite_fruit = "blueberry"

print(favorite_fruit[4:6])
# Output: be

# We can also have open-ended selections.
# If we remove the first index, the slice starts at the beginning of the string and if we remove the second index the slice continues to the end of the string.

print(favorite_fruit[:4])
# Output: blue

print(favorite_fruit[4:])
# Output: berry

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

# We can also concatenate, or combine, two existing strings together into a new string.

fruit_prefix = "blue"
fruit_suffix = "berries"

favorite_fruit = fruit_prefix + fruit_suffix

print(favorite_fruit)
# Output: blueberries

# We have to manually add in the spaces when concatenating strings if we want to include them.

fruit_sentence = "My favorite fruit is" + favorite_fruit

print(fruit_sentence)
# Output: My favorite fruit isblueberries

fruit_sentence = "My favorite fruit is " + favorite_fruit

print(fruit_sentence)
# Output: My favorite fruit is blueberries

first_name = "Julie"
last_name = "Blevins"


def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]


new_account = account_generator("Luis", "Contreras")
print(new_account)

# Python comes with some built-in functions for working with strings.
# One of the most commonly used of these functions is len().
# len() returns the number of characters in a string:

favorite_fruit = "blueberry"

length = len(favorite_fruit)

print(length)
# Output: 9

# If you are taking the length of a sentence the spaces are counted as well.

fruit_sentence = "I love blueberries"

print(len(fruit_sentence))
# Output: 18

# len() comes in handy when we are trying to select characters from the end of a string.
# What is the index of the last character,"y", of favorite_fruit from above? You can try to run the following code:

last_char = favorite_fruit[len(favorite_fruit)]

print(last_char)

# This will result in:
# IndexError: string index out of range, Why does this generate an IndexError?
# Because the indices start at 0, so the final character in favorite_fruit has an index of 8.
# len(favorite_fruit) returns 9 and, because there is no value at that index, an IndexError occurs.
# Instead, the last character in a string has an index that is len(string_name) - 1.

last_char = favorite_fruit[len(favorite_fruit)-1]

print(last_char)
# Output: y

# You could also slice the last several characters of a string using len():

length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)
# Output: erry
# Using a len() statement as the starting index and omitting the final index lets you slice n characters from the end of a string, where n is the amount you subtract from len().

first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    temp_password = first_name[len(first_name)-3:] + \
        last_name[len(last_name)-3:]
    return temp_password


temp_password = password_generator(first_name, last_name)
