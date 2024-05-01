from turtle import Turtle

class Player(Turtle):
    def __init__(self):
      super().__init__()
      self.color("green")
      self.shape("turtle")
      self.setheading(90)
      self.penup()


    def move_up(self):
        self.setheading(90)
        self.forward(10)


    def move_down(self):
        self.setheading(270)
        self.forward(10)


    def move_right(self):
        self.setheading(0)
        self.forward(10)


    def move_left(self):
        self.setheading(180)
        self.forward(10)
