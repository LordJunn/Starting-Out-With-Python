"""
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
"""
total = 0

def main():
    global total
    total += expenses("loan payment")
    total += expenses("insurance")
    total += expenses("gas")
    total += expenses("oil")
    total += expenses("tires")
    total += expenses("maintenance")    
    print(f'Total monthly cost of these expenses = ${total}')
    total *= 12
    print(f'Total annual cost of these expenses = ${total}')    

def expenses(expense):
    duit = int(input(f'Enter the monthly costs for the expense incurred from your {expense}: $'))
    return duit
    
main()