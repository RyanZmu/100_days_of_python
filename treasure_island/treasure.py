#  Treasure Island Choose Your Own Adventure - lesson nesting if statements
print('''
        _______
      .'_/_|_\\_'.
      \\`\\  |  /`/
       `\\  | //'
         `\\|/`
           `
''')
print("Welcome to Treasure Island!")
print("Can you find the treasure!?")

# Player info
player_name: str = input("What is your character's name?\n")
player_class: str = input("What class are you? Warrior, Mage or Ranger?\n")
player_direction: str = input("Which direction should you face when you start? North,South,West or East?\n").lower()

player_inv: list = ["a matchbox", "dagger", "rope"]
player_lvl: float = 1.00
is_game_over: bool = False

# Character info
print(f'''
        Your Character:
        Name: {player_name}
        Class: {player_class}
        Level: {int(player_lvl)}
        -------------------
''')

# Start of play through
print(f'''
        You awaken on a strange island with nothing but {','.join(player_inv)} on you.
        As you get up, you turn {player_direction} and start to walk briskly.
''')

# First encounters - nesting a ton of if statements for practice
# North
if player_direction == "north":
    print('''
        You immediately come across a small crab that is aggressive. 
        Do you fight or run?
''')
    player_choice: str = input("Fight or Run?").lower()
    if player_choice == "fight":
        print(f"You pull out your weapon and immediately kill the crab!")
        print('''
        Having vanquished the crab, which direction do you head? North, South, West or east? 
        ''')
    elif player_choice == "run":
        print(
            f"You run away in fear of the crustacean, you blindly run into a orc who chops your head off in one swing")
        is_game_over = True
    else:
        print("Enter a valid option! Fight or Run!")
# South
elif player_direction == "south":
    print(f'''
        Heading {player_direction} you notice that you are being followed, what do you do next?
        Do you shout out into the darkness or run and try to lose the entity?
         ''')
    player_choice: str = input(f"Shout or Run?").lower()
    if player_choice == "shout":
        print('''
        You shout out at the entity and in return you hear the creature start to sing softly.
        The creature then reveals itself and you see it is a woman who must have been lost, she is bruised
        and she is shivering.
                
        Do you tell her to stop following you or will you have her join you?
        ''')
        player_choice: str = input(f"Shoo or Join?")
        if player_choice == "shoo":
            print('''
        The woman gives you a sad face and runs away crying about a monster.
            ''')
        elif player_choice == "join":
            print('''
        The woman nods her head and walks over to you, she says "Hello, my name is Scarlet and I have 
        been lost in these caves for years. Please help me find a way out". You agree and she joins you. 
                     ''')
    elif player_choice == "run":
        print('''
        You run away screaming and hoping to elude whatever has been following you, unfortunately you didn't see
        the ledge in front of you and tumble down to your death.
        ''')
        is_game_over = True
# West
elif player_direction == "west":
    print(f'''
        Heading {player_direction} you hear a weird hum coming from behind a large boulder just across the room.
        
        You are curious to the noise. Do you walk around the boulder and find the source or do you run away in fear?
    ''')

    player_choice: str = input("Investigate or Run?").lower()

    if player_choice == "investigate":
        print('''
        You investigate the noise and it is revealed that the noise was coming from a small dog!
        
        Will you choose to keep the dog and bring them along with you, or will you shoo the dog away?
        ''')
        player_choice_dog: str = input("Keep or Shoo?").lower()

        if player_choice_dog == "keep":
            print('''
        You chose to keep the dog and bring him along, the dog barks and wags his tail and follows you. Now to name it!
        ''')
            dog_name: str = input("What do you name the dog?")
            print(f"{dog_name} barks excitedly!")
        elif player_choice_dog == 'shoo':
            print('''
        The dog whimpers and runs away! Poor thing.
        ''')

    elif player_choice == "run":
        print('''
     You run away scared of the humming! In doing so you fall into a small stream and proceed to drown violently.
     ''')
        is_game_over = True
# East
elif player_direction == 'east':
    print(f'''
     Heading {player_direction} you start to feel the ground shake and you notice a tree nearby fall over.
     
     Will you investigate what brought down the tree or will you run away? 
     ''')
    player_choice: str = input("Investigate or Run?").lower()

    if player_choice == "investigate":
        print(f'''
     You run over to find out what made the tree fall over, upon investigating you find a small elf like creature.
     He seems confused and scared but also nice.
     
     Do you ask him to join you or will you tell him to leave your presence?
      ''')
        player_choice_elf: str = input("Join or Shoo?").lower()
        if player_choice_elf == "join":
            print(f'''
         The elf jumps up and onto your shoulders, excited and eager to get away from this island.
         
         "Hey thanks for the lift buddy!" says the elf.
         
         You ask him his name and he stays silent and his eyes droop.
         
         "I don't know!"
          ''')
        elif player_choice_elf == "shoo":
            print(f'''
        You tell the elf where to shove it and he runs off crying.
        ''')
    elif player_choice == "run":
        print('''
     You run away as fast as you can and while doing so you trip on a rock and snap your neck. Violently.
         ''')
        is_game_over = True
else:
    print('Game Broke! Must have entered an invalid direction! North, South, West or East are valid')

# Game over check
if is_game_over:
    print("Sorry you died! Game over!")
