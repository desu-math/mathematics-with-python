
"""
Matrix Inverse (Using NumPy)

This program computes the inverse of
any square matrix using NumPy.
"""

import numpy as np

# -----------------------------
# Read Matrix
# -----------------------------

n = int(input("Enter the order of the matrix: "))

matrix = []

print(f"\nEnter the elements of the {n}×{n} matrix:")

for i in range(n):

    row = []

    for j in range(n):
        value = float(input(f"Element [{i+1}][{j+1}]: "))
        row.append(value)

    matrix.append(row)

A = np.array(matrix)

# -----------------------------
# Determinant
# -----------------------------

det = np.linalg.det(A)

print("\nDeterminant =", round(det, 6))

if np.isclose(det, 0):
    print("The matrix is singular.")
    print("Inverse does not exist.")
    exit()

# -----------------------------
# Inverse
# -----------------------------

inverse = np.linalg.inv(A)

print("\nInverse Matrix")
print(inverse)

