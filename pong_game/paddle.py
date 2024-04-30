from turtle import Turtle
from random import randint, choice

# Screen boundaries
MAX_X = 400
MIN_X = -400
MAX_Y = 400
MIN_Y = -400

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        # self.speed(0)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)


    def move_up(self):
        if self.ycor() < MAX_Y:
            self.forward(20)


    def move_down(self):
        if self.ycor() > MIN_Y:
            self.backward(20)


    # Refactor to try and detect ball instead of picking random points
    def cpu_player(self, ball):
        self.speed("slowest")
        print({'ball': ball.pos()})

        # Match balls axis
        self.sety(ball.ycor())

        # rand_num = randint(-400,400)
        # directions = [self.forward(rand_num), self.backward(rand_num)]
        # choice(directions)