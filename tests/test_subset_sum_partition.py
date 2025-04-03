import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_basic_cases():
    # Simple cases with known results
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) == 1
    assert count_equal_sum_partitions([1, 1, 1, 1]) == 3

def test_impossible_partitions():
    # Cases where equal sum partition is impossible
    assert count_equal_sum_partitions([1, 2, 3]) == 0
    assert count_equal_sum_partitions([1, 3, 5]) == 0

def test_single_element():
    # Single element can't be split into equal sum subsets
    assert count_equal_sum_partitions([1]) == 0
    assert count_equal_sum_partitions([10]) == 0

def test_even_sum_possible():
    # Test cases where partitioning is possible
    assert count_equal_sum_partitions([1, 5, 11, 5]) == 1
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) == 1

def test_error_cases():
    # Test error handling
    with pytest.raises(ValueError):
        count_equal_sum_partitions([])
    
    with pytest.raises(ValueError):
        count_equal_sum_partitions(None)

def test_zero_sum():
    # Test with zero values
    assert count_equal_sum_partitions([0, 0, 0, 0]) == 1

def test_mixed_numbers():
    # Test with mixed positive and negative numbers
    assert count_equal_sum_partitions([1, -1, 2, -2]) == 1