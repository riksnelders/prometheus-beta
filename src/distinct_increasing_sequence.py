def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence of distinct integers 
    in strictly increasing order.

    Args:
        arr (list): Input list of integers to check

    Returns:
        bool: True if the sequence is valid, False otherwise

    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element list is considered valid
    if len(arr) <= 1:
        return True
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        return False
    
    # Check for distinctness and strictly increasing order
    for i in range(1, len(arr)):
        # Check if current element is not greater than previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True