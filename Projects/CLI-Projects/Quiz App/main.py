from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

def game():
    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()
    print("Quiz Completed!")
    print(f"Your final score was {quiz.score}/{len(quiz.question_list)}\n")

from os import system
while input("Do you want to play a Quiz Game? (y/n): ") =='y':
    system('cls')
    game()