# Python’s functions offer us a very expressive syntax.
# We’re going to look into some of the finer details of how functions in Python work and some techniques we can use to be more intuitive while writing and calling functions.

# First, let’s consider some definitions:
# A parameter is a variable in the definition of a function.
# An argument is the value being passed into a function call.
# A function definition begins with def and contains the entire following indented block.
# And function calls are the places a function is invoked, with parentheses, after its definition

# The "def" keyword is the start of a function definition
import shapes
import reqs as requests
from bs4 import BeautifulSoup
import os
from review_lib import get_next_review, submit_review
from record_library import place_record, rotate_record, drop_needle


def function_name(parameter1, parameter2):
    # The placeholder variables used inside a function definition are called parameters
    print(parameter1)
    return parameter2
# The outdent signals the end of the function definition


# "Arguments" are the values passed into a function call
argument1 = "argument 1"
argument2 = "argument 2"

# A function call uses the functions name with a pair of parentheses
# and can return a value
return_val = function_name(argument1, argument2)

# In the above code we defined the function function_name that takes two parameters, parameter1 and parameter2.
# We then create two variables with the values "argument 1" and "argument 2" and proceed to call function_name with the two arguments.


def play_record(album):
    place_record(album)
    rotate_record(album)
    drop_needle(album)


next_album = "Blondie / Parallel Lines"

play_record(next_album)

# How do you define a variable that you can’t assign a value to yet? You use None.
# None is a special value in Python.
# It is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).

none_var = None
if none_var:
    print("Hello!")
else:
    print("Goodbye")

# Prints "Goodbye"

# None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”.
# None is also unique, which means that you can test if something is None using the is keyword.

# first we define session_id as None
session_id = None

if session_id is None:
    print("session ID is None!")
    # this prints out "session ID is None!"

# we can assign something to session_id
if active_session:
    session_id = active_session.id

# but if there's no active_session, we don't send sensitive data
if session_id is not None:
    send_sensitive_data(session_id)

# Above we initialize our session_id to None, then set our session_id if there is an active session. Since session_id could either be None we check if session_id is None before sending our sensitive data.

# define review here!
review = get_next_review()
if review is not None:
    submit_review(review)

# What does a function return when it doesn’t return anything? This sounds like a riddle, but there is a correct answer.
# A Python function that does not have any explicit return statement will return None after completing.
# This means that all functions in Python return something, whether it’s explicit or not.


def no_return():
    print("You've hit the point of no return")
    # notice no return statement


here_it_is = no_return()

print(here_it_is)
# Prints out "None"

# It’s possible to make this syntax even more explicit — a return statement without any value returns None also.


def fifty_percent_off(item):
    # Check if item.cost exists
    if hasattr(item, 'cost'):
        return item.cost / 2

    # If not, return None
    return


sale_price = fifty_percent_off(product)

if sale_price is None:
    print("This product is not for sale!")

# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")

# print out the value of prints_return
print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return
print(list_sort_return)

# Function arguments are required in Python.
# So a standard function definition that defines two parameters requires two arguments passed into the function.

# Function definition with two required parameters


def create_user(username, is_admin):
    create_email(username)
    set_permissions(is_admin)


# Function call with all two required arguments
user1 = create_user('johnny_thunder', True)

# Raises a "TypeError: Missing 1 required positional argument"
user2 = create_user('djohansen')

# Above we defined our function, create_user, with two parameters.
# We first called it with two arguments, but then tried calling it with only one argument and got an error.
# What if we had sensible defaults for this argument?
# Not all function arguments in Python need to be required. If we give a default argument to a Python function that argument won’t be required when we call the function.

# Function defined with one required and one optional parameter


def create_user(username, is_admin=False):
    create_email(username)
    set_permissions(is_admin)


# Calling with two arguments uses the default value for is_admin
user2 = create_user('djohansen')

# Above we defined create_user with a default argument for is_admin, so we can call that function with only the one argument 'djohansen'.
# It assumes the default value for is_admin: False.
# We can make both of our parameters have a default value (therefore making them all optional).

# We can make all three parameters optional


def create_user(username=None, is_admin=False):
    if username is None:
        username = "Guest"
    else:
        create_email(username)
    set_permissions(is_admin)


# So we can call with just one value
user3 = create_user('ssylvain')
# Or no value at all, which would create a Guest user
user4 = create_user()


def make_folders(folders_list, nest=False):
    if nest:
        """
        Nest all the folders, like
        ./Music/fun/parliament
        """
        path_to_new_folder = "."
        for folder in folders_list:
            path_to_new_folder += "/{}".format(folder)
            try:
                print(path_to_new_folder)
                os.makedirs("./" + path_to_new_folder)
            except FileExistsError:
                continue
    else:
        """
        Makes all different folders, like
        ./Music/ ./fun/ and ./parliament/
        """
        for folder in folders_list:
            try:
                os.makedirs(folder)

            except FileExistsError:
                continue


make_folders(['Music', 'fun', 'parliament'])

# Not all of your arguments need to have default values.
# But Python will only accept functions defined with their parameters in a specific order.
# The required parameters need to occur before any parameters with a default argument.

# Raises a TypeError


def create_user(is_admin=False, username, password):
    create_email(username, password)
    set_permissions(is_admin)

# In the above code, we attempt to define a default argument for is_admin without defining default arguments for the later parameters: username and password.
# If we want to give is_admin a default argument, we need to list it last in our function definition:

# Works perfectly


def create_user(username, password, is_admin=False):
    create_email(username, password)
    set_permissions(is_admin)


def get_id(html_id, website="http://coolsite.com"):
    request = requests.get(website)
    parsed_html = BeautifulSoup(website.content, features="html.parser")
    return parsed_html.find(id_=html_id)

# When we call a function in Python, we need to list the arguments to that function to match the order of the parameters in the function definition.
# We don’t necessarily need to do this if we pass keyword arguments.
# We use keyword arguments by passing arguments to a function with a special syntax that uses the names of the parameters.
# This is useful if the function has many optional default arguments or if the order of a function’s parameters is hard to tell.

# Define a function with a bunch of default arguments


def log_message(logging_style="shout", message="", font="Times", date=None):
    if logging_style == 'shout':
        # capitalize the message
        message = message.upper()
    print(message, date)


# Now call the function with keyword arguments
log_message(message="Hello from the past", date="November 20, 1693")


def draw_shape(shape_name="box", character="x", line_breaks=True):
    shape = shapes.draw_shape(shape_name, character)
    if not line_breaks:
        print(shape[1:-1])
    else:
        print(shape)


# call draw_shape() with keyword arguments here:
draw_shape(character='m', line_breaks=False)
