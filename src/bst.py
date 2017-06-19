"""Python implementation of a binary search tree."""

class Node(object):
    """Initialize a node object."""
    def __init__(self):
        self._data = 0
        self._rkid = None
        self._lkid = None
        
class BinarySearchTree(object):
    """Initialize a binary search tree object."""
    def __init__(self, itter=None):
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
        raise ValueError('This binary search tree only accepts ints and floats as values.')
    new_node = Node(data)
    if self._root is None:
        self._root = new_node
        self._depth = 1
    else:
        current_node = self._root
        prev_node = current_node
        current_depth = 1
        if data > self._root.data:
            dir = right
        else:
            dir = left
        while True:
            current_depth += 1
            if data > current_node.data:
                prev_node = current_node
                current_node = current_node._rkid
                if current_node is None:
                    prev_node._rkid = new_node
                    break
            elif data < current_node.data:
                prev_node = current_node
                current_node = current_node._lkid
                if current_node is None:
                    prev_node._lkid = new_node
                    break
            else:
                raise ValueError('Can\'t insert a node with the same value as another node.')
        if current_depth > self._max_depth:
            self._max_depth = current_depth
        if dir == right and self._rbal < current_depth:
            self._rbal = current_depth
        if dir == left and self._lbal < current_depth:
            self._lbal = current_depth
        self._size += 1

