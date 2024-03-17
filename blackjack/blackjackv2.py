import random
import modules.deck as deck
import utils.format_text as formatter

# Make the game have a GUI
# from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

# import sys


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Hello World")

#         button = QPushButton("My simple app.")
#         button.pressed.connect(self.close)

#         self.setCentralWidget(button)
#         self.show()

# app = QApplication(sys.argv)
# w = MainWindow()
# app.exec()

"""
Create a Blackjack Game

- Display the user's cards (add the values to help user)
- Display Computer's first card
- Ask for y to hit and n to stand
 - If no then display final value of hand, have computer draw a card and then the Computer's final hand
 - if yes then give player another card, display new value, determine if blackjack or bust, ask to hit again or stand

 Ace is 11/1 choose value that gets closet to or is 21

 Stretch:
  Account for suits and hands like Full House

Psuedo:
- Start Game and run until False
- Draw Cards()
 - Get the card value and suit
 - Add this to the player's or dealer's hand   
- 1st: Draw 2 cards for the player and two for the dealer
- 2nd: Show value of hand as well as cards to player
- Player actions()
 - Hit
 - Stand
 - Stretch: Split
 - Check for Blackjack (21) after every action, end_game = False
 - Output who got the Blackjack 
- 3rd: Stretch - Betting and Chip Storage
"""

DECK_OF_CARDS = deck.DECK_OF_CARDS

end_game: bool = False
first_draw: bool = True
player_hand: dict = {'cards_in_hand': [], 'value': 0, 'chips': 5000}
dealer_hand: dict = {'cards_in_hand': [], 'value': 0}


def draw_card(hand,name):
    # Draw a random card
    random_card_index: int = random.randint(0, len(DECK_OF_CARDS) - 1)
    drawn_card: dict = DECK_OF_CARDS[random_card_index]

    # Add card to hand
    hand['cards_in_hand'].append(drawn_card)

    # Update hand value
    hand['value'] += drawn_card['value']

    # Pass new hand to function to determine if blackjack or bust
    blackjack_check(hand_to_check=hand,name=name)
    return hand


def blackjack_check(hand_to_check,name):
    global end_game
   # Get current hand's value
    current_hand_value = hand_to_check['value']

    # Check for blackjack
    if current_hand_value == 21:
     end_game = True
     print(hand_to_check)
     print(f'BLACKJACK!! {name.upper()} WINS!')
    elif current_hand_value > 21:
     end_game = True
     print(hand_to_check)
     print(f'{name.upper()} BUST!')

    return end_game


def blackjack_game():
    global end_game, first_draw
    print({'end_game': end_game})

        # Init card draws for player
    if not end_game:

        if first_draw:
            draw_card(hand=player_hand,name='player')
            draw_card(hand=dealer_hand,name='dealer')
            first_draw = False

        player_prompt: str = input(f"Your hand: {player_hand['cards_in_hand']} for a total of {player_hand['value']}\n"\
                                   f"Dealer hand: {dealer_hand['cards_in_hand']} for a total of {dealer_hand['value']}\n"\
                                   f"You have a total of {player_hand['chips']} chips\n"\
                                   f"Do you want to Hit or Stand?\n")
    
        if player_prompt.lower() == 'hit':
            draw_card(hand=player_hand,name='player')
            if not end_game and dealer_hand['value'] < 17:
                draw_card(hand=dealer_hand,name='dealer')
        elif player_prompt.lower() == 'stand' and dealer_hand['value'] < 17:
            draw_card(hand=dealer_hand,name='dealer')
        elif dealer_hand['value'] > 17 and player_prompt.lower() == 'stand' and player_hand['value'] > dealer_hand['value']:
            end_game = True
            print('PLAYER WINS!')
        elif player_prompt.lower() == 'stand' and dealer_hand['value'] < player_hand['value']:
            end_game = True
            print("PLAYER WINS!")
        elif dealer_hand['value'] == player_hand['value']:
           end_game= True
           print('DEALER PUSH!')
    else:
       return
    

while not end_game:
    blackjack_game()
