import math

def approximate_euler(n):
    e = 1
    for i in range(1, n+1):
        e += 1/math.factorial(i)
    return e

n = int(input("Enter the number of terms to be used for approximation: "))
approx_e = approximate_euler(n)
print(f"The approximation of e using {n} terms is {approx_e}")
