"""Python implementation of a binary search tree."""

import timeit


class Node(object):
    """Initialize a node object."""

    def __init__(self, data):
        """."""
        self._data = data
        self._rkid = None
        self._lkid = None


class BinarySearchTree(object):
    """Initialize a binary search tree object."""

    def __init__(self, itter=None):
        """Init a binary search tree with no data or iterable."""
        self._size = 0
        self._rbal = 0
        self._lbal = 0
        self._max_depth = 0
        self._root = None
        if itter:
            if type(itter) not in [tuple, list, int, float]:
                raise TypeError('Please enter an iterable or number.')
            if type(itter) in [int, float]:
                self.insert(itter)
            else:
                for item in itter:
                    self.insert(item)

    def size(self):
        """Return number of nodes in binary search tree."""
        return self._size

    def balance(self):
        """Return difference between left and right balance."""
        return self._rbal - self._lbal

    def depth(self):
        """Return the max depth of the binary search tree."""
        return self._max_depth

    def search(self, val):
        """Search for a value and return a node if found."""
        if type(val) not in [int, float]:
            raise TypeError('This tree accepts numbers only.')
        current_node = self._root
        while current_node:
            if val == current_node._data:
                return current_node
            if val > current_node._data:
                current_node = current_node._rkid
            else:
                current_node = current_node._lkid
        return None

    def contains(self, val):
        """Evaluate whether a value is in a binary search tree."""
        return not not self.search(val)

    def insert(self, val):
        """Insert a new value into binary search tree."""
        if type(val) not in [int, float]:
            raise TypeError('This tree accepts numbers only.')
        if self.contains(val):
            raise ValueError('Node already in tree.')
        new_node = Node(val)
        if self._size == 0:
            self._root = new_node
            self._max_depth = 1
            self._rbal = 1
            self._lbal = 1
        else:
            current_depth = 1
            current_node = self._root
            while val is not current_node._data:
                current_depth += 1
                if val < current_node._data:
                    if current_node._lkid:
                        current_node = current_node._lkid
                    else:
                        current_node._lkid = new_node
                        new_node._parent = current_node
                        self._update_balances_and_depth(current_depth, val)
                elif val > current_node._data:
                    if current_node._rkid:
                        current_node = current_node._rkid
                    else:
                        current_node._rkid = new_node
                        new_node._parent = current_node
                        self._update_balances_and_depth(current_depth, val)
        self._size += 1

    def _update_balances_and_depth(self, current_depth, val):
        """Increment left/right balance on insert."""
        if current_depth > self._max_depth:
            self._max_depth = current_depth
        if val > self._root._data and self._rbal < current_depth:
            self._rbal = current_depth
        elif val < self._root._data and self._lbal < current_depth:
            self._lbal = current_depth


def _best_case():
    SETUP_CODE = """
from __main__ import _best_case
from bst import BinarySearchTree
from bst import Node
    """
    TEST_CODE = """
new_tree = BinarySearchTree([4,2,3,1,6,5,7])
new_tree.search(7)
    """
    return(timeit.repeat(setup=SETUP_CODE,
    stmt=TEST_CODE,
    number=100000))


def _worst_case():
    SETUP_CODE = """
from __main__ import _best_case
from bst import BinarySearchTree
from bst import Node
    """
    TEST_CODE = """
new_tree = BinarySearchTree([1,2,3,4,5,6,7])
new_tree.search(7)
    """
    return(timeit.repeat(setup=SETUP_CODE,
                        stmt=TEST_CODE,
                        number=100000))


if __name__ == '__main__':
    print(_best_case())
    print('O(log(n))')
    print(_worst_case())
    print('O(n)')
