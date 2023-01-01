import tkinter as tk
import math
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ----------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if its the 8th rep and time for a long break:
    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    # if its 2 / 4 6h rep, it's time for a break:
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    # if its the 1st/3rd/5th/7th rep:
    else:
        countdown(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM -------------------------- #
# you cannot use while loops when using tkinter, so we need to use
# the tkinter .after() function. Here it calls the countdown
# function with count -1 as the argument.


def countdown(count):
    # changing canvas properties works a bit different. Use .imemconfig
    # You pass in the object, and then you add the thing you want to change.

    # get the amount of minutes, and the remaining seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        # update the check marks
        mark = ""
        for i in range(math.floor(reps / 2)):
            mark += ""
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create the background
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# add the tomato
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(column=1, row=1)

# set text in the tomato
timer_text = canvas.create_text(101, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))


# timer text above tomato
label_timer = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                       font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

# buttons
start_button = tk.Button(text="Start", highlightthickness=0,
                         command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset",
                         highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# check marks
check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
