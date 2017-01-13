

################
# 4. Functions #
################

# use "def" to create new functions
def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x + y # Return values with a return statement
# call this functions with its parameters in the following way:
add(5,6) # prints out 'x is 5 and y is 6' and returns 11
# another way to call functions is with keyword arguments
add(y=6, x=5) # keyword arguments can arrive in any order

# we can define functions that take a variable number of positional arguments
def varargs(*args):
    return args

varargs(1,2,3)
# => (1,2,3)

# return value of such a function is a tuple
type(varargs(1,2,3))
# => <class 'tuple'>

# we can define functions that take a variable number of keyword arguments
def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness")
# => {'big': 'foot', 'loch': 'ness'}

# return value of such a function is a dictionary
type( keyword_args(big="foot", loch="ness") )
# => <class 'dict'>

# we can do both at once:
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# Returning multipl values (with tuple assignments)
def swap(x,y):
    return y, x # Return multiple values as a tuple without the parenthesis. (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x,y)   # now x is 2, y is 1

# A little about function scope:
x = 5

def set_x(num):
    # local variable x is NOT the same as the global variable x
    x = num     # => 43
    print(x)    # prints 43

def set_global_x(num):
    global x
    print(x)    # => 5
    x = num     # => global var x is now set to 6
    print (x)   # => 6

set_x(43)
set_global_x(6)

# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)            # => True
(lambda x, y: x**2 + y**2)(2,1) # => 5

# There are built-in higher order functions as well
list(map(add_10, [1,2,3]))          # => [11,12,13]
list(map(max, [1,2,3], [4,2,1]))    # => [4,2,3]

list(filter(lambda x: x > 5, [3,4,5,6,7])) # => [6,7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1,2,3]]        # => [11,12,13]
[x for x in [3,4,5,6,7] if x > 5]   # => [6,7]

# You can construct set and dict comprehensions as well
{x for x in 'abcddeef' if x not in 'abc'}   # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}                 # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
