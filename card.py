class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def return_card_value(self) -> int:
        if self.value == "A":
            return 1
        elif self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        else:
            return int(self.value)
