"""
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes
"""
print('Displaying the number of calories burned after 10, 15, 20, 25, and 30 minutes')
print('Minutes\t\tCalories burnt')
print('----------------------------')

for number in [10, 15, 20, 25, 30]:
    burn = number * 4.2
    print(number, '\t\t', burn)
