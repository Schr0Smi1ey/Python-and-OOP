# Using a generic exception handler
try:
    # Attempt to perform an operation that may raise any type of exception
    result = 10 / 0
    print("Result:", result)  # This line will not be executed
except Exception as e:
    print("An error occurred:", e)  # Handle any exception
finally:
    print("Exception Handled") # This block always executes, regardless of whether an exception occurred or not.
