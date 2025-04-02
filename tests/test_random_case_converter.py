import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Check that result is same length as input
    assert len(result) == len(input_str)
    
    # Check that result contains same characters as input
    assert set(result.lower()) == set(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that the function doesn't always produce the same output."""
    random.seed(42)  # Set seed for reproducibility
    input_str = "hello world"
    
    # Run multiple times to check for variation
    results = set()
    for _ in range(10):
        results.add(convert_to_random_case(input_str))
    
    # Should have more than one unique result due to randomness
    assert len(results) > 1

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and numbers."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    # Check that result is same length and contains same characters
    assert len(result) == len(input_str)
    assert set(result.lower()) == set(input_str.lower())