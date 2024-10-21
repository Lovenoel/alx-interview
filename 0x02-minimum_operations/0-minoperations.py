#!/usr/bin/python3
"""
a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    # Start checking for factors starting from 2
    while n > 1:
        # If n is divisible by factor, it's a valid step
        while n % factor == 0:
            # Add the factor to the operation count
            operations += factor
            n //= factor  # Divide n by the factor
        factor += 1  # Move to the next potential factor
    
    return operations
