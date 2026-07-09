
"""
Determinant of a Matrix (Without NumPy)

This program computes the determinant of
2×2 and 3×3 matrices using pure Python.
"""

# Matrix size
n = int(input("Enter the order of the matrix (2 or 3): "))

# Read matrix
matrix = []

print(f"\nEnter the elements of the {n}×{n} matrix:")

for i in range(n):
    row = []

    for j in range(n):
        value = float(input(f"Element [{i+1}][{j+1}]: "))
        row.append(value)

    matrix.append(row)

# -------------------------
# Determinant of 2×2 matrix
# -------------------------

if n == 2:

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    determinant = a * d - b * c

# -------------------------
# Determinant of 3×3 matrix
# -------------------------

elif n == 3:

    a11 = matrix[0][0]
    a12 = matrix[0][1]
    a13 = matrix[0][2]

    a21 = matrix[1][0]
    a22 = matrix[1][1]
    a23 = matrix[1][2]

    a31 = matrix[2][0]
    a32 = matrix[2][1]
    a33 = matrix[2][2]

    determinant = (
        a11 * (a22 * a33 - a23 * a32)
        - a12 * (a21 * a33 - a23 * a31)
        + a13 * (a21 * a32 - a22 * a31)
    )

else:
    print("\nThis program supports only 2×2 and 3×3 matrices.")
    exit()

print("\nDeterminant =", determinant)

if determinant == 0:
    print("The matrix is singular (no inverse).")
else:
    print("The matrix is non-singular (has an inverse).")
