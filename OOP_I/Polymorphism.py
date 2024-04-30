class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('Animal Making Sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):  
        print('Meow Meow')  # Override the make_sound() method with a cat-specific sound

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print('Ghew Ghew')  # Override the make_sound() method with a dog-specific sound

class Rat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        super().make_sound()  # Call the base class's make_sound() method

don = Cat('Real Don')
don.make_sound()  # Output: Meow Meow

sheffard = Dog('Local Sheffard')
sheffard.make_sound()  # Output: Ghew Ghew

ress = Rat('pess')
ress.make_sound()  # Output: Animal Making Sound (Calling the base class's make_sound() method)

# Polymorphism:
# - Polymorphism is a core concept in object-oriented programming that refers to the ability of different objects to respond to the same message or method invocation in different ways.
# - It allows objects of different classes to be treated as objects of a common superclass, and methods that are defined in the superclass can be called on objects of subclasses, exhibiting different behaviors based on the actual type of the object.
# - In this example, the make_sound() method is polymorphic, as it behaves differently depending on the type of the object it is called on.
# - Polymorphism promotes code reusability, flexibility, and maintainability by allowing for more generic and flexible code that can work with different types of objects without knowing their specific types at compile time.
