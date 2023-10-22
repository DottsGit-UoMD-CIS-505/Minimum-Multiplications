"""
Determining the minimum number of elementary multiplications needed to
multiply n matrices and an order that produces that minimum number.

Author: Nicholas Butzke
"""

import sys


def minmult(d):
    """
    Determining the minimum number of elementary multiplications needed to
    multiply n matrices and an order that produces that minimum number.

    Keep in mind indexing is different due to the book using 1 based numbering and python using 0 based number.
    Also the indexing will be different on the ranges because the book often does <= loop endings but python's range() end conditions do <.
    This effectively means that the indexing will be shifted around from the book but I tried to keep it close.
    The additions and subtractions that negate themselves are for my sanity
    """
    n = len(d) // 2
    M = [[0] * n for _ in range(n)]
    P = [[0] * n for _ in range(n)]

    for diagonal in range(1, (n - 1) + 1):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i - 1][j - 1] = sys.maxsize
            for k in range(i, (j - 1) + 1):
                cost = M[i - 1][k - 1] + M[(k + 1) - 1][j - 1] + d[i - 1] * d[k] * d[j]
                if cost < M[i - 1][j - 1]:
                    M[i - 1][j - 1] = cost
                    P[i - 1][j - 1] = k

    return M, P
