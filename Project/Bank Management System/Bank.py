class Bank:
    __users = {}
    __admins = {}
    __totalBankBalance = 0
    __totalLoanAmount = 0
    __LoanFeature = True
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address
        
    @classmethod
    def loginUser(cls,accountNumber,password):
            if accountNumber in cls.__users:
                if cls.__users[accountNumber].password == password:
                    print()
                    return cls.__users[accountNumber]
                else:
                    print('Incorrect Password')
                    return None
            else:
                print('Account not found')
                return None
    @classmethod
    def loginAdmin(cls,accountNumber,password):
            if accountNumber in cls.__admins:
                if cls.__admins[accountNumber].password == password:
                    print()
                    return cls.__admins[accountNumber]
                else:
                    print('Incorrect Password')
                    return None
            else:
                print('Admin Account not found')
                return None
            
    @classmethod
    def getUsers(cls):
        return cls.__users

    @classmethod
    def getAdmins(cls):
        return cls.__admins
    
    @classmethod
    def getTotalBankBalance(cls):
        return cls.__totalBankBalance

    @classmethod
    def setTotalBankBalance(cls, amount):
        if amount >= 0:
            cls.__totalBankBalance += amount
        else:
            print("Invalid Amount.")

        

    @classmethod
    def getTotalLoanAmount(cls):
        return cls.__totalLoanAmount
    
    @classmethod
    def setTotalLoanAmount(cls, amount):
        if amount >= 0:
            cls.__totalLoanAmount += amount
        else:
            print("Invalid Amount.")
    
    @classmethod
    def deleteUser(cls,accountNumber):
        if accountNumber in cls.__users:
            del cls.__users[accountNumber]
            print(f'Account number {accountNumber} deleted successfully')
        else:
            print('User not found')
    
    @classmethod
    def setLoanFeature(cls,flag):
        if flag == True:
            if cls.__LoanFeature == False:
                cls.__LoanFeature = True
                print('Loan Feature ON Successfully.')
            else:
                print('Loan Feature is ON already.')
        else:
            if cls.__LoanFeature == True:
                cls.__LoanFeature = False
                print('Loan Feature OFF Successfully.')
            else:
                print('Loan Feature is OFF already.')
    
    @classmethod
    def getLoanStatus(cls):
        return cls.__LoanFeature