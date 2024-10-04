"""
Write a program that asks the user to enter a series of single-digit numbers with nothing
separating them. The program should display the sum of all the single digit numbers in the
string. For example, if the user enters 2514, the method should return 12, which is the sum
of 2, 5, 1, and 4.
"""

def main():
    number = input('Enter a string of numbers: ')
    total = sum(number)
    print(f'Sum of numbers: {total}')
    
def sum(number):
    total = 0
    for i in number: # each char becomes an int, gets added
        total += int(i)
    
    return total

main()