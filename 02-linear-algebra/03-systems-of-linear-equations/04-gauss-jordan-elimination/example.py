"""
Gauss-Jordan Elimination

This program solves a system of linear equations
using the Gauss-Jordan Elimination algorithm.

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
# Gauss-Jordan Elimination
# -----------------------------------------

for pivot in range(n):

    # Swap rows if pivot is zero
    if A[pivot][pivot] == 0:
        for row in range(pivot + 1, n):
            if A[row][pivot] != 0:
                A[[pivot, row]] = A[[row, pivot]]
                break

    # Normalize the pivot row
    A[pivot] = A[pivot] / A[pivot][pivot]

    # Eliminate all other entries in the pivot column
    for row in range(n):

        if row != pivot:

            factor = A[row][pivot]

            A[row] = A[row] - factor * A[pivot]

print("\nReduced Row Echelon Form (RREF):")
print(A)

# -----------------------------------------
# Display Solution
# -----------------------------------------

print("\nSolution:")

for i in range(n):
    print(f"x{i+1} = {A[i][n]:.6f}")

