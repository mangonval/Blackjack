import random
from pprint import pprint

from card import Card
from deck import Deck
from game_controller import GameController
import pandas

from player import Player

game_controller = GameController()
deck_data = pandas.read_csv("blackjack_cards.csv")
deck = Deck(deck_data.values.tolist())
for card in deck.cards:
    print(f"{card.value} {card.suit}")

is_player_turn = True
is_dealer_turn = True
player_won = False
user = Player()
dealer = Player()

for _ in range(2):
    random_card = game_controller.deal_cards(deck.cards)
    user.hand.append(random_card)
    deck.cards.remove(random_card)
    random_card = game_controller.deal_cards(deck.cards)
    dealer.hand.append(random_card)
    deck.cards.remove(random_card)

user.score = game_controller.calculate_score(sorted(user.hand, key=lambda cards: card.return_card_value()))
dealer.score = game_controller.calculate_score(sorted(dealer.hand, key=lambda cards: card.return_card_value()))
if user.score == 21:
    player_won = True

while is_player_turn and not player_won:
    print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")
    print(f"This is the dealer hand: {dealer.hand[1].value}")
    player_decision = input(f"What do you want to do? 'hit', 'stand': ")
    if player_decision.lower() == "hit":
        random_card = game_controller.deal_cards(deck.cards)
        user.hand.append(random_card)
        deck.cards.remove(random_card)
    elif player_decision.lower() == "stand":
        is_player_turn = False
    user.score = game_controller.calculate_score(sorted(user.hand, key=lambda cards: card.return_card_value()))
    if user.score >= 21:
        is_player_turn = False

if dealer.score >= 17:
    is_dealer_turn = False

while is_dealer_turn:
    random_card = game_controller.deal_cards(deck.cards)
    dealer.hand.append(random_card)
    deck.cards.remove(random_card)
    dealer.score = game_controller.calculate_score(sorted(dealer.hand, key=lambda cards: card.return_card_value()))
    if dealer.score >= 17:
        is_dealer_turn = False


print(f"This is your hand: {user.convert_hand_to_list()} with a score of: {user.score}")


#
# game_controller = GameController()
# print(f"Score: {game_controller.calculate_score(sorted(deck.cards, key=lambda card: card.return_card_value()))}")
