"""Tests for Python implementation of Trie."""
import pytest
from trie import Trie, Node


@pytest.fixture
def init_empty_trie():
    """Init empty trie."""
    return Trie()


@pytest.fixture
def init_trie_one_word():
    """Init empty trie."""
    new_trie = Trie()
    new_trie.insert('cake')
    return new_trie


@pytest.fixture
def init_trie_three_words_shared_letters():
    """Init empty trie."""
    new_trie = Trie()
    new_trie.insert('be')
    new_trie.insert('bee')
    new_trie.insert('bell')
    return new_trie


@pytest.fixture
def init_jumbo_list():
    """Fixture for 250k word test."""
    word_file = open('/usr/share/dict/words', 'r')
    word_text = word_file.read()
    word_file.close()
    word_text = word_text.split('\n')
    word_text = word_text[:-1]
    return word_text


def test_init_empty_node():
    """Test that node init attributes empty by default."""
    new_node = Node()
    assert new_node._children == []
    assert new_node._data is None
    assert new_node._parent is None


def test_init_node_with_value_and_parent():
    """Test that node init with parent and val works."""
    parent_node = Node('c')
    new_node = Node(parent_node, 'a')
    assert new_node._parent == parent_node
    assert new_node._data == 'a'


def test_init_empty_trie_has_correct_attrs(init_empty_trie):
    """Test an empty trie intance has correct attributes."""
    root = init_empty_trie._root
    assert type(root) == Node
    assert root._data is None
    assert init_empty_trie._size == 0


def test_insert_iterable(init_empty_trie):
    """Check error is raised when iterable inserted."""
    with pytest.raises(TypeError):
        init_empty_trie.insert(['string'])


def test_insert_int(init_empty_trie):
    """Check error is raised when iterable inserted."""
    with pytest.raises(TypeError):
        init_empty_trie.insert(300)


def test_insert_two_words(init_empty_trie):
    """Check error is raised when iterable inserted."""
    with pytest.raises(ValueError):
        init_empty_trie.insert('hi there')


def test_insert_duplicate(init_trie_one_word):
    """Check error is raised when iterable inserted."""
    with pytest.raises(ValueError):
        init_trie_one_word.insert('cake')


def test_insert_empty_trie(init_empty_trie):
    """Test insert method on empty trie."""
    init_empty_trie.insert('hello')
    assert init_empty_trie.contains('hello') is True
    assert init_empty_trie._root._children[0]._data == 'h'


def test_insert_empty_trie_two_words_same_beginning(init_empty_trie):
    """Test insert method on empty trie."""
    init_empty_trie.insert('hello')
    init_empty_trie.insert('help')
    assert init_empty_trie.contains('hello') is True
    assert init_empty_trie.contains('help') is True
    assert init_empty_trie._root._children[0]._data == 'h'
    assert len(init_empty_trie._root._children) == 1


def test_insert_empty_trie_two_words_unique_letters(init_empty_trie):
    """Test insert method on empty trie."""
    init_empty_trie.insert('greetings')
    init_empty_trie.insert('ivory')
    assert init_empty_trie.contains('greetings') is True
    assert init_empty_trie.contains('ivory') is True
    assert init_empty_trie._root._children[0]._data == 'g'
    assert init_empty_trie._root._children[1]._data == 'i'
    assert len(init_empty_trie._root._children) == 2


def test_insert_empty_trie_two_words_shared_letters(init_empty_trie):
    """Test insert method on empty trie."""
    init_empty_trie.insert('morgan')
    init_empty_trie.insert('borgan')
    assert init_empty_trie.contains('morgan') is True
    assert init_empty_trie.contains('borgan') is True
    assert init_empty_trie._root._children[0]._data == 'm'
    assert init_empty_trie._root._children[1]._data == 'b'
    assert init_empty_trie._root._children[0]._children is not init_empty_trie._root._children[1]._children
    assert len(init_empty_trie._root._children) == 2


def test_contains(init_trie_one_word):
    """Check error is raised when iterable inserted."""
    assert init_trie_one_word.contains('cake') is True
    assert init_trie_one_word.contains('ca') is False


def test_contains_invalid_input_int(init_trie_one_word):
    """Check error is raised when iterable inserted."""
    with pytest.raises(TypeError):
        init_trie_one_word.contains(3)


