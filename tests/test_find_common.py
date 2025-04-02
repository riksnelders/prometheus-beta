import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test basic functionality of finding common elements"""
    assert set(find_common([1, 2, 3], [3, 4, 5])) == {3}
    assert set(find_common(['a', 'b', 'c'], ['b', 'c', 'd'])) == {'b', 'c'}

def test_find_common_empty_lists():
    """Test behavior with empty lists"""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test lists with no common elements"""
    assert find_common([1, 2], [3, 4]) == []

def test_find_common_duplicate_elements():
    """Test lists with duplicate elements"""
    assert set(find_common([1, 1, 2, 2], [2, 2, 3, 3])) == {2}

def test_find_common_different_types():
    """Test lists with mixed types"""
    assert set(find_common([1, 'a', 2], [2, 'a', 3])) == {2, 'a'}

def test_find_common_case_sensitivity():
    """Test case sensitivity for strings"""
    assert find_common(['A', 'b'], ['a', 'B']) == []

def test_find_common_hashable_elements():
    """Test lists with hashable elements"""
    assert set(find_common([(1,2), (3,4)], [(1,2), (5,6)])) == {(1,2)}