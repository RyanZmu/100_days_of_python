"""
Create a Hirst painting!
- Use colorgram to extract color palatte from a Damien Hirst painting
- Use this color scheme for the project
- Have dots with an even amount of space on all sizes randomly colored and place along a grid
- 10 by 10 rows
- Dots sized to 20
- Dots should be 50 spaces apart
"""
import colorgram as c
import turtle as t
import random as r

# Init objects
turtle_turtle = t.Turtle()
screen = t.Screen()


def create_painting(num_of_dots):
    t.colormode(255)
    turtle_turtle.speed('fastest')

    # Extract each RGB value and use it on the turtle
    colors_extract = c.extract("turtle_gui/images/hirst_example.jpg", 20)
    print(colors_extract)

    # Filter array for just RGB values
    color_palette_rgb = []
    for color in colors_extract:
        color_palette_rgb.append(color.rgb)
        turtle_turtle.color(color.rgb)
    print(color_palette_rgb)

    # Default the start point to left corner of screen
    print({"screen": screen.screensize()})
    screen_size = screen.screensize()
    turtle_max_x = screen_size[0]
    turtle_max_y = screen_size[1]

    print({"turtle_max_x": turtle_max_x })
    print({"turtle_max_y": turtle_max_y })

    turtle_turtle.penup()
    starting_coord = (-turtle_max_x, -turtle_max_y)
    turtle_turtle.setpos(starting_coord)

    # Draw dots and change colors each time
    for _ in range(0, num_of_dots):
        turtle_turtle.color(r.choice(color_palette_rgb))

        # Collect coords every loop
        current_coords = turtle_turtle.pos()
        print({"coords": current_coords})

        turtle_turtle.penup()
        turtle_turtle.fd(50)
        turtle_turtle.pendown()
        turtle_turtle.dot(20, r.choice(color_palette_rgb))
        turtle_turtle.penup()
        # turtle_turtle.fd(50)

        # Move 50 spaces then pendown to draw dot
        if current_coords[0] == turtle_max_x:
            print("next row")
            turtle_turtle.setpos(-turtle_max_x, current_coords[1] + 50)

        if current_coords[1] == turtle_max_y:
            turtle_turtle.penup()
            print("end")
            return
        # elif current_coords[0] < turtle_max_x and current_coords[1] < turtle_max_y:



    # turtle_turtle.color()

# for _ in range(0, 50):
create_painting(num_of_dots=100)

screen.exitonclick()
