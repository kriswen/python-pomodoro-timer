from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
#  https://colorhunt.co/palette/fa7070fefdedc6ebc5a1c398
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)  # to cancel the window.after in count_down function
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it's 1/3/5/7 reps - work
    if reps % 8 == 0:
        count_down(5)#long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    # if its 2/4/6 reps - short break
    elif reps % 2 == 0:
        count_down(5)#short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    # if its 8 reps - long break
    else:
        count_down(5)#work_secs)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    second = count % 60
    minute = math.floor(count / 60)
    # if second < 10:
    #     second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute:02}:{second:02}")
    print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:  # catch when count go down to zero, to call start_timer() again.
        start_timer()
        marks = ""
        # every 2 reps means completed 25 work section
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmarks_label.config(text=f"{marks}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
# def say_something(a,b,c,):
#     print(a, b, c)
# window.after(1000, say_something, 3,4,5)
# Canvas
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)  # highlightthickness to remove border
# read through a file to get image at file location
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # x and y of location, put in the center
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# Timer title Label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)
# Start Button & Reset Button
start_btn = Button(text="START", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="RESET", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)
# Checkmark Label
checkmarks_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
checkmarks_label.grid(column=1, row=4)

window.mainloop()
