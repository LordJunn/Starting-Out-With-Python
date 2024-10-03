"""
The local driver’s license office has asked you to create an application that grades the writ-
ten portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
are the correct answers:
1. A
2. C
3. A
4. A
5. D
6. B
7. C
8. A
9. C
10. B
11. A
12. D
13. C
14. A
15. D
16. C
17. B
18. B
19. D
20. A
Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question num-
bers of the incorrectly answered questions.
""" # C7PE7.txt
#correct_answers = ['B', 'A', 'D', 'C', 'A', 'B', 'D', 'C', 'B', 'A', 'D', 'C', 'B', 'A', 'C', 'D', 'A', 'D', 'A', 'C'] # to check etc stuff if needed
correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

def main():
    file = input('What is the file name? ')
    ans = fileOpenIndexConvertStr(file)
    correct, incorrect, xQ = grader(correct_answers, ans)
    
    if(correct >= 15):
        print('Pass!')
    else:
        print('Fail!')
    
    print(f'Total number of correctly answered questions: {correct}')
    print(f'Total number of incorrectly answered questions: {incorrect}')    

    if xQ:
        print(f'Question numbers of the incorrectly answered questions: {", ".join(map(str, xQ))}')      # ", ".join(map(str, incorrect_questions)) is gpt
    else:
        print('All questions answered correctly.')  
    
def fileOpenIndexConvertStr(fileName): # opens a file, converts item in it into string
    infile = open(fileName, 'r')
    acc = infile.readlines()
    infile.close()
    
    index = 0
    while index < len(acc):
        acc[index] = str(acc[index].strip()) # strip is necessary
        index += 1  
        
    return acc  

def grader(correct_answers, ans):
    correct = 0
    incorrect = 0
    xQ = []
    checker = input('Would you like to compare the answers? y for yes, anything else for no. ')
    
    for i in range(len(correct_answers)):
        
        if(checker == 'y'):
            print(f'{ans[i]} = {correct_answers[i]}')
            
        if ans[i] == correct_answers[i]:
            correct += 1
        else:
            incorrect += 1
            xQ.append(i + 1)
            
    return correct, incorrect, xQ

main()