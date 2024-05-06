from Bank import *
from User import *
from Admin import *
from Data import *



print('                     ###############################################################')
print(f'                   ############### Welcome to {janata.name} ####################')
print('                     ###############################################################')


def createAccount(self):
    print('------------------Creating User Account------------------')
    print()
    userName = input('Enter User Name: ')
    email = input('Enter Email: ')
    password = input('Enter Password: ')
    address = input('Enter Address: ')
    accountType = input('Enter Account Type(Savings or Current): ')
    print()
    username = admin.createAccount(userName,email,password,address,accountType)
    print(username)
    print(f'Account Created Successfully.')
    
def test(self,type):
    print()
    print('-----------------------Login-----------------------')
    print()
    if(type == 'user'):
        accountNumber = int(input('                 Enter Account Number: '))
        password = input('                       Enter Password: ')
        user = Bank.loginUser(accountNumber,password)
        return user
    else:
        adminId = int(input('                 Enter Admin ID: '))
        password = input('                 Enter Password: ')
        admin = Bank.loginAdmin(adminId,password)
        return admin
    
def userLogin(self,type):
    print()
    print('Please log in to continue')
    if(type == 'user'):
        print('(AcNum:1,Pass:test): ')
    else:
        print('(adminID:1,pass:test): ')
    user = test(None,type)
    while user == None:
        print('---------------------------------------------------')
        print('press [y] to try again')
        if(type == 'user'):
            print('press [c] to create account')
        print('press [n] to exit')
        print('---------------------------------------------------')
        choice = input('Enter your choice: ')
        if choice == 'y':
            user = test(None,type)
            if user != None:
                break
        elif choice == 'c':
            createAccount(None)
        elif choice == 'n':
            flag = True
            break
        else:
            print('Invalid Choice')
        continue
    return user


def adminPanel(self):
    print('------------------Admin Panel------------------')
    adminTemp = userLogin(None,'admin')
    if adminTemp is None:
        return None
    else:
        print(f'Logged in into account [{adminTemp}] Successfully.')
        print('---------------------------------------------------')
        print()
    while True:
        print()
        print('1. Create User Account')
        print('2. Delete User Account')
        print('3. Show Users List')
        print('4. Total Bank Balance')
        print('5. Total Loan Amount')
        print('6. Set User Bankrupt')
        print('7. ON/OFF Loan Feature')
        print('8. Exit')
        print()

        choice = int(input('Enter your choice: '))
        print()
        if choice == 1:
            createAccount(None)
        elif choice == 2:
            print('------------------Delete User Account------------------')
            print()
            accountNumber = int(input('Enter User Account Number: '))
            print()
            admin.deleteAccount(accountNumber)
        elif choice == 3:
            print('-------------------Users List-------------------')
            print()
            admin.showUsersList()
        elif choice == 4:
            print('-----------------------------------------------')
            admin.totalBankBalance()
        elif choice == 5:
            print('-----------------------------------------------')
            admin.totalLoanAmount()
        elif choice == 6:
            print('------------------Set Bankrupt------------------')
            print()
            accountNumber = int(input('Enter Account Number: '))
            admin.setBankRupt(accountNumber)
        elif choice == 7:
            print('-------------------')
            print('To [ON] press \'y\'')
            print('To [OFF] press \'n\'')
            print(f'Current Loan Feature Status is: {Bank.getLoanStatus()}')
            print('-------------------')
            choice = input('Enter your choice: ')
            flag = False
            if choice == 'y':
                flag = True
            admin.loanFeature(flag)
        elif choice == 8:
            print()
            break
        print('---------------------------------------------------')
        print()


def userPanel(self):
    print('------------------User Panel------------------')
    user = userLogin(None,'user')
    if user is None:
        return None
    else:
        print(f'Logged in into account [{user}] Successfully.')
        print('---------------------------------------------------')
        print()
    while True:
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Transfer Money')
        print('4. Take Loan')
        print('5. Show Balance')
        print('6. Show Loan')
        print('7. Show Transfer Amount')
        print('8. Show Transaction History')
        print('9. Exit')
        print('---------------------------------------------------')
        print()
        choice = int(input('Enter your choice: '))
        print()
        if choice == 1:
            print('------------------Deposit------------------')
            amount = int(input('Enter Amount: '))
            user.deposit(amount)
            print(f'{amount} tk deposited successfully.')
        elif choice == 2:
            print('------------------Withdraw------------------')
            amount = int(input('Enter Amount: '))
            user.withdraw(amount)
        elif choice == 3:
            print('------------------Transfer Amount------------------')
            accountNumber = int(input('Enter Account Number you want to transfer: '))
            amount = int(input('Enter Amount: '))
            user.transferAmount(accountNumber,amount)
        elif choice == 4:
            print('------------------Take Loan------------------')
            if Bank.getLoanStatus() == False:
                print('Bank currently not offering any Loan.Thank You!')
                print('---------------------------------------------------')
                continue
            amount = int(input('Enter Amount: '))
            user.takeLoan(amount)
        elif choice == 5:
            print('------------------Show Balance------------------')
            print(f'Your Balance is: {user.getBalance} tk.')
        elif choice == 6:
            print('------------------Show Loan------------------')
            print(f'Your Loan is: {user.getLoan} tk.') 
        elif choice == 7:
            print('------------------Show Transfer Amount------------------')
            print(f'Your Transfer Amount is: {user.getTransferAmount}.')
        elif choice == 8:
            print(f'-----------Transaction History[acNum:{user.accountNumber}]------------')
            user.showTransactionHistory()
        elif choice == 9:
            break
        else:
            print('Invalid Choice.')
        print('---------------------------------------------------')
        print()

def main():
    while True:
        print('---------------------------------------------------')
        print()
        print('1. Admin Panel')
        print('2. User Panel')
        print('3. Exit')
        print()
        choice = int(input('Enter your choice: '))
        print()
        if choice == 1:
            adminPanel(None)
        elif choice == 2:
            userPanel(None)
        elif choice == 3:
            break
        else:
            print('Invalid Choice.')

if __name__ == '__main__':
    main()