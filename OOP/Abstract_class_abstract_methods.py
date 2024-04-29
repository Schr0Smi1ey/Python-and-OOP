from abc import ABC, abstractmethod  # To use abstract class in Python, import ABC, abstractmethod from abc
# abc ---> Abstract Base Class
# abstract method ----> These are the methods present in a base class that must be implemented independently in the derived class.

class Animal(ABC):
    @abstractmethod  # This decorator makes the following function behave as an abstract method
    def eat(self):
        print('I am Eating')
    
    @abstractmethod
    def move(self):
        print('I am Moving')

class Monkey(Animal):  # Monkey inherits Animal: Monkey class must implement the eat and move methods of the Animal class
    def __init__(self, name):
        self.name = name
        super().__init__()  # Initialize the attributes of the base class
    
    def eat(self):
        print("I am eating Banana")
    
    def move(self):
        print("I am moving from tree to tree")

oley = Monkey('Lucky')
oley.eat()
oley.move()

# Explanation:
# - Abstract Base Class (ABC) allows us to define abstract methods, which are methods that must be implemented by subclasses.
# - Abstract methods are declared using the @abstractmethod decorator, and they do not provide any implementation in the base class.
# - In this example, the Animal class is an abstract base class with abstract methods eat() and move().
# - The Monkey class inherits from the Animal class and implements the eat() and move() methods according to its specific behavior.
# - If a class inherits from an abstract base class and does not implement all the abstract methods defined in the base class, it will also be considered abstract.
# - Using abstract classes and methods helps in defining a common interface for a group of related classes and ensures that specific behavior is implemented in subclasses.
