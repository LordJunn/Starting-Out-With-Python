"""
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.
"""

def main():
    aa = writer('A')
    classA = multiplication(aa, 20)
    bb = writer('B')
    classB = multiplication(bb, 15)    
    cc = writer('C')
    classC = multiplication(cc, 10)  
    income = classA + classB + classC
    print(f'The total income generated from ticket sales: ${income}')  
    
def multiplication(multiplicand, multiplier): # this one feels more all in one
    product = multiplicand * multiplier
    return product

def writer(word):
    item = int(input(f'How many tickets for Class {word} were sold? ')) # this is also an all in one
    return item

main()