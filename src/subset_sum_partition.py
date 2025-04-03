from typing import List, Optional
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways to partition a list of distinct numbers 
    into two subsets with equal total sums.

    This implementation uses a comprehensive combinatorial approach to count 
    all possible ways the numbers can be split into equal-sum partitions.

    Args:
        numbers (List[int]): A list of possibly non-distinct integers to partition.

    Returns:
        int: The number of ways to create two subsets with equal sums.

    Raises:
        ValueError: If the input list is None.
    """
    # Validate input
    if numbers is None:
        raise ValueError("Input list must not be None")
    
    # If list is empty or has only one element, return 0
    if len(numbers) <= 1:
        return 0
    
    # Total sum must be even
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return 0
    
    half_sum = total_sum // 2
    n = len(numbers)
    count = 0

    # Try all possible subset sizes
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if this subset sums to half of total
            if sum(subset) == half_sum:
                # Find complement subset
                complement = tuple(x for x in numbers if x not in subset)
                
                # Ensure complement also sums to half_sum
                if sum(complement) == half_sum:
                    count += 1
    
    # Divide by 2 to avoid counting duplicates
    return count // 2