
"""
Gaussian Elimination

This program solves a system of linear equations
using the Gaussian Elimination algorithm with
back substitution.

Author: Desalu Horsa
"""

import numpy as np

# -----------------------------------------
# Input
# -----------------------------------------

n = int(input("Enter the number of unknowns: "))

print("\nEnter the augmented matrix:")

A = np.zeros((n, n + 1), dtype=float)

for i in range(n):
    for j in range(n + 1):
        A[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))

print("\nOriginal Augmented Matrix:")
print(A)

# -----------------------------------------
# Forward Elimination
# -----------------------------------------

for pivot in range(n):

    # Pivoting (swap rows if pivot is zero)
    if A[pivot][pivot] == 0:

        for row in range(pivot + 1, n):

            if A[row][pivot] != 0:
                A[[pivot, row]] = A[[row, pivot]]
                break

    # Eliminate entries below the pivot
    for row in range(pivot + 1, n):

        factor = A[row][pivot] / A[pivot][pivot]

        A[row] = A[row] - factor * A[pivot]

print("\nRow Echelon Form:")
print(A)

# -----------------------------------------
# Back Substitution
# -----------------------------------------

x = np.zeros(n)

for i in range(n - 1, -1, -1):

    x[i] = A[i][n]

    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]

    x[i] /= A[i][i]

# -----------------------------------------
# Display Solution
# -----------------------------------------

print("\nSolution:")

for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")

