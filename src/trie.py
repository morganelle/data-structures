"""Python implementation of a trie data structure."""


class Node(object):
    """Node attributes for Trie."""

    def __init___(self, parent=None, data=None):
        """Instantiate a new Node."""
        self._parent = parent
        self._children = []
        self._data = data


class Trie(object):
    """Attributes and methods of a Trie."""

    def __init__(self):
        """Instantiate a new Trie."""
        self._root = Node()
        self._size = 0

    def contains(self, val):
        """Return a boolean as to whether a string is in the Trie."""
        if type(val) is not str:
            raise TypeError('Please enter a string.')
        current_node = self._root
        for char in val:
            if self._child_helper(current_node, char):
                current_node = self._child_helper(current_node, char)
            else:
                return False
        for child in current_node._children:
            if child == '$':
                return True
        return False

    def _child_helper(self, node, char):
        """Traverse children of a node."""
        for child in node._children:
            if child._data == char:
                return child
        return False

    def insert(self, val):
        """Insert a new word into the Trie."""
        if type(val) is not str:
            raise TypeError('Please enter a string.')
        if self.contains(val):
            raise ValueError('String is already in Trie.')
        current_node = self._root
        for char in val:
            if self._child_helper(current_node, char):
                current_node = self._child_helper(current_node, char)
            else:
                new_node = Node(current_node, char)
                current_node._children.append(new_node)
                current_node = new_node
        new_node = Node(current_node, '$')
        current_node._children.append(new_node)
        self._size += 1

    def remove(self, val);
        """Remove a word from the Trie."""
        if type(val) is not str:
            raise TypeError('Please enter a string.')
        if not self.contains(val):
            raise ValueError('String isn\'t in Trie.')
        current_node = self._root
        for char in val:
            if self._child_helper(current_node, char):
                current_node = self._child_helper(current_node, char)
        node = _parent_helper(current_node, '$')
        current_node._children.remove(node)
        while current_node is not self._root or len(current_node._children) > 0:
                current_node._parent._children.remove(current_node)
                current_node = current_node._parent
        self._size -= 1

    def _parent_helper(self, parent, char):
        """Identify node to remove."""
        for node in parent._children:
            if node._data == char:
                return node

    def size(self):
        """Return number of words in Trie."""
        return self._size
