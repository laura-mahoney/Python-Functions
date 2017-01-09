"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def is_home_town(town): #create my function 
    if town is "Danville":  #if the town is Danville, return true
        return True
    else:               #else return false
        return False


def full_name(first, last): #function declared to concatenate first and last name
    return first + last

def introduction(town, first, last):    
    if is_home_town == True:    #if hometown is true
        print "Hi, " + full_name(first, last) + ", we're from the same place!"
    else: 
        print "Hi, " + full_name(first,last) + ", where are you from?"
###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""
    if fruit is "strawberry":   #checking for each condition match, not checking length
        return True
    if fruit is  "cherry":
        return True
    if fruit is "blackberry":
        return True
    else: 
        return False        #false will be returned if the word is not a berry
    pass


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    if is_berry(fruit):     #is berry returns true if the fruit is a berry, and true produces the value 0
        return 0
    else:
        return 5    #return five if false
    pass


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""
    added_input = [] #we make an empty list 

    added_input.extend(lst) #we add the pre-existing list to it using extend
    added_input.append(num) #the final number gets appended, since it's one item
    
    return added_input  #returning the new list
    pass



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(itemprice, ST, tax = .05): #define parameters, inc optional parameters
    import math                            #import math module 
    total_with_tax = itemprice + (itemprice * tax) #set up calc for total when exceptions by state are not met
    
    if ST is "CA":              #set up conditions for each state based on fees and modify and return totals 
        state_fee = total_with_tax * .03
        total_with_fee = state_fee + total_with_tax
        return math.floor(total_with_fee)
    if ST is "PA":
        total_with_fee = total_with_tax + 2.0
        return total_with_fee
    if ST is "MA":
        if itemprice < 100: 
            total_with_fee = 1.0 + total_with_tax
        elif itemprice > 100: 
            total_with_fee = 3.0 + total_with_tax
        return total_with_fee
    else: 
        return total_with_tax # returns the total when exceptions by state are not met
    pass


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
def appended_list_byargs(somelist, *args):
    for a in args: 
        somelist.extend(a)
    return somelist

def repeat_three_times(word):
    
    def multiply_by_3(x):
        return x * 3

    multiply_by_3(word)


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
