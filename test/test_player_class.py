import unittest
from src.player_class import Player


class TestPlayer(unittest.TestCase):

    def test_player_has_name(self):
        self.player_1 = Player("lina", "rock")
        self.assertEqual("lina", self.player_1.name)

    def test_player_has_gesture(self):
        self.player_2 = Player("Mark", "scissors")
        self.assertEqual("scissors", self.player_2.gesture)
