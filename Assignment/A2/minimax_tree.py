"""
A Tree class for minimax strategy.
"""
from typing import Any
from game_state import GameState


class MinimaxTree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value: GameState, move: Any,
                 children: Any, score: Any) -> None:
        """
        Create Tree self with content value and 0 or more children.
        """
        self.value = value
        self.move = move
        self.children = children
        self.score = score


if __name__ == '__main__':
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod()
