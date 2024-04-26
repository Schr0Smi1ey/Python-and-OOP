n = int(input())
i = 0
while i < n:
    s = input()
    print(' '.join(s[::-1])) # ' '.join() ----> to add space after every element
    i += 1
