# Data Structures
Authors: Morgan Nomura and Sean Beseler

All modules and tests located in src directory.

## Binary Search Tree
Self-balancing binary search tree using AVL balancing.
- module: bst.py
- tests: test_bst.py
- methods:
    - size: Return number of nodes in binary search tree.
    - balance: Return difference between left and right balance.
    - depth: Return the max depth of the binary search tree.
    - search: Search for a value and return a node if found.
    - contains: Evaluate whether a value is in a binary search tree.
    - insert: Insert a new value into binary search tree.
    - breadth_first: sort bst breadth first.
    - pre_order: sort bst by pre-order.
    - in_order: sort bst in order.
    - post_order: post order sort of bst.

## Hash Table
Hash table using binary search tree bins. Two hashes are provided: an additive hash and a hash adapted from the Bernstein hash.
- module: hash_table.py
- tests: test_hash_table.py
- methods:
    - get: Returns the value for a given key; time complexity is the worst case is O(log n) but on average will be constant O(1).
    - set: Stores a key-value pair in the hash table. Time complexity is the worst case is O(log n) but on average will be constant O(1)
    - _hash: Creates a numeric value by which the key-value pair will be inserted into table. Time complexity will be O(n).


## Trie
Trie that stores single words.
- module: trie.py
- tests: test_trie.py
- methods:
    - insert: inserts a new word into the trie. Time complexity is O(n), n being the length of the word.
    - remove: removes a word from the trie. Time complexity is O(n), n being the length of the word.
    - size: returns the number of whole words in the trie. Time complexity is constant O(1).
    - contains: returns a boolean as to whether a word has been inserted in the trie. Time complexity is O(n)