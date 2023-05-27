def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

x = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(x))

if is_prime(x):
    print(f"{x} is a prime number and the sum of its digits is {digit_sum}.")
else:
    print(f"{x} is not a prime number and the sum of its digits is {digit_sum}.")


