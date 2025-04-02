import pytest
from src.palindrome_word_pairs import find_palindrome_word_pairs, is_palindrome


def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True


def test_basic_palindrome_pairs():
    """Test finding basic palindrome word pairs."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_word_pairs(words)
    assert [0, 1] in result or [1, 0] in result


def test_empty_list():
    """Test behavior with an empty list."""
    assert find_palindrome_word_pairs([]) == []


def test_single_word_list():
    """Test behavior with a single word."""
    words = ["hello"]
    assert find_palindrome_word_pairs(words) == []


def test_multiple_palindrome_pairs():
    """Test finding multiple palindrome pairs."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_word_pairs(words)
    assert [0, 1] in result or [1, 0] in result
    assert [1, 0] in result or [0, 1] in result


def test_invalid_input_type():
    """Test input type validation."""
    with pytest.raises(TypeError):
        find_palindrome_word_pairs("not a list")
    with pytest.raises(TypeError):
        find_palindrome_word_pairs(None)


def test_invalid_list_elements():
    """Test validation of list elements."""
    with pytest.raises(ValueError):
        find_palindrome_word_pairs([1, 2, 3])
    with pytest.raises(ValueError):
        find_palindrome_word_pairs(["valid", 123, "words"])


def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["hello", "world", "python"]
    assert find_palindrome_word_pairs(words) == []