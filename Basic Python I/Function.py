# Basic function definition and usage:
# - Functions are defined using the 'def' keyword followed by the function name and parameters.
# - Parameters are specified within parentheses.
# - The 'return' statement is used to return a value from the function.

# If we don't explicitly return anything from a function, by default it returns 'None'.

def double(num):
    # Doubles the given number
    num *= 2
    return num

def sum(num1, num2):
    # Returns the sum of two numbers
    return num1 + num2

# Example usage:
num1, num2 = double(8), double(12)
print(sum(num1, num2))

# Note: Functions encapsulate reusable pieces of code. They are defined with the 'def' keyword followed by the function name and parameters in parentheses.
# Inside the function, you perform operations and optionally use the 'return' statement to return a value.
# Parameters are values that are passed to the function when it is called, and arguments are the actual values passed to the function.
