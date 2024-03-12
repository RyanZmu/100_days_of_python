import random
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
 - Check for Blackjack (21) after every action, continue_game = False
 - Output who got the Blackjack 
- 3rd: Stretch - Betting and Chip Storage
"""


deck_of_cards: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'King', 'Queen', 'Jack']
card_suits: list = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
continue_game: bool = True
player_hand: list = [] 
dealer_hand: list = []


def draw_card():
    card_index: int = random.randint(0, len(deck_of_cards) - 1)
    suit_index: int = random.randint(0, len(card_suits) - 1)
    print(card_index)
    card_drawn: dict = {'suit': card_suits[suit_index], 'value': deck_of_cards[card_index]}
    return card_drawn

def check_blackjack(hand):
    print({'hand': hand})
    BLACKJACK: int = 21
    blackjack_or_bust: str = ""

    hand_value: int = 0
    # dealer_value: int = 0

    for card in range(0, len(hand)):
        if type(hand[card]['value']) is int :
            hand_value += hand[card]['value']
        else:
            # 10 because if it's a str, it means it is a king,queen or jack
            hand_value += 10

    if hand_value == 21:
        print('BLACKJACK!')
        blackjack_or_bust = 'BLACKJACK!'

        # continue_game = False

    if hand_value > 21:
        print("BUST")
        blackjack_or_bust = 'BUST!'
        # continue_game = False

    print({'hand_value': hand_value})
    return blackjack_or_bust


def player_action(action):
    global player_hand

    if player_action == 'Hit':
        player_hand.append(draw_card())

    if player_action == 'Stand':
        dealer_hand.append(draw_card())

    return


def blackjack_game():
    global player_hand, dealer_hand, continue_game

    # Get 2 cards for player and 1 for dealer
    player_hand.append(draw_card())
    player_hand.append(draw_card())

    dealer_hand.append(draw_card())

    print({'player': player_hand}, {'dealer_hand': dealer_hand})

    # Check for blackjack here ()
    player_check = check_blackjack(hand=player_hand)
    dealer_check = check_blackjack(hand=dealer_hand)

    player_formatted: str = ''
    player_total_value: int = 0

    dealer_formatted: str = ''
    dealer_total_value: int = 0

    # print({'player_total_value': player_hand[0]['value']})
    # print({'dealer_total_value': dealer_hand[0]['value']})
    # Format player and dealer hand
    for card in range(0, len(player_hand)):
        player_formatted += f'{player_hand[card]['value']} of {player_hand[card]['suit']} |'

        if type(player_hand[card]['value']) is not str:
            player_total_value += player_hand[card]['value']
        else:
            player_total_value += 10

    for card in range(0, len(dealer_hand)):
        dealer_formatted = f'{dealer_hand[card]['value']} of {dealer_hand[card]['suit']}'

        if type(dealer_hand[card]['value']) is not str:
            dealer_total_value += dealer_hand[card]['value']
        else:
            dealer_total_value += 10

    print({'player_total_value': player_total_value})
    print({'dealer_total_value': dealer_total_value})

    if player_check != 'BUST!' or dealer_check != 'BUST!':
        action_text: str = input(f'Your Hand is {player_formatted} for a total of {str(player_total_value)}\nThe Dealer\'s Hand is {dealer_formatted} for a total of {str(dealer_total_value)}\nHit or Stand? \n')
        player_action(action_text)
    elif player_check == 'BLACKJACK!':
        continue_game = False
        print('YOU GOT A BLACKJACK! You Win!')
    elif dealer_check == 'BLACKJACK!':
        continue_game = False
        print('DEALER BLACKJACK! YOU LOSE!')
    elif dealer_check == 'BUST!':
        continue_game = False
        print('DEALER BUST! YOU WIN!')
    # else:
    #     continue_game = False
    #     print('YOU BUST!')


while continue_game is True:
    print({'Continue': continue_game})
    blackjack_game()
