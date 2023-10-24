from tkinter import *

FONT_DEFAULT = ("Arial", 12)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # padding from the window
canvas = Canvas(width=200, height=200, highlightthickness=0)
background_img = PhotoImage(file="password.png")
canvas.create_image(100, 100, image=background_img)  # x,y coordinate given
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ", font=FONT_DEFAULT)
website_label.grid(row=1, column=0)

username_label = Label(text="Username: ", font=FONT_DEFAULT)
username_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=FONT_DEFAULT)
password_label.grid(row=3, column=0)

# Inputs
website_input = Entry(width=36, font=FONT_DEFAULT)
website_input.insert(END, string="website url")
website_input.grid(row=1, column=1, columnspan=2)

username_input = Entry(width=36, font=FONT_DEFAULT)
username_input.insert(END, string="username/email")
username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=26, font=FONT_DEFAULT)
password_input.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate", width=10)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
