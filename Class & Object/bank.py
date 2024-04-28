class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000000

    def get_balance(self):
        return f'Your Balance is : {self.balance}'
    
    def deposit(self,amount):
        if(amount > 0):
            self.balance += amount
            print(f'Amount {amount} deposited successfully')
            print("Your current balance is : ",self.balance)
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'You can\'t withdraw less than {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You can\'t withdraw greater than {self.max_withdraw}')
        else:
            if amount < self.balance:
                self.balance -= amount
                print(f'Amount {amount} withdrawn successfully')
                print("Your current balance is : ",self.balance)
            else:
                print(f'Your main balance({self.balance}) is less than {amount}')

Brac = Bank('Sarafat',12000)
print(Brac.get_balance())
Brac.withdraw(50)
Brac.withdraw(10000000000000)
Brac.withdraw(20000)
Brac.withdraw(4000)
Brac.deposit(1000)
Brac.deposit(3000)
