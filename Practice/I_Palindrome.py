def isPalindrome(s):
    ss = s[::-1]
    if ss[0] == 0:
        return False
    return ss == s

s = input()
ss = s[::-1]
ss = int(ss)
print(ss)
if(isPalindrome(s)):
    print("YES")
else:
    print("NO")