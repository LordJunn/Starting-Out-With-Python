"""
A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
burned, heart rate, sleeping patterns, and so on. One common physical activity that most
of these devices track is the number of steps you take each day.
If you have downloaded this book’s source code from the Premium Companion Website,
you will find a file named steps.txt in the Chapter 06 folder. (The Premium Companion
Website can be found at www.pearsonglobaleditions.com/gaddis.) The steps.txt file
contains the number of steps a person has taken each day for a year. There are 365 lines
in the file, and each line contains the number of steps taken during a day. (The first line is
the number of steps taken on January 1st, the second line is the number of steps taken on
January 2nd, and so forth.) Write a program that reads the file, then displays the average
number of steps taken for each month. (The data is from a year that was not a leap year,
so February has 28 days.) 
""" # steps.txt: https://github.com/abhaysamantni/Python_MidTerm/blob/master/steps.txt, sum is 1,933,336

current = 0

def main():
    global current
    total = 0
    for bulan in range(12):
        days = daysInMonth(bulan + 1)
        start = current
        end = current + days - 1
        print(f"Currently at month {bulan + 1} with {days} days, starting at {start + 1}, ending at {end + 1}") # format purposes
        num, counter = lineRead("steps.txt", start, end)
        avg = num/days
        print(f'Steps taken on month #{bulan + 1}: {avg:.2f}')
        current = counter
        total += num
    print(f'Total steps: {total}')

        
def lineRead(name, now, next): 
    infile = open(name, 'r')
    counter = now
    steps = 0
    lines = infile.readlines()
    
    while (counter <= next):
        owo = lines[now]
        steps += int(owo)
        now += 1 # turns out i forgotten to +1 to now, hence y it just repeats
        counter += 1

    infile.close()
    return steps, counter
    
def daysInMonth(i):
    n = 0
    if ((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
        n = 31
    elif (i == 2):
        n = 28
    elif ((i == 4) or (i == 6) or (i ==9) or (i == 11)):
        n = 30
    return n    

main()