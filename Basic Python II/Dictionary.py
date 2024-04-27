""" 
    Dictionaries are key-value pairs enclosed in {}.
    Unordered, mutable, keys must be immutable.
    Mapping unique keys to values. 
"""

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing elements
print("Accessing elements:")
print("Name:", my_dict['name'])  # Retrieves value for 'name' key (TC: O(1))

# Adding elements
my_dict['gender'] = 'Female'  # Adds 'gender' key with value 'Female' (TC: O(1))

# Updating elements
my_dict['age'] = 31  # Updates value for 'age' key (TC: O(1))

# Removing elements
del my_dict['city']  # Removes 'city' key and its value (TC: O(1))

# Iterating over dictionary
print("\nIterating over dictionary:")
for key,value in my_dict.items():  # Iterates over key-value pairs (TC: O(n))
    print(key, ":", value)

print("\nIterating over dictionary with index :")
for i,key,value in enumerate(my_dict.values()):  # enumerate() : assigns an index to each item in an iterable
    print(i, ":", value) 

# Dictionary methods
print("\nDictionary methods:")
print("Keys:", my_dict.keys())  # Returns keys as a view (TC: O(n))
print("Values:", my_dict.values())  # Returns values as a view (TC: O(n))
print("Items:", my_dict.items())  # Returns key-value pairs as a view (TC: O(n))
print("Get:", my_dict.get('name'))  # Returns value for 'name' key (TC: O(1))
print("Pop:", my_dict.pop('age'))  # Removes 'age' key and returns its value (TC: O(1))
print("Updated dictionary:", my_dict)

# Clearing the dictionary
my_dict.clear()  # Clears all key-value pairs (TC: O(1))
print("After clearing the dictionary:", my_dict)
