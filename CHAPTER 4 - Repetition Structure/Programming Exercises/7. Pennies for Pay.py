"""
Write a program that calculates the amount of money a person would earn over a period of
time if his or her salary is one penny the first day, two pennies the second day, and contin-
ues to double each day. The program should ask the user for the number of days. Display
a table showing what the salary was for each day, then show the total pay at the end of the
period. The output should be displayed in a dollar amount, not the number of pennies.
"""

total = 0
current = 1

days = int(input('Number of days? '))
for penny in range(1, days + 1):
    total += current
    current *= 2 # wait why wouldnt penny * penny work
    
total /= 100
print(f'Total = ${total:.2f}')