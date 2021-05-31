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

# A class instance is also called an object.
# The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.
# Instantiation takes a class and turns it into an object, the type() function does the opposite of that.
# When called with an object, it returns the class that the object is an instance of.

print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"
# We then print out the type() of cool_instance and it shows us that this object is of type __main__.CoolClass.
# In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class CoolClass that was defined here, in the script you’re currently running.”


class Facade:
    pass


facade_1 = Facade()
facade_1_type = type(facade_1)
print(type(facade_1))

# When we want the same data to be available to every instance of a class we use a class variable.
# A class variable is a variable that’s the same for every instance of the class.
# You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.


class Musician:
    title = "Rockstar"


drummer = Musician()
print(drummer.title)
# prints "Rockstar"

# Above we defined the class Musician, then instantiated drummer to be an object of type Musician.
# We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.
# If we defined another musician, like guitarist = Musician() they would have the same .title attribute.


class Grade:
    minimum_passing = 65

# Methods are functions that are defined as part of a class.
# The first argument in a method is always the object that is calling the method.
# Convention recommends that we name this first argument self.
# Methods always have at least this one argument.
# We define methods similarly to functions, except that they are indented to be part of the class.


class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(
            self.dog_time_dilation))


pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."
# Above we created a Dog class with a time_explanation method that takes one argument, self, which refers to the object calling the function.
# We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.
# Notice we didn’t pass any arguments when we called .time_explanation(), but were able to refer to self in the function body.
# When you call a method it automatically passes the object calling the method as the first argument.


class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."
