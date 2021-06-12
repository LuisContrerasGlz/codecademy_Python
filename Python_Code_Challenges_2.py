# As a refresher, function syntax looks like this:
# def some_function(some_input1, some_input2):
  # … do something with the inputs …
  # return output

def first_plus_last(lst):
  return lst[0] + lst[-1]

# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False


def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False


print(large_power(2, 13))
print(large_power(2, 12)

# Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.
# The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  resultSum=(food_bill + electricity_bill + internet_bill + rent)
  if budget < resultSum:
    return True
  else:
    return False

print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1, num2):
  doubleNum2=num2 * 2
  if num1 > doubleNum2:
    return True
  else:
    return False

print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False

# Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False

# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.
# An if statement that is always false is called a contradiction.
# You will rarely want to do this while programming, but it is important to realize it is possible to do this.

def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False

# Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!".
# If rating is between 5 and 9, return "This one was fun.".
# If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"

def some_function(some_input1, some_input2):
  # … do something with the inputs …
  return output

# A function that returns the sum of the first and last elements of a given list might look like this:
def first_plus_last(lst):
  return lst[0] + lst[-1]

# Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst.
# The function should then return this new list.

def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))
