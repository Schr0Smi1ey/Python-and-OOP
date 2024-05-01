def solve():
    n = int(input())
    s = input()
    arr = list(map(int,s.split()))
    ans = 1000000000
    for i in range(n):
        for j in range(i+1,n,1):
            ans = min(ans,arr[i]+arr[j] + j - i)
    print(ans)

t = int(input())
while t > 0:
    solve()
    t -= 1