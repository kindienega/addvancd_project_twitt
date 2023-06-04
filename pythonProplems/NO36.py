decimal = int(input("Enter a decimal integer: ")) # prompt the user to enter a decimal integer
hexadecimal = '' # initialize a string to store the hexadecimal value

# convert the decimal integer to hexadecimal by repeated division by 16
while decimal > 0:
    remainder = decimal % 16 # get the remainder
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal # convert the remainder to a string and prepend it to the hexadecimal string
    else:
        hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal # convert the remainder to a hexadecimal digit and prepend it to the hexadecimal string
    decimal //= 16 # divide the decimal integer by 16 (integer division)

print("The hexadecimal value is:", hexadecimal) # display the hexadecimal value
