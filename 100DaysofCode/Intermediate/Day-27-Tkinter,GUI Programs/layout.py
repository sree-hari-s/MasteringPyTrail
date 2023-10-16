import tkinter
"""
pack 
place 
grid

"""

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

# label
first_label = tkinter.Label(text="1st Label", font=("Arial", 24, "bold"))
first_label.grid(column=0,row=0)

second_label = tkinter.Label(text="2nd Label", font=("Arial", 24, "bold"))
second_label.grid(column=3,row=0)

# button
def button_clicked():
    first_label.config(text="Button Got Clicked")

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=2,row=2)

# Entry Component - input field 
def modify_label():
    new_text = input.get()
    second_label.config(text=new_text)

input = tkinter.Entry(width=30)


entry_button = tkinter.Button(text="Entry", command=modify_label)
entry_button.grid(column=4,row=3)

window.mainloop()
