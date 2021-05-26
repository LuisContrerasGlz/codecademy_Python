# A dictionary is an unordered set of key: value pairs.
# It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

# Suppose we want to store the prices of various items sold at a cafe:
# Avocado Toast is 6 dollars
# Carrot Juice is 5 dollars
# Blueberry Muffin is 2 dollars

# In Python, we can create a dictionary called menu to store this data:
menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Notice that:
# A dictionary begins and ends with curly braces { and }.
# Each item consists of a key ("avocado toast") and a value (6).
# Each key: value pair is separated by a comma.
# It’s considered good practice to insert a space () after each comma, but our code will still run without the space.

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)

# In dictionaries the keys can be numbers as well.

# For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

# Values can be of any type.
# We can use a string, a number, a list, or even another dictionary as the value associated with a key!

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": [
    "Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

# The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in that class.
# We can also mix and match key and value types. For example:

person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

translations = {"mountain": "orod", "bread": "bass",
                "friend": "mellon", "horse": "roch"}

# We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary.
# If we try to, we will get a TypeError.

# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} will get TypeError: unhashable type: 'list'
# The word “unhashable” in this context means that this ‘list’ is an object that can be changed.
# Dictionaries in Python rely on each key having a hash value, a specific identifier for the key.
# If the key can change, that hash value would not be reliable.
# So the keys must always be unchangeable, hashable data types, like numbers or strings.

children = {"von Trapp": ["Johannes", "Rosmarie",
                          "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# A dictionary doesn’t have to contain anything. Sometimes we need to create an empty dictionary when we plan to fill it later based on some other input.

empty_dict = {}

my_empty_dictionary = {}

# To add a single key: value pair to a dictionary, we can use the syntax:
# dictionary[key] = value

menu = {"oatmeal": 3, "avocado toast": 6,
        "carrot juice": 5, "blueberry muffin": 2}

# Add a new key:

menu["cheesecake"] = 8

# Now, menu looks like: {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)

# If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

# dd all three items to the sensors dictionary.
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Now, sensors looks like:
# {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# We know that we can add a key by using syntax like:
menu["avocado toast"] = 7

# This will create a key "avocado toast" and set the value to 7.
# But what if we already have an 'avocado toast' entry in the menu dictionary?
# In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.

menu = {"oatmeal": 3, "avocado toast": 6,
        "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
# Output: {"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

# Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# Python allows you to create a dictionary using a list comprehension, with this syntax:

students = {key: value for key, value in zip(names, heights)}
# students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:

# Takes a pair from the zipped list of pairs from names and heights
# Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# Creates a key : value item in the students dictionary
# Repeats steps 1-3 for the entire list of pairs

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# Once you have a dictionary, you can access the values in it by providing the key.

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
                    "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Then we can access the data in it like this:
# >>> building_heights["Burj Khalifa"]
# 828
# >>> building_heights["Ping An"]
# 599

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": [
    "Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])
print(zodiac_elements['fire'])

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
                    "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

print(building_heights["Landmark 81"])

# "Landmark 81" does not exist as a key in the building_heights dictionary! So this will throw a KeyError:
# KeyError: 'Landmark 81'

# One way to avoid this error is to first check if the key exists in the dictionary:

key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights["Landmark 81"])

# This will not throw an error, because key_to_check in building_heights will return False, and so we never try to access the key.

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": [
    "Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}

print(zodiac_elements["energy"])


# We saw that we can avoid KeyErrors by checking if a key is in a dictionary first.
# Another method we could use is a try/except:

key_to_check = "Landmark 81"
try:
    print(building_heights[key_to_check])
except KeyError:
    print("That key doesn't exist!")

# When we try to access a key that doesn’t exist, the program will go into the except block and print "That key doesn't exist!".

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30

try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")
