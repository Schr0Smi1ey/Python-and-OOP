class Book:
    def __init__(self, name) -> None:
        self.name = name
    # - The Book class defines an abstract method read() with the NotImplementedError raised.
    def read(self):
        raise NotImplementedError  # This will raise an error, meaning derived classes must implement this method

# - The Physics class inherits from the Book class and implements the read() method.
class Physics(Book):
    def __init__(self, name, Lab) -> None:
        super().__init__(name)
        self.Lab = Lab
    
    def read(self):
        print("Reading Physics book")

# - An instance of the Physics class is created with the name 'Topon' and Lab set to True.
topon = Physics('Topon', True)

topon.read()  # Output: Reading Physics book

# Check if Physics is a subclass of Book
print(issubclass(Physics, Book))  # Output: True

# Check if topon is an instance of Physics
print(isinstance(topon, Physics))  # Output: True

# Check if topon is an instance of Book
print(isinstance(topon, Book))  # Output: True

# Explanation:
# - The issubclass() function checks if a class is a subclass of another class and returns boolean result
# - The isinstance() function checks if an object is an instances of a class and returns the boolean result