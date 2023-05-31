while True:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        break
    digits = len(str(num))
    print(f"The number of digits in {num} is {digits}.")
