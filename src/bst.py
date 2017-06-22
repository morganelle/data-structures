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
        if itter is not None:
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
        current_node = self._root
        while True:
            if current_node is None:
                return None
            if val == current_node._data:
                return current_node
            if val > current_node._data:
                current_node = current_node._rkid
            else:
                current_node = current_node._lkid

    def contains(self, val):
        """Evaluate whether a value is in a binary search tree."""
        if self.search(val) is None:
            return False
        return True

    def insert(self, data):
        """Insert a new value into binary search tree."""
        if type(data) not in [int, float]:
            raise TypeError('This binary search tree only accepts ints and floats as values.')
        current_node = self._root
        current_depth = 0
        new_node = Node(data)
        if self._root is None:
            self._root = new_node
            self._depth = 1
        else:
            current_node = self._root
            prev_node = current_node
            current_depth = 0
            if data > self._root._data:
                dir = 'right'
            else:
                dir = 'left'
            while True:
                current_depth += 1
                if data > current_node._data:
                    prev_node = current_node
                    current_node = current_node._rkid
                    if current_node is None:
                        prev_node._rkid = new_node
                        break
                elif data < current_node._data:
                    prev_node = current_node
                    current_node = current_node._lkid
                    if current_node is None:
                        prev_node._lkid = new_node
                        break
                else:
                    raise ValueError('Can\'t insert a node with the same value as another node.')
            if current_depth > self._max_depth:
                self._max_depth = current_depth
            if dir == 'right' and self._rbal < current_depth:
                self._rbal = current_depth
            if dir == 'left' and self._lbal < current_depth:
                self._lbal = current_depth
        self._size += 1

    def breadth_first(self):
        """Sort bst breadth first."""
        nodes_to_vist = []
        curr = self._root
        nodes_to_vist.append(curr)
        while len(nodes_to_vist):
            curr = nodes_to_vist[0]
            if curr._lkid:
                nodes_to_vist.append(curr._lkid)
            if curr._rkid:
                nodes_to_vist.append(curr._rkid)
            yield curr._data
            nodes_to_vist.remove(curr)

    def _pre_order_helper(self, node):
        """Move the pre order along the tree."""
        curr = node
        yield curr._data
        if curr._lkid:
            for node_data in self._pre_order_helper(curr._lkid):
                yield node_data
        if curr._rkid:
            for node_data in self._pre_order_helper(curr._rkid):
                yield node_data

    def pre_order(self):
        """Sort bst by pre-order."""
        for node_data in self._pre_order_helper(self._root):
            yield node_data

    def _in_order_helper(self, node):
        """Move the pre order along the tree."""
        curr = node
        if curr._lkid:
            for node_data in self._in_order_helper(curr._lkid):
                yield node_data
        yield curr._data
        if curr._rkid:
            for node_data in self._in_order_helper(curr._rkid):
                yield node_data

    def in_order(self):
        """Sort bst in order."""
        for node_data in self._in_order_helper(self._root):
            yield node_data

    def _post_order_helper(self, node):
        """Move the pre order along the tree."""
        curr = node
        if curr._lkid:
            for node_data in self._post_order_helper(curr._lkid):
                yield node_data
        if curr._rkid:
            for node_data in self._post_order_helper(curr._rkid):
                yield node_data
        yield curr._data

    def post_order(self):
        """Post order sort of bst."""
        for node_data in self._post_order_helper(self._root):
            yield node_data

    def _new_depth(self, node, curr_depth):
        """."""
        right = curr_depth
        left = curr_depth
        if node._rkid:
            right = self._new_depth(node._rkid, curr_depth + 1)
        if node._lkid:
            left = self._new_depth(node._lkid, curr_depth + 1)
        if right > left:
            return right
        return left

    def _get_new_max(self):
        """."""
        right = 0
        left = 0
        if self.root._rkid:
            right = self._new_depth(self.root._rkid, 1)
        if self.root._lkid:
            left = self._new_depth(self.root._lkid, 1)
        if right < self._rbal:
            self._rbal = right
        if left < self._lbal:
            self._lbal = left
        if right > left:
            if right < self._max_depth:
                self._max_depth = right
        elif left < self._max_depth:
            self._max_depth = left

    def delete(self, val):
        """."""
        if not self.contains(val):
            raise ValueError('Value is not in the tree')
        node = self.search(val)
        parent = self.find_parent_node(node)
        if node._rkid and node._lkid:
            # import pdb; pdb.set_trace()
            self._del_node_two_children(parent, node)
        elif node._rkid or node._lkid:
            self._del_node_one_child(parent, node)
        else:
            self._del_node_no_children(parent, node)

    def find_parent_node(self, node, parent=None):
        """."""
        parent = parent
        if parent is None:
            parent = self._root
        if parent._rkid is node:
            return parent
        elif parent._rkid:
            other = self.find_parent_node(node, parent._rkid)
            if other is not None:
                return other
        if parent._lkid is node:
            return parent
        elif parent._lkid:
            other = self.find_parent_node(node, parent._lkid)
            if other is not None:
                return other
        return None

    def _del_node_no_children(self, parent, node):
        """."""
        if parent._rkid == node:
            parent._rkid = None
        else:
            parent._lkid = None

    def _del_node_one_child(self, parent, node):
        """."""
        if parent._rkid == node:
            if node._rkid:
                parent._rkid = node._rkid
            else:
                parent._rkid = node._lkid
        elif node._rkid:
            parent._lkid = node._rkid
        else:
            parent._lkid = node._lkid

    def _del_node_two_children(self, parent, node):
        """."""
        succ = self._get_successor(node)
        self.delete(succ._data)
        succ._rkid = node._rkid
        succ._lkid = node._lkid
        if node is not self._root:
            if parent._rkid is node:
                parent._rkid = succ
            else:
                parent._lkid = succ
        else:
            self._root = succ

    def _get_successor(self, node):
        """Find node to replace deleted node."""
        current_node = node
        if node._rkid:
            current_node = node._rkid
        while True:
            if not current_node._lkid:
                break
            current_node = current_node._lkid
        return current_node


def _best_case():
    """Best-case performance case of bst search."""
    setup_code = """
from __main__ import _best_case
from bst import BinarySearchTree
from bst import Node
    """
    test_code = """
new_tree = BinarySearchTree([4,2,3,1,6,5,7])
new_tree.search(7)
    """
    return(timeit.repeat(setup=setup_code, stmt=test_code, number=100000))


def _worst_case():
    setup_code = """
from __main__ import _best_case
from bst import BinarySearchTree
from bst import Node
    """
    test_code = """
new_tree = BinarySearchTree([1,2,3,4,5,6,7])
new_tree.search(7)
    """
    return(timeit.repeat(setup=setup_code, stmt=test_code, number=100000))


if __name__ == '__main__':
    print(_best_case())
    print('O(log(n))')
    print(_worst_case())
    print('O(n)')
