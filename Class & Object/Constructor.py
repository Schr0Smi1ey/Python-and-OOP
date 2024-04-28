class Phone:
    manufacturer = "China"  # Class attribute defining the manufacturer

    # Constructor method to initialize instance variables
    def __init__(self, owner, brand, price):
        self.owner = owner  # Instance variable for the owner of the phone
        self.brand = brand  # Instance variable for the brand of the phone
        self.price = price  # Instance variable for the price of the phone

    # Method to make a call to a given person
    def make_call(self, person):
        print("Calling:", person)


# Creating an instance of the Phone class for 'my_phone'
my_phone = Phone("Sarafat", "Redmi", 34000)

# Printing details of 'my_phone'
print("Owner:", my_phone.owner)
print("Brand:", my_phone.brand)
print("Price:", my_phone.price)

# Creating another instance of the Phone class for 'Her_phone'
her_phone = Phone("Sumaiya", "Realme", 18000)

# Printing details of 'Her_phone'
print("Owner:", her_phone.owner)
print("Brand:", her_phone.brand)
print("Price:", her_phone.price)

# Making a call from 'my_phone' to 'Her_phone'
my_phone.make_call("Sumaiya")

# Making a call from 'Her_phone' to 'my_phone'
her_phone.make_call("Sarafat")


# Note about the constructor : 

# The __init__ method is a special method in Python classes called a constructor.
# It is automatically called when a new instance of the class is created.
# It initializes the instance variables with the values passed during object creation.
