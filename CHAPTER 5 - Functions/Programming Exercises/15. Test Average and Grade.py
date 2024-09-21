"""
Write a program that asks the user to enter five test scores. The program should display a
letter grade for each score and the average test score. Write the following functions in the
program:
• calc_average. This function should accept five test scores as arguments and return the
average of the scores.
• determine_grade. This function should accept a test score as an argument and return
a letter grade for the score based on the following grading scale:
Score Letter Grade
90–100 A
80–89 B
70–79 C
60–69 D
Below 60 F
"""

def main():
    g1 = int(input('Insert test score #1: '))
    g2 = int(input('Insert test score #2: '))
    g3 = int(input('Insert test score #3: '))    
    g4 = int(input('Insert test score #4: '))
    g5 = int(input('Insert test score #5: '))
    
    tableHead()
    
    print(f'1\t{determine_grade(g1)}')
    print(f'2\t{determine_grade(g2)}')   
    print(f'3\t{determine_grade(g3)}')
    print(f'4\t{determine_grade(g4)}')   
    print(f'5\t{determine_grade(g5)}')
    
    avg = calc_average(g1, g2, g3, g4, g5)
    print(f'Avg\t{determine_grade(avg)}')    
    
def calc_average(a, b, c, d, e):
    total = a + b + c + d + e
    total /= 5
    return total

def determine_grade(score):
    grade = ''
    if score >= 90:
        grade += 'A'
    elif score >= 80:
        grade += 'B'
    elif score >= 70:
        grade += 'C'
    elif score >= 60:
        grade += 'D'
    else:
        grade += 'F'
    
    return grade    

def tableHead():
    print('Test\tLetter Grade')
    print('-------------------')

main()