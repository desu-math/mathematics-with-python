"""
Solving Linear Systems Using the Matrix Inverse Method
(NumPy Implementation)

This program solves AX = B using the inverse
of the coefficient matrix.

Author: Desalu Horsa
"""

import numpy as np

# -----------------------------------------
# Input
# -----------------------------------------

n = int(input("Enter the number of unknowns: "))

print("\nEnter the coefficient matrix A:")

A = np.zeros((n, n), dtype=float)

for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))

print("\nEnter the constant vector B:")

B = np.zeros((n, 1), dtype=float)

for i in range(n):
    B[i][0] = float(input(f"B[{i+1}]: "))

# -----------------------------------------
# Check Invertibility
# -----------------------------------------

det = np.linalg.det(A)

if abs(det) < 1e-10:
    print("\nThe coefficient matrix is not invertible.")
    exit()

# -----------------------------------------
# Compute the Inverse
# -----------------------------------------

A_inverse = np.linalg.inv(A)

# -----------------------------------------
# Solve the System
# X = A⁻¹B
# -----------------------------------------

X = np.matmul(A_inverse, B)   # This line equal with X = A_inverse @ B

# -----------------------------------------
# Display Results
# -----------------------------------------

print("\nCoefficient Matrix (A):")
print(A)

print("\nConstant Vector (B):")
print(B)

print("\nInverse Matrix (A⁻¹):")
print(A_inverse)

print("\nSolution Vector (X):")
print(X)

print("\nSolution:")

for i in range(n):
    print(f"x{i+1} = {X[i][0]:.6f}")

