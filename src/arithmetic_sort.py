def arithmetic_sort(arr):
    """
    Sort a list of integers using only basic arithmetic operations.
    
    This implementation uses a simple bubble sort-like algorithm 
    with only arithmetic comparisons and swaps.
    
    Args:
        arr (list): A list of integers to be sorted
    
    Returns:
        list: A new sorted list of integers
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Bubble sort using only arithmetic operations
    for i in range(n):
        for j in range(0, n - i - 1):
            # Arithmetic comparison: if current > next, swap
            if (sorted_arr[j] - sorted_arr[j + 1]) > 0:
                # Swap using only arithmetic operations
                sorted_arr[j] = sorted_arr[j] + sorted_arr[j + 1]
                sorted_arr[j + 1] = sorted_arr[j] - sorted_arr[j + 1]
                sorted_arr[j] = sorted_arr[j] - sorted_arr[j + 1]
    
    return sorted_arr