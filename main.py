from card import Card
from deck import Deck
from game_controller import GameController
import pandas

deck_data = pandas.read_csv("blackjack_cards.csv")

deck = Deck(deck_data.values.tolist())
for card in deck.cards:
    print(f"{card.value} {card.suit}")
#
# game_controller = GameController()
# print(f"Score: {game_controller.calculate_score(sorted(deck.cards, key=lambda card: card.return_card_value()))}")
