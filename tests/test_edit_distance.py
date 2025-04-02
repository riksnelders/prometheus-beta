import pytest
from src.edit_distance import compute_edit_distance

def test_same_strings():
    """Test when both strings are identical"""
    assert compute_edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test with empty strings"""
    assert compute_edit_distance("", "") == 0
    assert compute_edit_distance("hello", "") == 5
    assert compute_edit_distance("", "world") == 5

def test_simple_edits():
    """Test basic edit distance scenarios"""
    assert compute_edit_distance("kitten", "sitting") == 3
    assert compute_edit_distance("sunday", "saturday") == 3

def test_different_length_strings():
    """Test strings of different lengths"""
    assert compute_edit_distance("abc", "abcd") == 1
    assert compute_edit_distance("abcd", "abc") == 1

def test_completely_different_strings():
    """Test strings with no common characters"""
    assert compute_edit_distance("hello", "world") == 4

def test_case_sensitivity():
    """Test case-sensitive comparison"""
    assert compute_edit_distance("Hello", "hello") == 1

def test_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compute_edit_distance(123, "hello")
    with pytest.raises(TypeError):
        compute_edit_distance("hello", ["world"])
    with pytest.raises(TypeError):
        compute_edit_distance(None, None)