"""
Solving Linear Systems Using the Matrix Inverse Method
(Manual Implementation for a 2×2 System)

This program solves AX = B without using NumPy's
inverse function.

Author: Desalu Horsa
"""

# -----------------------------------------
# Input
# -----------------------------------------

print("Enter the coefficient matrix A (2×2):")

a = float(input("A[1][1]: "))
b = float(input("A[1][2]: "))
c = float(input("A[2][1]: "))
d = float(input("A[2][2]: "))

print("\nEnter the constant vector B:")

e = float(input("B[1]: "))
f = float(input("B[2]: "))

# -----------------------------------------
# Determinant
# -----------------------------------------

det = a * d - b * c

if det == 0:
    print("\nThe coefficient matrix is not invertible.")
    exit()

# -----------------------------------------
# Inverse Matrix
# -----------------------------------------

inverse = [
    [ d / det, -b / det],
    [-c / det,  a / det]
]

# -----------------------------------------
# Matrix Multiplication
# X = A⁻¹B
# -----------------------------------------

x = inverse[0][0] * e + inverse[0][1] * f
y = inverse[1][0] * e + inverse[1][1] * f

# -----------------------------------------
# Display Results
# -----------------------------------------

print("\nInverse Matrix:")

for row in inverse:
    print(row)

print("\nSolution:")

print(f"x = {x:.6f}")
print(f"y = {y:.6f}")

