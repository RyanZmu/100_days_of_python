from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# Class based TKinter

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(height=500, width=500, bg="white")
        self.question_text = self.canvas.create_text(
            250,
            250,
            text="Question Text",
            font=("Arial", 20, "italic"),
            width=230,
            fill=THEME_COLOR)
        self.score = Label(
            text=f"Score:{self.quiz.score}",
            padx=30,
            pady=30,
            background=THEME_COLOR,
            fg="white")
        self.true_button_image = PhotoImage(file="./quiz_project/images/right.png")
        self.false_button_image = PhotoImage(file="./quiz_project/images/wrong.png")
        self.true_button = Button(
            image=self.true_button_image,
            highlightthickness=0,
            command=self.check_true
        )
        self.false_button = Button(
            image=self.false_button_image,
            highlightthickness=0,
            command=self.check_false
        )

        self.canvas.grid(column=0, row=1, columnspan=2)
        self.score.grid(column=1, row=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of the quiz!\n\n Final Score: {self.quiz.score}"
                                   )
            # Disable buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)


