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
