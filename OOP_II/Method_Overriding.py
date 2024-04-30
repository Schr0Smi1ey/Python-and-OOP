""" 
Method Overriding: Method overriding allows a subclass (derived class) to redefine the behavior of a method inherited from its superclass (base class).

Key Points:

* Methods must have the same name and parameter list (signature).At compile time, the compiler checks if the method signature matches the superclass's method.
* Inheritance is required for overriding.
* The overriding method can have a different return type (covariant return types in some languages).
* Achieves runtime polymorphism, where the appropriate method is chosen at runtime based on the object's actual type.
"""

# Base class Shape
class Shape:
    def __init__(self, name):
        self.name = name
    
    # Generic method to calculate area
    def area(self):
        print('Area of a generic Shape')

    # Generic method to calculate perimeter
    def perimeter(self):
        print('Perimeter of a generic Shape')

# Derived class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        # Call the constructor of the superclass (Shape)
        super().__init__(name)
    
    # Method Overriding: Redefining area calculation for rectangles
    def area(self):
        print(f'Area of {self.name} is {self.length * self.width}')

    # Method Overriding: Redefining perimeter calculation for rectangles
    def perimeter(self):
        print(f'Perimeter of {self.name} is {2 * (self.length + self.width)}')

# Derived class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        # Call the constructor of the superclass (Shape)
        super().__init__(name)
    
    # Method Overriding: Redefining area calculation for circles
    def area(self):
        print(f'Area of {self.name} is {3.14 * (self.radius ** 2)}')
    
    # Method Overriding: Redefining perimeter calculation for circles
    def perimeter(self):
        print(f'Perimeter of {self.name} is {2 * 3.14 * self.radius}')

# Creating an instance of Rectangle
rect = Rectangle('Rectangle', 30, 40)
# Calling overridden method area() for Rectangle
rect.area()
# Calling overridden method perimeter() for Rectangle
rect.perimeter()

# Creating an instance of Circle
cir = Circle('Circle', 25)
# Calling overridden method area() for Circle
cir.area()
# Calling overridden method perimeter() for Circle
cir.perimeter()
