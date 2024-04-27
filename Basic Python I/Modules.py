# Importing the double function from the Function file
from Function import double

# Importing the full_name function from the kargs_and_multiple_return file and aliasing it as name
from kargs_and_multiple_return import full_name as name

# Importing all functions from the Default_parameters_and_args file
from Default_parameters_and_args import *

# Using the double function to double the value 90
Num = double(90)
print(Num)

# Using the full_name function (aliased as name) to combine first and last names
me = name("Sarafat", "karim")
print(me)

