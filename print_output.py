"""
Prints maxtric order.

Author: Nicholas Butzke
"""


def print_optimal_order(P, i, j, matrix_names):
    """Prints maxtric order."""
    if i == j:
        return matrix_names[i - 1]
    else:
        k = P[i - 1][j - 1]
        left = print_optimal_order(P, i, k, matrix_names)
        right = print_optimal_order(P, k + 1, j, matrix_names)
        return f"({left} * {right})"
