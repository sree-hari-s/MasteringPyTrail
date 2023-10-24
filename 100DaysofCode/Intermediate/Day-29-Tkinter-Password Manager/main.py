from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle

FONT_DEFAULT = ("Arial", 12)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list=password_letters + password_numbers + password_symbols
    shuffle(password_list)
    
    password = "".join(password_list)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please enter all fields!")
    else:
        with open('password.txt', 'a') as f:
            f.write(f"{website} | {username} | {password}\n")

        website_input.delete(0,'end')
        password_input.delete(0,'end')
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
website_input.grid(row=1, column=1, columnspan=2)

username_input = Entry(width=36, font=FONT_DEFAULT)
username_input.insert(END,'example@test.com')
username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=26, font=FONT_DEFAULT)
password_input.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate", width=10,command = generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command = save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
