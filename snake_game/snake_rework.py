from turtle import Turtle

class Snake():
    def __init__(self):
        self.piece = Turtle()
        self.piece.color("white")
        self.piece.speed(0)
        self.piece.penup()
        self.piece.shape("square")


    # def move_forward(self):
    #     for i in self.snake_body:
    #         i.piece.forward(10)
