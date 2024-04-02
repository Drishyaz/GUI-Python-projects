import math
from tkinter import *
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
    # this window.after_cancel() function cancels TIMER which is passed in the ()
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# this method starts the timer; we calculate time for different sessions in sec
def start_timer():
    global reps
    reps += 1                                   # reps keeps track of which session it should be

    work_sec = WORK_MIN * 60                    # 25 min; test 20s
    short_break_sec = SHORT_BREAK_MIN * 60      # 5 min; test 5s
    long_break_sec = LONG_BREAK_MIN * 60        # 20 min; test 10s
    # debugging
    # work_sec = 20
    # short_break_sec = 5
    # long_break_sec = 10

    # if it is the 8th reps, we take a LONG BREAK
    if reps % 8 == 0:
        # everytime we are sending the total sec to count_down()
        count_down(long_break_sec)
        # the label that shows TIMER is changed to the corresponding session name
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # even reps except 8th then we take short break
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    # if it is odd reps => 1st, 3rd, 5th or 7th then we WORK so 25 min * 60
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):                              # this method counts down from N to 0

    count_min = math.floor(count / 60)              # get the time remaining in minutes
    count_sec = count % 60                          # get the time remaining in seconds
    if count_sec < 10:                              # when the amount of sec gets to 0
        count_sec = f"0{count_sec}"

    # canvas.itemconfig() is like config()
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # display time in mm:ss format
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        # window.after(ms,function, something) does something and calls function() after ms time
    else:
        start_timer()
        # start the timer again and again whenever the count reaches 0
        marks = ""
        # counts the number of sessions that have happened so far
        # we need the check mark to appear when we complete one session = 1 work + 1 short break
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        checkmark.config(text=marks)
    # ✔️ ️


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()                                           # first initialize a window and its title
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)             # let's change the bg color to YELLOW

# placing the "TIMER" label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
timer_label.grid(row=0, column=1)

# placing the image in canvas in the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# to place an img in window, we need canvas; 'highlightthickness' maintains the border around the canvas
tomato_img = PhotoImage(file="tomato.png")              # the img can't be added directly until processed
canvas.create_image(100, 112, image=tomato_img)   # we create_image() the image, x, y
# this text shows the 00:00 COUNTDOWN
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)


# START and RESET buttons
start_button = Button(text="Start", command=start_timer)  # when we click START button, the timer starts
reset_button = Button(text="Reset", command=reset_timer)  # when we click RESET, timer cancels
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

# CHECKMARK LABEL
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()
