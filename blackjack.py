import random

import pandas

from deck import Deck
from card import Card


class Blackjack:
    def __init__(self):
        self.user_busted = None
        self.is_user_turn = True
        self.is_dealer_turn = True
        self.user_busted = False
        self.user_won = False
        self.deck = self.create_new_deck_from_csv()

    def get_random_card_from_deck(self) -> Card:
        random_card = random.choice(self.deck.cards)
        self.deck.cards.remove(random_card)
        return random_card

    def create_new_deck_from_csv(self):
        deck_data = pandas.read_csv("blackjack_cards.csv")
        return Deck(deck_data.values.tolist())
