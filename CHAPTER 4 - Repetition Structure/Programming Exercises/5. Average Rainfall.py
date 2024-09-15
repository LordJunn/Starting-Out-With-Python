"""
Write a program that uses nested loops to collect data and calculate the average rainfall over
a period of years. The program should first ask for the number of years. The outer loop will
iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.
"""

total = 0

years = int(input('Number of years? '))
for counter1 in range(1, years + 1):
    for counter2 in range(1, 13): # cuz 12+1
        rainfall = int(input(f'The inches of rainfall for month #{counter2}? '))
        total += rainfall
    
months = years * 12
avg = total/months

print(f'The number of months: {months}')
print(f'The  total inches of rainfall: {total}')        
print(f'The average rainfall per month for the entire period: {avg}')        