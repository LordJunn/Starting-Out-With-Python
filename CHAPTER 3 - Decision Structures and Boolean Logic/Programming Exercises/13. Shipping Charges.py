"""
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.50
Over 2 pounds but not more than 6 pounds $3.00
Over 6 pounds but not more than 10 pounds $4.00
Over 10 pounds $4.75
Write a program that asks the user to enter the weight of a package then displays the ship-
ping charges.
"""

weight = float(input("Enter the weight of a package: "))

if(weight > 10):
    charge = weight * 4.75
elif(weight > 6):
    charge = weight * 4
elif(weight > 2):
    charge = weight * 3
else:
    charge = weight * 1.5
    
print('Shipping charges:', charge)