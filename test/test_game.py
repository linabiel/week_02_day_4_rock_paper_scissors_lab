import unittest
from src.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Lina", "rock")
        self.player_2 = Player("Mark", "scissors")
        self.player_3 = Player("Colin", "paper")
        self.player_4 = Player("Sky", "rock")

    def test_if_gesture1_equals_gesture2(self):
        self.assertEqual("It's a draw!", play_game(
            self.player_1, self.player_4))

    def test_if_its_a_draw(self):
        self.assertEqual("It's a draw!", play_game(
            self.player_1, self.player_4))

    def test_if_gesture1_does_not_equal_gesture2(self):
        self.assertEqual("Rock wins!", play_game(
            self.player_1, self.player_2))

    def test_draw_is_declared_when_gestures_equal(self):
        self.assertEqual("It's a draw!", play_game(
            self.player_1, self.player_4))

    def test_rock_beats_scissors(self):
        self.assertEqual("Rock wins!", play_game(self.player_1, self.player_2))

    def test_scissors_beats_paper(self):
        self.assertEqual("Scissors wins!", play_game(
            self.player_2, self.player_3))

    def test_paper_beats_rock(self):
        self.assertEqual("Paper wins!", play_game(
            self.player_3, self.player_4))
