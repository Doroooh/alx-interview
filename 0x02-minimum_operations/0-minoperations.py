#!/usr/bin/python3

"""
   It contains th technique to calculate minimum operations.
"""


def minOperations(n):
    """ Method to  calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
        Args:
            n: Is a number to print H characters.
    """
    count = 0
    seg_ment = 2

    if n <= 1:
        return 0
    while n != 1:
        if n % seg_ment == 0:
            n = n // seg_ment
            count += seg_ment
        else:
            seg_ment += 1
    return count
