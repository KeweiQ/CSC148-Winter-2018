"""
Classes for concrete games.
"""
from typing import Any
from game_total_a1 import Game
from concrete_state_a1 import ChopsticksState, SubtractSquareState


class Chopsticks(Game):
    """
    A class contains methods for a chopsticks game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the chopsticks game.

        >>> c = Chopsticks(True)
        >>> c.current_state.player
        'p1'
        >>> c.current_state.state
        [1, 1, 1, 1]
        """

        self.current_state = ChopsticksState(is_p1_turn)

    def __str__(self) -> str:
        """
        Return a string about the current state of the game.

        >>> c = Chopsticks(True)
        >>> str(c)
        'Player 1: 1 - 1, Player 2: 1 - 1'
        """

        return "Player 1: {} - {}, " \
               "Player 2: {} - {}".format(self.current_state.state[0],
                                          self.current_state.state[1],
                                          self.current_state.state[2],
                                          self.current_state.state[3])

    def __eq__(self, other: Any) -> bool:
        """
        Return true if two gamesare same and have the same state.
        """

        return (type(self) == type(other) and
                self.current_state.state == other.state
                and self.current_state.player == other.player)

    def get_instructions(self) -> str:
        """
        Return instructions of the game.
        """

        return "1. Each of two players begins with one finger " \
               "pointed up on each of their hands.\n" \
               "2. Player A touches one hand to one of Player B's " \
               "hands, increasing the number of fingers " \
               "pointing up on Player B's hand by the number " \
               "on Player A's hand. " \
               "The number pointing up on Player A's hand " \
               "remains the same.\n" \
               "3. If Player B now has five fingers up, that " \
               "hand becomes \'dead\' or unplayable. " \
               "If the number of fingers should exceed five, " \
               "subtract five from the sum.\n" \
               "4. Now Player B touches one hand to one of " \
               "Player A's hands, and the distribution of " \
               "fingers proceeds as above, including the " \
               "possibility of a \'dead\' hand.\n" \
               "5. Play repeats steps 2-4 until some player " \
               "has two \'dead\' hands, thus losing."

    def str_to_move(self, move: str) -> str:
        """
        Make a movement for the game.

        >>> c = Chopsticks(True)
        >>> c.str_to_move("ll")
        'll'
        """

        return move

    def is_over(self, s: ChopsticksState) -> bool:
        """
        Check whether the game is over.

        >>> c = Chopsticks(True)
        >>> s = c.current_state
        >>> c.is_over(s)
        False
        """

        return ((s.state[0] == 0 and s.state[1] == 0)
                or (s.state[2] == 0 and s.state[3] == 0))

    def is_winner(self, player: str) -> bool:
        """
        Return the winner of the game.

        >>> c = Chopsticks(True)
        >>> c.is_winner("p1")
        False
        >>> c.is_winner("p2")
        False
        """

        s = self.current_state
        return self.is_over(s) and self.current_state.player != player


class SubtractSquare(Game):
    """
    A class contains methods for a subtract square game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the subtract square game.
        """

        self.current_state = SubtractSquareState(is_p1_turn)

    def __str__(self) -> str:
        """
        Return a string about the current state of the game.
        """

        return "Current number: {}".format(self.current_state.state)

    def __eq__(self, other: Any) -> bool:
        """
        Return true if two gamesare same and have the same state.
        """

        return (type(self) == type(other) and
                self.current_state.state == other.state
                and self.current_state.player == other.player)

    def get_instructions(self) -> str:
        """
        Return instructions of the game.
        """

        return "1. A positive whole number is randomly chosen " \
               "as the starting value by some neutral entity. " \
               "In our case,the computer will choose it randomly.\n" \
               "2. The player whose turn it is chooses some " \
               "square of a positive whole number " \
               "(such as 1, 4, 9, 16, . . . ) to subtract from the " \
               "value, provided the chosen square is not " \
               "larger. After subtracting, we have a new value " \
               "and the next player chooses a square to " \
               "subtract from it.\n" \
               "3. Play continues to alternate between the two " \
               "players until no moves are possible. " \
               "Whoever is about to play at that point loses!"

    def str_to_move(self, move: str) -> int:
        """
        Take a expected movement for the game.
        """

        return int(move)

    def is_over(self, s: SubtractSquareState) -> bool:
        """
        Check whether the game is over.
        """

        return len(s.get_possible_moves()) == 0

    def is_winner(self, player: str) -> bool:
        """
        Return the winner of the game.
        """

        s = self.current_state
        return self.is_over(s) and self.current_state.player != player


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
