# Defining a list of numbers
numbers = [1, 1, 1, 2, 6, 3, 4, 5]

# Append(value): Add a value to the end of the list - O(1)
numbers.append(6)
print("After append 6:", numbers)

# Insert(index, value): Insert a value at a specific index - O(n)
numbers.insert(0, 0)
print("After insert 0 at index 0:", numbers)

# Remove(value): Remove the first occurrence of a value in the list - O(n)
if 6 in numbers:  # Checking if 6 is in the list
    numbers.remove(6)  # Removing the first occurrence of 6
print("After removing 6:", numbers)

# Pop(): Remove and return the last element of the list - O(1)
numbers.pop()
print("After popping the last element:", numbers)

# Index(value): Return the index of the first occurrence of a value in the list - O(n)
ind = numbers.index(1)  # Finding the index of the first occurrence of 1
print("Index of 1:", ind)

# Count(value): Count the number of occurrences of a value in the list - O(n)
cnt = numbers.count(1)  # Counting the occurrences of 1
print("Number of 1s in the list:", cnt)

# Sort(): Sort the list in ascending order - O(n log n)
numbers.sort()
print("After sorting:", numbers)

# Reverse(): Reverse the elements of the list in place - O(n)
numbers.reverse()
print("After reversing the list:", numbers)
