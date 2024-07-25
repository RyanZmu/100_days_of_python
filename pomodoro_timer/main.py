from tkinter import *
import math

# ------------- CONSTANTS -------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark_pos = 1
timer = None

# ------------- TIMER RESET -------------- #
def reset_timer():
    global reps, timer, timer_text
    print("reset")
    reps = 0
    window.after_cancel(timer)
    action_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    # countdown(0)

# ------------- TIMER MECHANISM -------------- #
def start_timer():
    global reps, check_mark_pos, timer_active
    timer_active = True
    reps += 1
    print({'reps': reps})

    # Value of minutes in seconds
    work_sec = 5 #5/60
    short_break_sec = 3
    long_break_sec = 4

    # If it is 1st/3rd/5th/7th rep - pass into work countdown
    if reps % 8 == 0:
        countdown(long_break_sec)
        action_label.config(text="Long Break - 20 Minutes")
        print('long break')
    elif reps % 2 == 0:
        action_label.config(text="Short Break - 5 Minutes")
        countdown(short_break_sec)


        print('short')
    else:
        countdown(work_sec)
        action_label.config(text="Work - 25 Minutes")
        print('work')

# ------------- COUNTDOWN MECHANISM -------------- #
def countdown(count):
    global reps, check_mark, check_mark_pos, timer
    print(count)
    minute = math.floor(count / 60)
    seconds = count % 60

    # This way turns an int into a str = (Dynamic typing)
    # Python, like JS allows us to reassign vars from one data type to another
    if seconds == 0:
        seconds = f'{seconds}0'
    elif seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minute}:{seconds}')

    if count > 0:
       timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and count == 0:
            print("check!")
            print("check!")
            check_mark_pos += 1
            print({'check_mark_pos': check_mark_pos})
            check_mark.grid(column=2,row=3)
            # check_mark_pos += 1
            # print({'check_mark_pos': check_mark_pos})

        #     check_mark.grid(column=2,row=3)

# ------------- UI SETUP -------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=200, bg=YELLOW)

# Canvas widget
canvas = Canvas(width=640, height=628, bg=YELLOW, highlightthickness=0)
tomato_image_file = PhotoImage(file="pomodoro_timer/images/tomato.png")
canvas.create_image(320, 315, image=tomato_image_file)

timer_text = canvas.create_text(320, 350, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# timer.text.

# Add a label above the tomato, and a start/reset button on either side of the tomato
# Also add a label (checkmark) for how many Pomodoros are completed - Each 25 min work session = Checkmark
main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
action_label = Label(text="Pomodoro!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
start_button= Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)


check_mark_image = PhotoImage(file="pomodoro_timer/images/checkmark.png")
check_mark = Label(image=check_mark_image,bg=YELLOW)
# check_mark_canvas = Canvas(width=10, height=20, bg=YELLOW, highlightthickness=0)
# check_mark_image = PhotoImage(file="pomodoro_timer/images/checkmark.png")
# canvas.create_image(5, 5, image=check_mark_image)

main_label.grid(column=2, row=1)
action_label.grid(column=2, row=4)
canvas.grid(column=2, row=2)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

window.mainloop()
