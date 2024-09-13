"""
Write a program that asks the user to enter the amount of a purchase and the desired
number of payment instalments. The program should add 5 percent to the amount to get
the total purchase amount, and then divide it by the desired number of instalments, then
display messages telling the user the total amount of the purchase and how much each
instalment will cost.
"""

amount = float(input('The amount of a purchase? '))
installments = float(input('The desired number of payment instalments? '))

total = amount * 0.05
installment = total/installments

print('Total amount = $', format(total, '.2f'))
print('Each installment will cost $', format(installment, '.2f'))