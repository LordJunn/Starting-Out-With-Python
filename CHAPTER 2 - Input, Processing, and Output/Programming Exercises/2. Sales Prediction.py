"""
A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, then displays the
profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.
"""

percentage = 0.23
sales = float(input('Enter the projected amount of total sales: '))

profit = sales * percentage

print('The profit that will be made from $', format(sales, '.2f'), 'is $', format(profit, '.2f'))
