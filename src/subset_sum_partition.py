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
    if numbers is None or len(numbers) == 0:
        raise ValueError("Input list cannot be None or empty")
    
    if len(numbers) <= 1:
        return 0
    
    # Total sum must be even to split into equal subsets
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return 0
    
    half_sum = total_sum // 2
    n = len(numbers)
    
    # Store unique valid partitions to avoid duplicates
    unique_partitions = set()
    
    # Try all possible subset combinations
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            # If this subset sums to half, check complement
            if sum(subset) == half_sum:
                complement = tuple(x for x in numbers if x not in subset)
                if sum(complement) == half_sum:
                    # Sort to avoid duplicate counting
                    partition = tuple(sorted(subset))
                    complement_sorted = tuple(sorted(complement))
                    
                    # Add the partition or its complement to ensure uniqueness
                    unique_partitions.add(partition)
                    unique_partitions.add(complement_sorted)
    
    return len(unique_partitions) // 2