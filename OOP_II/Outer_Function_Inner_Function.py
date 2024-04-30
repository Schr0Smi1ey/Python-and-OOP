# Define the outer function
def outer_function():
    """
    Outer function that encapsulates and returns the inner function.
    """
    print("Initializing the outer function")

    # Define the inner function
    def inner_function():
        """
        Inner function that performs some specific task.
        """
        print("Inside the inner function")
        return 42

    # Return the inner function from the outer function
    return inner_function

# Call the outer function to obtain the inner function and then execute the inner function with another ()
print("Result returned by the inner function:", outer_function()())

# Define a function that takes another function as an argument
def perform_task(task):
    """
    Function that takes another function as an argument and executes it.

    Args:
        task (function): The function to be executed.
    """
    print("Performing a task")
    result = task()
    print("Task completed with result:", result)

# Call the function that takes another function as an argument
inner = outer_function()
perform_task(inner)
