def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from user
n = int(input("Enter a positive integer: "))

# Check if the input is positive
if n < 0:
    print("Error: Input must be a positive integer")
else:
    # Calculate the factorial using the recursive function
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
