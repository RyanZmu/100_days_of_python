"""
PONG Game!

"""
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from random import randint

# Screen settings
screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")

# Screen boundaries
MAX_X = 400
MIN_X = -400
MAX_Y = 400
MIN_Y = -400

# Set up divider - maybe add to scoreboard and call Board
dividing_line = Turtle()
dividing_line.color("white")
dividing_line.speed("fastest")
dividing_line.hideturtle()
dividing_line.teleport(0, MAX_Y)
dividing_line.setheading(270)

# Create divider down middle of board\
i = 0
while i<50:
    dividing_line.forward(10)
    dividing_line.penup()
    dividing_line.forward(10)
    dividing_line.pendown()
    i+=1

# Set up scoreboards - move then display
score_1 = Scoreboard()
score_1.teleport(-30, MAX_Y)
score_1.display_board()

score_2 = Scoreboard()
score_2.teleport(30, MAX_Y)
score_2.display_board()

# Create Paddles
paddle_1 = Paddle()
paddle_1.teleport(MIN_X - 5, 0)

paddle_2 = Paddle()
paddle_2.teleport(MAX_X, 0)

game_active = True

# Keys
screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")

# Create Ball
pong_ball = Ball()


while game_active:
    # Move ball if not out of bounds
    pong_ball.ball_check()
    screen.delay(3)
    paddle_2.cpu_player(pong_ball)

    # Determine if paddle was hit
    if pong_ball.distance(paddle_2) < 40:
        pong_ball.bounce()
    if pong_ball.distance(paddle_1) < 40:
        pong_ball.bounce()

    # Score keeping
    if pong_ball.xcor() > MAX_X:
        score_1.increase_score()
    elif pong_ball.xcor() < MIN_X:
        score_2.increase_score()


screen.exitonclick()
