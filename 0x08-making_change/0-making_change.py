#!/usr/bin/python3
"""
Coin Change Problem Solution
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount to achieve using the fewest coins.
    Returns:
        int: The minimum number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize DP table with a large value (inf)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
