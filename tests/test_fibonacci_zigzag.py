import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_basic():
    """Test basic functionality for different input sizes"""
    assert fibonacci_zigzag(1) == [1]
    assert fibonacci_zigzag(2) == [1, 1]
    assert fibonacci_zigzag(3) == [1, 1, 2]
    assert fibonacci_zigzag(5) == [1, 1, 2, 3, 5]
    assert fibonacci_zigzag(7) == [1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_zigzag_large_input():
    """Test for a larger input to ensure correct sequence generation"""
    result = fibonacci_zigzag(10)
    assert len(result) == 10
    assert result == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fibonacci_zigzag_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("not a number")