from tkinter import *
from tkinter import messagebox
from random import choice,randint
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
#-----------------------WORD GENERATOR --------------------
data = pd.read_csv("data/french_words.csv")
dict_data = data.to_dict(orient="records")
current_card = {}

def word_generator():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(dict_data)
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(word,text=current_card['French'],fill="black")
    flip_timer=window.after(3000,func=flip_card)

#------------------------Flip Card------------------------
def flip_card():
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(word,text=current_card['English'],fill="white")

#------------------------UI Setup------------------------
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
card_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
word=canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))


# Buttons setup
right = PhotoImage(file='images/right.png')
right_button = Button(image=right,highlightthickness=0,command=word_generator)
right_button.grid(row=1,column=0)

wrong = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong,highlightthickness=0,command=word_generator)
wrong_button.grid(row=1,column=1)

word_generator()
window.mainloop()