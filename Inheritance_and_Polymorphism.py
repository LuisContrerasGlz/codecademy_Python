# Classes are designed to allow for more code reuse, but what if we need a class that looks a lot like a class we already have?
# If the bulk of a class’s definition is useful, but we have a new use case that is distinct from how the original class was used, we can inherit from the original class.
# Think of inheritance as a remix — it sounds a lot like the original, but there’s something… different about it.

# class User:
#  is_admin = False
#  def __init__(self, username)
#    self.username = username

# class Admin(User):
#  is_admin = True

# Above we defined User as our base class.
# We want to create a new class that inherits from it, so we created the subclass Admin.
# In the above example, Admin has the same constructor as User.
# Only the class variable is_admin is set differently between the two.
# Sometimes a base class is called a parent class. In these terms, the class inheriting from it, the subclass, is also referred to as a child class.

class Bin:
    pass


class RecyclingBin(Bin):
    pass

# There’s one very important family of class definitions built in to the Python language.
# An Exception is a class that inherits from Python’s Exception class.

# We can validate this ourselves using the issubclass() function.
# issubclass() is a Python built-in function that takes two parameters.
# issubclass() returns True if the first argument is a subclass of the second argument.
# It returns False if the first class is not a subclass of the second.
# issubclass() raises a TypeError if either argument passed in is not a class.


issubclass(ZeroDivisionError, Exception)
# Returns True

# Why is it beneficial for exceptions to inherit from one another?
# Let’s consider an example where we create our own exceptions.
# What if we were creating software that tracks our kitchen appliances? We would be able to design a suite of exceptions for that need:


class KitchenException(Exception):
    """
    Exception that gets thrown when a kitchen appliance isn't working
    """


class MicrowaveException(KitchenException):
    """
    Exception for when the microwave stops working
    """


class RefrigeratorException(KitchenException):
    """
    Exception for when the refrigerator stops working
    """

# In this code, we define three exceptions.
# First, we define a KitchenException that acts as the parent to our other, specific kitchen appliance exceptions.
# KitchenException subclasses Exception, so it behaves in the same way that regular Exceptions do.
# Afterward we define MicrowaveException and RefrigeratorException as subclasses.
# Since our exceptions are subclassed in this way, we can catch any of KitchenException‘s subclasses by catching KitchenException.


def get_food_from_fridge():
    if refrigerator.cooling == False:
        raise RefrigeratorException
    else:
        return food


def heat_food(food):
    if microwave.working == False:
        raise MicrowaveException
    else:
        microwave.cook(food)
        return food


try:
    food = get_food_from_fridge()
    food = heat_food(food)
except KitchenException:
    food = order_takeout()

# In the above example, we attempt to retrieve food from the fridge and heat it in the microwave.
# If either RefrigeratorException or MicrowaveException is raised, we opt to order takeout instead.
# We catch both RefrigeratorException and MicrowaveException in our try/except block because both are subclasses of KitchenException.


class OutOfStock(Exception):
    pass

# Update the class below to raise OutOfStock


class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')

# Inheritance is a useful way of creating objects with different class variables, but is that all it’s good for?
# What if one of the methods needs to be implemented differently?
# In Python, all we have to do to override a method definition is to offer a new definition for the method in our subclass.
# An overridden method is one that has a different definition from its parent class.


class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

    def has_permission_for(self, key):
        if self.permissions.get(key):
            return True
        else:
            return False


class Admin(User):
    def has_permission_for(self, key):
        return True


class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text

# Overriding methods is really useful in some cases but sometimes we want to add some extra logic to the existing method.
# In order to do that we need a way to call the method from the parent class.
# Python gives us a way to do that using super().
# super() gives us a proxy object.
# With this proxy object, we can invoke the method of an object’s parent class (also called its superclass).

# We call the required function as a method on super():


class Sink:
    def __init__(self, basin, nozzle):
        self.basin = basin
        self.nozzle = nozzle


class KitchenSink(Sink):
    def __init__(self, basin, nozzle, trash_compactor=None):
        super().__init__(basin, nozzle)
        if trash_compactor:
            self.trash_compactor = trash_compactor

# Above we defined two classes.
# First, we defined a Sink class with a constructor that assigns a rinse basin and a sink nozzle to a Sink instance.
# Afterwards, we defined a KitchenSink class that inherits from Sink.
# KitchenSink‘s constructor takes an additional parameter, a trash_compactor.
# KitchenSink then calls the constructor for Sink with the basin and nozzle it received using the super() function, with this line of code:
# super().__init__(basin, nozzle)
# This line says: “call the constructor (the function called __init__()) of the class that is this class’s parent class.”


class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40

# Why we would even want to have two different classes with two differently implemented methods to use the same method name.
# This style is especially useful when we have an object for which it might not matter which class the object is an instance of.
# Instead, we’re interested in whether that object can perform a given task.


class Chess:
    def __init__(self):
        self.board = setup_board()
        self.pieces = add_chess_pieces()

    def play(self):
        print("Playing chess!")


class Checkers:
    def __init__(self):
        self.board = setup_board()
        self.pieces = add_checkers_pieces()

    def play(self):
        print("Playing checkers!")

# In the code above we define two classes, Chess and Checkers.
# In Chess we define a constructor that sets up the board and pieces, and a .play() method.
# Checkers also defines a .play() method.
# If we have a play_game() function that takes an instance of Chess or Checkers, it could call the .play() method without having to check which class the object is an instance of.


def play_game(chess_or_checkers):
    chess_or_checkers.play()


chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
    play_game(game)

# Prints out the following:
# Playing chess!
# Playing checkers!
# Playing chess!

# When two classes have the same method names and attributes, we say they implement the same interface.
# An interface in Python usually refers to the names of the methods and the arguments they take.
# Other programming languages have more rigid definitions of what an interface is, but it usually hinges on the fact that different objects from different classes can perform the same operation (even if it is implemented differently for each class).


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005

# All this talk of interfaces demonstrates flexibility in programming.
# Flexibility in programming is a broad philosophy, but what’s worth remembering is that we want to implement forms that are familiar in our programs so that usage is expected.
# For example, let’s think of the + operator.
# It’s easy to think of it as a single function that “adds” whatever is on the left with whatever is on the right, but it does many different things in different contexts:


# For an int and an int, + returns an int
2 + 4 == 6

# For a float and a float, + returns a float
3.1 + 2.1 == 5.2

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]

# Look at all the different things that + does! The hope is that all of these things are, for the arguments given to them, the intuitive result of adding them together.
# Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data.
# Polymorphism is an abstract concept that covers a lot of ground, but defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

len(a_list)
len(a_dict)
len(a_string)
