"""
A customer in a store is purchasing five items. Write a program that asks for the price of
each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7 percent.
"""

st = 0.07
item1 = float(input('Enter the price of item #1: '))
item2 = float(input('Enter the price of item #2: '))
item3 = float(input('Enter the price of item #3: '))
item4 = float(input('Enter the price of item #4: '))
item5 = float(input('Enter the price of item #5: '))

subtotal = item1 + item2 + item3 + item4 + item5
total = subtotal * st

print('Subtotal of the sale: $', subtotal)
print('The amount of sales tax:', format((st * 100), '.2f'), '%')
print('Total: $', total)