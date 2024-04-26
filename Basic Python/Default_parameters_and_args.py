# Example of a function with default parameters:

def sum(num1, num2, num3=0, num4=0):
    # Calculates the sum of the provided numbers
    total = num1 + num2 + num3 + num4
    return total

# Example usage of the function with default parameters:
total = sum(2, 4)  # Here we only passed two values, and the remaining two will use their default value (0)
total_I = sum(2, 4, 5)  # Here only the fourth parameter will use its default value (0)
total_II = sum(2, 3, 4, 5)  # Here we passed all the arguments properly

print("Total:", total)
print("Total_I:", total_I)
print("Total_II:", total_II)

# Example of a function with *args parameter:

def sum_I(num1, num2, *args):
    # Calculates the sum of the provided numbers including additional arguments
    total = num1 + num2
    for num in args:
        total += num
    return total

# Example usage of the function with *args parameter:
total_III = sum_I(2, 3, 4, 4, 5, 6, 7)  # Here we pass two required arguments and any number of additional arguments

print("Total_III:", total_III)

# Note:
# - Default parameters allow you to specify default values for parameters in case they are not provided when the function is called.
# - *args is used to pass a variable number of arguments to a function. It collects any number of positional arguments into a tuple.
# - A tuple is an immutable sequence data type in Python, represented by parentheses ().
