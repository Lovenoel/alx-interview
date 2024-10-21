def minOperations(n: int) -> int:
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    # Start checking for factors starting from 2
    while n > 1:
        # If n is divisible by factor, it's a valid step
        while n % factor == 0:
            operations += factor  # Add the factor to the operation count
            n //= factor  # Divide n by the factor
        factor += 1  # Move to the next potential factor
    
    return operations
