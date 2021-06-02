# Python’s functions offer us a very expressive syntax.
# We’re going to look into some of the finer details of how functions in Python work and some techniques we can use to be more intuitive while writing and calling functions.

# First, let’s consider some definitions:
# A parameter is a variable in the definition of a function.
# An argument is the value being passed into a function call.
# A function definition begins with def and contains the entire following indented block.
# And function calls are the places a function is invoked, with parentheses, after its definition

# The "def" keyword is the start of a function definition
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
