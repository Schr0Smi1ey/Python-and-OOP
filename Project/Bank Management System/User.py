from Bank import *

class User(Bank):
    def __init__(self,userName,email,password,address,accountType) -> None:
        self.userName = userName
        self.password = password
        self.email = email
        self.address = address
        self.accountType = accountType
        self.accountNumber = len(super().getUsers()) + 1
        self.history = []
        self.bankRupt = False
        self.type = 'User'
        self.__transaction = 1
        self.__loanTaken = 0
        self.__balance = 0
        self.__loan = 0
        self.__transferAmount = 0
        super().getUsers()[self.accountNumber] = self

    def __str__(self) -> str:
        return f'Account Number: {self.accountNumber} ¦ UserName: {self.userName} ¦ Email: {self.email} ¦ Address: {self.address}¦'
    
    @property
    def getBalance(self):
        return self.__balance
    
    @getBalance.setter
    def setBalance(self,balance):
        self.__balance = balance

    @property
    def getLoan(self):
        return self.__loan
    
    @property
    def getTransferAmount(self):
        return self.__transferAmount
    
    @property
    def isBankRupt(self):
        return self.bankRupt
    
    
    def deposit(self,amount):
        if(self.bankRupt):
            print('You are Bankrupt.')
            return ''
        if(amount >= 0):
            self.__balance += amount
            Bank.setTotalBankBalance(amount)
            self.history.append(f'{self.__transaction}. Deposited {amount} tk in account.')
            self.__transaction += 1
        else:
            print('Invalid Amount.')

    def withdraw(self,amount):
        if(self.bankRupt):
            print('You are Bankrupt.')
            return
        if(amount >= 0 and amount <= self.__balance):
            self.__balance -= amount
            self.history.append(f'{self.__transaction}. Withdrawn {amount} tk from account.')
            self.__transaction += 1
            print(f'{amount} withdrawn successfully.')
        else:
            if amount < 0:
                print('Invalid Amount.')
            else:
                print('Withdrawal amount exceeded.')
    
    def transferAmount(self,accountNumber,amount):
        if(self.bankRupt):
            print('You are Bankrupt.')
            return
        if(accountNumber in super().getUsers() and accountNumber != self.accountNumber):
            if(amount >= 0 and amount <= self.__balance):
                self.__balance -= amount
                super().getUsers()[accountNumber].__balance += amount
                self.history.append(f'{self.__transaction}. Transferred {amount} tk to {Bank.getUsers()[accountNumber]}.')
                self.__transaction += 1
                print(f'{amount} tk transferred to [{super().getUsers()[accountNumber]}] successfully.')
            else:
                if amount < 0:
                    print('Invalid amount.')
                else:
                    print('You don\'t have enough balance.')
        else:
            if(accountNumber == self.accountNumber):
                print('You can\'t transfer to your own account.')
            else:
                print('Account does not exist.')


    def takeLoan(self,amount):
        if(self.bankRupt):
            print('You are Bankrupt.')
            return
        if self.__loanTaken < 2:
            self.__loan += amount
            self.__loanTaken += 1
            self.__balance += amount
            Bank.setTotalLoanAmount(amount)
            self.history.append(f'{self.__transaction}. Loan taken {amount} tk.')
            self.__transaction += 1
            print(f'{amount} tk loan taken successfully.')
        else:
            print('You have already taken 2 loans.')
            
    

    def showTransactionHistory(self):
        if(len(self.history) == 0):
            print('No transaction history.')
            return
        
        for transaction in self.history:
            print(transaction)