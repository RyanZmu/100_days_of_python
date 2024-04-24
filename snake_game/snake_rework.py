from turtle import Turtle

class Snake():
    def __init__(self, pos):
        self.piece = Turtle()
        self.piece.setpos(pos)
        self.piece.color("white")
        self.piece.speed(0)
        self.piece.shapesize(outline=1.0)
        self.piece.penup()
        self.piece.shape("square")

