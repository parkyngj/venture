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
