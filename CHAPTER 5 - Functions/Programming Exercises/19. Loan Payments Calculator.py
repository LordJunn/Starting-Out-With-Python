"""
Suppose you have taken out a loan for a certain amount of money with a fixed monthly inter-
est rate and monthly payments, and you want to determine the monthly payment amount
necessary to pay off the loan within a specific number of months. The formula is as follows:
P = (R * A)/(1 - (1 + R)^(-M))
The terms in the formula are:
• P is the payment amount per month.
• R is the monthly interest rate, as a decimal (e.g. 2.5% = 0.025).
• A is the amount of the loan.
• M is the number of months.
Write a program that prompts the user to enter the loan amount, monthly interest rate as
a percentage and desired number of months. The program should pass these values to a
function that returns the monthly payment amount necessary. The program should display
this amount.
"""

def main():
    a = int(input('Amount of the loan? '))
    r = int(input('Monthly interest rate? '))
    m = int(input('Desired number of months? '))
    p = loaner(a, r, m)
    
    print(f'Payment amount per month: ${p:.2f}')
    
def loaner(a, r, m):
    r /= 100
    p = (r * a)/(1 - ((1 + r) ** (-m)))
    return p

main()