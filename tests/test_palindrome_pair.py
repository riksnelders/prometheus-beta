import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from palindrome_pair import palindrome_pair

def test_palindrome_pair_basic_true():
    """Test a basic case where a palindrome pair difference exists."""
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # 3-1 = 2 is a palindrome

def test_palindrome_pair_basic_false():
    """Test a basic case where no palindrome pair difference exists."""
    assert palindrome_pair([1, 2, 3, 4, 9]) == False

def test_palindrome_pair_empty_list():
    """Test an empty list returns False."""
    assert palindrome_pair([]) == False

def test_palindrome_pair_single_element():
    """Test a single-element list returns False."""
    assert palindrome_pair([1]) == False

def test_palindrome_pair_multiple_palindrome_differences():
    """Test a list with multiple palindrome differences."""
    assert palindrome_pair([10, 11, 12, 22]) == True  # 22-11 = 11 is a palindrome

def test_palindrome_pair_negative_numbers():
    """Test with negative numbers."""
    assert palindrome_pair([-5, -3, 0, 3, 5]) == True  # 3-(-3) = 6 is a palindrome

def test_palindrome_pair_floating_point():
    """Test with floating point numbers."""
    assert palindrome_pair([1.0, 2.0, 3.0, 4.0, 5.0]) == True  # 3-1 = 2 is a palindrome

def test_palindrome_pair_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")

def test_palindrome_pair_invalid_list_contents():
    """Test raising ValueError for non-numeric list contents."""
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "three", 4, 5])