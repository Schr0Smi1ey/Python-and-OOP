# Encapsulation ----> Encapsulation refers to the bundling of data and methods that operate on the data into a single unit or class. 
# It allows data to be hidden and only accessible through designated methods, thus protecting the integrity of the data.

# Access Modifiers ----> Access modifiers are keywords in object-oriented programming languages that specify the accessibility of classes, 
# methods, and attributes. In Python, access modifiers are implemented using naming conventions and are not enforced by the language itself.

class Bank:
    def __init__(self, Holder_name, initial_deposit):
        self.holder_name = Holder_name  # public attribute accessible from outside the class
        self.__balance = initial_deposit  # private attribute accessible only within the class
        self._Branch = 'Banani'  # protected attribute accessible within the class and its subclasses

    def get_balance(self):
        return self.__balance  # Getter method to access the private attribute

    def deposit(self, amount):
        self.__balance += amount  # Modify the private attribute
        return f'Your new balance is : {self.__balance}'  # Return a message with the updated balance

Sarafat = Bank('Sarafat', 500)
# print(Sarafat.__balance) # This will throw an error because __balance is a private attribute
print(Sarafat.holder_name)  # Access the public attribute directly
print(Sarafat.get_balance())  # Access the private attribute using the getter method
print(Sarafat._Branch)  # Access the protected attribute directly, although it's recommended to use getters and setters for consistency

# Explanation:
# - Encapsulation ensures that the internal state of an object is protected from outside interference.
# - Access modifiers like public, private, and protected help in controlling the visibility of attributes and methods.
# - In this example, holder_name is a public attribute accessible from outside the class.
# - __balance is a private attribute accessible only within the class, and it's accessed using a getter method get_balance().
# - _Branch is a protected attribute, typically used to denote attributes or methods that are intended for internal use within the class or its subclasses.
# - Using encapsulation and access modifiers promotes data integrity, reduces code complexity, and enhances code maintainability.
