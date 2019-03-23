"""
A stonehenge game.
"""
import copy
from typing import Any
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    Abstract class for a stonehenge game to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        length = input("Enter the side length: ")
        if length not in ["-1", "1", "2", "3", "4", "5"]:
            print("Invalid length {}!".format(length))
            length = input("Enter the side length: ")
        self.current_state = StonehengeState(p1_starts, int(length))

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        instructions = "Stonehenge is played on a hexagonal grid formed by " \
                       "removing the corners from a triangular grid. " \
                       "Boards can have various sizes based on their " \
                       "side-length " \
                       "(the number of cells in the grid along the bottom), " \
                       "but are always formed in a similar manner: " \
                       "For side-length n, the first row has 2 cells, " \
                       "and each row after has 1 additional cell up until " \
                       "there\'s a row with n + 1 cells, after which " \
                       "the last row has only n cells in it.\n" \
                       "Players take turns claiming cells.When a " \
                       "player captures at least half of the cells in a " \
                       "ley-line, then the player captures that ley-line." \
                       "The first player to capture at least " \
                       "half of the ley-lines is the winner.\n" \
                       "A ley-line, once claimed, cannot be" \
                       "taken by the other player."
        return instructions

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Return whether or not this game is over at state.
        """
        return len(state.get_possible_moves()) == 0

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        if not string.strip().isalpha():
            return -1
        return string.strip()


class StonehengeState(GameState):
    """
    The state of a stonehenge game at a certain point in time.
    """
    R1 = [["@", "A", "B"], ["@", "C"]]
    DL1 = [["@", "A"], ["@", "B", "C"]]
    DR1 = [["@", "A", "C"], ["@", "B"]]
    R2 = [["@", "A", "B"], ["@", "C", "D", "E"], ["@", "F", "G"]]
    DL2 = [["@", "A", "C"], ["@", "B", "D", "F"], ["@", "E", "G"]]
    DR2 = [["@", "C", "F"], ["@", "A", "D", "G"], ["@", "B", "E"]]
    R3 = [["@", "A", "B"], ["@", "C", "D", "E"],
          ["@", "F", "G", "H", "I"], ["@", "J", "K", "L"]]
    DL3 = [["@", "A", "C", "F"], ["@", "B", "D", "G", "J"],
           ["@", "E", "H", "K"], ["@", "I", "L"]]
    DR3 = [["@", "F", "J"], ["@", "C", "G", "K"],
           ["@", "A", "D", "H", "L"], ["@", "B", "E", "I"]]
    R4 = [["@", "A", "B"], ["@", "C", "D", "E"], ["@", "F", "G", "H", "I"],
          ["@", "J", "K", "L", "M", "N"], ["@", "O", "P", "Q", "R"]]
    DL4 = [["@", "A", "C", "F", "J"], ["@", "B", "D", "G", "K", "O"],
           ["@", "E", "H", "L", "P"], ["@", "I", "M", "Q"], ["@", "N", "R"]]
    DR4 = [["@", "J", "O"], ["@", "F", "K", "P"], ["@", "C", "G", "L", "Q"],
           ["@", "A", "D", "H", "M", "R"], ["@", "B", "E", "I", "N"]]
    R5 = [["@", "A", "B"], ["@", "C", "D", "E"], ["@", "F", "G", "H", "I"],
          ["@", "J", "K", "L", "M", "N"], ["@", "O", "P", "Q", "R", "S", "T"],
          ["@", "U", "V", "W", "X", "Y"]]
    DL5 = [["@", "A", "C", "F", "J", "O"], ["@", "B", "D", "G", "K", "P", "U"],
           ["@", "E", "H", "L", "Q", "V"], ["@", "I", "M", "R", "W"],
           ["@", "N", "S", "X"], ["@", "T", "Y"]]
    DR5 = [["@", "O", "U"], ["@", "J", "D", "V"], ["@", "F", "K", "Q", "W"],
           ["@", "C", "G", "L", "R", "X"], ["@", "A", "D", "H", "M", "S", "Y"],
           ["@", "B", "E", "I", "N", "T"]]

    def __init__(self, is_p1_turn: bool, length: int, row: list = None,
                 down_left: list = None, down_right: list = None) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        if length == 1:
            self.r = copy.deepcopy(self.R1)
            self.dl = copy.deepcopy(self.DL1)
            self.dr = copy.deepcopy(self.DR1)
        elif length == 2:
            self.r = copy.deepcopy(self.R2)
            self.dl = copy.deepcopy(self.DL2)
            self.dr = copy.deepcopy(self.DR2)
        elif length == 3:
            self.r = copy.deepcopy(self.R3)
            self.dl = copy.deepcopy(self.DL3)
            self.dr = copy.deepcopy(self.DR3)
        elif length == 4:
            self.r = copy.deepcopy(self.R4)
            self.dl = copy.deepcopy(self.DL4)
            self.dr = copy.deepcopy(self.DR4)
        elif length == 5:
            self.r = copy.deepcopy(self.R5)
            self.dl = copy.deepcopy(self.DL5)
            self.dr = copy.deepcopy(self.DR5)
        elif length == -1:
            self.r = row[:]
            self.dl = down_left[:]
            self.dr = down_right[:]
        self.state = [self.r, self.dl, self.dr]
        count_p1 = 0
        count_p2 = 0
        count_total = 0
        for l in self.state:
            for i in l:
                count_total += 1
                if i[0] == "1":
                    count_p1 += 1
                elif i[0] == "2":
                    count_p2 += 1
        self.n_p1 = count_p1
        self.n_p2 = count_p2
        self.total = count_total

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        if (self.total / 3) - 1 == 1:
            return """\
      {}   {}
     /   /
{} - {} - {}
     \\ / \\
  {} - {}   {}
       \\
        {}""".format(self.dl[0][0], self.dl[1][0], self.r[0][0],
                     self.r[0][1], self.r[0][2], self.r[1][0],
                     self.r[1][1], self.dr[1][0], self.dr[0][0])
        elif (self.total / 3) - 1 == 2:
            return """\
        {}   {}
       /   /
  {} - {} - {}   {}
     / \\ / \\ /
{} - {} - {} - {}
     \\ / \\ / \\
  {} - {} - {}   {}
       \\   \\
        {}   {}""".format(self.dl[0][0], self.dl[1][0], self.r[0][0],
                          self.r[0][1], self.r[0][2], self.dl[2][0],
                          self.r[1][0], self.r[1][1], self.r[1][2],
                          self.r[1][3], self.r[2][0], self.r[2][1],
                          self.r[2][2], self.dr[2][0], self.dr[0][0],
                          self.dr[1][0])
        elif (self.total / 3) - 1 == 3:
            return """\
          {}   {}
         /   /
    {} - {} - {}   {}
       / \\ / \\ /
  {} - {} - {} - {}   {}
     / \\ / \\ / \\ /
{} - {} - {} - {} - {}
     \\ / \\ / \\ / \\
  {} - {}   {}   {}   {}
       \\   \\   \\
        {}   {}   {}""".format(self.dl[0][0], self.dl[1][0], self.r[0][0],
                               self.r[0][1], self.r[0][2], self.dl[2][0],
                               self.r[1][0], self.r[1][1], self.r[1][2],
                               self.r[1][3], self.dl[3][0], self.r[2][0],
                               self.r[2][1], self.r[2][2], self.r[2][3],
                               self.r[2][4], self.r[3][0], self.r[3][1],
                               self.r[3][2], self.r[3][3], self.dr[3][0],
                               self.dr[0][0], self.dr[1][0], self.dr[2][0])
        elif (self.total / 3) - 1 == 4:
            return """\
            {}   {}
           /   /
      {} - {} - {}   {}
         / \\ / \\ /
    {} - {} - {} - {}   {}
       / \\ / \\ / \\ /
  {} - {} - {} - {} - {}   {}
     / \\ / \\ / \\ / \\ /
{} - {}   {}   {}   {}   {}
     \\ / \\ / \\ / \\ / \\
  {} - {}   {}   {}   {}   {}
       \\   \\   \\   \\
        {}   {}   {}   {}""".format(self.dl[0][0], self.dl[1][0], self.r[0][0],
                                    self.r[0][1], self.r[0][2], self.dl[2][0],
                                    self.r[1][0], self.r[1][1], self.r[1][2],
                                    self.r[1][3], self.dl[3][0], self.r[2][0],
                                    self.r[2][1], self.r[2][2], self.r[2][3],
                                    self.r[2][4], self.dl[4][0], self.r[3][0],
                                    self.r[3][1], self.r[3][2], self.r[3][3],
                                    self.r[3][4], self.r[3][5], self.r[4][0],
                                    self.r[4][1], self.r[4][2], self.r[4][3],
                                    self.r[4][4], self.dr[4][0], self.dr[0][0],
                                    self.dr[1][0], self.dr[2][0], self.dr[3][0])
        return """\
              {}   {}
             /   /
        {} - {} - {}   {}
           / \\ / \\ /
      {} - {} - {} - {}   {}
         / \\ / \\ / \\ /
    {} - {} - {} - {} - {}   {}
       / \\ / \\ / \\ / \\ /
  {} - {}   {}   {}   {}   {}   {}
     / \\ / \\ / \\ / \\ / \\ /
{} - {}   {}   {}   {}   {}   {}
     \\ / \\ / \\ / \\ / \\ / \\
  {} - {}   {}   {}   {}   {}   {}
       \\   \\   \\   \\   \\
        {}   {}   {}   {}   {}""".format(self.dl[0][0], self.dl[1][0],
                                         self.r[0][0], self.r[0][1],
                                         self.r[0][2], self.dl[2][0],
                                         self.r[1][0], self.r[1][1],
                                         self.r[1][2], self.r[1][3],
                                         self.dl[3][0], self.r[2][0],
                                         self.r[2][1], self.r[2][2],
                                         self.r[2][3], self.r[2][4],
                                         self.dl[4][0], self.r[3][0],
                                         self.r[3][1], self.r[3][2],
                                         self.r[3][3], self.r[3][4],
                                         self.r[3][5], self.dl[5][0],
                                         self.r[4][0], self.r[4][1],
                                         self.r[4][2], self.r[4][3],
                                         self.r[4][4], self.r[4][5],
                                         self.r[4][6], self.r[5][0],
                                         self.r[5][1], self.r[5][2],
                                         self.r[5][3], self.r[5][4],
                                         self.r[5][5], self.dr[5][0],
                                         self.dr[0][0], self.dr[1][0],
                                         self.dr[2][0], self.dr[3][0],
                                         self.dr[4][0])

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        result = []
        if self.n_p1 < self.total / 2 and self.n_p2 < self.total / 2:
            for l in self.r:
                for c in l:
                    append_lst(result, c)
        return result

    def make_move(self, move: Any) -> 'StonehengeState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        current_state = copy.deepcopy(self.state)
        p = self.get_current_player_name()[1]
        for l in current_state:
            for i in l:
                if move in i:
                    i[i.index(move)] = p
                    change_owner(i, p)
        new_state = StonehengeState(not self.p1_turn, -1, current_state[0],
                                    current_state[1], current_state[2])
        return new_state

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        s = self.__str__()
        return "Current Player: {}\n" \
               "Current State:\n{}".format(self.get_current_player_name(), s)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        if self.get_possible_moves() == []:
            return -1
        for move_1 in self.get_possible_moves():
            new_state_1 = self.make_move(move_1)
            if new_state_1.get_possible_moves() == []:
                return 1
            else:
                for move_2 in new_state_1.get_possible_moves():
                    new_state_2 = new_state_1.make_move(move_2)
                    if new_state_2.get_possible_moves() == []:
                        return -1
        return 0


def change_owner(i: list, p: str) -> None:
    """
    Change the owner of lay-line if need.
    """
    count = 0
    for e in i[1:]:
        if e == p:
            count += 1
    if count >= (len(i) - 1) / 2 and i[0] == "@":
        i[0] = p


def append_lst(lst: list, p: str) -> None:
    """
    Append p into lst if p is alpha.
    """
    if p.isalpha():
        lst.append(p)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod()
