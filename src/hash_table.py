"""Python implementation of a hash table."""
from hash_bst import BinarySearchTree


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
        return base

    def _build_bins(self, size):
        """Build bins from binary search trees."""
        bins = []
        bst = BinarySearchTree()
        for container in range(size):
            bins.append(bst)
        return bins

    def init(self, size, hash_function=_prime_hash):
        """Instantiate a new hash table."""
        self._bins = self._build_bins(size)
        self._hash_function = hash_function
        self._size = size

    def get_bin(self, hash_number):
        """Find bin based on hash number."""
        return hash_number % self._size

    def get(self, key):
        """Return a value for a given key."""
        hash_number = self._hash(key)
        binary_tree = self.bins[self._get_bin(hash_number)]
        node = binary_tree.search(hash_number)
        entries = node._entries
        for entry in entries:
            if key is entries[0]:
                return entries[1]
        raise KeyError('Key not in hash table.')

    def set(self, key, value):
        """Set a new value for a given key."""
        hash_number = self._hash(key)
        binary_tree = self.bins[self._get_bin(hash_number)]
        binary_tree.insert(hash_number, (key, value))

    def _hash(self, key):
        """Convert key into hash value."""
        if type(key) is not str:
            raise TypeError('Please enter a string as a key.')
        return self._hash_function(key)
