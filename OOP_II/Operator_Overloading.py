"""  
    Operator Overloading: Operator overloading allows programmers to define custom behavior for operators (like +, -, *, ==, etc.) when used with objects of a particular class.

    Key Points:
    * Operators are overloaded using special methods (often named using the operator symbol, e.g., __add__).
    * These special methods must have specific names according to the operator being overloaded (e.g., __add__ for the + operator).
    * Overloaded operators can only be used with objects of the same class or compatible types.

"""

"""  
Operator Overloading: Operator overloading allows programmers to define custom behavior for operators (like +, -, *, ==, etc.) when used with objects of a particular class.

Key Points:
* Operators are overloaded using special methods (often named using the operator symbol, e.g., __add__).
* These special methods must have specific names according to the operator being overloaded (e.g., __add__ for the + operator).
* Overloaded operators can only be used with objects of the same class or compatible types.
"""

# Class definition for Vector
class Vector:
    def __init__(self, X_Cord, Y_Cord) -> None:
        self.X_Cord = X_Cord
        self.Y_Cord = Y_Cord
    
    # '+' Operator overloading using the special method __add__()
    def __add__(self, other):
        # Check if 'other' is an instance of Vector
        if isinstance(other, Vector):
            # Return a new Vector instances with the sum of X_Cord and Y_Cord components
            return Vector(self.X_Cord + other.X_Cord, self.Y_Cord + other.Y_Cord)
    
    # '-' Operator overloading using the special method __sub__()
    def __sub__(self, other):
        # Check if 'other' is an instance of Vector
        if isinstance(other, Vector):
            # Return a new Vector instances with the difference of X_Cord and Y_Cord components
            return Vector(self.X_Cord - other.X_Cord, self.Y_Cord - other.Y_Cord)
        
    # String representation of the Vector object
    def __repr__(self) -> str:
        return f'({self.X_Cord},{self.Y_Cord})'

# Create two Vector objects
v1 = Vector(3, 4)
v2 = Vector(2, 6)

# Perform addition and subtraction operations using overloaded operators
print('v1 + v2 : ', v1 + v2)
print('v1 - v2 : ', v1 - v2)



"""  
Arithmetic Operators:
    Addition (+): __add__(self, other)
    Subtraction (-): __sub__(self, other)
    Multiplication (*): __mul__(self, other)
    Division (/): __truediv__(self, other)
    Floor Division (//): __floordiv__(self, other)
    Modulus (Remainder) (%): __mod__(self, other)
    Exponentiation (**): __pow__(self, other)
    Negation (Unary Minus) (-): __neg__(self)
    Absolute Value (abs()): __abs__(self)

Comparison Operators:
    Less Than (<): __lt__(self, other)
    Less Than or Equal to (<=): __le__(self, other)
    Equal to (==): __eq__(self, other)
    Not Equal to (!=): __ne__(self, other)
    Greater Than (>): __gt__(self, other)
    Greater Than or Equal to (>=): __ge__(self, other)

Assignment Operators (In-Place Operators):
    In-Place Addition (+=): __iadd__(self, other)
    In-Place Subtraction (-=): __isub__(self, other)
    In-Place Multiplication (*=): __imul__(self, other)
    In-Place Division (/=): __itruediv__(self, other)
    In-Place Floor Division (//=): __ifloordiv__(self, other)
    In-Place Modulus (%=): __imod__(self, other)
    In-Place Exponentiation (**=): __ipow__(self, other)

Unary Operators:
    Unary Positive (+): __pos__(self)
    Unary Negative (-): __neg__(self)
    Unary Absolute Value (abs()): __abs__(self)

Container Operators:
    Length (len()): __len__(self)
    Indexing ([]): __getitem__(self, key)
    Setting Item ([]): __setitem__(self, key, value)
    Deleting Item (del): __delitem__(self, key)
    Iteration (iter()): __iter__(self)
    Next Item (next()): __next__(self)

String Representation:
    Conversion to String (str()): __str__(self)
    Conversion to Representation String (repr()): __repr__(self)

Callables:
    Calling Objects (): __call__(self, *args, **kwargs)
    
"""