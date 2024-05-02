"""
USA Map Game

- Using data from a csv file to fill in the state names and locations.
- User inputs state names and if correct will be added to map
- Wins if they can name all 50 states
"""
import pandas
from turtle import Screen, Turtle

# Screen setup
screen = Screen()
# screen.setup(width=500, height=500)
screen.bgpic(picname="./csv_map_usa_game/usa_map_game/images/blank_states_img.gif")

# Read states scv
states_data = pandas.read_csv(filepath_or_buffer="csv_map_usa_game/usa_map_game/data/50_states.csv")
print(states_data)

# Collect state names
state_names = states_data["state"]
print(state_names)

# Create var to track amount of states guessed
states_guessed = []


while len(states_guessed) < 50:
    # Input
   player_guess = screen.textinput(title="50 States Game!", prompt="Name a state!").lower()
   print(player_guess)

    # Check if guess is correct
   for state in state_names:
    if state.lower() == player_guess:
        print(state.lower())
        print("That's a state!")
        states_guessed.append(state)

        # Make marker
        map_marker = Turtle()
        map_marker.hideturtle()
        map_marker.penup()

        # Get state coords
        state_coords_x = states_data[states_data["state"] == state]["x"]
        state_coords_y = states_data[states_data["state"] == state]["y"]

        print({"x": state_coords_x}, {"y": state_coords_y})

        # Write to map
        map_marker.teleport(x=int(state_coords_x), y=int(state_coords_y))
        map_marker.write(state)

screen.exitonclick()
