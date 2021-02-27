from card import Card


class Deck:
    def __init__(self, available_cards):
        self.cards = []
        for card in available_cards:
            new_card_to_add = Card(value=card[0], suit=card[1])
            self.cards.append(new_card_to_add)
