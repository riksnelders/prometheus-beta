import random

def convert_to_random_case(input_string):
    """
    Convert a string to alternating random case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A new string with characters converted to random case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check for invalid input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to random case
    random_case_chars = []
    for char in input_string:
        # Randomly choose between upper and lower case
        if random.choice([True, False]):
            random_case_chars.append(char.upper())
        else:
            random_case_chars.append(char.lower())
    
    return ''.join(random_case_chars)