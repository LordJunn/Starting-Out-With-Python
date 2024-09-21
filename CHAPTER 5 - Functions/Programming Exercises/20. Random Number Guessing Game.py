"""Write a program that generates a random number in the range of 1 through 100, and asks
the user to guess what the number is. If the user’s guess is higher than the random number,
the program should display “Too high, try again.” If the user’s guess is lower than the
random number, the program should display “Too low, try again.” If the user guesses the
number, the application should congratulate the user and generate a new random number
so the game can start over.
"""
import random

def main():
    killswitch = ''
    while(killswitch != 'n'):
        game()
        killswitch = input('Would you like to play again? Press "n" if not, anything else if yes. ')

def game():
    num = randomiser()
    guess = 0
    while (guess != num):
        guess = int(input('Guess what the number is: '))
        if (guess == num):
            print('Win!')
        elif(guess > num):
            print('Too high, try again.')
        else:
            print('Too low, try again.')    

def randomiser(): # stolen from C5PE16
    rand = random.randint(1, 100)
    return rand

main()