n = int(input())
s = input()
arr = list(map(int,s.split()))
mp = {}
for num in arr:
    mp[num] = mp.get(num,0) + 1
ans = 0
for key,value in mp.items():
    if key > value:
        ans += value
    else:
        ans += value - key
print(ans)

# Using mp.get(num, 0) to get the value associated with the key 'num' in dictionary 'mp'.
# If 'num' doesn't exist in 'mp', returns 0 as the default value.
