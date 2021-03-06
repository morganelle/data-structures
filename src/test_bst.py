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
def tree_init_list_shorter_list():
    """Init with nubers 1,3,4,6,7 tree fixture."""
    return BinarySearchTree([4, 3, 1, 6, 7])


@pytest.fixture
def tree_init_list_longer_list():
    """Init with number 1-7 tree fixture we need a differenct name."""
    return BinarySearchTree([4, 2, 3, 1, 6, 7, 5])


@pytest.fixture
def tree_init_one_node():
    """Init tree with one node."""
    tree = BinarySearchTree()
    tree.insert(3)
    return tree


@pytest.fixture
def tree_init_one_node_left():
    """Init binarySearch for del node 1 kid left."""
    return BinarySearchTree([4, 3])


@pytest.fixture
def tree_init_three_nodes_left():
    """Init binarySearch uneven."""
    return BinarySearchTree([4, 6, 5])


@pytest.fixture
def tree_init_three_nodes_right():
    """Init binarySearch uneven."""
    return BinarySearchTree([4, 5, 6])


@pytest.fixture
def tree_init_one_node_right():
    """Init binarySearch for del node 1 kid right."""
    return BinarySearchTree([2, 3])


@pytest.fixture
def imbalanced_left_tree():
    """Init imbalanced tree favoring left side."""
    return BinarySearchTree((7, 6, 5, 4, 3))


@pytest.fixture
def imbalanced_right_tree():
    """Init imbalanced tree favoring right side."""
    return BinarySearchTree((3, 4, 5, 6, 7))


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


def test_insert_depth(tree_init_three_nodes_left):
    """Test insert."""
    tree_init_three_nodes_left.delete(7)
    assert tree_init_three_nodes_left._max_depth is 3


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


def test_del_no_val(tree_init_list_longer_list):
    """Value error raised when delete called on value not in tree."""
    assert tree_init_list_longer_list.delete(10000) is None


def test_del_root_no_kids(tree_init_one_node):
    """Test del root when root has zero kids."""
    assert tree_init_one_node._root._data == 3
    tree_init_one_node.delete(3)
    assert tree_init_one_node._root is None


def test_del_node_left_kid(tree_init_three_nodes_left):
    """Test delete on node with one left child."""
    tree_init_three_nodes_left.delete(6)
    assert tree_init_three_nodes_left._root._data == 4
    assert tree_init_three_nodes_left._root._rkid._data == 5
    assert tree_init_three_nodes_left.depth() == 2
    assert tree_init_three_nodes_left._max_depth == 2


def test_del_root_one_kid_right(tree_init_one_node_right):
    """Test del root when root has one right kids."""
    assert tree_init_one_node_right._root._rkid._data == 3
    assert tree_init_one_node_right._root._parent is None
    assert tree_init_one_node_right._root._rkid._parent._data == 2
    tree_init_one_node_right.delete(2)
    assert tree_init_one_node_right._root._rkid is None
    assert tree_init_one_node_right._root._data == 3
    assert tree_init_one_node_right._root._parent is None


def test_del_root_one_kid_left(tree_init_one_node_left):
    """Test del root when root has one left kids."""
    assert tree_init_one_node_left._root._lkid._data == 3
    tree_init_one_node_left.delete(4)
    assert tree_init_one_node_left._root._lkid is None
    assert tree_init_one_node_left._root._data == 3
    assert tree_init_one_node_left._root._parent is None


def test_del_left_node_check_parent(tree_init_list_longer_list):
    """Test to check if we reasigned parent."""
    tree_init_list_longer_list.delete(2)
    assert tree_init_list_longer_list.search(3)._parent._data == 4
    tree_init_list_longer_list.delete(6)
    assert tree_init_list_longer_list.search(7)._parent._data == 4


def test_del_2kids_node_check_parent(tree_init_list_shorter_list):
    """Test to check if we reasigned parent."""
    tree_init_list_shorter_list.delete(3)
    assert tree_init_list_shorter_list.search(1)._parent._data == 4
    tree_init_list_shorter_list.delete(6)
    assert tree_init_list_shorter_list.search(7)._parent._data == 4


