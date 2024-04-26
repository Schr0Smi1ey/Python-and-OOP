# list,array, collection all mean the same

# Defining a list of numbers
# Index:   0  1  2  3  4  5  6  7  8
numbers = [1, 5, 4, 3, 3, 4, 5, 6, 6]
# Index:  -9 -8 -7 -6 -5 -4 -3 -2 -1

# Accessing elements by positive and negative indices
print("Index 3:", numbers[3])   # Accessing element at index 3
print("Index -3:", numbers[-3])  # Accessing element at index -3

# Printing the entire list of numbers
print(numbers)

# Slicing the list: list[start:end] -----> start(inclusive), end(exclusive)
print(numbers[2:6])  # Printing elements from index 2 to 5

# Slicing the list with step: list[start:end:step] -----> start(inclusive), end(exclusive), step(each move)
print(numbers[1:7:1])   # Will print elements from index 1 to 6
print(numbers[1:7:2])   # Will print elements with odd indices from index 1 to 5
print(numbers[2:7:-1])  # Will print an empty list since start > end when step is negative
print(numbers[7:2:-1])  # Will print elements from index 7 to 3 in reverse order
print(numbers[7:2:-2])  # Will print every alternate element from index 7 to 3 in reverse order
print(numbers[4:])      # Will print elements from index 4 to the end of the list
print(numbers[:6])      # Will print elements from the beginning of the list to index 5
print(numbers[:])       # Will print the entire list
print(numbers[::-1])    # Will print the entire list in reverse order (shortcut for reverse printing)

