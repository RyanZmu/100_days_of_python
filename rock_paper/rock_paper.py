import random

# Rock Paper Scissors!
# Write a program that will let a user choose Rock (0) Paper (1) or Scissors (2) and then play against the computer
print('''Lets play Rock, Paper, Scissors!
         Choose 0 for Rock, 1 for Paper or 2 for Scissors!       
''')

# Player and opponent choices as int
player_choice: int = int(input("What do you choose?\n"))
opponent_choice: int = random.randint(0, 2)

# If invalid number, display lost and exit program
if player_choice >= 3 or player_choice < 0:
    print(f"Invalid number {player_choice} entered! You Lose!")
    exit()

rps_list: list = ["Rock", "Paper", "Scissors"]

# Choices as rock,paper or scissors
player_rps: str = rps_list[player_choice]
opponent_rps: str = rps_list[opponent_choice]

print(f"You chose {player_rps}")
print(f"Opponent chose {opponent_rps}")

# Determine what wins
if player_choice == 0 and opponent_choice == 2:
    print("You Win!")
elif opponent_choice == 0 and player_choice == 2:
    print("You Lose!")
elif opponent_choice > player_choice:
    print("You Lose!")
elif player_choice > opponent_choice:
    print("You Win!")
elif opponent_choice == player_choice:
    print("It's a draw!")
