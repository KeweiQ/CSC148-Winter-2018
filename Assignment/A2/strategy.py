"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from minimax_stack import MinimaxStack
from minimax_tree import MinimaxTree


def interactive_strategy(game: Any) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def minimax_recursive_strategy(game: Any) -> Any:
    """
    Return a move that guarantees the highest possible
    score from the current position.
    This is a recursive version.
    """
    state = game.current_state
    player = state.get_current_player_name()
    s = []
    if player == "p1":
        counter = "p2"
    else:
        counter = "p1"
    for move in state.get_possible_moves():
        old_state = game.current_state
        s.append(-1 * get_score(game, state.make_move(move), counter, player))
        game.current_state = old_state
    max_score = max(s)
    return state.get_possible_moves()[s.index(max_score)]


def minimax_iterative_strategy(game: Any) -> Any:
    """
    Return a move that guarantees the highest
    possible score from the current position.
    This is an interactive version.
    """
    t = MinimaxTree(game.current_state, None, [], None)
    s = MinimaxStack()
    s.add(t)
    player = game.current_state.get_current_player_name()
    if player == "p1":
        counter = "p2"
    else:
        counter = "p1"
    old_state = game.current_state
    while not s.is_empty():
        i = s.remove()
        game.current_state = i.value
        if i.value.get_possible_moves() == [] and i.children == []:
            if game.is_winner(player) or game.is_winner(counter):
                i.score = -1
            else:
                i.score = 0
        elif i.value.get_possible_moves() != [] and i.children != []:
            lst = []
            for c in i.children:
                lst.append(-1 * c.score)
            i.score = max(lst)
        else:
            s.add(i)
            for move in i.value.get_possible_moves():
                new_state = i.value.make_move(move)
                new_tree = MinimaxTree(new_state, move, [], None)
                i.children.append(new_tree)
                s.add(new_tree)
    game.current_state = old_state
    possible_move = []
    for ch in t.children:
        if -1 * ch.score == t.score:
            possible_move.append(ch.move)
    return possible_move[0]


def get_score(game: Any, state: Any, player: str, counter: str) -> int:
    """
    Return the highest possible score for the current state.
    """
    game.current_state = state
    if game.is_over(state):
        if game.is_winner(player) or game.is_winner(counter):
            return -1
        return 0
    return max([-1 * get_score(game, state.make_move(move), counter, player)
                for move in state.get_possible_moves()])


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
