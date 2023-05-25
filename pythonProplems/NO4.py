def Line(m: float, b: float, x: float) -> float:
    """
    Computes the y-coordinate associated with the line specified by the slope m and
    y-intercept b at the given x-coordinate.
    
    Args:
    - m (float): the slope of the line
    - b (float): the y-intercept of the line
    - x (float): the x-coordinate for which to compute the y-coordinate
    
    Returns:
    - float: the y-coordinate associated with the line at the given x-coordinate
    """
    return m*x + b

slope = 5.0
yintercept = 10.0
xintercept = 2.0


yintercept = Line(slope, yintercept, xintercept)

print(f"The y-intercept of a line with slope {slope}, y-intercept {yintercept} and x-intercept {xintercept} is: {yintercept}")