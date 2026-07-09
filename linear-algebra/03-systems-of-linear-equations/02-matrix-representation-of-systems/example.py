
"""
Matrix Representation of Linear Systems

This program demonstrates how a system of
linear equations can be represented using:

1. Matrix equation form: AX = B
2. Augmented matrix form

Author: Desalu Horsa
"""


import numpy as np


# ------------------------------------------------
# Example Linear System
# ------------------------------------------------

# 2x + 3y = 7
# 4x -  y = 5


# Coefficient matrix A

A = np.array([
    [2, 3],
    [4, -1]
])


# Variable vector X

X = np.array([
    [2],
    [1]
])


# Constant vector B

B = np.array([
    [7],
    [5]
])


# ------------------------------------------------
# Verify AX = B
# ------------------------------------------------

result = A @ X


print("Coefficient Matrix A:")
print(A)


print("\nVariable Vector X:")
print(X)


print("\nConstant Vector B:")
print(B)


print("\nResult of A @ X:")
print(result)


# Check whether AX equals B

if np.array_equal(result, B):
    print("\nThe solution satisfies AX = B.")
else:
    print("\nThe solution does not satisfy AX = B.")


# ------------------------------------------------
# Augmented Matrix
# ------------------------------------------------

# Combine A and B horizontally

augmented_matrix = np.hstack((A, B))


print("\nAugmented Matrix:")
print(augmented_matrix)


# ------------------------------------------------
# Extract A and B from Augmented Matrix
# ------------------------------------------------

A_from_augmented = augmented_matrix[:, :-1]

B_from_augmented = augmented_matrix[:, -1:]


print("\nExtracted Coefficient Matrix A:")
print(A_from_augmented)


print("\nExtracted Constant Vector B:")
print(B_from_augmented)

