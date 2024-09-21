"""
Write a program that lets the user play the game of Rock, Paper, Scissors against the com-
puter. The program should work as follows:
1. When the program begins, a random number in the range of 1 through 3 is generated.
If the number is 1, then the computer has chosen rock. If the number is 2, then the
computer has chosen paper. If the number is 3, then the computer has chosen scissors.
(Don’t display the computer’s choice yet.)
2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
3. The computer’s choice is displayed.
4. A winner is selected according to the following rules:
• If one player chooses rock and the other player chooses scissors, then rock wins.
(Rock smashes scissors.)
• If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
• If one player chooses paper and the other player chooses rock, then paper wins.
(Paper wraps rock.)
• If both players make the same choice, the game must be played again to determine
the winner.
"""
import random

def main():
    computer = randomiser(1, 3)
    user = input('Enter your choice of “rock,” “paper,” or “scissors” at the keyboard: ')
    gamer = userchoice(user)
    print(f'Computer chose: {computerchoice(computer)}')
    winner(computer, gamer)

def randomiser(min, max): # modified from C5PE20
    rand = random.randint(min, max)
    return rand

def userchoice(choice):
    while (choice == 'rock' or 'paper' or 'scissors'):    
        if (choice == 'rock'):
            return 1
        elif (choice == 'paper'):
            return 2
        elif (choice == 'scissors'):
            return 3
        else: # initially it was if elif else, but this seems better
            choice = input(f'{choice} was an invalid choice. Enter your choice of “rock,” “paper,” or “scissors” at the keyboard: ')

def computerchoice(choice):
    if (choice == 1):
        return 'rock'
    elif (choice == 2):
        return 'paper'
    else:
        return 'scissors'    
    
def winner(comp, user): # 1 rock 2 paper 3 scissors
    if (comp == user):
        print("It's a tie! Let's play again!")
        main() # hehe recursive function idk
    elif (comp == 1):
        if(user == 2): 
            print("User wins by using paper to beat rock!")
        else:
            print("Computer wins by using rock to beat scissors!")
        return False
    elif (comp == 2):
        if(user == 1):
            print("User wins by using rock to beat paper!")
        else:
            print("Computer wins by using paper to beat scissors!")        
        return False    
    else:
        if(user == 1):
            print("User wins by using rock to beat scissors!")
        else:
            print("Computer wins by using paper to beat rock!")
        return False
                    
main()