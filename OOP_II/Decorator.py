import math
import time

# Define the decorator function
def timer(func):
    """
    Decorator function that adds timing functionality to another function.
    
    Args:
        func (function): The function to be decorated.
    
    Returns:
        function: The decorated function with timing functionality.
    """
    # Define the inner function
    def inner(*args, **kwargs):
        # Print a message indicating the start of timing
        print('time started')
        # Record the start time
        start = time.time()
        # Call the original function with any provided arguments and keyword arguments
        func(*args, **kwargs)
        # Record the end time
        end = time.time()
        # Print the total time taken
        print(f'total time taken: {end - start}')
        # Print a message indicating the end of timing
        print('time ended')
    # Return the inner function, which now contains timing functionality
    return inner

# Decorate the function using the @ syntax
@timer
def get_factorial(n):
    """
    Function to calculate the factorial of a number.
    
    Args:
        n (int): The number for which factorial is to be calculated.
    """
    # Print a message indicating the start of the factorial calculation
    print('factorial starting')
    # Calculate the factorial using the math module
    result = math.factorial(n)
    # Print the result
    print(f'factorial of {n} is: {result}')

# Call the decorated function with an argument
get_factorial(n=1200)

""" 
    When get_factorial(n = 1200) is invoked, it actually executes timer(get_factorial)().
    This is because the @timer syntax applies the timer decorator to the get_factorial function,
    effectively replacing it with the inner function returned by the decorator.
"""

""" 
    To decorate a function with a decorator:

    * Define a decorator function that accepts another function as its argument.(Timer() function in this case is a decorator function)
    * Inside the decorator function, define an inner function that wraps around the original function.(inner() function in this case)
    * Call the passed function within the inner function, along with any necessary arguments and keyword arguments.
    * Return the inner function from the decorator function.
    * Use the @ syntax to apply the decorator to the function you want to decorate
"""
