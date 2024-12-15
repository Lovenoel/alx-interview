#!/usr/bin/python3
"""
A module about the Prime Game played by Maria and Ben
"""


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x <= 0:
        return None

    # Find the maximum value in nums
    max_num = max(nums)

    # Use Sieve of Eratosthenes to find all primes up to max_num
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_num + 1, i):
                primes[multiple] = False

    # Precompute the number of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the count of primes is odd
        else:
            ben_wins += 1  # Ben wins if the count of primes is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
