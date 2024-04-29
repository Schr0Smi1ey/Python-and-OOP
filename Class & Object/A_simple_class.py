class phone:
    # Class attribute representing the the phone
    price = 19000
    brand = "Samsung" 

# Creating an instance of the phone class
my_phone = phone()

# Accessing and printing class attributes using the instance
print(my_phone.price)  # Output: 19000
print(my_phone.brand)  # Output: Samsung
print(my_phone.camera)  # Output: 32

# classes in OOP:
# a class is a blueprint for creating objects (instances).
# It defines the properties (attributes) and behaviors (methods) that all objects of that class will have.


# In this example, the 'phone' class defines attributes such as 'price', 'brand', and 'camera',
# which are shared by all instances of the class.
# When an instance of the class is created ('my_phone'), it inherits these attributes from the class definition.
# Each instance of the class can then have its own unique values for these attributes, but they are based on the blueprint provided by the class.

