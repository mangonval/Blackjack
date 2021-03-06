class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def calculate_score(self):
        self.score = 0
        for card in self.cards:
            if card.value == "A":
                self.score += 1
            elif card.value == "J" or card.value == "Q" or card.value == "K":
                self.score += 10
            else:
                self.score += int(card.value)
        for card in self.cards:
            if card.value == "A" and self.score + 10 <= 21:
                self.score += 10

    def add_card_to_hand(self, card_to_add):
        self.cards.append(card_to_add)
        self.calculate_score()
