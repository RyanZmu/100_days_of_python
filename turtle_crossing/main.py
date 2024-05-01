"""
Turtle Crossing!

Navigate the turtle to the other side of the street

- Choose you own difficulty
- Define and move player turtle
- Randomly generate cars across the screen
- Start at level 1 and increase speed of cars with each level increase
- Game over when hit - Reset levels and speeds
"""
from turtle import Screen
from car import Cars
from scoreboard import ScoreBoard
from player import Player
import time

# Screen setup
screen = Screen()
screen.setup(width= 900, height= 900)
screen.tracer(0)

# Screen boundaries
MAX_X = 600
MIN_X = -600
MAX_Y = 400
MIN_Y = -400

game_active = True

# Player setup - teleport to start
player = Player()
player.teleport(x= 0, y= MIN_Y)

# Create a scoreboard
scoreboard = ScoreBoard()

# Create cars
car = Cars()

# Player movements
screen.listen()
screen.onkey(fun=player.move_up, key= "Up")
screen.onkey(fun=player.move_down, key= "Down")
screen.onkey(fun=player.move_left, key= "Left")
screen.onkey(fun=player.move_right, key= "Right")


while game_active:
    # If no crash, keep cars moving - pass in player for collision checks
    if car.crashed:
        scoreboard.game_over()
        game_active = False
    else:
        car.move_cars(player=player)

    # If player gets to the top, increase level and speed of cars
    if player.ycor() > 380:
        scoreboard.increase_level()
        car.current_speed += 0.01
        time.sleep(1)
        player.teleport(x=0, y=MIN_Y)

    # If player gets to level 10, they win!
    if scoreboard.level == 10:
        scoreboard.winner()
        game_active = False

    # Update screen every loop
    screen.update()

screen.exitonclick()
