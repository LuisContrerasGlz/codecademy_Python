# Python equips us with many different ways to store data.
# A float is a different kind of number from an int, and we store different data in a list than we do in a dict.
# These are known as different types.
# We can check the type of a Python variable using the type() function.

a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"

print(type(an_int))
# prints "<class 'int'>"

# Above, we defined two variables, and checked the type of these two variables.
# A variable’s type determines what you can do with it and how you can use it.
# You can’t .get() something from an integer, just as you can’t add two dictionaries together using +.
# This is because those operations are defined at the type level.

print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

# A class is a template for a data type.
# It describes the kinds of information that class will hold and how a programmer will interact with that data.


class CoolClass:
    pass

# In the above example we created a class and named it CoolClass.
# We used the pass keyword in Python to indicate that the body of the class was intentionally left blank so we don’t cause an IndentationError.


class Facade:
    pass

# A class doesn’t accomplish anything simply by being defined.
# A class must be instantiated.
# In other words, we must create an instance of the class, in order to breathe life into the schematic.
# Instantiating a class looks a lot like calling a function.


# We would be able to create an instance of our defined CoolClass as follows:
cool_instance = CoolClass()

# Above, we created an object by adding parentheses to the name of the class.
# We then assigned that new instance to the variable cool_instance for safe-keeping so we can access our instance of CoolClass at a later time.


class Facade:
    pass


facade_1 = Facade()
