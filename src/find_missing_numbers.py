def find_missing_numbers(arr):
    """
    Find and return all the numbers that are missing from a given array of unique integers.
    
    Args:
        arr (list): A list of unique integers with no specific order.
    
    Returns:
        list: A sorted list of missing numbers in the range of the input array.
    
    Raises:
        ValueError: If the input is not a list or contains non-integer elements.
        TypeError: If the input array is empty.
    """
    # Input validation
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers")
    
    if not arr:
        raise TypeError("Input array cannot be empty")
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find the min and max of the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Create a set of the input array for O(1) lookup
    arr_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_val, max_val + 1) 
        if num not in arr_set
    ]
    
    return missing_numbers