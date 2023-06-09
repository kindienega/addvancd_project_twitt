def per(n):

    devisor = []
    for i in range(1, n):
        if n % i == 0 :
    devisor.append(i)
    return sum(devisor) == n

