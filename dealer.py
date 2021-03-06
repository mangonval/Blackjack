from player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.score_cap_to_stand = 17

    def dealer_has_to_stand(self) -> bool:
        if self.hand.score >= self.score_cap_to_stand:
            return True
        else:
            return False
