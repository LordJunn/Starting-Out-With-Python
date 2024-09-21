"""Write a program that generates a random number in the range of 1 through 100, and asks
the user to guess what the number is. If the user’s guess is higher than the random number,
the program should display “Too high, try again.” If the user’s guess is lower than the
random number, the program should display “Too low, try again.” If the user guesses the
number, the application should congratulate the user and generate a new random number
so the game can start over.

Optional Enhancement: Enhance the game so it keeps count of the number of guesses that
the user makes. When the user correctly guesses the random number, the program should
display the number of guesses.
"""
import random

def main():
    killswitch = ''
    while(killswitch != 'n'):
        game()
        killswitch = input('Would you like to play again? Press "n" if not, anything else if yes. ')

def game():
    counter = 0
    num = randomiser()
    guess = 0
    while (guess != num):
        guess = intchecker(1, 100)
        counter += 1 # ori was adding 1 in each if else, but here would be better
        if (guess == num):
            print('Win!')
            print(f'Total guesses made: {counter}')
        elif(guess > num):
            print('Too high, try again.')
        else:
            print('Too low, try again.')   

def randomiser(): # stolen from C5PE16
    rand = random.randint(1, 100)
    return rand

def intchecker(min, max): # ok yea this seems useful
    x = int(input('Guess what the number is: '))
    while((x < min) or (x > max)):
        x = int(input(f"Enter a bigger number, bigger than {min}, but smaller than {max}. "))
    return x


main()