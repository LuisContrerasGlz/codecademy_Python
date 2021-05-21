# We’ll explore how to use tools other people have built in Python that are not included automatically for you when you install Python.
# Python allows us to package code into files or sets of files called modules.
# A module is a collection of Python declarations intended broadly to be used as a tool.
# Modules are also often referred to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

# Usually, to use a module in a file, the basic syntax you need at the top of that file is:
# from module_name import object_name

# Often, a library will include a lot of code that you don’t need that may slow down your program or conflict with existing code.
# Because of this, it makes sense to only import what you need.

# One common library that comes as part of the Python Standard Library is datetime.
# datetime helps you work with dates and times in Python.

from matplotlib import pyplot as plt
import codecademylib3_seaborn
import random
from datetime import datetime

current_time = datetime.now()
print(current_time)

# There are hundreds of Python modules that you can use.
# Another one of the most commonly used is random which allows you to generate numbers or select items at random.

# With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:
# import random

# We’ll work with two common random functions:
# random.choice() which takes a list as an argument and returns a number from the list.
# random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in.

# Import random:

# Create random_list:
random_list = [random.randint(1, 100) for i in range(101)]

# Create randomer_number:
randomer_number = random.choice(random_list)

# Print randomer_number:
print(randomer_number)

# Notice that when we want to invoke the randint() function we call random.randint().
# This is default behavior where Python offers a namespace for the module.
# A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing.
# Your local namespace, meanwhile, is where your code is run.

# Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy.
# Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.
# Fortunately, this name can be altered by aliasing using the as keyword:
# import module_name as name_you_pick_for_the_module
# Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.

# You might also occasionally encounter import *.
# The * is known as a “wildcard” and matches anything and everything.
# This syntax is considered dangerous because it could pollute our local namespace.
# Pollution occurs when the same name could apply to two possible things.


numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()
