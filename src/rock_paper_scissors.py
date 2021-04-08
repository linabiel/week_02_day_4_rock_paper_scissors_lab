# import unittest ???
from src.player_class import Player


def play_game(player1, player2):
    if player1.gesture == player2.gesture:
        return True
    return False
