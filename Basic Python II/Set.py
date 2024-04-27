"""  
    * set is an unordered collection of unique elements enclosed within curly braces {}. 
    * mutable, can add or remove elements
    * No indexing
    * No slicing
    * No duplicate
    * Support mathematical set operation
"""
# set ---> {}
# tuple ---> ()
# list ---> []



# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Adding elements to a set
set1.add(6)  # Adds element 6 to set1 (TC: O(1))

# Removing elements from a set
set1.remove(3)  # Removes element 3 from set1 (TC: O(1))

# Union of sets
union_set = set1.union(set2)  # Combines elements from set1 and set2 without duplicates (TC: O(len(set1) + len(set2)))
# union_set = set1 | set2 ---> another way to do union
# Intersection of sets
intersection_set = set1.intersection(set2)  # Finds common elements between set1 and set2 (TC: O(min(len(set1), len(set2))))
# intersection_set = set1 & set2 ---> another way to do intersection
# Difference of sets
difference_set = set1.difference(set2)  # Finds elements in set1 that are not in set2 (TC: O(len(set1)))

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)  # Finds elements that are in either set1 or set2, but not in both (TC: O(len(set1) + len(set2)))

# Membership testing
print("Is 4 in set1?", 4 in set1)  # Checks if 4 is in set1 (TC: O(1))
print("Is 9 in set1?", 9 in set1)  # Checks if 9 is in set1 (TC: O(1))

# Checking subset and superset
print("Is set1 a subset of set2?", set1.issubset(set2))  # Checks if set1 is entirely contained in set2 (TC: O(len(set1) + len(set2)))
print("Is set1 a superset of set2?", set1.issuperset(set2))  # Checks if set1 contains all elements of set2 (TC: O(len(set1) + len(set2)))

# Clearing a set
set1.clear()  # Removes all elements from set1 (TC: O(1))

# Creating a frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])  # Creates an immutable set (TC: O(n))


# Printing set
for i,item in enumerate(set2): # enumerate() : assigns an index to each item in an iterable
    print(i,item)
