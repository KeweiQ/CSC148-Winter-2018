"""
An general class for game state.
"""
from typing import Any


class CurrentState:
    """
    A class about the current state of the game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the current state class.
        """

        if is_p1_turn is True:
            self.player = "p1"
        else:
            self.player = "p2"

    def __str__(self) -> str:
        """
        Return the information about current state of the game.
        """

        raise NotImplementedError("must implement a subclass!")

    def __eq__(self, other: Any) -> bool:
        """
        Return True if two games have the same game state.
        """

        raise NotImplementedError("must implement a subclass!")

    def get_possible_moves(self) -> list:
        """
        Return a list of possible movements for next step.
        """

        raise NotImplementedError("must implement a subclass!")

    def is_valid_move(self, move: str) -> bool:
        """
        Return True if the expected movement is vailid.
        """

        raise NotImplementedError("must implement a subclass!")

    def make_move(self, move: str) -> Any:
        """
        Make a movement for the game.
        """

        raise NotImplementedError("must implement a subclass!")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
