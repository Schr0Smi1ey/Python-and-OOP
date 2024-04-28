class Calculator:
    Brand = 'Casio'  # Class attribute defining the brand of the calculator

    # Method to add two numbers
    def add(self, a, b):
        return a + b

    # Method to multiply two numbers
    def mul(self, a, b):
        return a * b

    # Method to divide two numbers (floor division)
    def div(self, a, b):
        return a // b

    # Method to subtract one number from another
    def subt(self, a, b):
        return a - b

# Creating an instance of the Calculator class
my_calculator = Calculator()

# Performing arithmetic operations using the methods of the Calculator class
print("Adding 3 and 4:", my_calculator.add(3, 4))
print("Multiplying 3 and 4:", my_calculator.mul(3, 4))
print("Dividing 3 by 4:", my_calculator.div(3, 4))
print("Subtracting 3 from 4:", my_calculator.subt(3, 4))
