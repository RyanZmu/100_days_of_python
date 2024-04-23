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
first_snake.piece.color("blue")
snake[1].piece.color("red")

game_active = True


screen.tracer(1, 25)
# Move snake
def move_snake():
    dist = 2

    for _ in range(0, screen_x):
       for i in snake:
            if i.piece == first_snake.piece:
                i.piece.forward(dist)
                # snake_coords.append(i.piece.pos())
            else:
                i.piece.towards(snake_coords[len(snake_coords)-1])
                i.piece.forward(dist)

            snake_coords.append(i.piece.pos())

    print(snake_coords)
# screen.update()


def move_snake_up():
    dist = 2

    for _ in range(0, screen_x):
       for i in snake:
            last_coord = snake_coords[len(snake_coords)-1]
            if i.piece == first_snake.piece:
                i.piece.setheading(90)
                i.piece.forward(dist)
            else:
                i.piece.setheading(90)
                i.piece.setpos((last_coord[0],last_coord[1] - 20))
                i.piece.forward(dist)

            snake_coords.append(i.piece.pos())

    print(snake_coords)



def move_snake_down():
    dist = 2

    for _ in range(0, screen_x):
       for i in snake:
            last_coord = snake_coords[len(snake_coords)-1]
            if i.piece == first_snake.piece:
                i.piece.setheading(270)
                i.piece.forward(dist)
            else:
                i.piece.setheading(270)
                i.piece.setpos((last_coord[0],last_coord[1] + 20))
                i.piece.forward(dist)

            snake_coords.append(i.piece.pos())

    print(snake_coords)


def move_snake_right():
    dist = 2

    for _ in range(0, screen_x):
       for i in snake:
            last_coord = snake_coords[len(snake_coords)-1]
            if i.piece == first_snake.piece:
                i.piece.setheading(0)
                i.piece.forward(dist)
            else:
                i.piece.setheading(0)
                i.piece.setpos((last_coord[0]-20,last_coord[1]))
                i.piece.forward(dist)

            snake_coords.append(i.piece.pos())

    print(snake_coords)



def move_snake_left():
    dist = 2

    for _ in range(0, screen_x):
       for i in snake:
            last_coord = snake_coords[len(snake_coords)-1]
            if i.piece == first_snake.piece:
                i.piece.setheading(180)
                i.piece.forward(dist)
            else:
                i.piece.setheading(180)
                i.piece.setpos((last_coord[0]+20,last_coord[1]))
                i.piece.forward(dist)

            snake_coords.append(i.piece.pos())

    print(snake_coords)


screen.listen()
screen.onkeypress(key="Up",fun=move_snake_up)
screen.onkeypress(key="Down",fun=move_snake_down)
screen.onkeypress(key="Right",fun=move_snake_right)
screen.onkeypress(key="Left",fun=move_snake_left)


# Start snake
move_snake()


# while game_active:
#     move_snake_x()


screen.exitonclick()
