"""Tests for Python implementation of a radix sort."""
import pytest
from radix_sort import radix_sort as sort
from radix_sort import _verify_input, _get_digit
from random import randint


def test_non_list_tuple_string():
    """Test string input raises type error."""
    with pytest.raises(TypeError):
        sort('asqwpoeriuasdlqwer')


def test_non_list_tuple_dict():
    """Test string input raises type error."""
    with pytest.raises(TypeError):
        sort({1: 'cake', 2: 'pie'})


def test_invalid_items_string():
    """Test valid input type with invalid item raises type error."""
    with pytest.raises(TypeError):
        sort([4, 10, 'hello', 15])


def test_invalid_items_list():
    """Test valid input type with invalid item raises type error."""
    with pytest.raises(TypeError):
        sort([4, 10, [1, 2, 3], 15])


def test_invalid_items_negative_value():
    """Test valid input type with invalid item raises type error."""
    with pytest.raises(ValueError):
        sort([4, 10, -100, 15])


def test_invalid_item_string():
    """Test one-item list with invalid item raises type error."""
    with pytest.raises(TypeError):
        sort(['a'])


def test_one_item_list():
    """Test one-item list sorts properly."""
    assert sort([1]) == [1]


def test_short_list_with_similar_starting_number():
    """Test a shorter list with similar starting numbers."""
    assert sort([1123412, 104, 11, 150, 1203, 1]) == [1, 11, 104, 150, 1203, 1123412]


def test_short_list_with_tuple_input():
    """Test a shorter list with similar starting numbers."""
    assert sort((1123412, 104, 11, 150, 1203, 1)) == [1, 11, 104, 150, 1203, 1123412]


def test_longer_list_random_values():
    """Test longer list against result of sorted method."""
    input_list = [randint(0, 1000) for x in range(100)]
    assert sort(input_list) == sorted(input_list)


def test_longer_list_random_values_duplicates():
    """Test longer list with duplicates against result of sorted method."""
    input_list = [randint(0, 5) for x in range(100)]
    assert sort(input_list) == sorted(input_list)


def test_validation_method_valid():
    """Validation method returns None on valid input."""
    assert _verify_input(1) is None


def test_validation_method_invalid():
    """Validation method raises error on invalid input."""
    with pytest.raises(TypeError):
        _verify_input('greetings')


def test_validation_method_invalid_negative():
    """Validation method raises error on invalid input."""
    with pytest.raises(ValueError):
        _verify_input(-2)


def test_get_digit_longer_number():
    """Test get digit returns proper value."""
    assert _get_digit(13450, 2) == 4


def test_get_digit_shorter_number():
    """Test get digit returns proper value."""
    assert _get_digit(50, 0) == 0


def test_get_digit_returns_zero():
    """Test get digit returns 0 when no values in place."""
    assert _get_digit(50, 2) == 0
