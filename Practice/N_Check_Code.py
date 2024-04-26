s = input()
a,b = map(int,s.split())

s = input()
cnt = s.count('-')
if(cnt == 1 and s[a] == '-'):
    print("Yes")
else:
    print("No")