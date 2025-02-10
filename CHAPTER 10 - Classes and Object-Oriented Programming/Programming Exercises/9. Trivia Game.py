"""
In this programming exercise, you will create a simple trivia game for two players. The pro-
gram will work like this:
• Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
should be a total of 10 questions.) When a question is displayed, 4 possible answers are
also displayed. Only one of the answers is correct, and if the player selects the correct
answer, he or she earns a point.
• After answers have been selected for all the questions, the program displays the number
of points earned by each player and declares the player with the highest number of points
the winner.
To create this program, write a Question class to hold the data for a trivia question. The
Question class should have attributes for the following data:
• A trivia question
• Possible answer 1
• Possible answer 2
• Possible answer 3
• Possible answer 4
• The number of the correct answer (1, 2, 3, or 4)
The Question class also should have an appropriate _ _ init_ _ method, accessors, and
mutators.
The program should have a list or a dictionary containing 10 Question objects, one for
each trivia question. Make up your own trivia questions on the subject or subjects of your
choice for the objects
"""
import random

class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct = correct

    def question(self):
        return self.__question

    def answers(self):
        return [self.__answer1, self.__answer2, self.__answer3, self.__answer4]

    def correct(self):
        return self.__correct

    def set_question(self, question):
        self.__question = question

    def set_answers(self, answer1, answer2, answer3, answer4):
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4

    def set_correct(self, correct):
        self.__correct = correct
        
questions = [ # more than 10 questions for full rng
    Question("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3),
    Question("What is the chemical symbol for Gold?", "Au", "Ag", "Fe", "Hg", 1),
    Question("Who was the first President of the United States?", "Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams", 2),
    Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "J.K. Rowling", "Mark Twain", "Ernest Hemingway", 1),
    Question("Which river is the longest in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2),
    Question("What is 2 + 2?", "3", "4", "5", "6", 2),
    Question("What is the boiling point of water?", "90°C", "100°C", "110°C", "120°C", 2),
    Question("Who is known as the 'King of Pop'?", "Elvis Presley", "Michael Jackson", "Prince", "Freddie Mercury", 2),
    Question("What movie won the Oscar for Best Picture in 1994?", "Pulp Fiction", "Shawshank Redemption", "Forrest Gump", "Lion King", 3),
    Question("How many players are on a soccer team on the field at one time?", "9", "10", "11", "12", 3),
    Question("What does HTTP stand for?", "HyperText Transfer Protocol", "HyperText Transport Protocol", "Hyper Transfer Text Protocol", "HyperText Test Protocol", 1),
    Question("Who painted the Mona Lisa?", "Vincent van Gogh", "Claude Monet", "Leonardo da Vinci", "Pablo Picasso", 3),
    Question("What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3),
    Question("Which element has the chemical symbol O?", "Osmium", "Oxygen", "Oganesson", "Osmium", 2),
    Question("What year did the Titanic sink?", "1912", "1911", "1913", "1914", 1),
    Question("What is the smallest prime number?", "1", "2", "3", "4", 2)
]

def ask_question(question_obj):
    print(question_obj.question())
    answers = question_obj.answers()
    for i, answer in enumerate(answers, 1):
        print(f"{i}. {answer}")
    
    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer < 1 or user_answer > 4:
                print("Please choose a number between 1 and 4.")
            else:
                return user_answer == question_obj.correct()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    random.shuffle(questions)
    
    scores = {"Player 1": 0, "Player 2": 0}
    players = ["Player 1", "Player 2"]

    for i in range(5):
        for player in players:
            print(f"\n{player}'s Turn")
            question = questions.pop()  
            if ask_question(question):
                print("Correct!")
                scores[player] += 1
            else:
                print("Incorrect!")

    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")
        
    p1 = scores["Player 1"]
    p2 = scores["Player 2"]
    
    if p1 == p2:
        print("It's a tie!")
    else:
        winner = max(scores, key=scores.get)
        print(f"\n{winner} wins!")
    
main()