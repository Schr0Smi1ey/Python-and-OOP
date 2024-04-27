""" 
a tuple is a collection of ordered and immutable elements enclosed within parentheses (). 
Tuples are similar to lists but with one key difference: tuples cannot be modified after creation, 
making them immutable data structures.
"""

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing Elements
print("Accessing Elements:")
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 'c'
print()

# Tuple Packing and Unpacking
print("Tuple Packing and Unpacking:")
packed_tuple = 1, 2, 3  # Packing
x, y, z = packed_tuple  # Unpacking
print("Unpacked Values:", x, y, z)
print()

# Immutable Nature
print("Immutable Nature:")
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)
print()

# Common Operations
print("Common Operations:")
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

# Concatenation
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Repetition
repeated_tuple = ('hello',) * 3
print("Repeated Tuple:", repeated_tuple)

# Membership Testing
print("Membership Testing:", 1 in (1, 2, 3))
print()

# Use Cases
print("Use Cases:")
# Returning multiple values from a function
def get_coordinates():
    return 10, 20

x_coord, y_coord = get_coordinates()
print("Coordinates:", x_coord, y_coord)
print()

# Storing fixed collections of data
student1 = ('John', 20, 'Male')
student2 = ('Alice', 22, 'Female')
print("Student 1:", student1)
print("Student 2:", student2)
print()

# As keys in dictionaries
population_by_city = {('New York', 'NY'): 8_623_000, ('Los Angeles', 'CA'): 3_979_000}
print("Population of New York:", population_by_city[('New York', 'NY')])



# Methods : 

Tp = (1, 2, 3, 4, 5)

# 1. Count(value): Count the number of occurrences of a value in the tuple - O(n)
cnt = Tp.count(3)  # Counting the occurrences of 3
print("Number of 3s in the tuple:", cnt)

# 2. Index(value): Return the index of the first occurrence of a value in the tuple - O(n)
ind = Tp.index(4)  # Finding the index of the first occurrence of 4
print("Index of 4:", ind)

# 3. Tuple slicing: Accessing a subset of elements using slicing - O(k)
subset = Tp[1:4]  # Get elements from index 1 to 3
print("Subset:", subset)

# 4. Tuple concatenation: Combining two tuples - O(m+n)
another_tuple = (6, 7, 8)
concatenated_tuple = Tp + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# 5. Tuple repetition: Repeating the elements of a tuple - O(n)
repeated_tuple = Tp * 2
print("Repeated tuple:", repeated_tuple)
