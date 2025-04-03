import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_sequence():
    """Test a typical sequence with multiple increasing subsequences"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60, 80]

def test_all_equal_elements():
    """Test a sequence with all equal elements"""
    arr = [7, 7, 7, 7, 7, 7, 7]
    result = find_longest_increasing_subsequence(arr)
    assert result == [7]

def test_already_sorted_sequence():
    """Test a sequence that is already sorted"""
    arr = [1, 2, 3, 4, 5, 6, 7]
    result = find_longest_increasing_subsequence(arr)
    assert result == arr

def test_reverse_sorted_sequence():
    """Test a sequence sorted in descending order"""
    arr = [7, 6, 5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [7]

def test_empty_sequence():
    """Test an empty sequence"""
    arr = []
    result = find_longest_increasing_subsequence(arr)
    assert result == []

def test_single_element_sequence():
    """Test a sequence with a single element"""
    arr = [42]
    result = find_longest_increasing_subsequence(arr)
    assert result == [42]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test that a ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers or floats"):
        find_longest_increasing_subsequence([1, 2, "3", 4])

def test_mixed_sign_sequence():
    """Test a sequence with mixed positive and negative numbers"""
    arr = [-7, 10, -2, 3, 8, 1, 9]
    result = find_longest_increasing_subsequence(arr)
    assert result == [-7, -2, 3, 8, 9]

def test_floating_point_sequence():
    """Test a sequence with floating point numbers"""
    arr = [1.1, 2.2, 1.5, 3.3, 2.7, 4.4]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1.1, 2.2, 3.3, 4.4]