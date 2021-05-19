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

# .upper(), .lower(), and .title() all are performed on an existing string and produce a string in return.
# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of .split() is known as the delimiter).

# string_name.split(delimiter) If you do not provide an argument for .split() it will default to splitting at spaces.

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

# .split returned a list with each word in the string. Important to note: if we run .split() on a string with no spaces, we will get the same string in return.

line_one = "The sky has given over"
line_one_words = line_one.split()

# If we provide an argument for .split() we can dictate the character we want our string to be split on.
# This argument should be provided as a string itself.

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a']

# We provided 'n' as the argument for .split() so our string “santana” got split at each 'n' character into a list of three strings.

print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', ' ']
# When you split a string on a character that it also ends with, you’ll end up with an empty string at the end of the list.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# We can also split strings using escape sequences.
# Escape sequences are used to indicate that we want to split by something in a string that is not necessarily a character.
# The two escape sequences we will cover here are: \n Newline \t Horizontal Tab

# Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by tabs.
# \t is particularly useful when dealing with certain datasets because it is not uncommon for data points to be separated by tabs.

smooth_chorus = \
    """And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)

spring_storm_text = \
    """The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

# Now that you’ve learned to break strings apart using .split(), let’s learn to put them back together using .join().
# .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.
# 'delimiter'.join(list_you_want_to_join)
# The string .join() acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
# We take the list of strings, my_munequita, and we joined it together with our delimiter, ' ', which is a space. The space is important if you are trying to build a sentence from words, otherwise, we would have ended up with:

print(''.join(my_munequita))
# => 'MySpanishHarlemMonaLisa'

reapers_line_one_words = ["Black", "reapers", "with",
                          "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)

# In fact, you can use any string as a delimiter to join together a list of strings.

santana_songs = ['Oye Como Va', 'Smooth',
                 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']

# One often used string is a comma , because then we can create a string of comma separated variables, or CSV.

santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# You’ll often find data stored in CSVs because it is an efficient, simple file type used by popular programs like Excel or Google Spreadsheets.

# You can also join using escape sequences as the delimiter.

smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio',
                            'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among',
                      'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)

# When working with strings that come from real data, you will often find that the strings aren’t super clean.
# You’ll find lots of extra whitespace, unnecessary linebreaks, and rogue tabs.

# Python provides a great method for cleaning strings: .strip().
# Stripping a string removes all whitespace characters from the beginning and end.

featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'
# All the whitespace on either side of the string has been stripped, but the whitespace in the middle has been preserved.

# You can also use .strip() with a character argument, which will strip that character from either end of the string.
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '
# By including the argument '!' we are able to strip all of the ! characters from either side of the string.
# Notice that now that we’ve included an argument we are no longer stripping whitespace, we are ONLY stripping the argument.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ',
                    'you lay down your arms', '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)
