num = int(input("Enter a positive integer number: "))  # read input from user

if num < 0:  # check if number is negative
    print("Please enter a positive integer number.")
else:
    reversed_num = 0
    while num > 0:
        digit = num % 10  # extract the last digit
        reversed_num = reversed_num * 10 + digit  # add the digit to the reversed number
        num //= 10  # remove the last digit
    print("The reversed number is:", reversed_num)
