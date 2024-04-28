class Shop:
    def __init__(self, buyer):
        self.buyer = buyer  # Instance variable storing the buyer's name
        self.cart = []  # List to store items in the cart
        self.total_price = 0  # Total price of items in the cart
        self.total_item = 0  # Total number of items in the cart

    def add_to_cart(self, item, price, quantity):
        # Add item to cart along with its price and quantity
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})
        # Update total price and total item count
        self.total_price += price * quantity
        self.total_item += quantity
    
    def see_cart(self):
        # Print the items in the cart
        for item in self.cart:
            print(item)
    
    def remove_item(self, item):
        # Remove the specified item from the cart
        for i in self.cart:
            if i['item'] == item:
                self.cart.remove(i)
                self.total_item -= i['quantity']
                break
        print('Item removed successfully')
    
    def update_quantity(self, item, new_quantity):
        # Update the quantity of a specific item in the cart
        for i in self.cart:
            if i['item'] == item:
                # Update total price by subtracting the old price for the item and adding the new price
                self.total_price -= i['price'] * i['quantity']
                i['quantity'] = new_quantity
                self.total_price += i['price'] * new_quantity
                break

    def checkout(self, amount):
        # Process checkout and print the receipt
        if amount >= self.total_price:
            print('Payment Successful')
            print(f'Your total cost: {self.total_price}')
            print(f'Your total item number: {self.total_item}')
            print(f'Your change is {amount - self.total_price}')
            # Clear cart and reset total price and total item count
            self.cart.clear()
            self.total_price = 0
            self.total_item = 0
            print(f'Thank you for your shopping!')
        else:
            print(f'Insufficient amount. Please add more {self.total_price - amount} or remove some items')

# Creating an instance of the Shop class for 'buyer'
buyer = Shop('Sarafat Karim')

# Adding items to the cart
buyer.add_to_cart('Shirt', 500, 2)
buyer.add_to_cart('Bat', 5000, 1)
buyer.add_to_cart('Paper', 3, 75)
buyer.add_to_cart('Pen', 4, 6)
buyer.add_to_cart('Book', 5, 250)
buyer.add_to_cart('Perfume', 1, 400)

# Removing an item from the cart
buyer.remove_item('Bat')

# Updating the quantity of an item in the cart
buyer.update_quantity('Pen', 10)

# Viewing the cart
buyer.see_cart()
print()

# Checking out
buyer.checkout(8000)
