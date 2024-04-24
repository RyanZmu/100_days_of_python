from turtle import Turtle

class ScoreBoard():
    def __init__(self) -> None:
        self.board = Turtle()
        self.board.color("white")
        self.score = 0
        self.board.pensize(40)
        self.board.hideturtle()
        self.board.teleport(-300, 350)
        self.board.write(arg=f"Score: {self.score}", font=(10))

    def add_score(self):
        self.score += 1
        self.board.clear()
        self.board.write(arg=f"Score: {self.score}", font=(10))


    def game_over(self):
        self.board.clear()
        self.board.write(arg="You Lose!", font=(10))
