from turtle import Turtle, Screen
import random as r

# init Turtle objects
# Refactor into a reusable and less repetitive function in future revision
turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.color("red")
turtle_1.penup()

turtle_2 = Turtle()
turtle_2.shape('turtle')
turtle_2.color("blue")
turtle_2.penup()

turtle_3 = Turtle()
turtle_3.shape('turtle')
turtle_3.color("green")
turtle_3.penup()

turtle_4 = Turtle()
turtle_4.shape('turtle')
turtle_4.color("yellow")
turtle_4.penup()

turtle_5 = Turtle()
turtle_5.shape('turtle')
turtle_5.color("orange")
turtle_5.penup()

turtle_6 = Turtle()
turtle_6.shape('turtle')
turtle_6.color("purple")
turtle_6.penup()

# init Screen obj
screen = Screen()
screen.title("Turtle Race Day!")

# Get screensize
screen_size = screen.screensize()
screen_max_x = screen_size[0]
screen_max_y = screen_size[1]

# Create array of turtle objects
turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6]

# Track race progress
race_finished = False

# init finish sign to output winner
finish_sign = Turtle()
finish_sign.hideturtle()

# Prompt user
player_input = screen.textinput('Guess The Winner!', 'What turtle color will win? (red,blue,green,yellow,orange or purple)')


# Turtle Race
def prep_race():
    # Draw a start and finish line
    # Sort of weird but works for now
    start_line = Turtle()
    finish_line = Turtle()

    start_line.hideturtle()
    start_line.penup()
    start_line.setpos(-screen_max_x, -screen_max_y)
    start_line.pendown()
    start_line.right(90)
    start_line.forward(-screen_max_y*2)

    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setpos(screen_max_x, screen_max_y)
    finish_line.pendown()
    finish_line.left(90)
    finish_line.forward(-screen_max_y*2)

    # Set up Turtle starting positions
    turtle_start_x = -screen_size[0]
    turtle_start_y = -screen_size[1]

    # Move turtles to start positions
    for turtle in turtles:
        turtle_start_y += 80
        turtle.setpos(turtle_start_x, turtle_start_y)
    return


def race(turtle):
    global race_finished

    # Get xcoords and color
    turtle_pos = turtle.xcor()
    current_turtle_color = turtle.pen()["pencolor"]

    # Check if at screen end and output winner
    if turtle_pos >= screen_max_x:
        race_finished = True
        if player_input.lower() == current_turtle_color:
            finish_sign.write(f"You Win! The {current_turtle_color} turtle Won", align="center")
        else:
            finish_sign.write(f"You Lose! The {current_turtle_color} turtle Won", align="center")
    else:
        turtle.forward(10)
    return


# Set up turtles on starting line for the race
prep_race()

# Check that race is not over
# Gives a random turtle to race function (Refactor later and improve logic flow)
while race_finished == False:
    race(r.choice(turtles))

# Screen
screen.listen()
screen.exitonclick()
