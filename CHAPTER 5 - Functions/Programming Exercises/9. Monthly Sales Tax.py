"""
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter
the total sales for the month. From this figure, the application should calculate and display
the following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
"""

def main():
    sales = int(input('Enter the total sales for the month: '))
    cst = multiplication(sales, 0.05)
    sst = multiplication(sales, 0.025)
    total = cst + sst
    writer('county', cst)
    writer('state', sst)   
    writer('', total) 
    
def multiplication(multiplicand, multiplier): # stolen from C5PE8
    product = multiplicand * multiplier
    return product

def writer(word, amount):
    print(f'The amount of {word} sales tax: ${amount:.2f}')

main()