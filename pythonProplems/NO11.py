phone_number = input("Enter a 9-digit phone number: ")

# Check that the input is exactly 9 digits long
while len(phone_number) != 9:
    phone_number = input("Invalid input. Please enter a 9-digit phone number: ")

if phone_number[0] == '9':
    print("Mobile")
else:
    print("Fixed phone")
