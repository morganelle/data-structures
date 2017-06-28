"""Tests for binary search tree."""
# from bst import Node
from bst import BinarySearchTree
import pytest


@pytest.fixture
def empty_tree():
    """Init empty tree fixture."""
    return BinarySearchTree()


def test_init_error_string():
    """Test init with string."""
    with pytest.raises(TypeError):
        BinarySearchTree('cake')


def test_init(empty_tree):
    """Test bst attributes with no data."""
    assert empty_tree._size == 0
    assert empty_tree._rbal == 0
    assert empty_tree._lbal == 0
    assert empty_tree._max_depth == 0
    assert empty_tree._root is None


def test_init_list_float():
    """Test init with iterable."""
    new_tree = BinarySearchTree(2.5)
    assert new_tree._root._data == 2.5
    assert new_tree._size == 1
    assert new_tree._rbal == 1
    assert new_tree._lbal == 1
    assert new_tree._max_depth == 1


def test_init_list():
    """Test init with iterable."""
    new_tree = BinarySearchTree([2, 1, 3])
    assert new_tree._size == 3
    assert new_tree._rbal == 2
    assert new_tree._lbal == 2
    assert new_tree._max_depth == 2


def test_init_tuple():
    """Test init with iterable."""
    new_tree = BinarySearchTree((2, 1, 3))
    assert new_tree._size == 3
    assert new_tree._rbal == 2
    assert new_tree._lbal == 2
    assert new_tree._max_depth == 2


def test_size_on_iterable():
    """Test size."""
    new_tree = BinarySearchTree((2, 1, 3))
    assert new_tree.size() == 3


def test_size_on_inserts(empty_tree):
    """Test size after inserts."""
    new_tree = empty_tree
    assert new_tree.size() == 0
    new_tree.insert(2)
    assert new_tree.size() == 1
    new_tree.insert(1)
    assert new_tree.size() == 2
    new_tree.insert(3)
    assert new_tree.size() == 3


def test_balance_on_inserts():
    """Test balance after inserts."""
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


def test_depth_on_inserts():
    """Test depth after inserts."""
    new_tree = BinarySearchTree()
    assert new_tree.depth() == 0
    new_tree.insert(2)
    assert new_tree.depth() == 1
    new_tree.insert(1)
    assert new_tree.depth() == 2
    new_tree.insert(3)
    assert new_tree.depth() == 2
    new_tree.insert(4)
    assert new_tree.depth() == 3


def test_search_empty_tree():
    """Test search."""
    new_tree = BinarySearchTree()
    assert new_tree.search(2) is None


def test_search_after_insert():
    """Test search."""
    new_tree = BinarySearchTree()
    assert new_tree.search(2) is None
    new_tree.insert(2)
    assert new_tree.search(2)._data == 2


def test_search_string(empty_tree):
    """Searching for a string raises Value Error."""
    with pytest.raises(TypeError):
        empty_tree.search('2')


def test_contains():
    """Test contains method."""
    new_tree = BinarySearchTree([2, 1, 3, 4])
    assert new_tree.contains(2) is True
    assert new_tree.contains(1) is True
    assert new_tree.contains(10) is False
    assert new_tree.contains(4) is True


def test_insert_invalid_tuple(empty_tree):
    """Test inserting tuple raises error."""
    with pytest.raises(TypeError):
        empty_tree.insert((9, 'hello'))


def test_insert_dupe(empty_tree):
    """Test insert."""
    empty_tree.insert(2)
    with pytest.raises(ValueError):
        empty_tree.insert(2)


def test_contains_multiple_inserts(empty_tree):
    """Test insert."""
    new_tree = empty_tree
    assert new_tree.contains(2) is False
    new_tree.insert(2)
    assert new_tree.contains(2) is True
    new_tree.insert(1)
    assert new_tree.contains(1) is True
    new_tree.insert(3)
    assert new_tree.contains(4) is False
    new_tree.insert(4)
    assert new_tree.contains(4) is True
