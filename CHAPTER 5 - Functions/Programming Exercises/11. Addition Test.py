"""
Write a program that generates printable addition tests. The tests should consist of 5 ques-
tions which present a simple addition question in the following format, where the question
number goes from 1 to 5, and num1 and num2 are randomly generated numbers between
1 and 10:
Question 1
num1 + num2 = _____
The program should simply display the 5 questions – it should not prompt the user for any
input.
"""
import random

MIN = 1
MAX = 10

def main():
    for owo in range(1, 6):
        questioner(owo)

def questioner(number):
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    
    print(f'Question {number}')
    print(f'{num1} + {num2} = ______')
    print()
    
main()