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
print(screen.screensize())

screen_x = screen.screensize()[0]
screen_y = screen.screensize()[1]



snake = [Snake((0,0)), Snake((-20,0)), Snake((-40,0))]
snake_coords = []

first_snake = snake[0]
# first_snake.piece.color("blue")
# snake[1].piece.color("red")

game_active = True

# Set screen delay
screen.tracer(n=1, delay=50)


# Move snake
def move_snake():
    dist = 2

    for i in snake:
        i.piece.forward(dist)
        snake_coords.append(i.piece.pos())


def move_snake_up():
    coord = first_snake.piece.pos()
    for i in snake:
        last_coord = snake_coords[len(snake_coords)-1]
        if i.piece == first_snake.piece:
            i.piece.setheading(90)
            i.piece.setpos((coord[0], coord[1] + 20))
        else:
            i.piece.setheading(90)
            i.piece.setpos((last_coord[0],last_coord[1] - 20))

        snake_coords.append(i.piece.pos())


def move_snake_down():
    coord = first_snake.piece.pos()
    for i in snake:
        last_coord = snake_coords[len(snake_coords)-1]
        if i.piece == first_snake.piece:
            i.piece.setheading(270)
            i.piece.setpos((coord[0], coord[1] - 20))
            screen.tracer(n=1, delay=80)
        else:
            i.piece.setheading(270)
            i.piece.setpos((last_coord[0],last_coord[1] + 20))

        snake_coords.append(i.piece.pos())


def move_snake_right():
    coord = first_snake.piece.pos()
    for i in snake:
        last_coord = snake_coords[len(snake_coords)-1]
        if i.piece == first_snake.piece:
            i.piece.setheading(0)
            i.piece.setpos((coord[0]+20, coord[1]))
            screen.tracer(n=1, delay=80)
        else:
            i.piece.setheading(0)
            i.piece.setpos((last_coord[0]-20,last_coord[1]))

        snake_coords.append(i.piece.pos())


def move_snake_left():
    coord = first_snake.piece.pos()
    for i in snake:
        last_coord = snake_coords[len(snake_coords)-1]
        if i.piece == first_snake.piece:
            i.piece.setheading(180)
            i.piece.setpos((coord[0]-20, coord[1]))
            screen.tracer(n=1, delay=80)
        else:
            i.piece.setheading(180)
            i.piece.setpos((last_coord[0]+20,last_coord[1]))

        snake_coords.append(i.piece.pos())


print(snake_coords)

screen.listen()
screen.onkeypress(key="Up",fun=move_snake_up)
screen.onkeypress(key="Down",fun=move_snake_down)
screen.onkeypress(key="Right",fun=move_snake_right)
screen.onkeypress(key="Left",fun=move_snake_left)


# Start snake
while game_active:
    move_snake()

screen.exitonclick()
