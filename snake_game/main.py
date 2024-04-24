"""
Create a Snake game!

Phase 1:
- Create the Screen and Snake body
- Animate the snake
- Create a Snake Class for segments
- Control snake with arrow keys

Phase 2:
- Class inheritance
- Collision detection with food
- Scoreboard
- Collision detection with wall and tail
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Set Boundaries
MAX_X = 425
MIN_X = -425
MAX_Y = -425
MIN_Y = 425

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_active = True

while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Set a tolerance so the snake doesn't need to be exactly over the food piece
    dist_tolerance = 15
    # Check if snake eats food
    if snake.head.distance(food) <= dist_tolerance:
        food.create_food()
        snake.extend()
        scoreboard.add_score()

    # Check for body collisions
    for seg in snake.segments:
        print(seg.pos())
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_active= False

    # Check if snake hits a wall
    if snake.head.xcor() >= MAX_X or snake.head.xcor() <= MIN_X or snake.head.ycor() <= MAX_Y or snake.head.ycor() >= MIN_Y:
        game_active = False
        scoreboard.game_over()


screen.exitonclick()
