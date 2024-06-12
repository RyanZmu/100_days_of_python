from tkinter import *

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

# ------------- COUNTDOWN MECHANISM -------------- #

# ------------- UI SETUP -------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=200, bg=YELLOW)

# Canvas widget
canvas = Canvas(width=640, height=628, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="pomodoro_timer/images/tomato.png")
canvas.create_image(320, 315, image=tomato_image)
canvas.create_text(320, 350, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()



window.mainloop()
