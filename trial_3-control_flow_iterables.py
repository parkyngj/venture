

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
