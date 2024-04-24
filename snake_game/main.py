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
from turtle import Screen, Turtle
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

game_active = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Create a turtle and hide it to use for writing
game_sign = Turtle()
game_sign.color("white")
game_sign.hideturtle()

while game_active:
    screen.update()

    # add delay
    time.sleep(0.1)

    # Set a tolerance so the snake doesn't need to be exactly over the food piece
    dist_tolerance = 15

    # Check if snake eats food
    if snake.head.distance(food.food_item) <= dist_tolerance:
        print("food!")
        scoreboard.add_score()

        food.food_item.hideturtle()
        snake.create_snake()
        food.create_food()

    # Check for body collisions
    for i in snake.segments:
        print(i.pos())
        if snake.head.pos() == i.pos() and i != snake.head:
            print("Body Hit")

            game_active = False
            scoreboard.game_over()


    # Check if snake hits a wall
    if snake.head.xcor() >= MAX_X or snake.head.xcor() <= MIN_X or snake.head.ycor() <= MAX_Y or snake.head.ycor() >= MIN_Y:
        game_active = False
        scoreboard.game_over()

    else:
        snake.move()

screen.exitonclick()
