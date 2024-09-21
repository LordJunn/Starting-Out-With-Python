"""
A painting company has determined that for every 112 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $35.00 per hour
for labor. Write a program that asks the user to enter the square feet of wall space to be
painted and the price of the paint per gallon. The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""

def main():
    sqft = int(input('Enter the square feet of wall space to be painted: '))
    price = int(input('Enter the price of the paint per gallon: '))
    
    if (sqft % 112 == 0):
        gallon = (sqft // 112)
        hours = (sqft // 14)        
    else:
        gallon = (sqft // 112) + 1
        hours = (sqft // 14) + 8      

    paint = multiplication(gallon, price)
    labor = multiplication(hours, 35)
    
    print(f'The number of gallons of paint required: {gallon}')
    print(f'The hours of labor required: {hours}')
    print(f'The cost of the paint: ${paint}')
    print(f'The labor charges: ${labor}')
    
    total = paint + labor

    print(f'The total cost of the paint job: ${total}')

def multiplication(multiplicand, multiplier): # stolen from C5PE7
    product = multiplicand * multiplier
    return product

main()