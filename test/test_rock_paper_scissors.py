import unittest
from src.rock_paper_scissors import *
# from src.player_class import Player ???


class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Lina", "rock")
        self.player_2 = Player("Mark", "scissors")
        self.player_3 = Player("Colin", "paper")

    def test_if_gesture1_equals_gesture2(self):
        self.assertEqual(False, play_game(self.player_1, self.player_2))
