# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a Python file handling example.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending new line.\n")

# Reading line by line
with open("example.txt", "r") as file:
    print("\nFile content line by line:")
    for line in file:
        print(line.strip())

# Error handling
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print("Error : ",e)
