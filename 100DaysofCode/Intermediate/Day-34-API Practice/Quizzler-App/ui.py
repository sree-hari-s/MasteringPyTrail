from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score : 0",
            fg="white",
            background=THEME_COLOR,
            font=("Arial", 16, "bold"),
        )
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(
            150, 125,
            width=270,
            text="Question", 
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Buttons setup
        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0,command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0,command=self.is_false)
        self.false_button.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.score_label.config(text=f"Score : {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question,text="Game Over")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def is_true(self):
        self.give_feedback(self.quiz.check_answer('True'))
    
    def is_false(self):
        is_right=self.quiz.check_answer('False')
        self.give_feedback(is_right)
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500,self.next_question)