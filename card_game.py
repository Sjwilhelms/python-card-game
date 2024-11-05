import os
import random
from colorama import Fore, Back, Style

# clear console

os.system("clear")

# define the suits and the numbers

suits = ("Hearts", "Clubs", "Diamonds", "Spades")
numbers = (14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

# current hand
player1_card = []
player2_card = []

# cards won

player1_won = []
player2_won = []

# create deck of cards

def create_deck():
    # define player related variables
    deck = []
    #loop through each suit
    for suit in suits:
        #loop through cards
        for number in numbers:
            card = (number, suit)
            deck.append(card)
            
    random.shuffle(deck)

    return deck

deck_of_cards = create_deck()

###################################################

# play the game

while len(deck_of_cards) < 1:
    # pause for input
    input("press enter to deal the cards")

# deal players and remove dealt cards from the deck
player1_card = random.choice(deck_of_cards)
deck_of_cards.remove(player1_card)

player2_card = random.choice(deck_of_cards)
deck_of_cards.remove(player2_card)

# display player cards

def process_card(card_number):
    if card_number == 14:
        return "Ace"
    elif card_number == 13:
        return "King"
    elif card_number == 12:
        return "Queen"
    elif card_number == 11:
        return "Jack"
    elif card_number == 10:
        return "Ten"
    elif card_number == 9:
        return "Nine"
    elif card_number == 8:
        return "Eight"
    elif card_number == 7:
        return "Seven"
    elif card_number == 6:
        return "Six"
    elif card_number == 5:
        return "Five"
    elif card_number == 4:
        return "Four"
    elif card_number == 3:
        return "Three"
    elif card_number == 2:
        return "Two"
    else:
        return card_number

os.system("clear")

# display the cards
if player1_card[0] > player2_card[0]:
    print(
        f"{Fore.GREEN}Player 1 Card: {process_card(player1_card[0])} of {player1_card[1]}"
    )
    print(
        f"{Fore.RED}Player 2 Card: {process_card(player2_card[0])} of {player2_card[1]}"
    )

# compare the cards

# add the dealt cards to the winners deck

# display the number of cards left in the deck

# determine the winner of the hand/game