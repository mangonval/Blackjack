import random


from card import Card


class GameController:
    def __init__(self):
        return

    def deal_cards(self, deck) -> Card:
        return random.choice(deck)

    def calculate_score(self, list_of_cards) -> int:
        score = 0
        for card in list_of_cards:
            if card.value == "A":
                score += 1
            elif card.value == "J" or card.value == "Q" or card.value == "K":
                score += 10
            else:
                score += int(card.value)
        for card in list_of_cards:
            if card.value == "A" and score + 10 <= 21:
                score += 10
        return score

