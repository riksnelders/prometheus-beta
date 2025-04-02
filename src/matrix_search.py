def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The target integer to find
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If the matrix is empty or contains non-integer elements
    
    Time Complexity: O(m * n), where m is number of rows, n is number of columns
    Space Complexity: O(1)
    """
    # Validate input
    if not isinstance(matrix, list) or not matrix:
        return False
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check each row in the matrix
    for row in matrix:
        # Validate row
        if not isinstance(row, list):
            raise ValueError("Matrix must be a list of lists")
        
        # Check if target is in this row
        if target in row:
            return True
    
    return False