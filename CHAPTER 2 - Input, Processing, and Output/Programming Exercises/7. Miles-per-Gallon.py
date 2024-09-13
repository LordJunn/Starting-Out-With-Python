"""
A car's miles-per-gallon (MPG) can be calculated with the following formula:
MPG = Miles driven / Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car's MPG and display the result.
"""

miles = float(input('The number of miles driven? '))
gas = float(input('The gallons of gas used? '))

MPG = miles/gas

print("The car's miles-per-gallon = ", MPG)
