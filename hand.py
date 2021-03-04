class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.available_games = {
            "blackjack": self.calculate_score_for_blackjack
        }

    def calculate_score(self, game_being_played):
        self.available_games[game_being_played]

    def calculate_score_for_blackjack(self):
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
