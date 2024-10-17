#!/usr/bin/python3
""" Minimum Operations
This module defines a function to calculate the minimum number
of operations required to obtain exactly n 'H' characters in a text editor,
starting with a single 'H'. The only operations allowed are 'Copy All' and 'Paste'.
"""


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters 
    Args:
        n (int): The target number of 'H' characters to reach.

    Returns:
        int: The minimum number of operations (or 0 if n can't be reached).
    """
    
    # Initialize variables:
    # 'next' will hold the string to paste during a 'Paste' operation.
    # 'body' represents the current content of the editor.
    # 'op' keeps track of the number of operations performed.
    next = 'H'
    body = 'H'
    op = 0
    
    # Loop until the current content ('body') matches the target length 'n'.
    while (len(body) < n):
        
        # If the current length of 'body' divides 'n', we can perform a 'Copy All' and 'Paste' operation.
        if n % len(body) == 0:
            op += 2  # One 'Copy All' and one 'Paste' operation.
            next = body  # Update 'next' to the current content of 'body'.
            body += body  # Perform the 'Paste' operation by doubling 'body'.
        
        # If 'n' is not divisible by the current length of 'body', perform only a 'Paste' operation.
        else:
            op += 1  # Just one 'Paste' operation.
            body += next  # Add the previously copied content to 'body'.
    
    # If the final length of 'body' doesn't equal 'n', return 0 (indicating it's not possible).
    if len(body) != n:
        return 0
    
    # Return the total number of operations performed.
    return op
