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
        self._max_deth = 0
        self._root = None
        if iter is not None:
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

   def insert(self, val):
    """."""
    if val is None:
        raise ValueError('Value is none')
