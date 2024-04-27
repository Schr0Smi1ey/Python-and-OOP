# sum function

sum = lambda x,y : x + y
print("sum of 5,6 : ",sum(5,6))

double_it = lambda x : x*2
nums = [1,2,3,4,5,6,7]
print("Before doubled : ",nums)
doubled = map(double_it,nums)
print("After double : ",list(doubled))

square = map(lambda x : x * x,nums)
print("After Square : ",list(square))

actors = [
    {'Name' : 'Sarafat karim','Age' : 21},
    {'Name' : 'Nayeem Hossen','Age' : 23},
    {'Name' : 'Hadidur Rahman','Age' : 20},
    {'Name' : 'Muhaiminum Shaad','Age' : 25},
    {'Name' : 'Sajjad Karim','Age' : 30},
]

new_list = filter(lambda x : x['Age'] % 5 == 0,actors)
print(list(new_list))