""" 
Strings are sequences of characters enclosed in quotes, either single (''), double ("") or triple ('''''' or """"""). 
They're immutable, so we can't change them once created, but we can make new ones from existing ones.
"""

# single quotes
single_string = 'Sarafat'
# double quotes
double_string = "Karim"
# triple quotes
triple_string = '''Sajjad'''


# accessing individual characters using indexing
print("single_string[0] : ",single_string[0])
print("double_string[-2] : ",double_string[-2])


# String Slicing -->(Like as List)
print("single_string[:4] : ",single_string[:4])
print("double_string[::-1] : ",double_string[::-1])
print("triple_string[:7] : ",triple_string[:7])


# string concatenation
new_string = single_string + ' ' + double_string
print("single_string + double_string : ", new_string)


# Multiple String
Mul_string = """ Imam Hossen
                Sajeda Begum
             """
print("Multiple String : ",Mul_string)


# Methods of String : 

String = "Hello, World!"

# 1. Length of the string - O(1)
print("Length of the string:", len(String))

# 2. Convert to uppercase - O(n)
print("Uppercase:", String.upper())

# 3. Convert to lowercase - O(n)
print("Lowercase:", String.lower())

# 4. Capitalize the string - O(n)
print("Capitalized:", String.capitalize())

# 5. Count occurrences of a substring - O(n)
print("Occurrences of 'l':", String.count('l'))

# 6. Check if the string starts with a particular substring - O(1)
print("Starts with 'Hello':", String.startswith("Hello"))

# 7. Check if the string ends with a particular substring - O(1)
print("Ends with 'World!':", String.endswith("World!"))

# 8. Find the index of a substring - O(n)
print("Index of 'World':", String.find("World"))

# 9. Replace a substring with another substring - O(n)
print("Replaced 'Hello' with 'Hi':", String.replace("Hello", "Hi"))

# 10. Split the string into a list based on a delimiter - O(n)
print("Split by comma:", String.split(","))

# 11. Join elements of a list into a string - O(n)
words = ["Hello", "World", "!"]
print("Join words:", "-".join(words))

# 12. Strip leading and trailing whitespace - O(n)
whitespace_string = "   Hello, World!   "
print("Stripped whitespace:", whitespace_string.strip())

# 13. Check if all characters are alphanumeric - O(n)
alphanumeric_string = "Hello123"
print("Is alphanumeric?", alphanumeric_string.isalnum())

# 14. Check if all characters are alphabetic - O(n)
alpha_string = "Hello"
print("Is alphabetic?", alpha_string.isalpha())

# 15. Check if all characters are digits - O(n)
digit_string = "123"
print("Is digit?", digit_string.isdigit())

# 16. Check if all characters are lowercase - O(n)
lowercase_string = "hello"
print("Is lowercase?", lowercase_string.islower())

# 17. Check if all characters are uppercase - O(n)
uppercase_string = "HELLO"
print("Is uppercase?", uppercase_string.isupper())

