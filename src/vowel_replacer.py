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
    # Define vowel mappings for lowercase and uppercase
    vowel_map_lower = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
    vowel_map_upper = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    
    # Create result list to build the new string
    result = []
    
    # Iterate through each character in the input string
    for char in input_string:
        # Replace lowercase vowels
        if char in vowel_map_lower:
            result.append(vowel_map_lower[char])
        
        # Replace uppercase vowels
        elif char in vowel_map_upper:
            result.append(vowel_map_upper[char])
        
        # If not a vowel, keep the original character
        else:
            result.append(char)
    
    # Convert result list back to string and return
    return ''.join(result)