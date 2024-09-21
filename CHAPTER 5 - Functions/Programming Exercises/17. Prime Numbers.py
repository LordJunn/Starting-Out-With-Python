"""
A prime number is a number that is only evenly divisible by itself and 1. For example, the
number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, how-
ever, is not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and
returns true if the argument is a prime number, or false otherwise. Use the function in
a program that prompts the user to enter a number then displays a message indicating
whether the number is prime.

TIP: Recall that the % operator divides one number by another and returns the
remainder of the division. In an expression such as num1 % num2, the % operator will
return 0 if num1 is evenly divisible by num2.
"""

def main():
    number = int(input('Enter a number: '))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

def is_prime(num):
    if ((num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0)):
        if((num == 2) or (num == 3) or (num == 5) or (num == 7)):
            return True
        else:        
            return False
    else:
        return True
    
main()