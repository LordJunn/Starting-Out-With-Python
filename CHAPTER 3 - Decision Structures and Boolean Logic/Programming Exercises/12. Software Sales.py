"""
A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:
Quantity Discount
10–19 10%
20–49 20%
50–99 30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The pro-
gram should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.
"""

retail = 99

quantity = int(input("Enter the number of books that you purchased this month: "))

if(quantity >= 100):
    price = (quantity * retail)*0.6
    print('Discount amount = 40%')
elif(quantity >= 50):
    price = (quantity * retail)*0.7
    print('Discount amount = 30%')
elif(quantity >= 20):
    price = (quantity * retail)*0.8
    print('Discount amount = 20%')
elif(quantity >= 10):
    price = (quantity * retail)*0.9
    print('Discount amount = 10%')
else:
    price = quantity * retail
    
print(f'Total amount of the purchase after the discount = ${price}') # adding f & {thing} is better than print("", thing)