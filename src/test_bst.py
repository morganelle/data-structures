"""Tests for binary search tree."""
# from bst import Node
from bst import BinarySearchTree
import pytest


@pytest.fixture
def empty_tree():
    """Init empty tree fixture."""
    return BinarySearchTree()


@pytest.fixture
def tree_init_list():
    """Init with numbers 1-7 tree fixture."""
    return BinarySearchTree([4, 2, 3, 1, 6, 5, 7])


@pytest.fixture
def tree_init_short_list():
    """Init with numbers 1-7 tree fixture."""
    return BinarySearchTree([2, 1, 3])


@pytest.fixture
def tree_init_one_node():
    """Init with numbers 1-7 tree fixture."""
    return BinarySearchTree([100])


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


def test_breadth_first(tree_init_list):
    """Test breadth first."""
    gen = tree_init_list.breadth_first()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 6
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 5
    assert next(gen) is 7


def test_pre_order(tree_init_list):
    """Test pre-order first."""
    gen = tree_init_list.pre_order()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 6
    assert next(gen) is 5
    assert next(gen) is 7


def test_in_order(tree_init_list):
    """Test pre-order first."""
    gen = tree_init_list.in_order()
    assert next(gen) is 1
    assert next(gen) is 2
    assert next(gen) is 3
    assert next(gen) is 4
    assert next(gen) is 5
    assert next(gen) is 6
    assert next(gen) is 7


def test_post_order(tree_init_list):
    """Test pre-order first."""
    gen = tree_init_list.post_order()
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 2
    assert next(gen) is 5
    assert next(gen) is 7
    assert next(gen) is 6
    assert next(gen) is 4


def test_breadth_first_short(tree_init_short_list):
    """Test breadth first traversal on small tree."""
    gen = tree_init_short_list.breadth_first()
    assert next(gen) is 2
    assert next(gen) is 1
    assert next(gen) is 3


def test_pre_order_short(tree_init_short_list):
    """Test pre order traversal on small tree."""
    gen = tree_init_short_list.pre_order()
    assert next(gen) is 2
    assert next(gen) is 1
    assert next(gen) is 3


def test_in_order_short(tree_init_short_list):
    """Test in order traversal on small tree."""
    gen = tree_init_short_list.in_order()
    assert next(gen) is 1
    assert next(gen) is 2
    assert next(gen) is 3


def test_post_order_short(tree_init_short_list):
    """Test post order traversal on small tree."""
    gen = tree_init_short_list.post_order()
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 2


def test_breadth_first_one(tree_init_one_node):
    """Test breadth first traversal on small tree."""
    gen = tree_init_one_node.breadth_first()
    assert next(gen) is 100


def test_pre_order_one(tree_init_one_node):
    """Test pre order traversal on small tree."""
    gen = tree_init_one_node.pre_order()
    assert next(gen) is 100


def test_in_order_one(tree_init_one_node):
    """Test in order traversal on small tree."""
    gen = tree_init_one_node.in_order()
    assert next(gen) is 100


def test_post_order_one(tree_init_one_node):
    """Test post order traversal on small tree."""
    gen = tree_init_one_node.post_order()
    assert next(gen) is 100


def test_breadth_first_empty(empty_tree):
    """Test breadth first on empty tree."""
    with pytest.raises(StopIteration):
        next(empty_tree.breadth_first())


def test_pre_order_empty(empty_tree):
    """Test pre order on empty tree."""
    with pytest.raises(StopIteration):
        next(empty_tree.pre_order())


def test_in_order_empty(empty_tree):
    """Test in order on empty tree."""
    with pytest.raises(StopIteration):
        next(empty_tree.in_order())


def test_post_order_empty(empty_tree):
    """Test post order on empty tree."""
    with pytest.raises(StopIteration):
        next(empty_tree.post_order())
