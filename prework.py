# QUESTION 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
# The first line of the code has been defined as below.
# def hello_name(user_name):

def hello_name(user_name):
    print(f'hello_{user_name.upper()}!') if (type(user_name) == str and bool(
        user_name)) else print('Input must be a name')
# getting used to how to use a ternary in python
# if input is str and is not empty: print 'hello_USERNAME'
# # else: print input is invalid


# QUESTION 2
# Write a python function, first_odds that prints
# the odd numbers from 1-100 and returns nothing
# def first_odds():

def first_odds():
    for num in range(1, 101):  # 1-100
        if (num % 2 != 0):  # odds only
            print(num)


# QUESTION 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.
# def max_num_in_list(a_list):

def max_num_in_list(a_list):
    # guard clause if input type not list
    if (type(a_list) != list):
        raise TypeError('Input not a list')

    # if list only contains numbers, quick return max
    if (all(isinstance(val, (int, float)) for val in a_list)):
        return max(a_list)
    # if lists contains other data types
    else:
        # ask user to continue and exclude non numbers
        response = input(
            'This list contains values that are not numbers. These values will be ignored.\n' +
            'Type [Y] to continue or any other key to exit: ')
        # user continues
        if response.lower() == 'y':
            # I read about list comprehensions so I tried to implement one here
            # create new list of only numbers from input list and return the max
            list_comp = [val for val in a_list if (
                type(val) == int or type(val) == float)]
            return max(list_comp)
        # user does not enter 'y' or 'Y'
        else:
            raise Exception('User exited')
# learning to throw errors in python and practicing getting user input
# this is probably not the best way to handle errors


# QUESTION 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
# The return should be boolean Type (true/false).
# def is_leap_year(a_year):

def is_leap_year(a_year):
    # this one might be a little unnecessary but I wanted to practice a bit with guard clauses and type casting in python
    if (type(a_year) == list and len(a_year) == 1):
        a_year = a_year.pop()

    if (type(a_year) == str):
        a_year = int(a_year)

    if (type(a_year) != int):
        raise TypeError('Input must be a number')

    # 400 first to prevent returning false on multiples of 400
    if (a_year % 400 == 0):
        return True
    # 100 next to prevent returning true on multiples of 100
    elif (a_year % 100 == 0):
        return False
    # all other years where year % 4 == 0 should return true
    elif (a_year % 4 == 0):
        return True
    # any other year is not a leap year return false
    # could also use: elif (a_year % 4 != 0):
    else:
        return False
# since 400 is divisible by 100 and 4 and 100 is divisible by 4
# only need to check one case at a time since


# QUESTION 5
# Write a function to check to see if all numbers in the list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.
# def is_consecutive(a_list):

def is_consecutive(a_list):
    # if input is not a list
    if (type(a_list) != list):
        raise TypeError('Input must be a list')

    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
# left side is input list sorted
# right side is a temp list of all integers in input list from min to max
# if any nonconsecutive values in input list, lists will not be equal --> evaluate to false
# only works with list of integers
