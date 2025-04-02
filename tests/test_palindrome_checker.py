import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindromes"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_case_insensitive_palindromes():
    """Test palindromes with mixed case"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A Santa at NASA") == True
    assert is_palindrome("Race a Car") == False

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation"""
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("hello world") == False

def test_numeric_palindromes():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_alphanumeric_palindromes():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("R2ac3e3car2") == True
    assert is_palindrome("R2ac3e2car") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome(" ") == True  # single space
    assert is_palindrome("!@#$%^&*()") == True  # only non-alphanumeric
    assert is_palindrome("a") == True  # single character

def test_non_string_input():
    """Test non-string inputs"""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    assert is_palindrome(None) == False