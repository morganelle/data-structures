"""Test hash init_hash_ten."""

import pytest
from hash_table import HashTable
from hash_bst import BinarySearchTree


@pytest.fixture
def init_hash_ten():
    """."""
    return HashTable(10)


@pytest.fixture
def init_hash_with_custom_function():
    """."""
    def naive_hash(key):
        """Build hash based on additive values."""
        base = 0
        for char in key:
            base += ord(char)
            base -= 1
        return base
    return HashTable(10, naive_hash)


# @pytest.fixture
# def init_hash_words():
#     """."""
#     word_hash = HashTable(36)
#     word_file = open('/usr/share/dict/words')
#     word_file = word_file.read()
#     word_file = str(word_file).strip()
#     word_text = word_file.split('\n')
#     for i in range(len(word_text)):
#         word_hash.set(word_text[i], i)
#     word_file.close()
#     return word_hash


def test_get_letter_value():
    """Test get letter value helper."""
    assert HashTable._get_letter_value(None, '0') == 1
    assert HashTable._get_letter_value(None, 'a') == 43
    assert HashTable._get_letter_value(None, 'A') == 11
    assert HashTable._get_letter_value(None, 'B') == 12
    assert HashTable._get_letter_value(None, 'Z') == 36


def test_prime_hash(init_hash_ten):
    """Test output of advanced hash method."""
    assert init_hash_ten._prime_hash('01') == 10
    assert init_hash_ten._prime_hash('10') == 12
    assert init_hash_ten._prime_hash('A') == 10
    assert init_hash_ten._prime_hash('0') == 0
    assert init_hash_ten._prime_hash('a') == 42
    assert init_hash_ten._prime_hash('B') == 11
    assert init_hash_ten._prime_hash('Z') == 35


def test_naive_hash(init_hash_ten):
    """Test output of naive hash method."""
    assert init_hash_ten._naive_hash('01') == 1
    assert init_hash_ten._naive_hash('10') == 1
    assert init_hash_ten._naive_hash('A') == 10
    assert init_hash_ten._naive_hash('0') == 0
    assert init_hash_ten._naive_hash('a') == 42
    assert init_hash_ten._naive_hash('B') == 11
    assert init_hash_ten._naive_hash('Z') == 35


def test_build_bins_ten(init_hash_ten):
    """."""
    bins = init_hash_ten._build_bins(10)
    assert len(bins) == 10


def test_build_bins_twenty(init_hash_ten):
    """."""
    bins = init_hash_ten._build_bins(20)
    assert len(bins) == 20


def test_hash_custom(init_hash_with_custom_function):
    """."""
    assert init_hash_with_custom_function._hash('A') == 64


def test_hash_default(init_hash_ten):
    """."""
    assert init_hash_ten._hash('01') == 10
    assert init_hash_ten._hash('10') == 12
    assert init_hash_ten._hash('A') == 10
    assert init_hash_ten._hash('0') == 0
    assert init_hash_ten._hash('a') == 42
    assert init_hash_ten._hash('B') == 11
    assert init_hash_ten._hash('Z') == 35


def test_hash_error_int(init_hash_ten):
    """."""
    with pytest.raises(TypeError):
        init_hash_ten._hash(1)


def test_hash_error_float(init_hash_ten):
    """."""
    with pytest.raises(TypeError):
        init_hash_ten._hash(1.0)


def test_hash_error_list(init_hash_ten):
    """."""
    with pytest.raises(TypeError):
        init_hash_ten._hash(['a'])


def test_init_error_size_str():
    """."""
    with pytest.raises(TypeError):
        HashTable('a')


def test_init_error_size_float():
    """."""
    with pytest.raises(TypeError):
        HashTable(10.6)


def test_init_error_size_list():
    """."""
    with pytest.raises(TypeError):
        HashTable([10])


def test_init_error_size_too_small():
    """."""
    with pytest.raises(ValueError):
        HashTable(0)


def test_init_error_size_too_small_neg():
    """."""
    with pytest.raises(ValueError):
        HashTable(-1)


def test_init_bins_built(init_hash_ten):
    """."""
    assert len(init_hash_ten._bins) == 10
    assert init_hash_ten._size == 10


def test_init_bins_bst(init_hash_ten):
    """."""
    for container in init_hash_ten._bins:
        assert type(container) == BinarySearchTree


def test_init_hash_custom_function_correct(init_hash_with_custom_function):
    """."""
    assert init_hash_with_custom_function._hash_function('A') == 64


def test_init_hash_default_function_correct(init_hash_ten):
    """."""
    assert init_hash_ten._hash_function('01') == 10
    assert init_hash_ten._hash_function('10') == 12
    assert init_hash_ten._hash_function('A') == 10
    assert init_hash_ten._hash_function('0') == 0
    assert init_hash_ten._hash_function('a') == 42
    assert init_hash_ten._hash_function('B') == 11
    assert init_hash_ten._hash_function('Z') == 35


def test_root_empty_bin(init_hash_ten):
    """."""
    assert init_hash_ten._bins[0]._root is None


def test_set_empty_bin(init_hash_ten):
    """."""
    init_hash_ten.set('A', 'a big cake')
    assert init_hash_ten._bins[0]._root._entries[0][0] == 'A'
    assert init_hash_ten._bins[0]._root._entries[0][1] == 'a big cake'


def test_set_populated_bin(init_hash_ten):
    """."""
    init_hash_ten.set('A', 'a big cake')
    init_hash_ten.set('0', 'a bigger cake')
    assert init_hash_ten._bins[0]._root._entries[0][0] == 'A'
    assert init_hash_ten._bins[0]._root._entries[0][1] == 'a big cake'
    assert init_hash_ten._bins[0]._root._lkid._entries[0][0] == '0'
    assert init_hash_ten._bins[0]._root._lkid._entries[0][1] == 'a bigger cake'


def test_set_dupe_key_bin(init_hash_ten):
    """."""
    init_hash_ten.set('A', 'a big cake')
    with pytest.raises(KeyError):
        init_hash_ten.set('A', 'a bigger cake')


def test_node_collision(init_hash_ten):
    """."""
    init_hash_ten.set('A', 'a big cake')
    init_hash_ten._bins[0].insert(10, ('key', 'value'))
    assert init_hash_ten._bins[0]._root._entries[0][0] == 'A'
    assert init_hash_ten._bins[0]._root._entries[0][1] == 'a big cake'
    assert init_hash_ten._bins[0]._root._entries[1][0] == 'key'
    assert init_hash_ten._bins[0]._root._entries[1][1] == 'value'


def test_get_inserted_pair(init_hash_ten):
    """."""
    init_hash_ten.set('hello', 10000)
    assert init_hash_ten.get('hello') == 10000


def test_get_multiple_inserts(init_hash_ten):
    """."""
    init_hash_ten.set('hello', 10000)
    assert init_hash_ten.get('hello') == 10000
    init_hash_ten.set('A', 'a big cake')
    assert init_hash_ten.get('A') == 'a big cake'


def test_get_nonexistent_key(init_hash_ten):
    """."""
    init_hash_ten.set('hello', 10000)
    with pytest.raises(KeyError):
        init_hash_ten.get('hi')


# def test_word_dict(init_hash_words):
#     """."""
#     distr = []
#     # print('here')
#     for container in init_hash_words._bins:
#         distr.append(container.size())
#     # print('done')
#     assert len(distr) == 36
#     assert distr == []
