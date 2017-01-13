

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

# Some literature on when to use sets vs tuples vs lists vs dicts
# http://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
