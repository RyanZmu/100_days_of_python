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

# ------------- TIMER RESET -------------- #

# ------------- TIMER MECHANISM -------------- #
def start_timer():
    countdown(WORK_MIN * 60)


# ------------- COUNTDOWN MECHANISM -------------- #
def countdown(count):
    print(count)
    minute = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f'{minute}:{seconds}')

    if count > 0:
        window.after(1000, countdown, count - 1)
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
start_button= Button(text="Start", command=start_timer)
reset_button = Button(text="Reset")

check_mark_image = PhotoImage(file="pomodoro_timer/images/checkmark.png")
check_mark = Label(image=check_mark_image,bg=YELLOW)

# check_mark_canvas = Canvas(width=10, height=20, bg=YELLOW, highlightthickness=0)
# check_mark_image = PhotoImage(file="pomodoro_timer/images/checkmark.png")
# canvas.create_image(5, 5, image=check_mark_image)

main_label.grid(column=2, row=1)
canvas.grid(column=2, row=2)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)
check_mark.grid(column=2,row=3)

window.mainloop()
