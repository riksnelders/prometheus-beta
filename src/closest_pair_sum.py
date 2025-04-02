def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in the array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int): Target sum to find closest pair to
    
    Returns:
        tuple: A tuple containing the pair of numbers that sum closest to target
        
    Raises:
        ValueError: If the input array has fewer than 2 elements
    """
    # Check for invalid input
    if not arr or len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    # Initialize variables to track the closest pair
    closest_diff = float('inf')
    closest_pair = None
    
    # Compare each unique pair of numbers
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update closest pair if current pair is closer to target
            # Use strict comparison to ensure first occurrence of equal closeness is returned
            if current_diff < closest_diff or (current_diff == closest_diff and arr[i] != closest_pair[0]):
                closest_diff = current_diff
                closest_pair = (arr[i], arr[j])
    
    return closest_pair