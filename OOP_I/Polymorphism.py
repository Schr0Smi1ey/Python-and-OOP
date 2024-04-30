class Animal:
    def __init__(self,name):
        self.name = name
    
    def Make_Sound(self):
        print('Animal Making Sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def Make_Sound(self):  
        print('Meow Meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def Make_Sound(self):
        print('Ghew Ghew')

class Rat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def Make_Sound(self):
        super().Make_Sound() # Will call the base class (Make_Sound()) method

don = Cat('Real Don')
don.Make_Sound()

sheffard = Dog('Local Sheffard')
sheffard.Make_Sound()

ress = Rat('pess')
ress.Make_Sound()