def test_contains_invalid_input_iterable(init_trie_one_word):
    """Check error is raised when iterable inserted."""
    with pytest.raises(TypeError):
        init_trie_one_word.contains(['cake'])


def test_remove_word_empty_trie(init_empty_trie):
    """Test remove on empty trie."""
    with pytest.raises(ValueError):
        init_empty_trie.remove('you')


def test_remove_float_trie(init_trie_one_word):
    """Test remove on empty trie."""
    with pytest.raises(TypeError):
        init_trie_one_word.remove(1.0)


def test_remove_non_existent_word_trie(init_trie_one_word):
    """Test remove on empty trie."""
    with pytest.raises(ValueError):
        init_trie_one_word.remove('you')


def test_remove_words_shared_beginning(init_trie_three_words_shared_letters):
    """Test remove on words with shared beginning letters."""
    init_trie_three_words_shared_letters.remove('be')
    assert init_trie_three_words_shared_letters.contains('be') is False
    init_trie_three_words_shared_letters.remove('bell')
    assert init_trie_three_words_shared_letters.contains('bell') is False
    assert init_trie_three_words_shared_letters.contains('bee') is True


def test_size_trie_before_and_after_remove(init_trie_three_words_shared_letters):
    """Test trie size before and after a removal."""
    assert init_trie_three_words_shared_letters.size() == 3
    init_trie_three_words_shared_letters.remove('bee')
    assert init_trie_three_words_shared_letters.size() == 2


def test_size_trie_before_and_after_insert(init_trie_three_words_shared_letters):
    """Test trie size before and after a removal."""
    assert init_trie_three_words_shared_letters.size() == 3
    init_trie_three_words_shared_letters.insert('happy')
    assert init_trie_three_words_shared_letters.size() == 4


def test_insert_jumbo_list(init_jumbo_list):
    """Test insert on jumbo word list."""
    jumbo_trie = Trie()
    for word in init_jumbo_list:
        jumbo_trie.insert(word)
    assert len(init_jumbo_list) == jumbo_trie.size()
    assert jumbo_trie.contains('apple')


def test_traversal_start_not_string(init_trie_three_words_shared_letters):
    """Test traversal error when start arg is not a string. NOTE: currently returning a generator object."""
    gen = init_trie_three_words_shared_letters.traversal(3)
    with pytest.raises(TypeError):
        next(gen)


def test_traversal_start_empty_string(init_trie_three_words_shared_letters):
    """Test traversal error when start arg is not a string. NOTE: currently returning a generator object."""
    gen = init_trie_three_words_shared_letters.traversal('')
    with pytest.raises(ValueError):
        next(gen)


def test_traversal_start_string_with_space(init_trie_three_words_shared_letters):
    """Test traversal error when start arg is not a string. NOTE: currently returning a generator object."""
    gen = init_trie_three_words_shared_letters.traversal(' ')
    with pytest.raises(ValueError):
        next(gen)


def test_traversal_all_words(init_trie_three_words_shared_letters):
    """Test all words with a shared start are generated."""
    gen = init_trie_three_words_shared_letters.traversal('be')
    assert next(gen) == 'be'
    assert next(gen) == 'bee'
    assert next(gen) == 'bell'


def test_traversal_all_words_with_insert_not_in_gen(init_trie_three_words_shared_letters):
    """Test all words with a shared start are generated."""
    init_trie_three_words_shared_letters.insert('bacon')
    gen = init_trie_three_words_shared_letters.traversal('be')
    assert next(gen) == 'be'
    assert next(gen) == 'bee'
    assert next(gen) == 'bell'


def test_traversal_all_words_with_insert_in_gen(init_trie_three_words_shared_letters):
    """Test all words with a shared start are generated."""
    init_trie_three_words_shared_letters.insert('bacon')
    gen = init_trie_three_words_shared_letters.traversal('b')
    assert next(gen) == 'be'
    assert next(gen) == 'bee'
    assert next(gen) == 'bell'


def test_non_matching_start_raises_stop_iteration(init_trie_three_words_shared_letters):
    """Test non-matching start for traversal."""
    gen = init_trie_three_words_shared_letters.traversal('hi')
    with pytest.raises(ValueError):
        next(gen)
