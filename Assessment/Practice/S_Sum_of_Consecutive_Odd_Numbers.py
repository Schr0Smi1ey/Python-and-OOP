def solve():
    s = input()
    x,y = map(int,s.split())
    if x > y:
        x,y = y,x
    sum = 0
    for i in range(x + 1,y , 1):
        if i % 2 == 1:
            sum += i
    print(sum)

t = int(input())
while t > 0:
    solve()
    t -= 1