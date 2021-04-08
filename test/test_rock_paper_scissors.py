import unittest
from src.rock_paper_scissors import *

class TestRockPaperScissors(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("lina", "rock")
        self.player_2 = Player("mark", "scissors")
        self.player_3 = Player("Colin", "paper")