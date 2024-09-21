"""
One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
of feet as an argument and returns the number of inches in that many feet. Use the function
in a program that prompts the user to enter a number of feet then displays the number of
inches in that many feet.
"""

def main():
    feet = int(input('Insert a number of feet: '))
    inches = multiplication(feet, 12)
    print(f'{feet} feet = {inches} inch')

def multiplication(multiplicand, multiplier): # stolen from C5PE9, assume this as feet_to_inches
    product = multiplicand * multiplier
    return product

main()