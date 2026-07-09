
"""
Matrix Inverse (Without NumPy)

This program computes the inverse of a 2×2 matrix
using minors, cofactors, the adjoint, and the
general inverse formula.
"""

# -----------------------------
# Read Matrix
# -----------------------------

print("Enter the elements of a 2×2 matrix:")

a = float(input("Element [1][1]: "))
b = float(input("Element [1][2]: "))
c = float(input("Element [2][1]: "))
d = float(input("Element [2][2]: "))

A = [
    [a, b],
    [c, d]
]

# -----------------------------
# Step 1: Determinant
# -----------------------------

det = a * d - b * c

print("\nDeterminant =", det)

if det == 0:
    print("The matrix is singular.")
    print("Inverse does not exist.")
    exit()

# -----------------------------
# Step 2: Minors
# -----------------------------

M11 = d
M12 = c
M21 = b
M22 = a

print("\nMatrix of Minors")
print([[M11, M12],
       [M21, M22]])

# -----------------------------
# Step 3: Cofactors
# -----------------------------

C11 =  M11
C12 = -M12
C21 = -M21
C22 =  M22

cofactor = [
    [C11, C12],
    [C21, C22]
]

print("\nCofactor Matrix")
print(cofactor)

# -----------------------------
# Step 4: Adjoint
# -----------------------------

adjoint = [
    [C11, C21],
    [C12, C22]
]

print("\nAdjoint Matrix")
print(adjoint)

# -----------------------------
# Step 5: Inverse
# -----------------------------

inverse = [
    [adjoint[0][0] / det, adjoint[0][1] / det],
    [adjoint[1][0] / det, adjoint[1][1] / det]
]

print("\nInverse Matrix")

for row in inverse:
    print([round(value, 4) for value in row])

