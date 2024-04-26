s = input() # first take whole input as a string
a , b = map(int,s.split()) # then split it as int(separated by space) and assign to variable
arr = []
for i in range(a,b+1,1):
    n = i
    flag = True
    while n > 0:
        x = n % 10
        if x != 4 and x != 7:
            flag = False
            break
        n //= 10 # need to perform floor division
    if flag:
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    for num in arr:
        print(num,end=' ')