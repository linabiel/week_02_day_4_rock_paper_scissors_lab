# import unittest ???
from src.player_class import Player


def play_game(player1, player2):
    if player1.gesture == player2.gesture:
        return "It's a draw!"
    if player1.gesture == "rock" and player2.gesture == "scissors":
        return "Rock wins!"
    if player1.gesture == "rock" and player2.gesture == "paper":
        return "Paper wins!"
    if player1.gesture == "paper" and player2.gesture == "rock":
        return "Paper wins!"
    if player1.gesture == "paper" and player2.gesture == "scissors":
        return "Scissors wins!"
    if player1.gesture == "scissors" and player2.gesture == "paper":
        return "Scissors wins!"
    if player1.gesture == "scissors" and player2.gesture == "rock":
        return "Rock wins!"
    # if player1.gesture == "rock" and player2.gesture == "paper":
    #     return "Paper wins!"
    # if player1.gesture == "rock" and player2.gesture == "paper":
    #     return "Paper wins!"
