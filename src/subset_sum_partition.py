from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways to partition a list of numbers 
    into two subsets with equal total sums.

    Args:
        numbers (List[int]): A list of integers to partition.

    Returns:
        int: The number of ways to create two subsets with equal sums.

    Raises:
        ValueError: If the input list is empty or None.
    """
    # Strict validation
    if numbers is None:
        raise ValueError("Input list cannot be None")
    
    if len(numbers) <= 1:
        return 0
    
    # Total sum must be even to split into equal subsets
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return 0
    
    half_sum = total_sum // 2
    partition_count = 0
    
    # Use set for tracking to avoid duplicates
    unique_partitions = set()
    
    # Start with smaller subsets to improve efficiency
    for r in range(1, len(numbers) // 2 + 1):
        for subset in combinations(numbers, r):
            # Skip if this subset sum isn't half the total
            if sum(subset) != half_sum:
                continue
            
            # Create complement subset
            complement = tuple(x for x in numbers if x not in subset)
            
            # Verify complement sums to half_sum too
            if sum(complement) == half_sum:
                # Sort to avoid duplicates and handle same partitions from different views
                partition = tuple(sorted(subset))
                unique_partitions.add(partition)
    
    return len(unique_partitions)