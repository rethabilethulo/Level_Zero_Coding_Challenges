def maximum(x , y, z):
    if (x >= y) and (x >= z):
        biggest = x

    elif (y >= x) and (y >= z):
        biggest = y   

    else:
        biggest = z

    return biggest

"""Main code"""


print("Maximum number is",maximum(20, 5, 10))