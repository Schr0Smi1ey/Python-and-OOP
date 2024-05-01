n = int(input())
s = input()
arr = list(map(int,s.split()))
ans = 0
while all(num % 2 == 0 for num in arr) and all(num != 0 for num in arr):
    ans += 1
    for i in range(n):
        arr[i] //= 2
print(ans)