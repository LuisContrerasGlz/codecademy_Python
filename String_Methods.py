# Do you have a gigantic string that you need to parse for information?
# Do you need to sanitize a users input to work in a function?
# Do you need to be able to generate outputs with variable values?
# All of these things can be accomplished with string methods!

# Python comes with built-in string methods that gives you the power to perform complicated tasks on strings very quickly and efficiently.
# These string methods allow you to change the case of a string, split a string into many smaller strings,
# join many small strings together into a larger string, and allow you to neatly combine changing variables with string outputs.

# string_name.string_method(arguments) a string method is called at the end of a string and each one has its own method specific arguments.

# There are three string methods that can change the casing of a string.
# These are .lower(), .upper(), and .title().

# .lower() returns the string with all lowercase characters.
# .upper() returns the string with all uppercase characters.
# .title() returns the string in title case, which means the first letter of each word is capitalized.

favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)
# => 'smooth'
# It’s important to remember that string methods can only create new strings, they do not change the original string.

print(favorite_song)
# => 'SmOoTH'

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author)
print(poem_author_fixed)
