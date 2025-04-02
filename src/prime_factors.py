def get_prime_factors(n):
    """
    Return a sorted list of prime factors for a given positive integer.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        list: A sorted list of prime factors.

    Raises:
        ValueError: If input is less than 1.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # Find prime factors
    factors = []
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    # If n is a prime number greater than sqrt(n)
    if n > 1:
        factors.append(n)
    
    return sorted(factors)