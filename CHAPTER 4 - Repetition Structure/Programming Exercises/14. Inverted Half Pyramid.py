"""
Write a program that uses nested loops to draw this pattern:
*******
******
*****
****
***
**
*
"""

BASE_SIZE = 7 # stolen from C4P19

for r in range(BASE_SIZE):
    for c in range(BASE_SIZE - r):
        print('*', end='')
    print() 