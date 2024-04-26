# Simple if-else statement
if (x := 5) > 7:
    print("x is greater than 7")
else: 
    print("x is less than or equal to 7")

# If-else ladder
Karim, Rahim, Saraf = True, False, False

if Rahim:
    print("It's Rahim")
elif Karim:
    print("It's Karim")
elif Saraf:
    print("It's Saraf")
else:
    print("No one")

# Nested if-else statement
a = 10
b = 5
c = 20

if a > b:
    if a > c:
        print("a is the largest")
    else:
        print("c is the largest")
else:
    if b > c:
        print("b is the largest")
    else:
        print("c is the largest")

