import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    """Test prime numbers."""
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(17) == [17]
    assert get_prime_factors(29) == [29]

def test_prime_factors_special_cases():
    """Test special case inputs."""
    assert get_prime_factors(1) == []
    assert get_prime_factors(2) == [2]

def test_prime_factors_errors():
    """Test error handling."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)
    
    with pytest.raises(TypeError):
        get_prime_factors("12")
    with pytest.raises(TypeError):
        get_prime_factors(3.14)