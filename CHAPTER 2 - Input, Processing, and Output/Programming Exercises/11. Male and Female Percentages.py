"""
Write a program that asks the user for the number of males and the number of females regis-
tered in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage
of females can be calculated as 12 ÷ 20 = 0.6, or 60%.
"""

males = float(input('How many males are registered in the class? '))
females = float(input('How many females are registered in the class? '))

total = males + females
male = (males/total)*100
female = (females/total)*100

print('The percentage of males =', male)
print('The percentage of females =', female)