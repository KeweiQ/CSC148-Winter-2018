""""
An general class for game.
"""
from typing import Any


class Game:
    """
    A class of different games
    """

    def __init__(self) -> None:
        """
        Initialize the game.
        """

        raise NotImplementedError("must implement a subclass!")

    def __str__(self) -> str:
        """
        Return the information about the game.
        """

        raise NotImplementedError("must implement a subclass!")

    def __eq__(self, other: Any) -> bool:
        """
        Return whether two games are the same kind.
        """

        raise NotImplementedError("must implement a subclass!")

    def get_instructions(self) -> str:
        """
        Return instructions of the game.
        """

        raise NotImplementedError("must implement a subclass!")

    def str_to_move(self, move: str) -> int:
        """
        Take a expected movement for the game.
        """

        raise NotImplementedError("must implement a subclass!")

    def is_over(self, s: Any) -> bool:
        """
        Check whether the game is over.
        """

        raise NotImplementedError("must implement a subclass!")

    def is_winner(self, player: str) -> bool:
        """
        Return the winner of the game.
        """

        raise NotImplementedError("must implement a subclass!")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
