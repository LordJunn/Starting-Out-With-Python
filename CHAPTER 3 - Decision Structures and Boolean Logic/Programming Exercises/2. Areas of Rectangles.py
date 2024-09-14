"""
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectan-
gle has the greater area, or if the areas are the same.
"""

l1 = int(input('Enter the length of rectangle #1: '))
w1 = int(input('Enter the width of rectangle #1: '))
a1 = l1 * w1

l2 = int(input('Enter the length of rectangle #2: '))
w2 = int(input('Enter the width of rectangle #2: '))
a2 = l2 * w2

if (a1 == a2):
    print('The areas are the same.')
elif(a1 > a2):
    print('The first rectangle has the greater area.')
else:
    print('The second rectangle has the greater area.')