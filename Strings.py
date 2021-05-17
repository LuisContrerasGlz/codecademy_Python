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
