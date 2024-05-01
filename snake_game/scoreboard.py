from turtle import Turtle

# Read high score and set to a variable
with open(file="./snake_game/high_scores", mode="r") as hs_file:
    high_score = int(hs_file.read())

class ScoreBoard():
    def __init__(self) -> None:
        self.board = Turtle()
        self.board.color("white")
        self.high_score = high_score
        self.score = 0
        self.board.pensize(40)
        self.board.hideturtle()
        self.board.teleport(-300, 350)
        self.update_board()


    def update_board(self):
        self.board.clear()
        self.board.write(arg=f"Score: {self.score} High Score: {self.high_score}", font=(10))


    def add_score(self):
        self.score += 1
        self.update_board()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open(file="./snake_game/high_scores", mode="w") as hs_file:
            hs_file.write(f"{self.high_score}")

        # Reset score
        self.score = 0
        self.update_board()
