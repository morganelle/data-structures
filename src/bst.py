"""Python implementation of a binary search tree."""

import timeit


class Node(object):
    """Node object methods."""

    def __init__(self, data):
        """Instantiate a node object."""
        self._data = data
        self._parent = None
        self._rkid = None
        self._lkid = None


class BinarySearchTree(object):
    """Binary search tree object methods and attributes."""

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
        return

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
                        self._get_new_max()
                elif val > current_node._data:
                    if current_node._rkid:
                        current_node = current_node._rkid
                    else:
                        current_node._rkid = new_node
                        new_node._parent = current_node
                        self._get_new_max()
        self._size += 1

    def _balance_helper_breadth_first(self, node):
        """Yield a subtree for a given node."""
        output = []
        nodes_to_vist = []
        curr = node
        if curr:
            nodes_to_vist.append(curr)
        while len(nodes_to_vist):
            curr = nodes_to_vist[0]
            if curr._lkid is not None:
                nodes_to_vist.append(curr._lkid)
            if curr._rkid is not None:
                nodes_to_vist.append(curr._rkid)
            output.append(curr._data)
            nodes_to_vist.remove(curr)
        return output

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
        """Set the new right and left balance."""
        right = curr_depth
        left = curr_depth
        if node._rkid:
            right = self._new_depth(node._rkid, curr_depth + 1)
        if node._lkid:
            left = self._new_depth(node._lkid, curr_depth + 1)
        if right > left:
            return right
        return left

    def _get_new_max(self, insert=True):
        """Get the new max depth."""
        right = 1
        left = 1
        if self._root:
            if self._root._rkid:
                right = self._new_depth(self._root._rkid, 2)
            if self._root._lkid:
                left = self._new_depth(self._root._lkid, 2)
            self._rbal = right
            self._lbal = left
            if insert:
                if right > left:
                    if right > self._max_depth:
                        self._max_depth = right
                elif left > self._max_depth:
                    self._max_depth = left
            else:
                if right > left:
                    if right < self._max_depth:
                        self._max_depth = right
                elif left < self._max_depth:
                    self._max_depth = left

    def delete(self, val):
        """Check the status of a node."""
        if not self.contains(val):
            return None
        node = self.search(val)
        if node._rkid and node._lkid:
            self._del_node_two_children(node._parent, node)
        elif node._rkid or node._lkid:
            self._del_node_one_child(node._parent, node)
        else:
            self._del_node_no_children(node._parent, node)
        self._get_new_max(False)
        self._size = len(self._balance_helper_breadth_first(self._root))

    def _del_node_no_children(self, parent, node):
        """Delete a node that has zero kids."""
        if parent:
            if parent._rkid == node:
                parent._rkid = None
            else:
                parent._lkid = None
        else:
            self._root = None

    def _del_node_one_child(self, parent, node):
        """Delete a node that has one kids."""
        if parent:
            if parent._rkid == node:
                if node._rkid:
                    parent._rkid = node._rkid
                    node._rkid._parent = parent
                else:
                    parent._rkid = node._lkid
                    node._lkid._parent = parent
            elif node._rkid:
                parent._lkid = node._rkid
                node._rkid._parent = parent
            else:
                parent._lkid = node._lkid
                node._lkid._parent = parent
        else:
            if node._rkid:
                self._root = node._rkid
                node._rkid._parent = None
            else:
                self._root = node._lkid
                node._lkid._parent = None

    def _del_node_two_children(self, parent, node):
        """Delete a node that has two kids."""
        succ = self._get_successor(node)
        self.delete(succ._data)
        succ._rkid = node._rkid
        succ._lkid = node._lkid
        if node._rkid:
            node._rkid._parent = succ
        if node._lkid:
            node._lkid._parent = succ
        if node is not self._root:
            if parent._rkid is node:
                parent._rkid = succ
                succ._parent = parent
            else:
                parent._lkid = succ
                succ._parent = parent
        else:
            self._root = succ
            succ._parent = None

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


def _best_case():  # pragma no cover
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


def _worst_case():  # pragma no cover
    """Worst-case performance case of bst search."""
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


if __name__ == '__main__':  # pragma no cover
    print(_best_case())
    print('O(log(n))')
    print(_worst_case())
    print('O(n)')
