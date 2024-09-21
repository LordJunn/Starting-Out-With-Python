"""
A county collects property taxes on the assessment value of property, which is 60 percent of
the property’s actual value. For example, if an acre of land is valued at $10,000, its assess-
ment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
actual value of a piece of property and displays the assessment value and property tax.
"""

def main():
    prop = float(input("What is the property's actual value? "))
    proptax = taxtation(prop, 0.6)
    ass = taxtation(proptax, 0.0072)
    print(f'Assessment value: ${proptax:.2f}')
    print(f'Assessment value: ${ass:.2f}')

def taxtation(cost, tax):
    money = cost * tax
    return money

main()