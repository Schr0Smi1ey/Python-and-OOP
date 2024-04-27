ans = []
str = input()
l = r = cnt = last = 0
for i in range(len(str)):
    if str[i] == 'R':
        r += 1
    else:
        l += 1
    if r == l:
        cnt += 1
        ans.append(str[last:i+1])
        r = l = 0
        last = i + 1
    i += 1
print(cnt)
for s in ans:
    print(s)