from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=60, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=2,row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=3,row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=2)

result = Label(text="0")
result.grid(column=2,row=2)

label_kms = Label(text="Km")
label_kms.grid(column=3,row=2)

def convert():
    try:
        miles=float(miles_input.get())
        kms = round(miles*1.609344,2)
    except ValueError:
        kms=0
    result.config(text=f"{kms}")

calculate = Button(text="Calculate",command=convert)
calculate.grid(column=2,row=3)

window.mainloop()