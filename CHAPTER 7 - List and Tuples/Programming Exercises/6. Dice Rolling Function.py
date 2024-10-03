"""
In a program, write a function named roll that accepts an integer argument number_
of_throws. The function should generate and return a sorted list of number_of_throws
random numbers between 1 and 6. The program should prompt the user to enter a positive
integer that is sent to the function, and then print the returned list.
"""
                  
import random

def main():
    throws = int(input('How many dice throws would you like? '))
    if throws > 0:
        dices = roll(throws)
        print(f'Sorted dice throws = {dices}')
    else:
        print('What about a positive number? ')
    
def roll(number_of_throws):
    dice = [0] * number_of_throws
    for i in range(number_of_throws):
        dice[i] = random.randint(1, 6)    
    
    dice.sort()
    
    return dice
    
main()