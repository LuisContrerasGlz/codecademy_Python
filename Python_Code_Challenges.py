# Create a function named every_other_letter that takes a string named word as a parameter.
# The function should return a string containing every other letter in word.

def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other
