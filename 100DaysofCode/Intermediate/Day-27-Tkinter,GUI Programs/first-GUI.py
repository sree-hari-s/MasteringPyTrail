import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="1st Label", font=("Arial", 24, "bold"))
my_label.pack()

bottom_label = tkinter.Label(text="2nd Label", font=("Arial", 24, "bold"))
bottom_label.pack(side="bottom")

# button
def button_clicked():
    my_label.config(text="Button Got Clicked")

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry Component - input field 
def modify_label():
    new_text = input.get()
    bottom_label.config(text=new_text)

input = tkinter.Entry(width=30)
input.pack()

entry_button = tkinter.Button(text="Entry", command=modify_label)
entry_button.pack()

window.mainloop()
