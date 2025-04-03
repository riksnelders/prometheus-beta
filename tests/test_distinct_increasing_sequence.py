import pytest
from src.distinct_increasing_sequence import is_valid_increasing_sequence

def test_valid_increasing_sequences():
    """Test various valid increasing sequences"""
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True
    assert is_valid_increasing_sequence([-5, -3, 0, 2, 4]) == True

def test_invalid_increasing_sequences():
    """Test various invalid increasing sequences"""
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False  # Decreasing
    assert is_valid_increasing_sequence([1, 1, 2, 3, 4]) == False  # Repeated elements
    assert is_valid_increasing_sequence([1, 3, 2, 4, 5]) == False  # Not strictly increasing
    assert is_valid_increasing_sequence([1, 2, 2, 3, 4]) == False  # Repeated elements

def test_edge_cases():
    """Test edge cases"""
    assert is_valid_increasing_sequence([]) == True  # Empty list
    assert is_valid_increasing_sequence([42]) == True  # Single element list
    assert is_valid_increasing_sequence([0]) == True  # Single zero
    assert is_valid_increasing_sequence([-1]) == True  # Single negative number

def test_error_cases():
    """Test error handling"""
    with pytest.raises(TypeError):
        is_valid_increasing_sequence("not a list")
    
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(123)
    
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(None)

def test_non_integer_inputs():
    """Test lists with non-integer elements"""
    assert is_valid_increasing_sequence([1.0, 2.0, 3.0]) == False
    assert is_valid_increasing_sequence(['1', '2', '3']) == False
    assert is_valid_increasing_sequence([True, False]) == False