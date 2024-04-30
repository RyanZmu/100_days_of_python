from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.resizemode("user")
        self.shapesize(5.0,5.0)
        self.color("white")
        self.speed("fastest")
        self.score = 0


    def display_board(self):
        self.write(self.score)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score)
