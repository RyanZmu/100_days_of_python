"""
USA Map Game

- Using data from a csv file to fill in the state names and locations.
- User inputs state names and if correct will be added to map
- Win if can name all 50 states
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
states_not_guessed = state_names.tolist()


while len(states_guessed) < 50:
   # Input
    player_guess = screen.textinput(title="50 States Game!", prompt="Name a state!\nType 'Exit' to quit and save a copy of all states that you didn't guess!").lower()
    print(player_guess)

    if player_guess != "exit":
        # Check if guess is correct
        for state in state_names:
            if state.lower() == player_guess:
                print(state.lower())
                print("That's a state!")
                states_guessed.append(state)
                print(states_not_guessed)

                # Make map marker
                map_marker = Turtle()
                map_marker.hideturtle()
                map_marker.penup()

                # Get state coords
                state_coords_x = states_data[states_data["state"] == state]["x"]
                state_coords_y = states_data[states_data["state"] == state]["y"]


                # Write to map
                map_marker.teleport(x=state_coords_x.iloc[0], y=state_coords_y.iloc[0])
                map_marker.write(state)

    else:
        # Exit and create a csv of all missed states
        states_not_guessed = pandas.DataFrame([state for state in state_names if state not in states_guessed])
        states_not_guessed.to_csv("./csv_map_usa_game/usa_map_game/states_not_guess.csv")

        # Output a goodbye message to user with file path
        bye = Turtle()
        bye.hideturtle()
        bye.teleport(-400,300)
        screen.delay(5000)
        bye.write(arg="SAVING MISSED STATES CSV to ./csv_map_usa_game/usa_map_game/states_not_guess.csv - Study Up!", font=("Arial", 14, "normal")),
        screen.bye()

if len(states_guessed) == 50:
        winner = Turtle()
        winner.hideturtle()
        winner.teleport(-200,300)
        winner.write(arg="YOU WIN! GREAT JOB! click anywhere to close", font=("Arial", 14, "normal")),

screen.exitonclick()
