n = int(input())
s = input()
arr = list(map(int,s.split()))

maxima = -100000000
minima = 100000000
i = j = -1
for k in range(n):
    if arr[k] > maxima:
        maxima = arr[k]
        i = k
    if arr[k] < minima:
        minima = arr[k]
        j = k

arr[i],arr[j] = arr[j],arr[i]
for num in arr:
    print(num,end=' ')