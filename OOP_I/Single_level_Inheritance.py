# Define a base class Gadget representing common attributes of electronic gadgets
class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    # Override __repr__ method to provide a string representation of the object
    def __repr__(self):
        return f'{self.brand} costs {self.price} and is {self.color} in color. It is made in {self.origin}'

# Define a child class Phone inheriting from Gadget
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, camera, charger):
        super().__init__(brand, price, color, origin)  # Initialize attributes from the base class
        self.camera = camera
        self.charger = charger
     
    # Method specific to Phone class
    def make_call(self):
        return f'{self.brand} is making a call.'
    
    # Override __repr__ method to include Phone-specific attributes
    def __repr__(self):
        return super().__repr__() + f' and has {self.camera} MP camera and {self.charger} W charger.'

# Define another child class Laptop inheriting from Gadget
class Laptop(Gadget):
    def __init__(self, brand, price, color, origin, ssd, OLED, charger):
        super().__init__(brand, price, color, origin)  # Initialize attributes from the base class
        self.ssd = ssd
        self.OLED = OLED
        self.charger = charger
    
    # Methods specific to Laptop class
    def coding(self):
        return f'{self.brand} is coding'

    def webDev(self):
        return f'{self.brand} is developing a website'
    
    # Override __repr__ method to include Laptop-specific attributes
    def __repr__(self):
        return super().__repr__() + f' and has {self.ssd} GB SSD and OLED display({self.OLED}) and {self.charger} W charger.'

# Creating an object of Phone
my_phone = Phone('Samsung', 35000, 'Black', 'India', 64, 67)
print(my_phone)  # Output the representation of the phone object
print(my_phone.make_call())  # Output the result of making a call using the phone

# Creating an object of Laptop
my_laptop = Laptop('Asus', 89000, 'Black', 'China', 512, True, 67)
print(my_laptop)  # Output the representation of the laptop object
print(my_laptop.coding())  # Output the result of coding using the laptop
print(my_laptop.webDev())  # Output the result of web development using the laptop

# Single inheritance: Refers to a class hierarchy where a derived class inherits from only one base class. Here, Phone and Laptop inherit from the base class Gadget.
# super() keyword: Used to call methods from the base class. In this code, it's used to invoke the __init__ method of the base class in the child classes.
# Base class (or parent class): Gadget class serves as the base class from which the Phone and Laptop classes inherit common attributes and behaviors.
# Derived class (or child class): Phone and Laptop classes are derived classes that inherit attributes and behaviors from the base class Gadget.


"""  
a base class, also known as a parent class or superclass:

    * Holds common attributes and behaviors.
    * Serves as a template for creating derived classes.
    * Allows for code reuse by providing shared functionality.
    * Is inherited by other classes, called derived or child classes.
"""