##############
# 5. Modules #
##############

# you can import modules
import math
print(math.sqrt(16)) # => 4.0

# you can choose to import specific functions from a module
from math import ceil, floor
print(ceil(3.7))    # => 4.0
print(floor(3.7))   # => 3.0

# you can import all functions from a module
# warning: not recommended
from math import *

# can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16) # => True

# python modules are just ordinary python files. you can write your own, and import them. the name of the module is the same as the name of the file.
# you can find out which functions and attributes defines a module
import math
dir(math)
# => ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# if you have a Python script named math.py in the same folder as your current script, the file math.py will be loaded instead of the built-in Python module
# this happens because the local folder has priority over Python's built-in libraries
