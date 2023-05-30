def sum_of_cubes(low, high):
    for num in range(low, high+1):
        digit_sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            digit_sum += digit ** 3
            temp //= 10
        if digit_sum == num:
            print(num)
result = sum_of_cubes(100, 1000)