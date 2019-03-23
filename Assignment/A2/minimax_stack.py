"""
A stack class for minimax strategy.
"""
from typing import Any
from minimax_tree import MinimaxTree


class MinimaxStack:
    """
    Last-in, first-out (LIFO) stack for minimax.
    """

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.
        """
        self._contains = []

    def add(self, obj: MinimaxTree) -> None:
        """
        Add object obj to top of Stack self.
        """
        self._contains.append(obj)

    def remove(self) -> Any:
        """
        Remove and return top element of Stack self.
        Assume Stack self is not emp.
        """
        if self.is_empty() is True:
            return "Cannot remove from empty stack!"
        return self._contains.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.
        """
        return len(self._contains) == 0


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod()
