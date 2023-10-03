# necessary modules
from tkinter import *
from tkinter import messagebox
from threading import Timer
import datetime

# Function to set the alarm
def set_alarm():
    alarm_time = alarm_entry.get()  # Get the alarm time from the entry field
    try:
        # Parse the entered time in 'HH:MM:SS' format
        alarm_time_parts = alarm_time.split(':')
        alarm_datetime = datetime.time(int(alarm_time_parts[0]), int(alarm_time_parts[1]), int(alarm_time_parts[2]))
        current_time = datetime.datetime.now().time()

        # Calculate the time difference between current time and alarm time
        time_difference = datetime.datetime.combine(datetime.date.today(), alarm_datetime) - datetime.datetime.combine(datetime.date.today(), current_time)

        # Display a message with the remaining time until the alarm goes off
        messagebox.showinfo("Alarm Set", f"Alarm will go off in {time_difference}")

        # Schedule the alarm to go off after the calculated time difference
        timer = Timer(time_difference.total_seconds(), trigger_alarm)
        timer.start()
    except (ValueError, IndexError):
        messagebox.showerror("Invalid Input", "Please enter the alarm time in 'HH:MM:SS' format.")

# Function to trigger the alarm
def trigger_alarm():
    messagebox.showinfo("Alarm", "Wake up!")

# main application window
root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")

#  widgets
label = Label(root, text="Enter Alarm Time (HH:MM:SS):")
label.pack()

alarm_entry = Entry(root)
alarm_entry.pack()

set_button = Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

# main event loop
root.mainloop()
