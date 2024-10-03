"""
Design a program that lets the user enter the total rainfall for each of 12 months into a
list. The program should calculate and display the total rainfall for the year, the average
monthly rainfall, the months with the highest and lowest amounts.
"""

MONTHS = 12

def main():
    total = 0
    rain = [0] * MONTHS
    
    for i in range(MONTHS):
        rain[i] = int(input(f'Total rainfall for month #{i + 1}? '))
        total += rain[i]

    avg = total/MONTHS

    high = rain[0]
    mhigh = 0
    low = rain[0]
    mlow = 0
    
    for i in range(MONTHS):
        if(rain[i] > high):
            mhigh = i
            high = rain[i]
        elif(rain[i] < low):
            mlow = i
            low = rain[i]
            
    print(f'Total rainfall for the year: {total}')
    print(f'Average monthly rainfall: {avg}') 
    print(f'The month with the highest amount: {mhigh + 1}, amount: {high}')   
    print(f'The month with the lowest amount: {mlow + 1}, amount: {low}')     

main()