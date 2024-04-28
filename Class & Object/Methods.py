class Phone:
    # Class attributes (shared among all instances of the class)
    Brand = "SamSung"
    price = 19000  # Price of the phone
    color = "Black"  # Color of the phone
    camera = 32  # Camera megapixels
    features = ['camera','battery','Display']  # List of features

    # Method to make a call
    def make_call(self):
        print("Call Done")
    # Method to send SMS
    def send_message(self,phone,message):
        text = f"Sent SMS to {phone} with the message {message}"
        return text
# Creating an instance of the Phone class
my_phone = Phone()

# Calling the make_call method of the Phone class using the instance
my_phone.make_call()

# Calling the send_message method of the Phone class using the instance
message = my_phone.send_message(1234567,"HEllO, I LOVE YOU")
print(message)

"""
Explanation:
- Class: A blueprint for creating objects(instances).In this case, the Phone class defines the structure and behavior of phones.
- Class attributes: Data that is shared among all instances of the class.These are accessed using the class name.
- Method: Functions defined within a class that perform operations on the object's data or interact with the object in some way. Here, make_call is a method of the Phone class.
- Instance: A specific realization of a class.my_phone is an instance of the Phone class.
- self: A reference to the instance itself. It is the first parameter of instance methods,must be include in each method and is automatically passed when calling the method.
- Accessing attributes and calling methods: Attributes and methods of a class are accessed using the dot notation (e.g., my_phone.make_call()).
"""
