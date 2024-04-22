from turtle import Turtle

class Snake():
    def __init__(self):
        self.snake = Turtle()
        self.snake.color("white")
        self.snake.speed(0)
        self.snake.penup()
        self.current_coords = self.snake.pos()
        self.snake.shape("square")


    def move_forward(self):
        self.snake.forward(25)
        self.current_coords = self.snake.pos()


    # 90
    def turn_up(self):
        self.snake.setheading(90)
        self.current_coords = self.snake.pos()


    # 270
    def turn_down(self):
        self.snake.setheading(270)
        self.current_coords = self.snake.pos()


    # 0
    def turn_right(self):
        self.snake.setheading(0)
        self.current_coords = self.snake.pos()


    # 180
    def turn_left(self):
        self.snake.setheading(180)
        self.current_coords = self.snake.pos()
