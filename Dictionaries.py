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
