"""
To play the PowerBall lottery, you buy a ticket that has five numbers in the range of 1–69,
and a “PowerBall” number in the range of 1–26. (You can pick the numbers yourself, or you
can let the ticket machine randomly pick them for you.) Then, on a specified date, a winning
set of numbers is randomly selected by a machine. If your first five numbers match the first
five winning numbers in any order, and your PowerBall number matches the winning Pow-
erBall number, then you win the jackpot, which is a very large amount of money. If your
numbers match only some of the winning numbers, you win a lesser amount, depending on
how many of the winning numbers you have matched.
In the student sample programs for this book, you will find a file named pbnumbers.txt,
containing the winning PowerBall numbers that were selected between February 3, 2010
and May 11, 2016 (the file contains 654 sets of winning numbers). Figure 8-6 shows an
example of the first few lines of the file’s contents. Each line in the file contains the set of six
numbers that were selected on a given date. The numbers are separated by a space, and the
last number in each line is the PowerBall number for that day. For example, the first line in
the file shows the numbers for February 3, 2010, which were 17, 22, 36, 37, 52, and the
PowerBall number 24.
Write one or more programs that work with this file to perform the following:
• Display the 10 most common numbers, ordered by frequency
• Display the 10 least common numbers, ordered by frequency
• Display the 10 most overdue numbers (numbers that haven’t been drawn in a long
time), ordered from most overdue to least overdue
• Display the frequency of each number 1–69, and the frequency of each Powerball
number 1–26
""" # gpt, with modification
MAXNUM = 69
MAXBALL = 26
TOTAL = 0

def main():
    file = 'pbnumbers.txt'
    num, ball, num2 = reader(file)
    analyze(num, ball, num2)

def reader(file):
    global TOTAL
    with open(file, 'r') as file:
        lines = file.readlines()
        
    numbers = []
    powerballs = []
    numbers2 = []
    
    for line in lines:
        parts = line.strip().split()
        numbers.extend(map(int, parts[:-1])) 
        powerballs.append(int(parts[-1]))
        numbers2.append([int(num) for num in parts[:-1]])
        
    TOTAL = len(lines)
        
    return numbers, powerballs, numbers2

def analyze(numbers, powerballs, numbers2):
    global TOTAL
    total = TOTAL # len(numbers woildnt work)
    numfreq = [0] * MAXNUM
    ballfreq = [0] * MAXBALL
    lastSeen = [-1] * MAXNUM
    
    for num in numbers:
        if 1 <= num <= MAXNUM:
            numfreq[num - 1] += 1
            
    for pb in powerballs:
        if 1 <= pb <= MAXBALL:
            ballfreq[pb - 1] += 1
            
    for index, draw in enumerate(numbers2):
        for num in draw:
            if 1 <= num <= MAXNUM:
                lastSeen[num - 1] = index
            
    
    # creating list, or tuple
    numlist = [(i + 1, numfreq[i]) for i in range(MAXNUM)] 
    balllist = [(i + 1, ballfreq[i]) for i in range(MAXBALL)] 
    overlist = [(i + 1, total if lastSeen[i] == -1 else total - lastSeen[i]) for i in range(MAXNUM)]
    
    # sort function, sorts tuple, [:10] 1st 10 elem from list
    
    # uses lambda algo to sort, desending order, then smaller num as prio
    mcnum = sorted(numlist, key=lambda x: (-x[1], x[0]))[:10]
    mcball = sorted(balllist, key=lambda x: (-x[1], x[0]))[:10]
    mcover = sorted(overlist, key=lambda x: (-x[1], x[0]))[:10]
    # uses lambda algo to sort, ascending order, then smaller num as prio
    lcnum = sorted(numlist, key=lambda x: (x[1], x[0]))[:10]
    lcball = sorted(balllist, key=lambda x: (x[1], x[0]))[:10]
    
    print("10 Most Common Numbers (1-69):")
    for num, freq in mcnum:
        print(f"Number {num}: {freq} times")       

    print("\n10 Most Common PowerBall Numbers (1-26):")
    for num, freq in mcball:
        print(f"Number {num}: {freq} times")    
            
    print("\n10 Least Common Numbers (1-69):")
    for num, freq in lcnum:
        print(f"Number {num}: {freq} times") 

    print("\n10 Least Common PowerBall Numbers (1-26):")
    for num, freq in lcball:
        print(f"Number {num}: {freq} times")    
        
    # Display results
    print("\n10 Most Overdue Numbers (1-69):")
    for num, overdue in mcover:
        print(f"Number {num}: Overdue by {overdue} draws")        
        
    print("\nFrequency of Each Number (1-69):")
    for i in range(MAXNUM):
        print(f"Number {i + 1}: {numfreq[i]} times")
    
    print("\nFrequency of Each PowerBall Number (1-26):")
    for i in range(MAXBALL):
        print(f"PowerBall {i + 1}: {ballfreq[i]} times")        
        
main()        