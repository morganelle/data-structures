"""Tests for binary search tree."""
# from bst import Node
from bst import BinarySearchTree
import pytest


def test_init_error_string():
    """Test init with string."""
    with pytest.raises(TypeError):
        BinarySearchTree('cake')


def test_init():
    """Test init with no data."""
    new_tree = BinarySearchTree()
    assert new_tree._size == 0
    assert new_tree._rbal == 0
    assert new_tree._lbal == 0
    assert new_tree._max_depth == 0
    assert new_tree._root is None


def test_init_list_float():
    """Test init with iterable."""
    new_tree = BinarySearchTree(2.5)
    assert new_tree._root._data == 2.5
    assert new_tree._size == 1
    assert new_tree._rbal == 0
    assert new_tree._lbal == 0
    assert new_tree._max_depth == 0


def test_init_list():
    """Test init with iterable."""
    new_tree = BinarySearchTree([2, 1, 3])
    assert new_tree._size == 3
    assert new_tree._rbal == 1
    assert new_tree._lbal == 1
    assert new_tree._max_depth == 1


def test_init_tuple():
    """Test init with iterable."""
    new_tree = BinarySearchTree((2, 1, 3))
    assert new_tree._size == 3
    assert new_tree._rbal == 1
    assert new_tree._lbal == 1
    assert new_tree._max_depth == 1


def test_size():
    """Test size."""
    new_tree = BinarySearchTree()
    assert new_tree.size() == 0
    new_tree.insert(2)
    assert new_tree.size() == 1
    new_tree.insert(1)
    assert new_tree.size() == 2
    new_tree.insert(3)
    assert new_tree.size() == 3


def test_balance():
    """Test balance."""
    new_tree = BinarySearchTree()
    assert new_tree.balance() == 0
    new_tree.insert(2)
    assert new_tree.balance() == 0
    new_tree.insert(1)
    assert new_tree.balance() == -1
    new_tree.insert(3)
    assert new_tree.balance() == 0
    new_tree.insert(4)
    assert new_tree.balance() == 1


def test_depth():
    """Test depth."""
    new_tree = BinarySearchTree()
    assert new_tree.depth() == 0
    new_tree.insert(2)
    assert new_tree.depth() == 0
    new_tree.insert(1)
    assert new_tree.depth() == 1
    new_tree.insert(3)
    assert new_tree.depth() == 1
    new_tree.insert(4)
    assert new_tree.depth() == 2


def test_search():
    """Test search."""
    new_tree = BinarySearchTree()
    assert new_tree.search(2) is None
    new_tree.insert(2)
    assert new_tree.search(2)._data == 2
    new_tree.insert(1)
    assert new_tree.search(1)._data == 1
    new_tree.insert(3)
    assert new_tree.search(4) is None
    new_tree.insert(4)
    assert new_tree.search(4)._data == 4


def test_contains():
    """Test contains method."""
    new_tree = BinarySearchTree()
    assert new_tree.contains(2) is False
    new_tree.insert(2)
    assert new_tree.contains(2) is True
    new_tree.insert(1)
    assert new_tree.contains(1) is True
    new_tree.insert(3)
    assert new_tree.contains(4) is False
    new_tree.insert(4)
    assert new_tree.contains(4) is True


def test_insert_tuple():
    """Test inserting tuple raises error."""
    new_tree = BinarySearchTree()
    with pytest.raises(TypeError):
        new_tree.insert((9, 'hello'))


def test_insert_dupe():
    """Test insert."""
    new_tree = BinarySearchTree()
    new_tree.insert(2)
    with pytest.raises(ValueError):
        new_tree.insert(2)


def test_insert():
    """Test insert."""
    new_tree = BinarySearchTree()
    assert new_tree.contains(2) is False
    new_tree.insert(2)
    assert new_tree.contains(2) is True
    new_tree.insert(1)
    assert new_tree.contains(1) is True
    new_tree.insert(3)
    assert new_tree.contains(4) is False
    new_tree.insert(4)
    assert new_tree.contains(4) is True

    
def test_breadth_first():
    """test breadth first"""
    new_tree = BinarySearchTree([4,2,3,1,6,5,7])
    gen = new_tree.breadth_first()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 6
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 5
    assert next(gen) is 7

    
def test_pre_order():
    """test pre-order first"""
    new_tree = BinarySearchTree([4,2,3,1,6,5,7])
    gen = new_tree.pre_order()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 6
    assert next(gen) is 5
    assert next(gen) is 7


def test_in_order():
    """test pre-order first"""
    new_tree = BinarySearchTree([4,2,3,1,6,5,7])
    gen = new_tree.in_order()
    assert next(gen) is 1
    assert next(gen) is 2
    assert next(gen) is 3
    assert next(gen) is 4
    assert next(gen) is 5
    assert next(gen) is 6
    assert next(gen) is 7

def test_post_order():
    """test pre-order first"""
    new_tree = BinarySearchTree([4,2,3,1,6,5,7])
    gen = new_tree.post_order()
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 2
    assert next(gen) is 5
    assert next(gen) is 7
    assert next(gen) is 6
    assert next(gen) is 4

def test_del():
    """Test del."""
    new_tree = BinarySearchTree([4,2,3,1,6,5,7])
    assert new_tree.contains(4) is True
    new_tree.delete(4)
    assert new_tree.contains(4) is False
    assert new_tree.contains(7) is True
    new_tree.delete(7)
    assert new_tree.contains(7) is False
    assert new_tree.contains(6) is True
    new_tree.delete(6)
    assert new_tree.contains(6) is False
    assert new_tree.contains(2) is True
    new_tree.delete(2)
    assert new_tree.contains(2) is False
    assert new_tree.contains(1) is True
    new_tree.delete(1)
    assert new_tree.contains(1) is False
    assert new_tree.contains(3) is True
    new_tree.delete(3)
    assert new_tree.contains(3) is False
    assert new_tree.contains(5) is True
    new_tree.delete(5)
    assert new_tree.contains(5) is False

