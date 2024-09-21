"""
In this chapter, you saw an example of how to write an algorithm that determines
whether a number is even or odd. Write a program that generates 100 random numbers
and keeps a count of how many of those random numbers are even, and how many of
them are odd.
"""
import random

odd = 0
even = 0

def main():
    for count in range(100):
        number = randomiser()
        oddeven(number)
        
    print(f'Odd: {odd}, Even: {even}')

def randomiser():
    rand = random.randint(1, 1000)
    return rand

def oddeven(num):
    global odd
    global even
    
    if (num % 2 == 0):
        even += 1
    else:
        odd += 1
    
main()