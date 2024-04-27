# Importing specific functions from modules
from math import sqrt, pi

# Importing all functions from modules
from random import randint, choice

# Importing an entire module
import time
import os # os --> operating system
import datetime

# Using the imported functions
print("Square root of 16:", sqrt(16))
print("Value of pi:", pi)

print("Random integer between 1 and 100:", randint(1, 100))
print("Random choice from a list:", choice(['apple', 'banana', 'cherry']))

# Using the imported module
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Done sleeping!")

# Additional functionality
print("\nAdditional Functionality:")
print("Current working directory:", os.getcwd())
print("List of directory from CWD : ",os.listdir())
print("Current date and time:", datetime.datetime.now())
