#!/usr/bin/python3
"""Coin Change Problem Solver"""


def makeChange(coins, total):
    """Determines the minimum number of coins needed to meet a given total.

    Args:
        coins (list): Available coin denominations.
        total (int): Target amount.

    Returns:
        int: Minimum number of coins needed to achieve the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to prioritize larger denominations.
    coins.sort(reverse=True)

    current_sum = 0  # Tracks the cumulative total of selected coins.
    coin_count = 0   # Tracks the number of coins used.

    for coin in coins:
        # Use as many coins of the current denomination as possible.
        if current_sum < total:
            max_use = (total - current_sum) // coin  # Max coins of this type.
            current_sum += max_use * coin
            coin_count += max_use

        # Break early if we've already reached the target total.
        if current_sum == total:
            return coin_count

    # If unable to reach the exact total, return -1.
    return -1
