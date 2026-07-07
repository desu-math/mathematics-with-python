
"""
NumPy Basics
------------
This program demonstrates the basic features of the NumPy library.

Author: Desalu Horsa
Repository: mathematics-with-python
"""

import numpy as np

# ---------------------------------
# Creating Arrays
# ---------------------------------

print("----- Creating Arrays -----")

# One-dimensional array
a = np.array([10, 20, 30, 40])

# Two-dimensional array (Matrix)
A = np.array([
    [1, 2],
    [3, 4]
])

print("\nOne-dimensional array:")
print(a)

print("\nTwo-dimensional array:")
print(A)

# ---------------------------------
# Accessing Array Elements
# ---------------------------------

print("\n----- Accessing Elements -----")

print("First element of a:", a[0])
print("Last element of a:", a[-1])

print("Element at row 1, column 1:", A[0, 0])
print("Element at row 2, column 2:", A[1, 1])

# ---------------------------------
# Array Properties
# ---------------------------------

print("\n----- Array Properties -----")

print("Dimensions (ndim):", A.ndim)
print("Shape:", A.shape)
print("Size:", A.size)
print("Data type:", A.dtype)

# ---------------------------------
# Basic Operations
# ---------------------------------

print("\n----- Basic Operations -----")

B = np.array([
    [5, 6],
    [7, 8]
])

print("\nMatrix B:")
print(B)

print("\nA + B =")
print(A + B)

print("\nA - B =")
print(A - B)

print("\n2 × A =")
print(2 * A)
