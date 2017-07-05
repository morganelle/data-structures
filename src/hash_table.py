"""Python implementation of a hash table."""
from hash_bst import BinarySearchTree  # pragma no cover


class HashTable(object):
    """Methods and attributes of a hash table."""

    def _get_letter_value(self, char):
        """."""
        try:
            return int(char) + 1
        except ValueError:
            return ord(char) - 54

    def _prime_hash(self, key):
        """Build hash based on prime number and offset."""
        base = 1
        offset = 3
        for char in key:
            base = base * offset + self._get_letter_value(char)
        base -= 4
        return base

    def _naive_hash(self, key):
        """Build hash based on additive values."""
        base = 0
        for char in key:
            base += self._get_letter_value(char)
            base -= 1
        return base

    def _build_bins(self, size):
        """Build bins from binary search trees."""
        bins = []
        #bst = BinarySearchTree()
        for container in range(size):
            bins.append(BinarySearchTree())
        return bins

    def __init__(self, size, hash_function=False):
        """Instantiate a new hash table."""
        if type(size) is not int:
            raise TypeError('Please enter an integer for size.')
        if size < 1:
            raise ValueError('Please enter a positive integer as size.')
        self._bins = self._build_bins(size)
        if hash_function:
            self._hash_function = hash_function
        else:
            self._hash_function = self._prime_hash
        self._size = size

    def get(self, key):
        """Return a value for a given key."""
        hash_number = self._hash(key)
        binary_tree = self._bins[hash_number % self._size]
        node = binary_tree.search(hash_number)
        if node:
            entries = node._entries
            for entry in entries:
                if key is entry[0]:
                    return entry[1]
        raise KeyError('Key not in hash table.')

    def set(self, key, value):
        """Set a new value for a given key."""
        hash_number = self._hash(key)
        binary_tree = self._bins[hash_number % self._size]
        binary_tree.insert(hash_number, (key, value))

    def _hash(self, key):
        """Convert key into hash value."""
        if type(key) is not str:
            raise TypeError('Please enter a string as a key.')
        return self._hash_function(key)
