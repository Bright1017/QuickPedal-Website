import math

# As an exercise, write a function called nineLines that uses
# threeLines to print nine blank lines. How would you print twentyseven new lines?

# count = 0

# print ("First Line.")
# threeLines()
# print ("Second Line.")


# def newline():
#     global count
#     print(1)
#     count += 1

# def threelines():
#     newline()
#     newline()
#     newline()



# def ninelines():
#     threelines()
#     threelines()
#     threelines()

# def twentyseven_lines():
#     ninelines()
#     ninelines()
#     ninelines()

# twentyseven_lines()
# print("Total lines printed:", count)

# def printtwice(bruce):
#     print(bruce, bruce)

# # chika = "i'm going to be a good backend developer"

# # printtwice(chika)

# def catTwice(part1, part2):
#     cat = part1 + part2
#     printtwice(cat)

# chant1 = "i want to be a "
# chant2 = "developer"
# catTwice(chant1,chant2)



# def countdown(n):
#     if n == 0:
#         print("we've gotten to the end of the countdown")
    
#     else:
#         print(n)
#         countdown(n-1)
        
# countdown(10)

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(4))

# count = 0

# def newline():
#     global count
#     count += 1


# def fourLines():
#     newline()
#     newline()
#     newline()
#     newline()
# fourLines()

# # 
# def nLines(n):
#     while n > 0:
#         print(n)
#         n = n-1
#     print("You've gotten to the end of the countdown")

# nLines(count)


"""
As an exercise, write a compare function that returns 1 if
x > y, 0 if x == y, and -1 if x < y.
"""

# sol

# def compare(x,y):
#     if x > y: # this will check if the obj value in x variable is greater than y variable
#         return 1
#     elif x == y: # this will check if both variable have the same values 
#         return 0
#     else:
#         if x < y: # this will check if the obj value in x variable is less than y variable
#             return -1
        
# compare()

# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n-1
#     print('Blastoff!')

# countdown(10)

# def sequence(n):
#     while n != 1:
#         print(n),
    
#     if n%2 == 0:
#         n = n/2
#     else:
#         n = n*3+1
# sequence(3)

# x = 1.0
# while x < 10.0:
#     print(x), '\t', math.log(x)/math.log(2.0)
#     x = x + 1.0

# fruit = "banana"
# index = 0

# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1


# fruit = "banana"
# letter = fruit[1]
# print(letter)