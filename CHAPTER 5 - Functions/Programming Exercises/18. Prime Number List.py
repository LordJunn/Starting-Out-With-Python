"""
This exercise assumes that you have already written the is_prime function in Programming
Exercise 17. Write another program that displays all of the prime numbers from 1 to 100.
The program should have a loop that calls the is_prime function.
"""
import random

def main():
    for count in range(100):
        if is_prime(count):
            print(f"{count}")

def is_prime(num): # stolen from C5PE18
    if ((num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0)):
        if((num == 2) or (num == 3) or (num == 5) or (num == 7)):
            return True
        else:        
            return False
    else:
        return True
    
main()