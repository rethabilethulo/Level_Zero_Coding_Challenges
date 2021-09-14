def triangle(x,y,z):

    """Calculating the semi-perimeter(s)"""
    s = (x + y + z) * 0.5

    """Calculating the area"""
    area = (s * (s - x) * (s - y) *(s - z)) ** 0.5

    return area

triangle(2,3,4)