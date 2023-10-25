from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

language_label = Label(text="French")

canvas = Canvas(width=800,height=526)
card = PhotoImage(file='images/card_front.png')
canvas.create_image(400,263,image=card)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))

# Buttons setup
right = PhotoImage(file='images/right.png')
right_button = Button(image=right,highlightthickness=0)
right_button.grid(row=1,column=0)

wrong = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong,highlightthickness=0)
wrong_button.grid(row=1,column=1)

window.mainloop()