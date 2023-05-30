# Initialize max and count variables
max = None
count = 0

# Read integers until an empty input is provided
while True:
    try:
        num = input("Enter a Number(or  Enter to 0 End): ")
        if num == "0":
            break
        num = int(num)

        # Update max and count variables
        if max is None or num > max:
            max = num
            count = 1
        elif num == max:
            count += 1
    except ValueError:
        print("Please enter a valid integer.")

# Print the result
if max is not None:
    print(f"The largest number is {max}.")
    print(f"The occurrence count of the largest number is {count}.")
else:
    print("No Numbers were entered.")
