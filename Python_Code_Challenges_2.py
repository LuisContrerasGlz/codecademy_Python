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
