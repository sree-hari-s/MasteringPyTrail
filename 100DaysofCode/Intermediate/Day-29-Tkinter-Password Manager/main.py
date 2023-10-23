from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)  # padding from the window
canvas = Canvas(width=200, height=200, highlightthickness=0)
background_img = PhotoImage(file='password.png')
canvas.create_image(100, 100, image=background_img)  # x,y coordinate given
canvas.grid()
window.mainloop()
