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
    """Init empty tree fixture."""
    return BinarySearchTree([4, 2, 3, 1, 6, 5, 7])


@pytest.fixture
def tree_init_list_shorter_list():
    """Init empty tree fixture."""
    return BinarySearchTree([4, 3, 1, 6, 7])


@pytest.fixture
def tree_init_list_longer_list():
    """Init empty tree fixture."""
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


def test_insert_tuple(empty_tree):
    """Test inserting tuple raises error."""
    with pytest.raises(TypeError):
        empty_tree.insert((9, 'hello'))


def test_insert_dupe(empty_tree):
    """Test insert."""
    empty_tree.insert(2)
    with pytest.raises(ValueError):
        empty_tree.insert(2)


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


def test_breadth_first(tree_init_list):
    """test breadth first."""
    gen = tree_init_list.breadth_first()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 6
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 5
    assert next(gen) is 7


def test_pre_order(tree_init_list):
    """test pre-order first."""
    gen = tree_init_list.pre_order()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 6
    assert next(gen) is 5
    assert next(gen) is 7


def test_in_order(tree_init_list):
    """test pre-order first."""
    gen = tree_init_list.in_order()
    assert next(gen) is 1
    assert next(gen) is 2
    assert next(gen) is 3
    assert next(gen) is 4
    assert next(gen) is 5
    assert next(gen) is 6
    assert next(gen) is 7


def test_post_order(tree_init_list):
    """test pre-order first"""
    gen = tree_init_list.post_order()
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 2
    assert next(gen) is 5
    assert next(gen) is 7
    assert next(gen) is 6
    assert next(gen) is 4


# def test_del_node_no_kids():
#     pass


# def test_del_node_one_kid():
#     pass


# def test_del_node_two_kids():
#     pass


def test_del_root_no_kids(tree_init_one_node):
    """."""
    assert tree_init_one_node._root._data == 3
    tree_init_one_node.delete(3)
    assert tree_init_one_node._root is None


def test_del_root_one_kid_right(tree_init_one_node_right):
    """."""
    assert tree_init_one_node_right._root._rkid._data == 3
    assert tree_init_one_node_right._root._parent is None
    assert tree_init_one_node_right._root._rkid._parent._data == 2
    tree_init_one_node_right.delete(2)
    assert tree_init_one_node_right._root._rkid is None
    assert tree_init_one_node_right._root._data == 3
    assert tree_init_one_node_right._root._parent is None


def test_del_root_one_kid_left(tree_init_one_node_left):
    """."""
    assert tree_init_one_node_left._root._lkid._data == 3
    tree_init_one_node_left.delete(4)
    assert tree_init_one_node_left._root._lkid is None
    assert tree_init_one_node_left._root._data == 3
    assert tree_init_one_node_left._root._parent is None


def test_del_left_node_check_parent(tree_init_list_longer_list):
    """."""
    tree_init_list_longer_list.delete(2)
    assert tree_init_list_longer_list.search(3)._parent._data == 4
    tree_init_list_longer_list.delete(6)
    assert tree_init_list_longer_list.search(7)._parent._data == 4


def test_del_2kids_node_check_parent(tree_init_list_shorter_list):
    """."""
    tree_init_list_shorter_list.delete(3)
    assert tree_init_list_shorter_list.search(1)._parent._data == 4
    tree_init_list_shorter_list.delete(6)
    assert tree_init_list_shorter_list.search(7)._parent._data == 4


def test_del_node_one_kid_right(tree_init_one_node_right):
    """."""
    assert tree_init_one_node_right._root._rkid._data == 3
    tree_init_one_node_right.delete(3)
    assert tree_init_one_node_right._root._rkid is None
    assert tree_init_one_node_right._root._data == 2


def test_del_node_one_kid_left(tree_init_one_node_left):
    """."""
    assert tree_init_one_node_left._root._lkid._data == 3
    tree_init_one_node_left.delete(3)
    assert tree_init_one_node_left._root._lkid is None
    assert tree_init_one_node_left._root._data == 4


def test_del_root_two_kids(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(4)
    tree_init_list.delete(4)
    assert tree_init_list.contains(4) is False
    assert tree_init_list._root._data == 5
    assert tree_init_list._root._rkid._parent._data == 5
    assert tree_init_list._root._lkid._data == 2
    assert tree_init_list._root._rkid._data == 6
    assert tree_init_list._root._rkid._lkid is None
    assert tree_init_list.contains(7)
    tree_init_list.delete(7)
    assert tree_init_list.contains(7) is False
    assert tree_init_list.contains(6)
    tree_init_list.delete(6)
    # # import pdb; pdb.set_trace()
    assert tree_init_list.contains(6) is False
    # assert tree_init_list.contains(2) is True
    # tree_init_list.delete(2)
    # assert tree_init_list.contains(2) is False
    # assert tree_init_list.contains(1) is True
    # tree_init_list.delete(1)
    # assert tree_init_list.contains(1) is False
    # assert tree_init_list.contains(3) is True
    # tree_init_list.delete(3)
    # assert tree_init_list.contains(3) is False
    # assert tree_init_list.contains(5) is True
    # tree_init_list.delete(5)
    # assert tree_init_list.contains(5) is False


def test_del_left_node_two_kids(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(2)
    assert tree_init_list._root._data == 4
    tree_init_list.delete(2)
    assert tree_init_list.contains(2) is False
    assert tree_init_list._root._data == 4
    assert tree_init_list._root._lkid._data == 3
    assert tree_init_list._root._lkid._lkid._data == 1


def test_del_right_node_two_kids(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(6)
    assert tree_init_list._root._data == 4
    tree_init_list.delete(6)
    assert tree_init_list.contains(6) is False
    assert tree_init_list._root._data == 4
    assert tree_init_list._root._rkid._data == 7
    assert tree_init_list._root._rkid._rkid is None


def test_del_right_branch(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(1)
    assert tree_init_list._root._data == 4
    tree_init_list.delete(1)
    assert tree_init_list.contains(1) is False
    assert tree_init_list.contains(2)
    assert tree_init_list.contains(3)
    assert tree_init_list._root._lkid._lkid is None


def test_del_left_branch(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(5)
    assert tree_init_list._root._data == 4
    tree_init_list.delete(5)
    assert tree_init_list.contains(5) is False
    assert tree_init_list.contains(6)
    assert tree_init_list.contains(7)
    assert tree_init_list._root._rkid._lkid is None
