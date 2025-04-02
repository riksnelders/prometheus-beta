def find_palindrome_word_pairs(words):
    """
    Find pairs of indices where words are palindromes when their characters are reversed.
    
    Args:
        words (list): A list of words to check for palindrome pairs.
    
    Returns:
        list: A list of index pairs where the reversed words form palindromes.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-string elements.
    """
    # Input validation
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are strings
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    # Store palindrome word pairs
    palindrome_pairs = []
    
    # Check all pairs of indices
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip comparing a word with itself
            if i == j:
                continue
            
            # Check if reversed word is a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append([i, j])
    
    return palindrome_pairs


def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    Args:
        word (str): The word to check.
    
    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]