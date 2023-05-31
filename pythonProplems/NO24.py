def find_proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number(n):
    divisors = find_proper_divisors(n)
    if sum(divisors) == n:
        return True
    else:
        return False

# test for perfect numbers less than 10000
perfect_numbers = []
for i in range(1, 10000):
    if is_perfect_number(i):
        perfect_numbers.append(i)

print("Perfect numbers less than 10000:", perfect_numbers)

# get input from user
num = int(input("Enter a positive integer: "))

# check if the number is perfect and print its proper divisors
divisors = find_proper_divisors(num)
if sum(divisors) == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
print("Proper divisors of", num, "are:", divisors)
