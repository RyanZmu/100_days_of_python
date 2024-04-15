import turtle as t
import random as r

# Imported via Alias
print(r.randint(1,20))

timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("green")

# Challenge 1: Draw a Square
timmy_turtle.forward(100)
timmy_turtle.right(90)
timmy_turtle.forward(100)
timmy_turtle.right(90)
timmy_turtle.forward(100)
timmy_turtle.right(90)
timmy_turtle.forward(100)
timmy_turtle.right(90)


# Challenge 2: Draw a dashed line
i = 0
while i<20:
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)
    timmy_turtle.pendown()
    i+=1

colors = ["red", "blue", "green", "orange", "purple", "grey", "black", "brown"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)


for shape_side_n in range(3, 10):
    timmy_turtle.color(r.choice(colors))
    draw_shape(shape_side_n)


# Challenge 4: random walking + color changing
# Tuples
# Data type (1,3,8) - Like a list but ordered and immutable
# Useful when you want a const list that can't be changed
my_tuple= (1,3,8)
my_tuple[0]

# If you need to change a tuple, you can change it to a list and now it is mutable
list(my_tuple)

# Change turtle modules color mode
t.colormode(255)


# Create random RGB colors
def random_color():
    r_int = r.randint(0, 255)
    g_int = r.randint(0, 255)
    b_int = r.randint(0, 255)

    color = (r_int, g_int, b_int)
    return color


def random_walk():
    timmy_turtle.pensize(20)
    timmy_turtle.speed("fastest")
    directions=[0,90,180,270]

    # Use random color function
    timmy_turtle.color(random_color())

    timmy_turtle.forward(30)
    timmy_turtle.setheading(r.choice(directions))
    return


for _ in range(200):
    random_walk()


# Challenge 5: Draw a spirograph
def draw_circle(size_of_gap):
    timmy_turtle.pensize(1)
    timmy_turtle.speed("fastest")

    # Divide by size of gap to ensure the turtle will not go over lines twice
    for _ in range(int(360 / size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)


draw_circle(size_of_gap=5)

screen = t.Screen()
screen.exitonclick()
