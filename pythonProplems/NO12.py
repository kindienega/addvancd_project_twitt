# Prompt user to enter the size of the list
size = int(input("Enter the size of the list: "))

# Initialize an empty list to hold the numbers
numbers = []

# Prompt user to enter each number in the list
for i in range(size):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the maximum and minimum values in the list
max_num = max(numbers)
min_num = min(numbers)

# Display the maximum and minimum values
print(f"Maximum value: {max_num}")
print(f"Minimum value: {min_num}")
