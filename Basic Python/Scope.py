# Global variable
balance = 5000

def buy(item, price):
    # Local Variable
    dream_phone = 'xPhone'

    # To modify the global variable, declare it as global
    global balance

    # We can only access the global variable without using global keyword,But to modify we must first declare it as global before any use
    print('Previous Balance Value:', balance)
    balance -= price  # Now we can modify the global variable
    print(f'Balance after buying {item}:', balance)

# Trying to access a local variable globally will result in an error
# print(dream_phone)

# Function call
buy('New headphones', 200)
