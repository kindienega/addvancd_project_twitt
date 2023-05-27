
#  Write a flat method triangle() that computes the area of a triangle using its two formal parameters h and w, where h is the height and we is the length of the buses of the triangle.

def triangle(h, w):
    """
    Compute the area of a triangle given its height and base length.
    """
    return 0.5 * h * w

height = 5.0
width = 10.0

area = triangle(height, width)


print(f"The area of a triangle with height {height} and width {width} is: {area}")