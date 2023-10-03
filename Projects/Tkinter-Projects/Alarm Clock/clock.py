#necessary modules
from tkinter import *
from time import strftime

# main application window
root = Tk()
root.title("Clock")
root.geometry("500x200")

# Function to update the time display
def time():
    current_time = strftime("%H:%M:%S %p")  # Get the current time in 'hh:mm:ss AM/PM' format
    label.config(text=current_time)  # Update the text of the Label widget
    label.after(1000, time)  # Schedule the time function to be called again after 1000 milliseconds (1 second)

# Label widget to display the time
label = Label(root, font=("Courier New", 40), background="#C5B24B", foreground="black" ,justify="center")
label.pack(anchor="center")

# Call function to display time
time()

# main event loop
root.mainloop()
