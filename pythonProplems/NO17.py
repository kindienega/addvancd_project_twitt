
digits = input("Enter the first 9 digits of the ISBN: ")

# Check that the input is exactly 9 digits long
while len(digits) != 9:
    digits = input("Invalid input. Please enter 9 digits: ")

# Calculate the check sum
check_sum = 0
for i in range(9):
    check_sum += int(digits[i]) * (i + 1)

check_digit = check_sum % 11

# Check if check digit is 10 and replace with 'X'
if check_digit == 10:
    isbn = digits + 'X'
else:
    isbn = digits + str(check_digit)

print("The 10-digit ISBN is:", isbn.zfill(10))