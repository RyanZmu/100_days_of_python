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
from snake_rework import Snake


screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")


snake = [Snake(), Snake(), Snake()]
first_snake = snake[0]
first_snake.piece.color("blue")
snake[1].piece.color("red")

game_active = True


# Move snake
def move_snake():
    dist = 20

    for i in snake:
        if i.piece == first_snake.piece:
            i.piece.penup()
            i.piece.forward(dist)
            i.piece.pendown()
        else:
            i.piece.penup()
            i.piece.forward(dist)
            i.piece.pendown()
            screen.delay(30)
            print(i.piece.pos())




        # if dist < max_dist:
        #     screen.delay(30)
        #     dist += 2
        #     i.piece.forward(dist)
        #     print(dist)
        # else:
        #     screen.delay(30)
        #     dist += 2
        #     i.piece.forward(dist)

    screen.update()
    screen.tracer(1, 500)



while game_active:
    move_snake()


screen.exitonclick()
