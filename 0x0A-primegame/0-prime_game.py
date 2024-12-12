#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determine the winner of a prime game session with `x` rounds.
    
    Args:
        x (int): Number of rounds to be played.
        nums (list of int): List of numbers representing the upper limit for each round.
    
    Returns:
        str or None: The name of the winner ('Maria' or 'Ben'), or None if there's a tie.
    """
    if x < 1 or not nums:
        # Return None if no rounds to play or input list is empty
        return None

    marias_wins, bens_wins = 0, 0  # Initialize win counters for Maria and Ben

    # Generate a list of primes up to the maximum number in nums
    k = max(nums)  # Determine the largest number in nums
    primes = [True for _ in range(1, k + 1, 1)]  # Initialize all numbers as prime
    primes[0] = False  # Mark 1 as non-prime

    for s, is_prime in enumerate(primes, 1):  # Check each number for primality
        if s == 1 or not is_prime:
            continue
        # Mark multiples of the current prime number as non-prime
        for t in range(s + s, k + 1, s):
            primes[t - 1] = False

    # Iterate through the rounds and calculate the winner for each
    for _, k in zip(range(x), nums):
        # Count primes less than or equal to n
        primes_count = len(list(filter(lambda x: x, primes[0: k])))

        # If the count of primes is even, Ben wins; otherwise, Maria wins
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the overall winner or if it's a tie
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
