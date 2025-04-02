def replace_vowels(input_string):
    """
    Replace each vowel in the input string with the next vowel in the alphabet, 
    preserving the original case.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A new string with vowels replaced by the next vowel in the alphabet.
    
    Examples:
        >>> replace_vowels("hello")
        'holle'
        >>> replace_vowels("AEIOU")
        'EIOUA'
        >>> replace_vowels("Python")
        'Pythun'
    """
    # Define vowel sequences (lowercase and uppercase)
    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'
    
    # Create result list to build the new string
    result = []
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if lowercase vowel
        if char in vowels_lower:
            # Find current index and replace with next vowel (wrapping around)
            current_index = vowels_lower.index(char)
            next_index = (current_index + 1) % len(vowels_lower)
            result.append(vowels_lower[next_index])
        
        # Check if uppercase vowel
        elif char in vowels_upper:
            # Find current index and replace with next vowel (wrapping around)
            current_index = vowels_upper.index(char)
            next_index = (current_index + 1) % len(vowels_upper)
            result.append(vowels_upper[next_index])
        
        # If not a vowel, keep the original character
        else:
            result.append(char)
    
    # Convert result list back to string and return
    return ''.join(result)