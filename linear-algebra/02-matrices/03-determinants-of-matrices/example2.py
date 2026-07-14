"""
Determinant of a Matrix (Using NumPy)

This program computes the determinant
of any square matrix using NumPy.
"""

import numpy as np

# Matrix order
n = int(input("Enter the order of the matrix: "))

matrix = []

print(f"\nEnter the elements of the {n}×{n} matrix:")

for i in range(n):

    row = []

    for j in range(n):
        value = float(input(f"Element [{i+1}][{j+1}]: "))
        row.append(value)

    matrix.append(row)

# Convert to NumPy array
A = np.array(matrix)

# Compute determinant
determinant = np.linalg.det(A)

print("\nMatrix:")
print(A)

print(f"\nDeterminant = {determinant:.2f}")

if np.isclose(determinant, 0):
    print("The matrix is singular (no inverse).")
else:
    print("The matrix is non-singular (has an inverse).")

