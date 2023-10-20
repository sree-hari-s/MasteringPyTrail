from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    check_mark.config(text="")
    heading_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps == 8:
        # 8th rep
        heading_label.config(text="Break", fg=RED)
        countdown(long_break_seconds)
    elif reps % 2 == 0:
        # 2nd/4th/6th reps:
        heading_label.config(text="Short-Break", fg=PINK)
        countdown(short_break_seconds)
    else:
        # 1st/3rd/5th/7th reps:
        heading_label.config(text="Work", fg=GREEN)
        countdown(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """
    Display the timer in 00:00 format
    """
    count_min = floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = floor(reps / 2)
        for _ in range(0, work_session):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

heading_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
heading_label.grid(column=2, row=1)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

stop_button = Button(text="Stop", highlightthickness=0, command=reset_timer)
stop_button.grid(column=3, row=3)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
check_mark.grid(column=2, row=4)

window.mainloop()
