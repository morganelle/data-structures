"""Tests for Python implementation of a bubble sort sort."""
import pytest
from insertion_sort import insertion_sort as sort
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


def test_longer_list_random_values():
    """Test longer list against result of sorted method."""
    input_list = [randint(0, 1000) for x in range(100)]
    assert sort(input_list) == sorted(input_list)


def test_longer_list_random_values_negatives():
    """Test longer list of negative and positive values against result of sorted method."""
    input_list = [randint(-1000, 1000) for x in range(100)]
    assert sort(input_list) == sorted(input_list)


def test_longer_list_random_values_duplicates():
    """Test longer list with duplicates against result of sorted method."""
    input_list = [randint(0, 5) for x in range(100)]
    assert sort(input_list) == sorted(input_list)

