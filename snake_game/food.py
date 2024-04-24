from turtle import Turtle
from random import choice, randint
# POSITIONS = [(0,-100), (120,40), (-100,-40)]

class Food():
    def __init__(self):
        self.create_food()


    def create_food(self):
        self.food_item = Turtle()
        self.food_item.color("blue")
        self.food_item.shape("circle")

        self.food_item.penup()
        self.food_item.teleport(x=randint(-400,400),y=randint(-400,-00))
        self.food_item.pendown()
