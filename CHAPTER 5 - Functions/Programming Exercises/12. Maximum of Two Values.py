"""
Write a function named max that accepts two integer values as arguments and returns the
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
the function, the function should return 12. Use the function in a program that prompts the
user to enter two integer values. The program should display the value that is the greater
of the two.
"""

def main():
    number1 = int(input('Insert number #1: '))
    number2 = int(input('Insert number #2: '))
    greater = max(number1, number2)
    print(f'{greater}')

def max(num1, num2):
    if(num1 >= num2):
        return num1
    else:
        return num2
    
main()