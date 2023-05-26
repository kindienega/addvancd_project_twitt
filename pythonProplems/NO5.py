import math 
def intersect(m1, b1, m2, b2):
    # Check if the lines are parallel
    if m1 == m2:
        return 0
    
    # Calculate the intersection point
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    
    # Return 1 if the intersection point is finite, otherwise return 0
    if not math.isinf(x) and not math.isinf(y):
        return 1
    else:
        return 0
result= intersect(10,6,10,7)
print(result)