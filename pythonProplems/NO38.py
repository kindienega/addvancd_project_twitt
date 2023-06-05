def isPrime(n):
    """
    This function takes an integer n as input and returns True if n is prime, or False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
x = int(input("Enter an integer: "))
result = isPrime(x)
print(result)