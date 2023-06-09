
n = int(input("pls enter int :  "))

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
#total = 0
def sum_of(n):
    total = 0
    for i in range(1, n+1):
        tt = fact(i)
        total += tt
    return total
#sum_of(n)
print(sum_of(n))


