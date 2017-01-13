# Single line comments start with a hashtag.

"""But if we want to make a multiline comment, we can
    do so by wrapping our comment in three "s!
"""

#########################################
# 1. Primitive Data Types and Operators #
#########################################

# We have numbers
3 # => 3

# Math is what you would expect

1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Result of division is always a float
10.0 / 3 # => 3.3333333333333335

# We can get floor division by using two slashes instead
5 // 3          # => 1
5.0 // 3.0      # => 1.0 # works on floats too!
-5 // 3         # => -2
-.5.0 // -3.0   # => -2.0

# We have the modulo operation to get remainders
7 % 3 # =>1

# Exponentiation (x**y is x^y)
2**5 # => 32

# We can enforce precendence of operations using parentheses
(1 + 3) * 2 # => 8

# Boolean values are primitives, and capitalized
True
False

# We can negate with the keyword not
not True    # => False
not False   # => True

# Boolean operators and and or, which are both case-sensitive
True and False  #=> False
True or False   #=> True

# Checking for equality entails using ==
1 == 1  # => True
1 == 2  # => False

# Inequality is !=
1 != 1  # False
2 != 1  # True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Comparisons can be chained!
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too
"Hello " + "world!" # => "Hello world!"

# .format can be used to format strings, like this:
"{} can be {}".format("strings", "interpolated") # => "strings can be interpolated"

# You can repeat the formatting arguments to save some typing:
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")

# You can use keywords if you don't want to count:
"{name} wants to eat {food}".format(name="Bob", food="lasagna") # => "Bob wants to eat lasagna"

# NOTE: If the Python 3 code we are writing also needs to run on Python 2.5 and below, we can also still use the old style of formatting:
"%s can be %s the %s way" % ("strings", "interpolated", "old") # => "strings can be interpolated the old way"

# None is an object
None # => None

# Don't use the equality "==" symbol to compare objects to None
# Use 'is' instead. This checks for equalty of object identity
"etc" is None   # => False
None is None    # => True

# None, 0 and empty strings/lists/dicts/tuples all evaluate to False
bool(0)     # => False
bool("")    # => False
bool([])    # => False
bool({})    # => False
bool(())    # => False

################################
# 2. Variables and Collections #
################################

# Python has a print function
print("I'm Python. Nice to meet you!") # => I'm Python. Nice to meet you!

# By default, the print function also prints out a newline at the end.
# Use the optional argument end to change the end character
print("Hello World", end="!") # => Hello, World!

# Simple way to get input data from console:
input_string_var = input("Enter some data: ") # Returns the data as a string

# Declare variables by simple assignment
some_var = 5
some_var # => 5

# Trying to access a previously unassigned variable is an exception
some_unassigned_var # Raises a NameError

# If can be used as an expression
"yahoo!" if 3 > 2 else 2 # => "yahoo!"

# Lists store sequences
li = []

# You can start with prepopulated list
other_lit = [1,2,3]

# Add stuff to the end of a list with append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1,2]
li.append(4)    # li is now [1,2,4]
li.append(3)    # li is now [1,2,4,3]
# Remove from the end of the list with pop
li.pop()        # => 3, and li is now [1,2,4]
# Let's put 3 back
li.append(3)    # li is now [1,2,4,3] again

# Access list elements by nindex
li[0] # => 1
# Negative indexing works
li[-1] # => 3

# Looking out of bounds is an IndexError
li[4] # => Raises an IndexError

# Can look at ranges with slice syntax
# (It is a closed/open range)
li[1:3]     # => [2,4]
# Omit up to and including some index N:
li[2:]      # => [4,3]
# Slice off after and including some index N:
li[:3]      # => [1,2,4]
# Select every second entry
li[::2]     # => [1,4]
# Return a reversed copy of the list
li[::-1]    # => [3,4,2,1]
# Use any combinato of these to make advanced slices
# the key is li[start:end:step]

# Make a one layer deep copy using slices:
li2 = li[:] # => li2 = [1,2,4,3], but (li2 is li) will result in False

# Remove an item at index N with "del"
del li[2]       # li is now [1,2,3]

# Remove first occurrence of a value with .remove
li.remove(2)    # li is now [1,3]
li.remove(2)    # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1,2)  # li is now [1,2,3] again
# the format is li.insert(INDEX, VALUE)

# Get the index of the first item found matching the argument
li.index(2)     # => 1
li.index(4)     # => Raises a ValueError

