"""
A “sleep debt” represents the difference between a person’s desirable and actual amount
of sleep. Write a program that prompts the user to enter how many hours they slept each
day over a period of seven days. Using 8 hours per day as the desirable amount of sleep,
determine their sleep debt by calculating the total hours of sleep they got over the seven-day
period and subtracting that from the total hours of sleep they should have got. If the user
does not have a sleep debt, display a message expressing your jealousy.
"""

desired = 8 * 7
total = 0

for w in range(1, 8):
    sleep = int(input(f'How many hours did you sleep on day #{w}: '))
    total += sleep
    
debt = desired - total
if debt <= 0:
    print('Grr, expressing my jealousy.')
else:
    print(f'You need to sleep at least {debt} more hour  .')