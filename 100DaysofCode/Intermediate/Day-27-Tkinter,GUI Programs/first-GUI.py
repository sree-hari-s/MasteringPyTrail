import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500,height=300)

#label 
my_label = tkinter.Label(text= "1st Label")
my_label.pack()
window.mainloop()