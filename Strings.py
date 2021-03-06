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

# We used len() to get a slice of characters at the end of a string.
# There’s a much easier way to do this — we can use negative indices!
# Negative indices count backward from the end of the string, so string_name[-1] is the last character of the string, string_name[-2] is the second last character of the string, etc.

favorite_fruit = 'blueberry'
print(favorite_fruit[-1])
# => 'y'

print(favorite_fruit[-2])
# => 'r'

print(favorite_fruit[-3:])
# => 'rry' we are able to slice the last three characters of ‘blueberry’ by having a starting index of -3 and omitting a final index.

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# We’ve been selecting characters from strings, slicing strings, and concatenating strings.
# Each time we perform one of these operations we are creating an entirely new string.
# This is because strings are immutable.
# This means that we cannot change a string once it is created.
# We can use it to create other strings, but we cannot change the string itself.
# This property, generally, is known as mutability.
# Data types that are mutable can be changed, and data types, like strings, that are immutable cannot be changed.

first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"

fixed_first_name = "R" + first_name[1:]

# Occasionally when working with strings, you’ll find that you want to include characters that already have a special meaning in python.
# For example let’s say I create the string

# favorite_fruit_conversation = "He said, "blueberries are my favorite!""

# We’ll have accidentally ended the string before we wanted to by including the " character.
# The way we can do this is by introducing escape characters.
# By adding a backslash in front of the special character we want to escape, \", we can include it in a string.

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

password = "theycallme\"crazy\"91"

# Because strings are lists, that means we can iterate through a string using for or while loops.
# This opens up a whole range of possibilities of ways we can manipulate and analyze strings.


def print_each_letter(word):
    for letter in word:
        print(letter)


favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'


def get_length(word):
    numberChar = 0
    for letter in word:
        numberChar += 1
    return numberChar

# When we iterate through a string we do something with each character.
# By including conditional statements inside of these iterations, we can start to do some really cool stuff.


favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1
print(counter)

# First, we define our string, favorite_fruit, and a variable called counter, which we set equal to zero.
# Then the for loop will iterate through each character in favorite_fruit and compare it to the letter b.
# Each time a character equals b the code will increase the variable counter by one.
# Then, once all characters have been checked, the code will print the counter, telling us how many bs were in “blueberry”.
# This is a great example of how iterating through a string can be used to solve a specific application, in this case counting a certain letter in a word.


def letter_check(word, letter):
    for character in word:
        if character == letter:
            return True
    return False

# There’s an even easier way than iterating through the entire string to determine if a character is in a string.
# We can do this type of check more efficiently using in. in checks if one string is part of another string.

# E.G letter in word
# Here, letter in word is a boolean expression that is True if the string letter is in the string word.


print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

# In fact, this method is more powerful than the function in the last exercise because it not only works with letters, but with entire strings as well.

print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False


def contains(big_string, little_string):
    return little_string in big_string


def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
