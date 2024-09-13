"""
One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
the mass of an object in pounds and then calculates and displays the mass of the object in
kilograms.
"""

PtK = 0.454
pounds = float(input('Enter the mass of an object in pound: '))

kilograms = pounds * PtK

print('The mass of the object in kilograms is', kilograms)