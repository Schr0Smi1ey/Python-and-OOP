# read only --> you can just read the value but can't set the value. value can not be changed.
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.


class User:
    def __init__(self,name,age,balance):
        self.name = name
        self.__age = age
        self.__balance = balance
    
    # Getter without any setter --> ReadOnly attribute
    @property
    def age(self):
        return self.__age
    
    # Getter
    @property
    def balance(self):
        return self.__balance
    
    # Setter
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            print('You can\'t add negative money')
        self.__balance += amount


karim = User('Karim',21,500)
print(karim.age)
# karim.age = 22  -------> This will throw an error
print(karim.balance)
karim.balance += 400
print(karim.balance)

""" 
    Getter:

    - Defined using the @property decorator.
    - Acts like an attribute when accessed (e.g., karim.age).
    - Returns the value of the private attribute (age).

    Setter:

    - Defined within the balance property using @balance.setter.
    - Receives a value (amount) as an argument.
    - Performs validation or operations before updating the private attribute.
    - In this case, ensures the amount is non-negative.

    Read-only Property:

    - Defined with @property but without a setter.
    - Can only be accessed like an attribute (e.g., karim.age).
    - Performs calculations or retrieves values based on the object's state.
    - Cannot be assigned a new value directly.
"""