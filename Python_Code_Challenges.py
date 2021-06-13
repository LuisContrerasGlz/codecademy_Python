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
