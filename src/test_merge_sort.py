"""Tests for Python implementation of a merge sort."""
import pytest
from merge_sort import merge_sort as sort
from merge_sort import list_split, sort_lists
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


def test_list_split():
    """Test helper function list split returns sorted list."""
    input_list = [randint(0, 1000) for x in range(100)]
    assert list_split(input_list) == sorted(input_list)


def test_list_split_valid():
    """Test helper function list split raises error on short list."""
    with pytest.raises(TypeError):
        list_split(['a'])


def test_sort_list():
    """Test helper function sort list on two valid lists."""
    list1 = [5, 20]
    list2 = [-100, 14]
    assert sort_lists(list1, list2) == [-100, 5, 14, 20]
