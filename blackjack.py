import random

from card import Card


class Blackjack():
    def __init__(self):
        self.user_busted = None
        self.is_user_turn = True
        self.is_dealer_turn = True
        self.user_busted = False
        self.user_won = False

    def deal_cards(self, deck) -> Card:
        return random.choice(deck)
