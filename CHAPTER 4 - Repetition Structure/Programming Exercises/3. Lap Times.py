"""
Write a program that asks the user to enter the number of times that they have run around
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
When the loop finishes, the program should display the time of their fastest lap, the time of
their slowest lap, and their average lap time.
"""

# Initialize variables, apparently i gotta do this instead of making it
fastest = None
slowest = None
total = 0

times = int(input('Enter the number of times that you have run around a racetrack: '))
for counter in range(1, times + 1):
    lap = int(input(f'Enter the lap time for lap #{counter}: '))
    # Initialize fastest and slowest with the first lap time
    if fastest is None or slowest is None:
        fastest = lap
        slowest = lap
    if(lap > fastest):
        fastest = lap
    if(lap < slowest):
        slowest = lap    
    total += lap
    
avg = total/times    
print('Fastest lap =', fastest)
print('Slowest lap =', slowest)
print('Average lap time =', avg)