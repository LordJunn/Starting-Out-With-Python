"""
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.
"""


MAX = 5 

total = 0.0

print('This program calculates the sum of')
print(MAX, 'days worth of bugs you will enter.')


for counter in range(MAX):
    number = int(input(f'the number of bugs collected during day #{counter + 1}: '))
    total = total + number

print('The total bugs collected is', total)