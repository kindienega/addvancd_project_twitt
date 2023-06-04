# Outer loop to iterate through rows
for i in range(1, 9):
    # Print spaces before the numbers
    print(" " * (16 - 2 * i), end="")
    # Inner loop to print the numbers in each row
    for j in range(0, i):
        print(2**j, end=" ")
    # Inner loop to print the numbers in each row (in reverse order)
    for k in range(i-2, -1, -1):
        print(2**k, end=" ")
    # Move to the next line after each row is printed
    print()
