# Element access in array

numbers = [10,20,30,40,50]

for num in numbers:
    print(num ,end=' ')   # Using end=' ' to print with a space after each element

print('\n')
# Element access in string
message = "I Love You"

for char in message:
    print(char,end= ' ')

print('\n')

# Range Based For loop

for i in range(1,10,1):
    print(i,end= ' ')

print('\n')

for i in range(0,5,1):
    print(numbers[i] ,end=' ') 


""" 
    'end' in print() determines the character printed after the output. 
    Default is '\n', meaning a newline, starting the next print on a new line. 
"""
