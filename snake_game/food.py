from turtle import Turtle
from random import choice, randint
# POSITIONS = [(0,-100), (120,40), (-100,-40)]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(0.5,0.5)


    def create_food(self):
        self.goto(x=randint(-400,400),y=randint(-400,400))
