class MathHelper:
    """A helper class for mathematical operations."""

    # Static attribute (shared across all instances)
    PI = 3.14159

    @staticmethod
    def is_even(number):
        """
        Checks if a number is even.

        Args:
            number: The number to check.

        Returns:
            True if the number is even, False otherwise.
        """
        return number % 2 == 0

    @classmethod
    def get_circle_area(cls, radius):
        """
        Calculates the area of a circle.

        Args:
            radius: The radius of the circle.

        Returns:
            The area of the circle.
        """
        return cls.PI * radius**2

# Accessing static attribute (no instance needed)
print(f"Value of PI: {MathHelper.PI}")

# Using static method (no instance needed)
number = 10
if MathHelper.is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Creating an instance
helper = MathHelper()  # Not required for static methods and attributes
print(helper.PI)  # Accessing static attribute using an instance
print(helper.get_circle_area(6)) # Using class method through an instance
print(MathHelper.get_circle_area(6))

# Using class method through the class
circle_radius = 5
circle_area = MathHelper.get_circle_area(circle_radius)
print(f"Area of circle with radius {circle_radius}: {circle_area:.2f}")



""" 
    Static Attribute (PI):
        - The PI attribute is a static attribute that is shared across all instances of the MathHelper class.
        - Static attributes are defined using the class name and can be accessed without creating an instance of the class.
        - Accessed directly using the class name (e.g., MathHelper.PI).
    
    Static Method (is_even):
        - Defined using the @staticmethod decorator.
        - Doesn't receive any implicit arguments like self or cls means it can't modify the instance attribute.
        - Acts like a regular function within the class namespace.
        - Useful for utility functions that don't operate on the class or its instances.
        - Called directly using the class name (e.g., MathHelper.is_even(number)).
    
    Class Method (get_circle_area):
        - Defined using the @classmethod decorator.
        - Receives the class itself as the first argument (cls).
        - Can access class attributes and call other class methods.
        - Useful for creating factory methods or alternative constructors.
        - Called using the class name or an instance (e.g., MathHelper.get_circle_area(radius)).
"""