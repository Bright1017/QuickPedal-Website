# import math

# def area(redius):
#     temp = math.pi * redius ** 2
#     return temp

# print(f"As an exercise, write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.")


# def compare(x,y):
#     if x > y:
#         return 1
    
#     elif x == y:
#         return 0
    
#     else:
#         return -1
    
"""
As an exercise, write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2).
Then use this function in a function called intercept(x1, y1, x2,
y2) that returns the y-intercept of the line through the points (x1,
y1) and (x2, y2).
"""
# solving slope

# def slope(x1,y1,x2,y2):
#     pointA= x2 - x1
#     pointB = y2 - y1

#     result = (pointB) / (pointA)
#     return result

# def intercept(xi,yi,x2,y2):
#     return slope()



# slope(1,2,4,6)

""" As an exercise, write a compare function that returns 1 if
x > y, 0 if x == y, and -1 if x < y.

solve
"""

def compare(x,y):
    if x > y:
        print(1)
    elif x == y:
        print(0)
    else:
        if x < y:
            print("-1")

compare(2,3)