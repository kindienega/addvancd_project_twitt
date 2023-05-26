def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# get input from user
number = int(input("Enter a Number: "))

# check if input is valid
if number < 0:
    print("Invalid input. Number entered must be a positive integer.")
else:
    # calculate and print Fibonacci value
    result = fibonacci(number)
    print(f"The Fibonacci value of {number} is {result}")
