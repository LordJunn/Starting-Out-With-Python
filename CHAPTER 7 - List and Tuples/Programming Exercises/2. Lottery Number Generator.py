"""
Design a program that generates a seven-digit lottery number. The program should gener-
ate seven random numbers, each in the range of 0 through 9, and assign each number to a
list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
displays the contents of the list.
"""
import random

LOTTO = 7

def main():
    lottery = [0] * LOTTO # [0, 0, 0, 0, 0, 0, 0] works
    
    for rng in range(LOTTO):
        lottery[rng] = random.randint(0, 9)
        
    print("The winning numbers: " , end="")
    for display in range(LOTTO):
        print(lottery[display], end="")
    
main()