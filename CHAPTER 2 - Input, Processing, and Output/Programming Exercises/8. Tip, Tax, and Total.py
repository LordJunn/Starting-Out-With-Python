"""
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, then calculate the amounts
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
"""

food = float(input('The charge for the food? '))
tip = food * 0.18
tax = food * 0.07
total = food + tip + tax

print('Tip = $', format(tip, '.2f'))
print('Tax = $', format(tax, '.2f'))
print('Total = $', format(total, '.2f'))