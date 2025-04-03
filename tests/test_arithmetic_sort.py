import pytest
from src.arithmetic_sort import arithmetic_sort

def test_basic_sorting():
    """Test sorting a basic list of positive integers"""
    input_list = [5, 2, 9, 1, 7]
    assert arithmetic_sort(input_list) == [1, 2, 5, 7, 9]

def test_already_sorted():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert arithmetic_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    assert arithmetic_sort(input_list) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_empty_list():
    """Test sorting an empty list"""
    assert arithmetic_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert arithmetic_sort([42]) == [42]

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 7, -1]
    assert arithmetic_sort(input_list) == [-5, -2, -1, 0, 3, 7]

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        arithmetic_sort("not a list")

def test_invalid_element_type():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError):
        arithmetic_sort([1, 2, "3", 4])