class Shop:
    cart = []  # Class attribute shared by all instances of the class

    # Constructor to initialize instance variables
    def __init__(self, buyer):
        self.buyer = buyer  # Instance attribute unique to each instance
        self.cart_in = []   # Instance attribute unique to each instance

    # Method to add an item to the cart
    def add_to_cart(self, item):
        self.cart.append(item)  # Adding item to the class attribute cart
        self.cart_in.append(item)  # Adding item to the instance attribute cart_in

# Creating an instance of the Shop class for 'sarafat'
sarafat = Shop('Sarafat')
sarafat.add_to_cart('Shirt')
sarafat.add_to_cart('Shoe')

# Printing the contents of cart and cart_in for 'sarafat'
print(sarafat.cart)    # Output: ['Shirt', 'Shoe']
print(sarafat.cart_in) # Output: ['Shirt', 'Shoe']

# Creating another instance of the Shop class for 'sumaiya'
sumaiya = Shop('Sumaiya')
sumaiya.add_to_cart('Dress')
sumaiya.add_to_cart('Bag')

# Printing the contents of cart and cart_in for 'sumaiya'
print(sumaiya.cart)    # Output: ['Shirt', 'Shoe', 'Dress', 'Bag']
print(sumaiya.cart_in) # Output: ['Dress', 'Bag']

# Note about class attributes and instance attributes
# - Class attributes are variables defined within a class that are shared among all instances of the class.
# - Instance attributes are variables specific to each instance of the class.
# - In this example, 'cart' is a class attribute shared by all instances, while 'cart_in' is an instance attribute unique to each instance.
# - Modifications to the class attribute 'cart' affect all instances, while modifications to the instance attribute 'cart_in' are specific to each instance.
