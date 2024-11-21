#!/usr/bin/python3
"""
Rotational a 2D Matrix
"""


def copyMat(matrix):
    """
    *********************************
    ***********Copy Matrix***********
    *********************************
    @matrix: a 2D Matrix of type list
    returns:
            a copy of a given matrix
    """
    ln = len(matrix)
    m = []
    for a in range(ln):
        d = []
        for b in range(ln):
            d.append(matrix[a][b])
        m.append(d)
    return m


def rotate_2d_matrix(matrix):
    """
    ****************************************
    ***rotational Matrix 90 degrees clockwise***
    ****************************************
    @matrix: n x n 2D Matrix of type list
    returns:
            Nothing
    """
    ln = len(matrix)
    m = copyMat(matrix)
    for a in range(ln):
        for b in range(ln):
            matrix[b][ln-1-a] = m[a][b]
