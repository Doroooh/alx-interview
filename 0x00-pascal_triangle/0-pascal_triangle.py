#!/usr/bin/python3
"""A module for generating Pascal's Triangle up to a specified number of rows."""

def pascal_triangle(n):
    """return a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_t = []

    for r in range(n):
        pascal_t.append([])
        pascal_t[r].append(1)

        for m in range(1, r):
            s = pascal_t[r-1][m-1]
            t = pascal_t[r-1][m]
            pascal_t[r].append(s+t)

        if(n != 0 and r != 0):
            pascal_t[r].append(1)

    return pascal_t
