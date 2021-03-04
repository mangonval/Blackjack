from hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()
        self.score = 0

    def convert_hand_to_list(self) -> []:
        hand_as_list = []
        for card in self.hand.cards:
            hand_as_list.append(card.value)
        return hand_as_list

