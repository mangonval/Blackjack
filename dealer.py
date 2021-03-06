from player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.score_cap_to_stand = 17
