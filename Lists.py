# What is a List?
# In programming, it is common to want to work with collections of data.
# In Python, a list is one of the many built-in data structures that allows us to work with a collection of data in sequential order.

heights = [61, 70, 67, 64]

ints_and_strings = [1, 2, 3, "four", "five", "Cool"]
sam_height_and_testscore = ["Sam", 67, 85.5,  True]

# Empty Lists
# A list doesn’t have to contain anything. You can create an empty list like this:

empty_list = []

# Usually, it’s because we’re planning on filling it up later based on some other input.

# In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data.
# We call this built-in functionality a method.

# For lists, methods will follow the form of list_name.method().
# Some methods will require an input value that will go between the parenthesis of the method ( ).

# An example of a popular list method is .append(), which allows us to add an element to the end of a list.

append_example = ['This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)

# Will output: ['This', 'is', 'an', 'example', 'list']

example_list = [1, 2, 3, 4]

# Using Append
example_list.append(5)
# print(example_list)

# Using Remove
example_list.remove(5)
# print(example_list)

# We can add a single element to a list using the .append() Python method.
# Suppose we have an empty list called garden:

garden = []

# We can add the element "Tomatoes" by using the .append() method:
garden.append("Tomatoes")

print(garden)

# Will output:['Tomatoes']

# When we use .append() on a list that already has elements, our new element is added to the end of the list.

orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)

# When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
# We can only use + with other lists.
# If we want to add a single element using +, we have to put it into a list with brackets ([])

my_list = [1, 2, 3]
my_list + [4]

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders


broken_prices = [5, 3, 4, 5, 4] + [4]

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]

print(employees[6])

# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]

# If we select the -1 index, we get the final element, "love".

print(pancake_recipe[-1])

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]

print(last_element)
print(index5_element)

# To change a value in a list, reassign the value using the specific index.

garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"

print(garden)

# Negative indices will work as well.
garden[-1] = "Raspberries"

print(garden)

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# We can remove elements in a list using the .remove() Python method.
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]

# We could remove "Chris" by using the .remove() method
shopping_line.remove("Chris")

print(shopping_line)

# We can also use .remove() on a list that has duplicate elements.
# Only the first instance of the matching element is removed:

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Remove a element
shopping_line.remove("Chris")
print(shopping_line)

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
new_store_order_list.remove("Mango")

print(new_store_order_list)

# Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.
# We will often find that a two-dimensional list is a very good structure for representing grids such as games like tic-tac-toe.

# A 2d list with three lists in each of the indices.
tic_tac_toe = [
    [["X"], ["O"], ["X"]],
    [["O"], ["X"], ["O"]],
    [["O"], ["O"], ["X"]]
]

heights = [["Jenny", 61], ["Alexus", 70], [
    "Sam", 67], ["Grace", 64], ["Vik", 68]]

ages = [["Aaron", 15], ["Dhruti", 16]]

class_name_test = [
    ["Jenny", 90],
    ["Alexus", 85.5],
    ["Sam", 83],
    ["Ellie", 101.5]
]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

incoming_class = [
    ["Kenny", "American", 9],
    ["Tanya", "Russian", 9],
    ["Madison", "Indian", 7]
]

incoming_class[2][2] = 8
incoming_class[-3][-3] = "Ken"

print(incoming_class)

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")

print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], [
    "Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False

customer_data[1].remove(False)

customer_data_final = customer_data + \
    [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
