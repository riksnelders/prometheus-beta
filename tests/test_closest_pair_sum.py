import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_closest_pair():
    """Test finding closest pair in a simple scenario"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    assert find_closest_pair_sum(arr, target) == (2, 5)

def test_multiple_closest_pairs():
    """Test when multiple pairs have same closeness"""
    arr = [1, 2, 3, 4, 5]
    target = 6
    # Should return first occurrence of pairs with same closeness
    assert find_closest_pair_sum(arr, target) == (1, 5)

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, -2, 3, 4, 5]
    target = 2
    assert find_closest_pair_sum(arr, target) == (-2, 4)

def test_identical_numbers():
    """Test with array containing identical numbers"""
    arr = [2, 2, 2, 2]
    target = 4
    assert find_closest_pair_sum(arr, target) == (2, 2)

def test_large_numbers():
    """Test with large numbers"""
    arr = [1000, 2000, 3000, 4000, 5000]
    target = 6500
    assert find_closest_pair_sum(arr, target) == (3000, 3500)

def test_error_on_small_array():
    """Test error raised when array is too small"""
    with pytest.raises(ValueError):
        find_closest_pair_sum([1], 5)

def test_error_on_empty_array():
    """Test error raised on empty array"""
    with pytest.raises(ValueError):
        find_closest_pair_sum([], 5)