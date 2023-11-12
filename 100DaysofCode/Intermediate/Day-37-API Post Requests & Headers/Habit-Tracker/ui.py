from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import datetime as dt

THEME_COLOR = "#375362"
TODAY = dt.datetime.now()


class TrackerInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Habit Tracker")
        self.window.resizable(width=False, height=False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.cal = Calendar(
            self.window,
            selectmode="day",
            year=TODAY.year,
            month=TODAY.month,
            day=TODAY.day,
        )
        self.cal.grid(row=0, column=0, columnspan=4)

        self.window.mainloop()
