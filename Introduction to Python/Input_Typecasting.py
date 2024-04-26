firstMoney = input("From Sarafat: ")
secondMoney = input("From Karim: ")
Total = firstMoney + secondMoney
print("Total Money I got: ", Total)

# Note: In Python, the default input type is string. So, here firstMoney and secondMoney are taking input as strings.
# This means if we input 100 for firstMoney and 200 for secondMoney, Total will be '100200' (a concatenation of strings).

print(type(firstMoney))
print(type(secondMoney))

# To treat firstMoney and secondMoney as integers, we need to explicitly typecast them.

Total_int = int(firstMoney) + int(secondMoney)

print("Total Money: ", Total_int)
