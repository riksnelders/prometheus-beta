import pytest
from src.common_element_checker import has_common_element

def test_common_element_basic():
    """Test basic scenario with a common element"""
    assert has_common_element([1, 2, 3], [4, 5, 3]) == True

def test_no_common_element():
    """Test scenario with no common elements"""
    assert has_common_element([1, 2, 3], [4, 5, 6]) == False

def test_empty_arrays():
    """Test with empty arrays"""
    assert has_common_element([], []) == False
    assert has_common_element([1], []) == False
    assert has_common_element([], [1]) == False

def test_single_element_match():
    """Test with single element match"""
    assert has_common_element([1], [1]) == True

def test_different_types():
    """Test with different types of elements"""
    assert has_common_element([1, 'a', True], ['b', 1, 2.0]) == True

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        has_common_element(1, [1, 2, 3])
    
    with pytest.raises(TypeError):
        has_common_element([1, 2, 3], "not a list")

def test_large_arrays():
    """Test with large arrays"""
    large_arr1 = list(range(1000))
    large_arr2 = list(range(500, 1500))
    assert has_common_element(large_arr1, large_arr2) == True

def test_no_match_in_large_arrays():
    """Test with large arrays that don't match"""
    large_arr1 = list(range(1000))
    large_arr2 = list(range(1000, 2000))
    assert has_common_element(large_arr1, large_arr2) == False