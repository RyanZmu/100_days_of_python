from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

etch.pensize(4)

# Functions
def move_forward():
    etch.forward(10)


def move_backward():
    etch.backward(10)


def move_left():
    etch.left(10)


def move_right():
    etch.right(10)


def clear_drawing():
    etch.clear()
    etch.penup()
    etch.home()
    etch.pendown()

# Event Listeners
screen.onkey(key='Up', fun=move_forward)
screen.onkey(key='Down', fun=move_backward)
screen.onkey(key='Left', fun=move_left)
screen.onkey(key='Right', fun=move_right)
screen.onkey(key='c', fun=clear_drawing)



screen.listen()
screen.exitonclick()