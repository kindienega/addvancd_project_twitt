def triangle(h, w):
    """
    Compute the area of a triangle given its height and base length.
    """
    return 0.5 * h * w

height = 5.0
width = 10.0

area = triangle(height, width)

print(f"The area of a triangle with height {height} and width {width} is: {area}")