import pytest
from src.vowel_replacer import replace_vowels

def test_replace_vowels_lowercase():
    """Test replacement of lowercase vowels."""
    assert replace_vowels("hello") == "holle"
    assert replace_vowels("python") == "pythun"
    assert replace_vowels("apple") == "epplo"

def test_replace_vowels_uppercase():
    """Test replacement of uppercase vowels."""
    assert replace_vowels("HELLO") == "HOLLE"
    assert replace_vowels("PYTHON") == "PYTHUN"
    assert replace_vowels("AEIOU") == "EIOUA"

def test_replace_vowels_mixed_case():
    """Test replacement of mixed case vowels."""
    assert replace_vowels("Hello World") == "Holle Wurld"
    assert replace_vowels("pYtHoN") == "pUtHun"

def test_replace_vowels_no_vowels():
    """Test strings with no vowels."""
    assert replace_vowels("rhythm") == "rhythm"
    assert replace_vowels("123") == "123"

def test_replace_vowels_empty_string():
    """Test empty string."""
    assert replace_vowels("") == ""

def test_replace_vowels_special_characters():
    """Test strings with special characters."""
    assert replace_vowels("h3ll0!") == "h3ll0!"
    assert replace_vowels("a!e@i#o$u%") == "e!i@o#u$a%"