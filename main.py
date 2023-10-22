"""
Determining the minimum number of elementary multiplications needed to
multiply n matrices and an order that produces that minimum number.

Author: Nicholas Butzke
"""

from minimum_multiplication import minmult
from print_output import print_optimal_order


matrix_dimensions = [10, 4, 4, 5, 5, 20, 20, 2, 2, 50]
M, P = minmult(matrix_dimensions)
matrix_names = [f"A{i}" for i in range(1, len(matrix_dimensions) // 2 + 1)]
optimal_order = print_optimal_order(
    P,
    1,
    len(matrix_dimensions) // 2,
    matrix_names,
)
optimal_cost = M[0][len(matrix_dimensions) // 2 - 1]

print("M Matrix:")
for row in M:
    for element in row:
        print(f"{element:4}", end=" ")
    print()
print("P Matrix:")
for row in P:
    for element in row:
        print(f"{element:4}", end=" ")
    print()
print("Optimal Order:", optimal_order)
print("Optimal Cost:", optimal_cost)
