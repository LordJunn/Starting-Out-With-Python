"""
Create a change-counting game that gets the user to enter the number of coins required
to make exactly one dollar. The program should prompt the user to enter the number of
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
dollar, the program should congratulate the user for winning the game. Otherwise, the
program should display a message indicating whether the amount entered was more than
or less than one dollar.
"""

p = 1
n = 5
d = 10
q = 25

penny = int(input("Enter the number of pennies: "))
nickel = int(input("Enter the number of nickels: "))
dime = int(input("Enter the number of dimes: "))
quarter = int(input("Enter the number of quarters: "))

total = (p * penny) + (n * nickel) + (d * dime) + (q * quarter)

if(total > 100):
    print('The amount entered was more than than one dollar')
elif(total == 100):
    print('Congratulations!')
else:
    print('The amount entered was less than one dollar')