def lcm(a, b):
    # find the greater number between a and b
    greater = max(a, b)
    # loop through multiples of greater number
    while True:
        # check if the current multiple is divisible by both a and b
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

# Example usage
print(lcm(12, 30)) 
