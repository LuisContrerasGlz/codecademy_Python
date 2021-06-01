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

# Methods can also take more arguments than just self:


class DistanceConverter:
    kms_in_a_mile = 1.609

    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile


converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

# Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers.
# Notice again that even though how_many_kms takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).


class Circle:
    pi = 3.14

    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

# There are several methods that we can define in a Python class that have special behavior.
# These methods are sometimes called “magic,” because they behave differently from regular methods.
# Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.
# The first dunder method we’re going to use is the __init__() method (note the two underscores before and after the word “init”).
# This method is used to initialize a newly created object.
# It is called every time the class is instantiated.
# Methods that are used to prepare an object being instantiated are called constructors.
# The word “constructor” is used to describe similar features in other object-oriented programming languages but programmers who refer to a constructor in Python are usually talking about the __init__() method.


class Shouter:
    def __init__(self):
        print("HELLO?!")


shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"

# Above we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout.
# Pay careful attention to the instantiation syntax we use.
# Shouter() looks a lot like a function call, doesn’t it? If it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by the __init__() method.


class Shouter:
    def __init__(self, phrase):
        # make sure phrase is a string
        if type(phrase) == str:

            # then shout it out
            print(phrase.upper())


shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

# Above we’ve updated our Shouter class to take the additional parameter phrase.
# When we created each of our objects we passed an argument to the constructor.
# The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)

# We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has?
# This is because each instance of a class can hold different kinds of data.
# The data held by an object is referred to as an instance variable.
# Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.


class FakeDict:
    pass


# We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"


class Store:
    pass


alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# Instance variables and class variables are both accessed similarly in Python.
# This is no mistake, they are both considered attributes of an object.
# If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.


class NoCustomAttributes:
    pass


attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute
except AttributeError:
    print("This text gets printed!")

# prints "This text gets printed!"

# What if we aren’t sure if an object has an attribute or not?
# hasattr() will return True if an object has a given attribute and False otherwise.
# If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute.
# In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

# The syntax and parameters for these functions look like this:

# hasattr(object, “attribute”) has two parameters:
# object : the object we are testing to see if it has a certain attribute
# attribute : name of attribute we want to see if it exists

# getattr(object, “attribute”, default) has three parameters (one of which is optional):
# object : the object whose attribute we want to evaluate
# attribute : name of attribute we want to evaluate
# default : the value that is returned if the attribute does not exist (note: this parameter is optional)

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")

# Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful.
# Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.
# This convenience is most apparent when the constructor creates the instance variables, using the arguments passed in to it.

#  If we were creating a search engine, and we wanted to create classes for each separate entry we could return. We’d do that like this:


class SearchEngineEntry:
    def __init__(self, url):
        self.url = url


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

# Since the self keyword refers to the object and not the class being called, we can define a secure method on the SearchEngineEntry class that returns the secure link to an entry.


class SearchEngineEntry:
    secure_prefix = "https://"

    def __init__(self, url):
        self.url = url

    def secure(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)


codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

# Above we define our secure() method to take just the one required argument, self.
# We access both the class variable self.secure_prefix and the instance variable self.url to return a secure URL.
# This is the strength of writing object-oriented programs.
# We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:

        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor.
# We can use the dir() function to investigate an object’s attributes at runtime.
# dir() is short for directory and offers an organized presentation of object attributes.


class FakeDict:
    pass


fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'attribute']

# That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created.
# These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list.
# Do you remember being able to use type() on Python’s native data types? This is because they are also objects in Python. Their classes are int, float, str, list, and dict. These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically.
# But these instances are still full-blown objects to Python.

fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(dir(5))


def this_function_is_an_object(num):
    return "Cheese is {} times better than everything else".format(num)


print(dir(this_function_is_an_object))

# One of the first things we learn as programmers is how to print out information that we need for debugging.
# Unfortunately, when we print out an object we get a default representation that seems fairly useless.


class Employee():
    def __init__(self, name):
        self.name = name


argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

# This default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.
# We learned about the dunder method __init__().
# Now, we will learn another dunder method called __repr__().
# This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter, self, and must return a string.


class Employee():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"
# We implemented the __repr__() method and had it return the .name attribute of the object.
# When we printed the object out it simply printed the .name of the object!


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
