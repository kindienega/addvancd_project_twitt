def count_primes(n):
    """
    Returns the number of primes between 2 and n (inclusive).
    """
    primes = [2]
    for i in range(3, n+1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes)
    
n = int(input("Enter a positive integer greater than 2: "))
num_primes = count_primes(n)
print("There are", num_primes, "primes between 2 and", n)
