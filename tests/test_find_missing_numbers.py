import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test finding missing numbers in a simple sequence"""
    arr = [1, 2, 4, 5]
    assert find_missing_numbers(arr) == [3]

def test_find_missing_numbers_larger_range():
    """Test finding multiple missing numbers in a larger range"""
    arr = [1, 2, 4, 6, 7, 9, 10]
    assert find_missing_numbers(arr) == [3, 5, 8]

def test_find_missing_numbers_no_missing():
    """Test scenario where no numbers are missing"""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_negative_numbers():
    """Test finding missing numbers with negative integers"""
    arr = [-3, -1, 0, 2]
    assert find_missing_numbers(arr) == [-2, 1]

def test_find_missing_numbers_unordered():
    """Test that the function works with unordered input"""
    arr = [5, 2, 8, 1, 9]
    assert find_missing_numbers(arr) == [3, 4, 6, 7]

def test_find_missing_numbers_invalid_input_type():
    """Test raising error for non-list input"""
    with pytest.raises(ValueError):
        find_missing_numbers("not a list")

def test_find_missing_numbers_non_integer_elements():
    """Test raising error for non-integer list elements"""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, "3", 4])

def test_find_missing_numbers_empty_list():
    """Test raising error for empty input list"""
    with pytest.raises(TypeError):
        find_missing_numbers([])