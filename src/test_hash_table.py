"""Test hash init_hash_ten."""

import pytest
from hash_table import HashTable
from hash_bst import BinarySearchTree


@pytest.fixture
def init_hash_ten():
    """Build hash table with 10 bins."""
    return HashTable(10)


@pytest.fixture
def init_hash_with_custom_function():
    """Return hash table with naive hash."""
    def naive_hash(key):
        """Build hash based on additive values."""
        base = 0
        for char in key:
            base += ord(char)
            base -= 1
        return base
    return HashTable(10, naive_hash)


@pytest.fixture
def init_hash_words():
    """Fixture for 250k word test."""
    def naive_hash(key):
        """Build hash based on additive values."""
        base = 0
        for char in key:
            base += ord(char)
            base -= 1
        return base

    word_hash = HashTable(36, naive_hash)
    word_file = open('/usr/share/dict/words', 'r')
    word_text = word_file.read()
    word_file.close()
    word_text = word_text.split('\n')
    for i in range(len(word_text)):
        word_hash.set(word_text[i], i)
    return word_hash


def test_get_letter_value(init_hash_ten):
    """Test get letter value helper."""
    assert init_hash_ten._get_letter_value('0') == 1
    assert init_hash_ten._get_letter_value('a') == 43
    assert init_hash_ten._get_letter_value('A') == 11
    assert init_hash_ten._get_letter_value('B') == 12
    assert init_hash_ten._get_letter_value('Z') == 36


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
    """Test length of bins built for 10."""
    bins = init_hash_ten._build_bins(10)
    assert len(bins) == 10


def test_build_bins_twenty(init_hash_ten):
    """Test length of bins built for 20."""
    bins = init_hash_ten._build_bins(20)
    assert len(bins) == 20


def test_hash_custom(init_hash_with_custom_function):
    """Test non-default hash function."""
    assert init_hash_with_custom_function._hash('A') == 64


def test_hash_default(init_hash_ten):
    """Test default hash function values."""
    assert init_hash_ten._hash('01') == 10
    assert init_hash_ten._hash('10') == 12
    assert init_hash_ten._hash('A') == 10
    assert init_hash_ten._hash('0') == 0
    assert init_hash_ten._hash('a') == 42
    assert init_hash_ten._hash('B') == 11
    assert init_hash_ten._hash('Z') == 35


def test_hash_error_int(init_hash_ten):
    """Test hash function with invalid int input."""
    with pytest.raises(TypeError):
        init_hash_ten._hash(1)


def test_hash_error_float(init_hash_ten):
    """Test hash function with invalid float input."""
    with pytest.raises(TypeError):
        init_hash_ten._hash(1.0)


def test_hash_error_list(init_hash_ten):
    """Test hash function with invalid list input."""
    with pytest.raises(TypeError):
        init_hash_ten._hash(['a'])


def test_init_error_size_str():
    """Test hash table init with invalid size - string."""
    with pytest.raises(TypeError):
        HashTable('a')


def test_init_error_size_float():
    """Test hash table init with invalid size input - float."""
    with pytest.raises(TypeError):
        HashTable(10.6)


def test_init_error_size_list():
    """Test hash table init with invalid size input - list."""
    with pytest.raises(TypeError):
        HashTable([10])


def test_init_error_size_too_small():
    """Test hash table init with too small size."""
    with pytest.raises(ValueError):
        HashTable(0)


def test_init_error_size_too_small_neg():
    """Test hash table init with too small size - negative number."""
    with pytest.raises(ValueError):
        HashTable(-1)


def test_init_bins_bst(init_hash_ten):
    """Test bins are BinarySearchTree instances."""
    for container in init_hash_ten._bins:
        assert type(container) == BinarySearchTree


def test_init_hash_custom_function_correct(init_hash_with_custom_function):
    """Test custom hash function method produces correct hash value."""
    assert init_hash_with_custom_function._hash_function('A') == 64


def test_init_hash_default_function_correct(init_hash_ten):
    """Test default hash function method produces correct hash value."""
    assert init_hash_ten._hash_function('01') == 10
    assert init_hash_ten._hash_function('10') == 12
    assert init_hash_ten._hash_function('A') == 10
    assert init_hash_ten._hash_function('0') == 0
    assert init_hash_ten._hash_function('a') == 42
    assert init_hash_ten._hash_function('B') == 11
    assert init_hash_ten._hash_function('Z') == 35


def test_root_empty_bin(init_hash_ten):
    """Test empty bin has no data at root."""
    assert init_hash_ten._bins[0]._root is None


def test_set_empty_bin(init_hash_ten):
    """Test setting data in an empty bin."""
    init_hash_ten.set('A', 'a big cake')
    assert init_hash_ten._bins[0]._root._entries[0][0] == 'A'
    assert init_hash_ten._bins[0]._root._entries[0][1] == 'a big cake'


def test_set_populated_bin(init_hash_ten):
    """Test setting data in a populated table."""
    init_hash_ten.set('A', 'a big cake')
    init_hash_ten.set('0', 'a bigger cake')
    assert init_hash_ten._bins[0]._root._entries[0][0] == 'A'
    assert init_hash_ten._bins[0]._root._entries[0][1] == 'a big cake'
    assert init_hash_ten._bins[0]._root._lkid._entries[0][0] == '0'
    assert init_hash_ten._bins[0]._root._lkid._entries[0][1] == 'a bigger cake'


def test_set_dupe_key_bin(init_hash_ten):
    """Test setting duplicate key produces KeyError."""
    init_hash_ten.set('A', 'a big cake')
    with pytest.raises(KeyError):
        init_hash_ten.set('A', 'a bigger cake')


def test_node_collision(init_hash_ten):
    """Test node collision populates entries list."""
    init_hash_ten.set('A', 'a big cake')
    init_hash_ten._bins[0].insert(10, ('key', 'value'))
    assert init_hash_ten._bins[0]._root._entries[0][0] == 'A'
    assert init_hash_ten._bins[0]._root._entries[0][1] == 'a big cake'
    assert init_hash_ten._bins[0]._root._entries[1][0] == 'key'
    assert init_hash_ten._bins[0]._root._entries[1][1] == 'value'


def test_get_inserted_pair(init_hash_ten):
    """Test get method."""
    init_hash_ten.set('hello', 10000)
    assert init_hash_ten.get('hello') == 10000


def test_get_multiple_inserts(init_hash_ten):
    """Test get method on multiple inserts."""
    init_hash_ten.set('hello', 10000)
    assert init_hash_ten.get('hello') == 10000
    init_hash_ten.set('A', 'a big cake')
    assert init_hash_ten.get('A') == 'a big cake'


def test_get_nonexistent_key(init_hash_ten):
    """Test get method for non-existent key produces KeyError."""
    init_hash_ten.set('hello', 10000)
    with pytest.raises(KeyError):
        init_hash_ten.get('hi')


def test_word_dict(init_hash_words):
    """Test hashing function on large data set of words."""
    distr = []
    for container in init_hash_words._bins:
        distr.append(container.size())
    assert len(distr) == 36
    assert distr == [59, 57, 57, 59, 59, 58, 60, 62, 58, 62, 58, 60, 60, 59, 57, 61, 56, 61, 56, 59, 54, 59, 57, 58, 59, 61, 56, 60, 60, 56, 60, 60, 58, 57, 60, 61]
    assert init_hash_words.get('abacination') == 24
    assert init_hash_words.get('woodcrafty') == 233195
    assert init_hash_words.get('zoopsia') == 235631
