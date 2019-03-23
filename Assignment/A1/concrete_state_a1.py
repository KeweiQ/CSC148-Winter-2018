"""
A class about states for concrete games.
"""
from typing import Any
from current_state_a1 import CurrentState


class ChopsticksState(CurrentState):
    """
    A state recorder of the chopsticks game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the state recorder of a chopsticks game.

        >>> c = ChopsticksState(True)
        >>> c.player
        'p1'
        >>> c.state
        [1, 1, 1, 1]
        """

        super().__init__(is_p1_turn)
        self.state = [1, 1, 1, 1]

    def __str__(self) -> str:
        """
        Return a string about the current state of the game.

        >>> c = ChopsticksState(True)
        >>> str(c)
        'Player 1: 1 - 1, Player 2: 1 - 1'
        """

        return "Player 1: {} - {}, " \
               "Player 2: {} - {}".format(self.state[0], self.state[1],
                                          self.state[2], self.state[3])

    def __eq__(self, other: Any) -> bool:
        """
        Return true if two same games have the same state.
        """

        return (type(self) == type(other) and self.state == other.state
                and self.player == other.player)

    def get_current_player_name(self) -> str:
        """
        Return the current player.

        >>> c = ChopsticksState(True)
        >>> c.get_current_player_name()
        'p1'
        """

        return self.player

    def get_possible_moves(self) -> list:
        """
        Return a list of possible movements for next step.

        >>> c = ChopsticksState(True)
        >>> c.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """

        a = []
        if self.player == "p1":
            if self.state[0] != 0:
                if self.state[2] != 0:
                    a.append("ll")
                if self.state[3] != 0:
                    a.append("lr")
            if self.state[1] != 0:
                if self.state[2] != 0:
                    a.append("rl")
                if self.state[3] != 0:
                    a.append("rr")
        elif self.player == "p2":
            if self.state[2] != 0:
                if self.state[0] != 0:
                    a.append("ll")
                if self.state[1] != 0:
                    a.append("lr")
            if self.state[3] != 0:
                if self.state[0] != 0:
                    a.append("rl")
                if self.state[1] != 0:
                    a.append("rr")

        return a

    def is_valid_move(self, move: str) -> bool:
        """
        Return True if the expected movement is vailid.

        >>> c = ChopsticksState(True)
        >>> c.is_valid_move("ll")
        True
        """

        if move in ["ll", "lr", "rl", "rr"]:
            if self.player == "p1":
                if move[0] == "l":
                    return self.state[0] != 0
                elif move[0] == "r":
                    return self.state[1] != 0
            elif self.player == "p2":
                if move[0] == "l":
                    return self.state[2] != 0
                elif move[0] == "r":
                    return self.state[3] != 0
        return False

    def make_move(self, move: str) -> Any:
        """
        Make a movement for the game.
        """

        if self.player == "p1":
            s = ChopsticksState(False)
            if move == "ll":
                num = self.state[0] + self.state[2]
                if num >= 5:
                    num -= 5
                s.state = [self.state[0], self.state[1], num, self.state[3]]
            elif move == "rl":
                num = self.state[1] + self.state[2]
                if num >= 5:
                    num -= 5
                s.state = [self.state[0], self.state[1], num, self.state[3]]
            elif move == "lr":
                num = self.state[0] + self.state[3]
                if num >= 5:
                    num -= 5
                s.state = [self.state[0], self.state[1], self.state[2], num]
            elif move == "rr":
                num = self.state[1] + self.state[3]
                if num >= 5:
                    num -= 5
                s.state = [self.state[0], self.state[1], self.state[2], num]
        else:
            s = ChopsticksState(True)
            if move == "ll":
                num = self.state[2] + self.state[0]
                if num >= 5:
                    num -= 5
                s.state = [num, self.state[1], self.state[2], self.state[3]]
            elif move == "rl":
                num = self.state[3] + self.state[0]
                if num >= 5:
                    num -= 5
                s.state = [num, self.state[1], self.state[2], self.state[3]]
            elif move == "lr":
                num = self.state[2] + self.state[1]
                if num >= 5:
                    num -= 5
                s.state = [self.state[0], num, self.state[2], self.state[3]]
            elif move == "rr":
                num = self.state[3] + self.state[1]
                if num >= 5:
                    num -= 5
                s.state = [self.state[0], num, self.state[2], self.state[3]]

        return s


class SubtractSquareState(CurrentState):
    """
    A state recorder of the substract square game.
    """

    def __init__(self, is_p1_turn: bool, something=-1) -> None:
        """
        Initialize the recorder of a substract square game.
        """

        super().__init__(is_p1_turn)
        if something == -1:
            original_number = input("Please choose the original number:")
            while (not original_number.isdigit()) or \
                    float(original_number) % 1 != 0 or int(original_number) < 0:
                original_number = input("Please choose the original number:")
            self.state = int(original_number)
        else:
            self.state = something

    def __str__(self) -> str:
        """
        Return a string about the current state of the game.

        >>> s = SubtractSquareState(True, 20)
        >>> str(s)
        'Current number: 20'
        """

        return "Current number: {}".format(self.state)

    def __eq__(self, other: Any) -> bool:
        """
        Return true if two same games have the same state.
        """

        return (type(self) == type(other) and self.state == other.state
                and self.player == other.player)

    def get_current_player_name(self) -> str:
        """
        Return the current player.

        >>> s = SubtractSquareState(True, 20)
        >>> s.get_current_player_name()
        'p1'
        """

        return self.player

    def get_possible_moves(self) -> list:
        """
        Return a list of possible movements for next step.

        >>> s = SubtractSquareState(True, 20)
        >>> s.get_possible_moves()
        [1, 4, 9, 16]
        """

        i = 1
        a = []
        while i ** 2 <= self.state:
            a.append(i ** 2)
            i += 1

        return a

    def is_valid_move(self, move: int) -> bool:
        """
        Return True if the expected movement is valid.

        >>> s = SubtractSquareState(True, 20)
        >>> s.is_valid_move(5)
        False
        """

        return move in self.get_possible_moves()

    def make_move(self, move: str) -> Any:
        """
        Make a movement for the game.
        """

        new_number = self.state - int(move)
        if self.player == "p1":
            s = SubtractSquareState(False, new_number)
        else:
            s = SubtractSquareState(True, new_number)

        return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
