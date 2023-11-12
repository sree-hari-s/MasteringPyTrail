from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import datetime as dt
import requests
import webbrowser

THEME_COLOR = "#F0F0F0"
TODAY = dt.datetime.now()
USERNAME = "sreeharis"
TOKEN = "fasjkhfalksjhffas"
GRAPH_ID = "graph2"

headers = {
    "X-USER-TOKEN": TOKEN
}
URL = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2.html"

class TrackerInterface:
    def __init__(self):
        self.headers = headers
        self.window = Tk()
        self.window.title("Habit Tracker")
        self.window.resizable(width=False, height=False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Calendar setup
        self.cal = Calendar(
            self.window,
            selectmode="day",
            year=TODAY.year,
            month=TODAY.month,
            day=TODAY.day,
        )
        self.cal.grid(row=0, column=0, columnspan=4)
        # Input fields
        self.units = Label(text="Hours/Day:")
        self.units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
        self.user_in = Entry(width=10)
        self.user_in.grid(row=1, column=2, sticky="w")
        # Buttons setup
        self.add = Button(
            text="Add",
            command=self.add_pixel
        )
        self.add.grid(row=2, column=0, pady=10)
        self.update = Button(
            text="Update",
            command=self.change_pixel
        )
        self.update.grid(
            row=2,
            column=1,
        )
        self.delete = Button(
            text="Delete",
            command=self.del_pixel
        )
        self.delete.grid(
            row=2,
            column=2,
        )
        self.link = Button(
            text="View Progress",
            command=self.open_browser
        )
        self.link.grid(row=2, column=3)

        self.window.mainloop()

    def open_browser(self):
        webbrowser.open(URL, new=1)

    def format_date(self):
        self.cal.config(date_pattern="yyyyMMdd")
        self.date = self.cal.get_date()
        self.cal.config(date_pattern="dd/MM/yyyy")
        return self.date

    def add_pixel(self):
        self.endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2/"
        self.pixel_add = {
            "date": self.format_date(),
            "quantity": self.user_in.get(),
        }
        requests.post(url=self.endpoint, json=self.pixel_add, headers=self.headers)
        self.user_in.delete(0, END)
        messagebox.showinfo(message="Pixel added.")

    def del_pixel(self):
        self.endpoint = (
            f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2/{self.format_date()}"
        )
        requests.delete(url=self.endpoint, headers=self.headers)
        messagebox.showinfo(message="Pixel deleted.")

    def change_pixel(self):
        self.endpoint = (
            f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2/{self.format_date()}"
        )
        self.pixel_update = {
            "quantity": self.user_in.get(),
        }
        requests.put(
            url=self.endpoint, json=self.pixel_update, headers=self.headers
        )
        self.user_in.delete(0, END)
        messagebox.showinfo(message="Pixel updated.")