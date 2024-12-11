#!/usr/bin/python3
"""(501) 0x22. Prime Game task 0. Prime Game

"""

def findPrimesToN(n):
    """Generates a list of all prime numbers up to the given number n.

    Args:
        n (int): The upper limit for generating prime numbers (inclusive).

    Returns:
        list: A list of prime numbers in ascending order up to n.
        None: If the input is invalid (e.g., not an integer or negative).

    """

    if (type(n) is not int or n < 0):
        return None

    # Use a list to store prime numbers in order of discovery.
    primes = []
    for candidate in range(2, n + 1):
        prime = True
        for divisor in range(2, candidate):
            if (candidate % divisor == 0):
                prime = False
                break
        if (prime):
            primes.append(candidate)
    return primes

def isWinner(x, nums):
    """Determines the winner of a prime number game between Ben and Maria.

    In each round, players start with a set of consecutive integers from 1 to n.
    They take turns picking a prime number and removing it and all its multiples
    from the set. The player unable to make a move loses that round.

    Args:
        x (int): Number of rounds to be played.
        nums (list of int): List containing the value of n for each round.

    Returns:
        str: The name of the player who wins the most rounds ("Maria" or "Ben").
        None: If the input is invalid or there is no winner.

    """
    if (type(nums) is not list or not all([type(n) is int for n in nums]) or
            not all([n > -1 for n in nums])):
        return None

    if (type(x) is not int or x != len(nums)):
        return None

    nums.sort()
    primes = findPrimesToN(nums[-1])
    if (primes is None):
        return None

    Maria_wins = 0
    Ben_wins = 0
    for n in nums:
        prime_ct = 0
        for prime in primes:
            if (prime <= n):
                prime_ct += 1
            else:
                break
        # An odd number of primes gives Maria the win (as she starts the game).
        if prime_ct % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if (Maria_wins > Ben_wins):
        return "Maria"
    elif (Ben_wins > Maria_wins):
        return "Ben"
    else:
        return None

'''
Pythonic Implementation Using the Sieve of Eratosthenes:

For optimized prime number generation, the Sieve of Eratosthenes is a classical algorithm.
It is particularly useful for generating all prime numbers less than a given number efficiently.

Original Algorithm: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

Modified to include n:
def _primes(n):
    """Returns a list of all prime numbers less than or equal to n."""
    sieve = [True] * (n + 1)
    for i in range(3, int((n + 1)**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * (((n + 1) - i * i - 1) //
                                             (2 * i) + 1)
    return [2] + [i for i in range(3, n + 1, 2) if sieve[i]]
'''

"""
Primes up to 10000 (example):
This list showcases the distribution of prime numbers up to 10,000.
Below is a truncated version showing only the first few and the last few primes:

2, 3, 5, 7, 11, ..., 9973, 9979.
"""
