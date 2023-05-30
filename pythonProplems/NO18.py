def compute_exponential(x):
    result = 1.0  # initialize the result to 1.0
    term = 1.0  # initialize the first term to 1.0
    i = 1  # initialize the counter to 1

    while abs(term) > 1e-8:  # keep computing terms until they are smaller than 1e-8
        term *= x / i  # compute the next term
        result += term  # add the next term to the result
        i += 1  # increment the counter

    return result

x = 4.0
result = compute_exponential(x)
print(f"e^{x} = {result}")

