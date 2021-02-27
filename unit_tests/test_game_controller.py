import unittest

from game_controller import GameController
from deck import Deck


class TestGameController(unittest.TestCase):

    def test_calculate_score(self):
        game_controller = GameController()
        deck = Deck([["A", "Hearts"], ["A", "Hearts"], ["A", "Hearts"], ["A", "Hearts"]])
        self.assertEqual(game_controller.calculate_score(deck.cards), 14)