# You can concatenate lists together with + (not destructive to any lists used in the concatenation)
li + other_li           # => [1,2,3,4,5,6]
# .extend is the destructive version of +
li.extend(other_li)     # => Now li is [1,2,3,4,5,6]

# Check for existence of an element in a list with "in"
1 in li # => True

# Return the length of a list with "len()"
len(li) # => 6

# Tuples are like lists, but immutable
tup = (1,2,3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError

# Note: Tuple of length one has to have comma after the last element, but tuples of other lengths, even zero, don't
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# You can do most of the list operations on tuples too, like asking length, concatenation, selection, inclusion
len(tup)        # => 3
tup + (4,5,6)   # => (1,2,3,4,5,6)
tup[:2]         # => (1,2)
2 in tup        # => True

# Unpack tuples or lists into respective variables
a,b,c = (1,2,3)         # a is now 1, b is now 2, and c is now 3
d,e,f = 4,5,6           # d is now 4, e is now 5, and f is now 6
# Can do extended unpacking
a, *b, c = (1,2,3,4)    # a is now 1, b is now [2,3], and c is now 4
# Can swap two values as such
d, e = e, d             # now d is 5 and e is 4

# Note keys for dictionary must be immutable types.
    # This is to ensure that the key can be converted into a constant hash value for quick look-ups.
    # Immutable types include integers, floats, strings, and tuples
invalid_dict    = {[1,2,3]: "123"}      # => Raises a TypeError: unhashable type: 'list'
valid_dict       = {(1,2,3): [1,2,3]}    #=> Values can be of any type, however

# We can look up values with []
filled_dict["one"] # => 1

# Get all keys as an iterable with "keys()", and wrap it in list() to turn it into a list.
# Note: Dictionary key ordering isn't guaranteed. Our results may not match this exactly.
list(filled_dict.keys()) #=> ["three", "two", "one"]

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict    # => True
1 ni filled_dict        # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"] # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")  # => 1
filled_dict.get("four") # => None
# "get()" method supports a default argument when the value is missing
filled_dict.get('one', 4)   # => 1
filled_dict.get('four', 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)   # filled_dict['five'] is set to 5
filled_dict.setdefault("five", 6)   # filled_dict['five'] is still 5

# Adding to a dictionary
filled_dict.update({"four": 4}) # => {"one": 1, "two": 2, "three": 3, "four": 4}
# filled_dict["four"] = 4       # another way to add to dictionary

# Remove keys from a dictionary with del
del filled_dict['one'] # Removes the key "one" from filled dict

# Sets store sets (no duplicates, fast lookup for inclusion)
empty_set = set()
# Initialize a set with some values:
some_set = {1, 1, 2, 2, 3, 4} # some_set is {1,2,3,4} (note that the duplicates 1 and 2 have been collapsed)

# Similar to keys of dictionary, elements of a set must be immutable
invalid_set = {[1], 1} # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Can assign new variables to a set
filled_set = some_set

# Add one more item to the set
filled_set.add(5) # filled_set is now {1,2,3,4,5}

# Can do set intersection with &
other_set = {3,4,5,6}
filled_set & other_set # => {3,4,5}

# Can do set union with |
filled_set | other_set # => {1,2,3,4,5,6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True

# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False

#################################
# 3. Control Flow and Iterables #
#################################

# Let's make a variable equal to 5
some_var = 5

# Here is an if statement. Indentation is significant in Python.
# this prints "some var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10")
elif some_var < 10:
    print("some var is smaller than 10")
else:
    print("some_var is indeed 10")

"""
For loops iterate oer lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers from the lowest number to the highest number
prints:
    4
    5
    6
    7
"""
for i in range(4,8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers from the lower number to the upper number, while incrementing by step. If step is not included, then default value is 1
prints:
    4
    6
"""
for i in range(4,8,2):
    print(i)

"""
While loops go until a condition is no longer met
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1

# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# e.g. the object returned by the range function is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# We can loop over it:
for i in our_iterable:
    print(i) # Prints one, two, three

# However, we cannot address the iterable's elements by index.
our_iterable[1]
# => TypeError: 'dict_keys' object does not support indexing

# An iterable is an object that knows how to create an iterator
our_iterator = iter(our_iterable)
# our_iterator is a dict_keyiterator object that can remember the state as we traverse through it
# we get the next object with "next()"
next(our_iterator) # => "one"
next(our_iterator) # => "two"
next(our_iterator) # => "three"
# After the iterator has returned all of its data, it gives you a StopIteration Exception
next(our_iterator) # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it
list(filled_dict.keys()) # => Returns ["one", "two", "three"]

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
