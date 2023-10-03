from tkinter import *
from tkinter import messagebox
import random

FONT = 'Arial 20 bold'

def no():
    messagebox.showinfo(' ', 'Lol')
    quit()

def motionMouse(event):
    btnNo.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('Annoying Button')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Click No?', font=FONT)
label.pack()  

btnNo = Button(root, text='No', font=FONT)
btnNo.place(x=170, y=100)
btnNo.bind('<Enter>', motionMouse)

btnYes = Button(root, text='Yes', font=FONT, command=no)
btnYes.pack() 

root.mainloop()
