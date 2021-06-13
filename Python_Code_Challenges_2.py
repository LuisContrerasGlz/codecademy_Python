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

# Write a function named append_sum that has one parameter — a list named named lst.
# The function should add the last two elements of lst together and append the result to lst.
# It should do this process three times and then return lst.

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))

# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements.
# If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times.
# The function should return False otherwise.

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

# Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result.
# Return the new sorted list.

def combine_sort(lst1, lst2):
  unsorted=lst1 + lst2
  sortedList=sorted(unsorted)
  return sortedList

# A function that prints all odd numbers in a list would look like this:

def odd_nums(lst):
  for item in lst:
    if item % 2 == 1:
      print(item)

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  countNumbers=0
  for item in nums:
    if (item % 10 == 0):
      countNumbers += 1
  return countNumbers

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting.
# Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

def add_greetings(names):
  new_list=[]
  for name in names:
    new_list.append("Hello, " + name)
  return new_list


# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

def tenth_power(num):
  return num ** 10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

def square_root(num):
  return num ** 0.5

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  tip_amount=(total * percentage) / 100
  return tip_amount

# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Create a function named lots_of_math().
# This function should have four parameters named a, b, c, and d.
# The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.

def lots_of_math(a, b, c, d):
  first=a + b
  second=c - d
  third=first * second
  fourth=third % a
  print(first)
  print(second)
  print(third)
  return fourth

# A function that finds the difference in length between two Strings:
def lengthDiff(str1, str2):
  return len(str1) - len(str2)

# Write a function called unique_english_letters that takes the string word as a parameter.
# The function should return the total number of unique letters in the string.
# Uppercase and lowercase letters should be counted as different letters.

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques=0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Write a function named count_char_x that takes a string named word and a single character named x as parameters.
# The function should return the number of times x appears in word.

def count_char_x(word, x):
  occurrences=0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences

print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters.
# This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  words=sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
