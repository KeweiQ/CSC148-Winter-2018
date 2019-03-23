"""
Test module Queue.
"""
import unittest
from queue_lab import Queue


class EmptyTestCase(unittest.TestCase):
    """Test behaviour of an empty Queue.
    """

    def setUp(self):
        """Set up an empty queue.
        """

        self.queue = Queue()

    def tearDown(self):
        """Clean up.
        """

        self.queue = None

    def testIsEmpty(self):
        """Test is_empty() on empty Queue.
        """
        self.assertTrue(
            self.queue.is_empty(),
            'is_empty returned False on an empty Queue!')


class SingletonTestCase(unittest.TestCase):

    """Check whether adding a single item makes it appear at the front.
    """

    def setUp(self):
        """Set up a queue with a single element.
        """

        self.queue = Queue()
        self.queue.add('a')

    def tearDown(self):
        """Clean up.
        """

        self.queue = None

    def testIsEmpty(self):
        """Test is_empty() on non-empty Queue.
        """

        self.assertFalse(
            self.queue.is_empty(),
            'is_empty returned True on non-empty Queue!')

    def testRemove(self):
        """Test remove() on a non-empty Queue.
        """

        front = self.queue.remove()
        self.assertEqual(
            front, 'a',
            'The item at the front should have been "a" but was ' +
            front + '.')
        self.assertTrue(
            self.queue.is_empty(),
            'Queue with one element not empty after remove().')


class TypicalTestCase(unittest.TestCase):

    """A comprehensive tester of typical behaviour of Queue.
    """

    def setUp(self):
        """Set up an empty queue.
        """

        self.queue = Queue()

    def tearDown(self):
        """Clean up.
        """

        self.queue = None

    def testAll(self):
        """Check adding and removing several items.
        """

        for item in range(20):
            self.queue.add(item)
            self.assertFalse(
                self.queue.is_empty(),
                'Queue should not be empty after adding item ' +
                str(item))
        item = 0
        while not self.queue.is_empty():
            front = self.queue.remove()
            self.assertEqual(
                front, item,
                'Wrong item at the front of the Queue. Found ' +
                str(front) + ' but expected ' + str(item))
            item += 1


def list_queue(l: list, q: Queue) -> None:
    """
    A special stack.
    """

    for e in l:
        q.add(e)
    while q.is_empty is False:
        if type(q[0]) == list:
            for a in q[0]:
                q.add(a)
        else:
            print(q[0])
            q.remove()


if __name__ == '__main__':
    unittest.main(exit=False)
    q = Queue()
    i = input("Type a integer:")
    while str(i) != 148:
        q.add(str(i))
        i = input("Type a integer:")
    s = 0
    for e in q:
        s += e
    print(s)
