from typing import List, Optional

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways to partition a list of distinct numbers 
    into two subsets with equal total sums.

    Args:
        numbers (List[int]): A list of distinct integers to partition.

    Returns:
        int: The number of ways to create two subsets with equal sums.

    Raises:
        ValueError: If the input list is empty or None.
    """
    # Validate input
    if numbers is None or len(numbers) == 0:
        raise ValueError("Input list must be non-empty")

    # Total sum of all numbers must be even to have equal subset sums
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return 0

    # Target sum for each subset 
    target_sum = total_sum // 2
    n = len(numbers)

    # Dynamic programming to track subset sum possibilities
    # dp[i][j] represents the number of ways to achieve sum j 
    # using a subset of the first i numbers
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: zero sum can be achieved in one way (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # Don't include current number
            dp[i][j] = dp[i-1][j]
            
            # Include current number if it doesn't exceed current sum
            if numbers[i-1] <= j:
                dp[i][j] += dp[i-1][j - numbers[i-1]]
    
    # Half the total ways (as we want to count unique partitions)
    return dp[n][target_sum] // 2