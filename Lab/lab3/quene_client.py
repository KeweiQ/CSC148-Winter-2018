"""
Client interface for class Queue.
"""
from queue_lab import Queue


def list_queue(list_: list, q: Queue) -> list:
    """
    Return a list of non-list elements of list_ after processing them
    through q.

    >>> l = [1, 2, [3, 4]]
    >>> q = Queue()
    >>> list_queue(l, q)
    [1, 2, 3, 4]
    """
    result_list = []
    for i in list_:
        q.add(i)
    while not q.is_empty():
        i = q.remove()
        if not isinstance(i, list):
            result_list.append(i)
        else:
            for j in i:
                q.add(j)
    return result_list


if __name__ == '__main__':
    q = Queue()
    i = input("Type an integer:")
    while i != "148":
        if i.isdigit():
            q.add(int(i))
        i = input("Type an integer:")
    sum = 0
    while not q.is_empty():
        i = q.remove()
        sum += i
    print(sum)
