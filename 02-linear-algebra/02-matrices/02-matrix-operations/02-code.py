
"""
Matrix Operations Calculator
----------------------------
This program performs common matrix operations using NumPy.

Operations:
1. Matrix Addition
2. Matrix Subtraction
3. Scalar Multiplication
4. Matrix Multiplication
5. Matrix Transpose

Author: Desalu Horsa
Repository: mathematics-with-python
"""

import numpy as np


# ------------------------------------------
# Helper Function
# ------------------------------------------

def input_matrix(rows, cols):
    """Read a matrix from the user."""

    matrix = []

    print(f"\nEnter the elements of a {rows} × {cols} matrix:")

    for i in range(rows):

        row = []

        for j in range(cols):
            value = float(input(f"Element [{i + 1}][{j + 1}]: "))
            row.append(value)

        matrix.append(row)

    return np.array(matrix)


# ------------------------------------------
# Matrix Operations
# ------------------------------------------

def addition():

    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    print("\nMatrix A")
    A = input_matrix(rows, cols)

    print("\nMatrix B")
    B = input_matrix(rows, cols)

    print("\nA + B =")
    print(A + B)


def subtraction():

    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    print("\nMatrix A")
    A = input_matrix(rows, cols)

    print("\nMatrix B")
    B = input_matrix(rows, cols)

    print("\nA - B =")
    print(A - B)


def scalar_multiplication():

    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    scalar = float(input("Enter the scalar: "))

    print("\nMatrix A")
    A = input_matrix(rows, cols)

    print(f"\n{scalar} × A =")
    print(scalar * A)


def matrix_multiplication():

    print("\nMatrix A")
    rows_A = int(input("Rows: "))
    cols_A = int(input("Columns: "))

    A = input_matrix(rows_A, cols_A)

    print("\nMatrix B")
    rows_B = int(input("Rows: "))
    cols_B = int(input("Columns: "))

    if cols_A != rows_B:
        print("\nMatrix multiplication is not possible.")
        print("The number of columns of Matrix A must equal the number of rows of Matrix B.")
        return

    B = input_matrix(rows_B, cols_B)

    print("\nA × B =")
    print(np.matmul(A, B))


def transpose():

    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    A = input_matrix(rows, cols)

    print("\nTranspose of A =")
    print(A.T)


# ------------------------------------------
# Main Program
# ------------------------------------------

while True:

    print("\n========== Matrix Operations ==========")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Scalar Multiplication")
    print("4. Matrix Multiplication")
    print("5. Matrix Transpose")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        scalar_multiplication()

    elif choice == "4":
        matrix_multiplication()

    elif choice == "5":
        transpose()

    elif choice == "6":
        print("\nThank you for using the Matrix Operations Calculator.")
        break

    else:
        print("\nInvalid choice. Please try again.")
