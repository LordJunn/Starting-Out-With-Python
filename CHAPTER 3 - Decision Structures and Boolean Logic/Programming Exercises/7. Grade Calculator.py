"""
A class has two tests worth 25 points each along with a main exam worth 50 points. For a stu-
dent to pass the class, they must obtain an overall score of at least 50 points, and must obtain at
least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than
25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows:
If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
If they get less than 80 but more than 60, they get a “Credit” grade.
If they get less than 60, they get a ”Pass” grade.
Write a program that prompts the user to enter their points for both tests and the exam and
converts the values to integers. The program should first check if the points entered for the
tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam
score is not between 0 and 50, the program should display an error message. Otherwise,
the program should display the total points and the grade.
"""

t1 = int(input("Enter your points for test #1: "))
t2 = int(input("Enter your points for test #2: "))
e = int(input("Enter your points for exam: "))

total = t1 + t2 + e

if not (0 <= t1 <= 25):
    print('Error. Test score #1 is not between 0 and 25')
elif not (0 <= t2 <= 25):
    print('Error. Test score #2 is not between 0 and 25')
elif not (0 <= e <= 50):
    print('Error. Exam is not between 0 and 50') 
else:
    if(total >= 80):
        print('Distinction.')
    elif(total >= 60 and e >= 25):
        print('Credit.')
    elif((50 <= total < 60) and e >= 25):
        print('Pass.')
    else:
        print('Fail.')