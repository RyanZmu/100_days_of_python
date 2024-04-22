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

game_active = True

# Screen init
screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor('black')

# Capture the max x and y values
x_axis_boundary = 420
y_axis_boundary = -420

# Create a snake array - initial snake piece has a default heading and coord
# test_snake = Snake()
snake = [Snake(), Snake(), Snake()]
snake_dist = 30.0


def add_snake():
    new_snake = Snake()
    new_snake.snake.hideturtle()
    snake.append(new_snake)
    # group_snake()
    new_snake.snake.showturtle()
    snake.dist += 10.0

    print(snake)


def move_up():
    for section in snake:
        section.turn_up()
        # group_snake()



def move_down():
    for section in snake:
        section.turn_down()
        # group_snake()



def move_right():
    for section in snake:
        section.turn_right()
        # group_snake()



def move_left():
    for section in snake:
        section.turn_left()
        # group_snake()


# def group_snake():
#     first_seg_coords = snake[0].snake.pos()
#     first_heading = snake[0].snake.heading()

#     for section in snake:
#         print(section.snake == snake[0].snake)
#         if section.snake != snake[0].snake:
#             print('not first section')
#             section.snake.teleport(first_seg_coords[0],first_seg_coords[1])
#             section.snake.setheading(first_heading)
#         else:
#             section.move_forward()


# Snake controls
screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left", fun=move_left)

# Test key for making new segments, delete once food implemented
screen.onkeypress(key="c", fun=add_snake)

"""
To DO:
Make the snake 3 pieces long
"""

# while game_active: - if screen.listen() is triggered, changes snake direction
while game_active:
    screen.tracer(1, 25)
    # snake[0].move_forward()
    dist = 10

    first_snake = snake[0].snake
    last_snake = snake[len(snake)-1].snake
    print({"distance from first to last": first_snake.distance(last_snake)})

    distance_between_snakes = first_snake.distance(last_snake)

    # if distance_between_snakes >= snake_dist:
    #     # screen.delay(100)
    #     group_snake()

    # Color snake blue to debug
    snake[0].snake.color('blue')

    for seg in range(len(snake)):
        last_piece_coord = snake[seg - 1].snake.pos()
        screen.delay(100)
        if snake[seg].snake != snake[0].snake:
            snake[seg].snake.setpos(last_piece_coord)
        if snake[seg].snake.pos == snake[seg - 1].snake.pos():
            snake[seg].setpos(snake[seg - 1].snake.xcor() - 1, snake[seg - 1].snake.ycor())

    for segment in snake:
        # if segment.snake.pos() == snake[0].snake.pos():

        # Start moving snake initially
        if segment.snake.xcor() < x_axis_boundary:
            segment.snake.forward(dist)
            print(segment.snake.pos())
            dist += 10

        # If too far right
        if segment.snake.xcor() >= x_axis_boundary:
            segment.turn_left()
            # segment.move_forward()
            segment.snake.forward(dist)
            print(segment.snake.pos())
            print("too far right")
            dist += 10

        # If too far left
        if segment.snake.xcor() <= -x_axis_boundary:
            segment.turn_right()
            # segment.move_forward()
            segment.snake.forward(dist)
            print(segment.snake.pos())
            print("too far left")
            dist += 10

        # If too far up
        if segment.snake.ycor() >= -y_axis_boundary:
            segment.turn_down()
            # segment.move_forward()
            segment.snake.forward(dist)
            print(segment.snake.pos())
            print("too far up")
            dist += 10

        # If too far down
        if segment.snake.ycor() <= y_axis_boundary:
            segment.turn_up()
            # segment.move_forward()
            segment.snake.forward(dist)
            print(segment.snake.pos())
            print("too far down")
            dist += 10



screen.exitonclick()
