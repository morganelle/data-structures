"""Tests for binary search tree."""
from bst import Node
from bst import BinarySearchTree

def test_init():
    """testing init"""
    new_tree = BinarySearchTree()
    assert new_tree._size == 0
    assert new_tree._rbal == 0
    assert new_tree._lbal == 0
    assert new_tree._max_depth == 0
    assert new_tree._root == None
    new_tree = BinarySearchTree([2,1,3])
    assert new_tree._size == 3
    assert new_tree._rbal == 2
    assert new_tree._lbal == 2
    assert new_tree._max_depth == 2
    
def test_size()
"""testing size"""
    new_tree = BinarySearchTree()
    assert new_tree.size() == 0
    new_tree = BinarySearchTree.insert(2)
    assert new_tree.size() == 1
    new_tree = BinarySearchTree.insert(1)
    assert new_tree.size()== 2
    new_tree = BinarySearchTree.insert(3)
    assert new_tree.size() == 3

def test_balance()
"""testing balance"""
    new_tree = BinarySearchTree()
    assert new_tree.balance() == 0
    new_tree = BinarySearchTree.insert(2)
    assert new_tree.balance() == 0
    new_tree = BinarySearchTree.insert(1)
    assert new_tree.balance()== -1
    new_tree = BinarySearchTree.insert(3)
    assert new_tree.balance() == 0
    new_tree = BinarySearchTree.insert(4)
    assert new_tree.balance() == 1

def test_depth()
"""testing depth"""
    new_tree = BinarySearchTree()
    assert new_tree.depth() == 0
    new_tree = BinarySearchTree.insert(2)
    assert new_tree.depth() == 1
    new_tree = BinarySearchTree.insert(1)
    assert new_tree.depth()== 2
    new_tree = BinarySearchTree.insert(3)
    assert new_tree.depth() == 2
    new_tree = BinarySearchTree.insert(4)
    assert new_tree.depth() == 3


def test_search()
"""testing search"""
    new_tree = BinarySearchTree()
    assert new_tree.search(2) == None
    new_tree = BinarySearchTree.insert(2)
    assert new_tree.search(2)._data == 2
    new_tree = BinarySearchTree.insert(1)
    assert new_tree.balance(1)._data== 1
    new_tree = BinarySearchTree.insert(3)
    assert new_tree.balance(4) == None
    new_tree = BinarySearchTree.insert(4)
    assert new_tree.balance(4)._data == 4
    
def test_contains()
"""testing contains"""
    new_tree = BinarySearchTree()
    assert new_tree.contians(2) == False
    new_tree = BinarySearchTree.insert(2)
    assert new_tree.contains(2)== True
    new_tree = BinarySearchTree.insert(1)
    assert new_tree.contains(1)== True
    new_tree = BinarySearchTree.insert(3)
    assert new_tree.contains(4) == False
    new_tree = BinarySearchTree.insert(4)
    assert new_tree.contains(4) == True

def test_insert()
"""testing insert"""
    new_tree = BinarySearchTree()
    assert new_tree.contians(2) == False
    new_tree = BinarySearchTree.insert(2)
    assert new_tree.contains(2)== True
    new_tree = BinarySearchTree.insert(1)
    assert new_tree.contains(1)== True
    new_tree = BinarySearchTree.insert(3)
    assert new_tree.contains(4) == False
    new_tree = BinarySearchTree.insert(4)
    assert new_tree.contains(4) == True
