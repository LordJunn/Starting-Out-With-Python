"""
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a program
that asks the user to enter the replacement cost of a building, then displays the minimum
amount of insurance he or she should buy for the property.
"""

def main():
    insure = insurance()
    print(f'The minimum amount of insurance you should buy for the property = ${insure:.2f}')

def insurance():
    amount = float(input('Enter the replacement cost of a building: '))
    amount *= 0.8
    return amount

main()