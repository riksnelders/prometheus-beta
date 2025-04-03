import pytest
from src.validate_phone_number import validate_phone_number

def test_valid_phone_number_formats():
    """Test all three valid phone number formats"""
    # Format 1: (123) 456-7890
    assert validate_phone_number('(123) 456-7890') == True
    
    # Format 2: 123-456-7890
    assert validate_phone_number('123-456-7890') == True
    
    # Format 3: 123 456 7890
    assert validate_phone_number('123 456 7890') == True

def test_invalid_phone_number_formats():
    """Test various invalid phone number formats"""
    # Incorrect separators
    assert validate_phone_number('123.456.7890') == False
    assert validate_phone_number('1234567890') == False
    
    # Incorrect parentheses
    assert validate_phone_number('(123)456-7890') == False
    assert validate_phone_number('123(456)7890') == False
    
    # Wrong number of digits
    assert validate_phone_number('(12) 456-7890') == False
    assert validate_phone_number('(123) 45-7890') == False
    
    # Empty string
    assert validate_phone_number('') == False
    
    # Whitespace-only string
    assert validate_phone_number('   ') == False

def test_whitespace_handling():
    """Test that function handles leading and trailing whitespace"""
    assert validate_phone_number('  (123) 456-7890  ') == True
    assert validate_phone_number('  123-456-7890  ') == True
    assert validate_phone_number('  123 456 7890  ') == True