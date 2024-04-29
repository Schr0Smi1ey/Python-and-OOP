class Bank:
    def __init__(self, name, balance):
        self.name = name  # Instance variable storing the account holder's name
        self.balance = balance  # Instance variable storing the account balance
        self.min_withdraw = 100  # Minimum withdrawal limit
        self.max_withdraw = 1000000  # Maximum withdrawal limit

    def get_balance(self):
        return f'Your Balance is : {self.balance}'  # Method to get the account balance
    
    def deposit(self, amount):
        if amount > 0:  # Check if the deposit amount is positive
            self.balance += amount  # Update the account balance
            print(f'Amount {amount} deposited successfully')
            print("Your current balance is : ", self.balance)

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You can\'t withdraw less than {self.min_withdraw}')  # Check if withdrawal amount is less than the minimum limit
        elif amount > self.max_withdraw:
            print(f'You can\'t withdraw greater than {self.max_withdraw}')  # Check if withdrawal amount is greater than the maximum limit
        else:
            if amount <= self.balance:  # Check if withdrawal amount is less than or equal to the account balance
                self.balance -= amount  # Update the account balance after withdrawal
                print(f'Amount {amount} withdrawn successfully')
                print("Your current balance is : ", self.balance)
            else:
                print(f'Your main balance ({self.balance}) is less than {amount}')  # Insufficient balance for withdrawal

# Creating an instance of the Bank class
Brac = Bank('Sarafat', 12000)

# Printing the account balance using the get_balance method
print(Brac.get_balance())

# Trying different withdrawal and deposit scenarios
Brac.withdraw(50)    # Output: "You can't withdraw less than 100"
Brac.withdraw(10000000000000)    # Output: "You can't withdraw greater than 1000000"
Brac.withdraw(20000)    # Output: "Amount 20000 withdrawn successfully"
Brac.withdraw(4000)    # Output: "Amount 4000 withdrawn successfully"
Brac.deposit(1000)    # Output: "Amount 1000 deposited successfully"
Brac.deposit(3000)    # Output: "Amount 3000 deposited successfully"