def test_del_node_one_kid_right(tree_init_one_node_right):
    """Test del node when root has one right kids."""
    assert tree_init_one_node_right._root._rkid._data == 3
    tree_init_one_node_right.delete(3)
    assert tree_init_one_node_right._root._rkid is None
    assert tree_init_one_node_right._root._data == 2


def test_del_node_one_kid_left(tree_init_one_node_left):
    """Test del node when root has one left kids."""
    assert tree_init_one_node_left._root._lkid._data == 3
    tree_init_one_node_left.delete(3)
    assert tree_init_one_node_left._root._lkid is None
    assert tree_init_one_node_left._root._data == 4


def test_del_root_two_kids(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(4)
    assert tree_init_list.size() is 7
    tree_init_list.delete(4)
    assert tree_init_list.size() is 6
    assert tree_init_list.contains(4) is False
    assert tree_init_list._root._data == 5
    assert tree_init_list._root._rkid._parent._data == 5
    assert tree_init_list._root._lkid._data == 2
    assert tree_init_list._root._rkid._data == 6
    assert tree_init_list._root._rkid._lkid is None
    assert tree_init_list.contains(7)
    tree_init_list.delete(7)
    assert tree_init_list.size() is 5
    assert tree_init_list.contains(7) is False
    assert tree_init_list.contains(6)
    tree_init_list.delete(6)
    assert tree_init_list.contains(6) is False


def test_del_left_node_two_kids(tree_init_list):
    """Test del node when has two  kids."""
    assert tree_init_list.contains(2)
    assert tree_init_list._root._data == 4
    assert tree_init_list.size() is 7
    tree_init_list.delete(2)
    assert tree_init_list.size() is 6
    assert tree_init_list.contains(2) is False
    assert tree_init_list._root._data == 4
    assert tree_init_list._root._lkid._data == 3
    assert tree_init_list._root._lkid._lkid._data == 1


def test_del_right_node_two_kids(tree_init_list):
    """Test del node when root has one right kids."""
    assert tree_init_list.contains(6)
    assert tree_init_list._root._data == 4
    assert tree_init_list.size() is 7
    tree_init_list.delete(6)
    assert tree_init_list.size() is 6
    assert tree_init_list.contains(6) is False
    assert tree_init_list._root._data == 4
    assert tree_init_list._root._rkid._data == 7
    assert tree_init_list._root._rkid._rkid is None


def test_del_right_branch(tree_init_list):
    """Test del on branch node right."""
    assert tree_init_list.contains(1)
    assert tree_init_list._root._data == 4
    tree_init_list.delete(1)
    assert tree_init_list.contains(1) is False
    assert tree_init_list.contains(2)
    assert tree_init_list.contains(3)
    assert tree_init_list._root._lkid._lkid is None


def test_del_left_branch(tree_init_list):
    """Test del on branch node left."""
    assert tree_init_list.contains(5)
    assert tree_init_list._root._data == 4
    tree_init_list.delete(5)
    assert tree_init_list.contains(5) is False
    assert tree_init_list.contains(6)
    assert tree_init_list.contains(7)
    assert tree_init_list._root._rkid._lkid is None


def test_del_rebalance(tree_init_list):
    """Test rebalance after delete."""
    assert tree_init_list._rbal == 3
    assert tree_init_list._lbal == 3
    assert tree_init_list._max_depth == 3
    tree_init_list.delete(4)
    assert tree_init_list._rbal == 3
    assert tree_init_list._lbal == 3
    assert tree_init_list._max_depth == 3
    tree_init_list.delete(7)
    assert tree_init_list._rbal == 2
    assert tree_init_list._lbal == 3
    assert tree_init_list._max_depth == 3
    tree_init_list.delete(6)
    assert tree_init_list._rbal == 1
    assert tree_init_list._lbal == 3
    assert tree_init_list._max_depth == 3
    tree_init_list.delete(1)
    tree_init_list.delete(3)
    assert tree_init_list._rbal == 1
    assert tree_init_list._lbal == 2
    assert tree_init_list._max_depth == 2
    tree_init_list.delete(2)
    assert tree_init_list._rbal == 1
    assert tree_init_list._lbal == 1
    assert tree_init_list._max_depth == 1


def test_del_rebalance_right(tree_init_three_nodes_right):
    """Test max depth on right-imbalanced tree."""
    tree_init_three_nodes_right.delete(6)
    assert tree_init_three_nodes_right._max_depth is 2
