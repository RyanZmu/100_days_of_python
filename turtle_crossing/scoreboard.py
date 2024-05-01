from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.teleport(-400, 400)
        self.update_board()


    def update_board(self):
        self.clear()
        self.write(f"LEVEL: {self.level}")


    def increase_level(self):
        self.level += 1
        self.update_board()


    def game_over(self):
        self.clear()
        self.teleport(0,0)
        self.write("*squish*")


    def winner(self):
        self.clear()
        self.teleport(0,0)
        self.write("WINNER!")
