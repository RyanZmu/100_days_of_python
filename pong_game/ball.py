from turtle import Turtle
from random import randint, choice

START_ANGLES = [0,70,130,210]
HIT_POS= [()]

# Screen boundaries
MAX_X = 400
MIN_X = -400
MAX_Y = 400
MIN_Y = -400


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.out_of_bounds = False
        self.penup()
        self.ball_check()


    def reset_start_location(self):
        # Chooses a random location along Y-Axis
        self.teleport(0, randint(MIN_Y,MAX_Y))
        self.setheading(choice(START_ANGLES))
        self.out_of_bounds = False


    def bounce(self):
        current_heading = self.heading()
        self.setheading(current_heading + 45)
        self.forward(5)
        print(current_heading)
        print("bounce")


    def ball_check(self):
        # Checks if ball is out of bounds
        if self.xcor() > MAX_X:
            print("Out of bounds")
            self.out_of_bounds = True
            self.reset_start_location()
        elif self.xcor() < MIN_X:
            print("Out of bounds")
            self.out_of_bounds = True
            self.reset_start_location()

        # Checks if ball hits top or bottom wall
        if self.ycor() > MAX_Y:
            print("Top")
            self.bounce()
        elif self.ycor() < MIN_Y:
            print("Bottom")
            self.bounce()
        else:
            self.forward(5)
