def full_name(first_name, last_name):
    # Concatenating first and last name
    name = f'{first_name} {last_name}'
    return name

# Case I: Passing arguments in serial order
my_name = full_name('Sarafat', 'Karim')
print("My name:", my_name)

# Case II: Passing arguments not in serial order but as key-value pairs
her_name = full_name(last_name="Ahmed", first_name="Sumaiya")
print("Her name:", her_name)


# **kwargs: Passing a variable number of parameters as key-value pairs

def prof_name(first_name, last_name, **kwargs):
    name = f'{first_name} {last_name}'
    print("Additional info:")
    for key,value in kwargs.items():
        print(key + ' : ' + value)  # Printing all key-value pairs in kwargs
    return name

name = prof_name('Sarafat', 'Karim', title='SDE', department='Computer Science', experience='10 years')


# Multiple return values
def math_op(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

    return add, sub, mul   # Returning multiple values as a tuple. It could also be returned as a list.

# Unpacking the tuple returned by math_op
results = math_op(3, 4)
print("\nMath operations results:")
for result in results:
    print(result, end=' ')
