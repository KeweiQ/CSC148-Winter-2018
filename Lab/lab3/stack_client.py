"""
Client interface for class Stack.
"""
from stack_lab import Stack


def list_stack(l: list, s: Stack) -> list:
    """
    Return a list of non-list elements of list_ after processing them
    through s.

    >>> l = [1, 2, [3, 4]]
    >>> q = Stack()
    >>> list_stack(l, q)
    [4, 3, 2, 1]
    """
    result_list = []
    for i in l:
        s.add(i)
    while not s.is_empty():
        i = s.remove()
        if not isinstance(i, list):
            result_list.append(i)
        else:
            for j in i:
                s.add(j)
    return result_list


if __name__ == '__main__':
    s = Stack()
    i = input("Type a string:")
    while i != "end":
        s.add(i)
        i = input("Type a string:")
    while s.is_empty() is False:
        print(s.remove())
