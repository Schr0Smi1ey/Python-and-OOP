from Bank import *
from User import *
class Admin(Bank):
    def __init__(self,userName,email,password,address):
        self.userName = userName
        self.email = email
        self.password = password
        self.address = address
        self.type = 'Admin'
        self.adminID = len(Bank.getAdmins()) + 1
        Bank.getAdmins()[self.adminID] = self

    def __str__(self) -> str:
        return f'AdminId: {self.adminID} UserName: {self.userName} Email: {self.email} Address: {self.address}'
    
    def createAccount(self,userName,email,password,address,accountType):
        User(userName,email,password,address,accountType)
    
    def deleteAccount(self,accountNumber):
        Bank.deleteUser(accountNumber)
    
    def showUsersList(self):
        for key,value in Bank.getUsers().items():
            print(value.__str__() + '\n')
    
    def totalBankBalance(self):
        print(f'Total Bank Balance is : {Bank.getTotalBankBalance()}')
    
    def totalLoanAmount(self):
        print(f'Total Loan Amount : {Bank.getTotalLoanAmount()}')

    def setBankRupt(self,accountNumber):
        if accountNumber in Bank.getUsers():
            Bank.getUsers()[accountNumber].bankRupt = True
            print(f'User [{Bank.getUsers()[accountNumber]}] set to Bankrupt successfully.')
        else:
            print('User not found')
    
    def deleteUser(self,accountNumber):
        if accountNumber in Bank.getUsers():
            del Bank.getUsers()[accountNumber]
        else:
            print('User not found')