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

from datetime import datetime

current_time = datetime.now()
print(current_time)
