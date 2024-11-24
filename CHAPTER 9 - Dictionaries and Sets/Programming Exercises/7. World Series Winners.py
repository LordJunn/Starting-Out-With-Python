"""
In this chapter’s source code folder (available on the Premium Companion Website at www.
pearsonglobaleditions.com/gaddis), you will find a text file named WorldSeriesWinners.
txt. This file contains a chronological list of the World Series’ winning teams from 1903
through 2009. The first line in the file is the name of the team that won in 1903, and the
last line is the name of the team that won in 2009. (Note the World Series was not played
in 1904 or 1994. There are entries in the file indicating this.)
Write a program that reads this file and creates a dictionary in which the keys are the names
of the teams, and each key’s associated value is the number of times the team has won the
World Series. The program should also create a dictionary in which the keys are the years,
and each key’s associated value is the name of the team that won that year.
The program should prompt the user for a year in the range of 1903 through 2009. It
should then display the name of the team that won the World Series that year, and the
number of times that team has won the World Series.
""" # ok fk u the text file was THE ONE THATS WRONG REEEE
# kys i had to literally refer line by line with wikipedia
 
def main():
    file = 'WorldSeries.txt'
    teamW, yearW = winners(file, 1903)
    
    if teamW is None or yearW is None:
        return 
    
    try:
        year = int(input("Enter a year between 1903 and 2009: "))
        if year < 1903 or year > 2009:
            print("Year must be between 1903 and 2009.")
            return
        
        if year in yearW:
            team = yearW[year]
            wins = teamW[team]
            print(f"In {year}, the World Series was won by {team}.")
            print(f"{team} has won the World Series {wins} times.")
        elif year == 1904 or year == 1994:
            print(f"No World Series was played for the year {year}.")
        else:
            print(f"No World Series winner for the year {year}.")

    
    except ValueError:
        print("Please enter a valid year.")

def winners(data, y):
    teamW = {}
    yearW = {}
    
    try:
        with open(data, 'r') as file:
            year = y
            for line in file:
                team = line.strip()

                if team:  # To confirm that it isn't whitespace or empty
                    if 'World Series Not Played' in team:
                        year += 1
                    
                    else:                
                        print(f'{year}: {team}')    
                        yearW[year] = team
                        if team in teamW:
                            teamW[team] += 1
                        else:
                            teamW[team] = 1
                        year += 1
                    
                        
    except FileNotFoundError:
        print(f"The file '{data}' was not found.")
        return None, None
    
    return teamW, yearW

main()