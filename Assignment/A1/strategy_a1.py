from typing import Any
import random


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Any) -> Any:
    """
    Return a move for game through random choosing by computer.
    """
    return random.randint(1, 100)
