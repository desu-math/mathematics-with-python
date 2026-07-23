# Solving Systems of Linear Equations Using the Matrix Inverse

## Introduction

The **Matrix Inverse Method** is a technique for solving a system of linear equations by expressing the system in matrix form and using the inverse of the coefficient matrix.

Unlike Gaussian Elimination and Gauss-Jordan Elimination, which transform the augmented matrix through row operations, this method solves the system using matrix multiplication.

Since the theory of inverse matrices has already been covered in the **Matrix Inverse** topic, this section focuses on applying that concept to solve linear systems.

---

# Matrix Form of a Linear System

Consider the system:

```text
2x + y = 5

x + 3y = 7
```

This system can be written in matrix form as:

```text
AX = B
```

where

```text
A = [2  1
     1  3]
```

is the **coefficient matrix**,

```text
X = [x
     y]
```

is the **unknown vector**, and

```text
B = [5
     7]
```

is the **constant vector**.

---

# Derivation of the Matrix Inverse Method

Starting with

```text
AX = B
```

multiply both sides by the inverse of the coefficient matrix:

```text
A⁻¹AX = A⁻¹B
```

Using the property

```text
A⁻¹A = I
```

we obtain

```text
IX = A⁻¹B
```

Since

```text
IX = X
```

the solution becomes

```text
X = A⁻¹B
```

This is the fundamental formula of the Matrix Inverse Method.

---

# Conditions for Using the Matrix Inverse Method

The method can be used only if the coefficient matrix is **invertible**.

This requires:

* The coefficient matrix must be **square** (same number of equations and unknowns).
* The determinant of the coefficient matrix must be **nonzero**.

If

```text
det(A) = 0
```

then the inverse of **A** does not exist, and this method cannot be applied.

---

# Solving Procedure

The Matrix Inverse Method consists of the following steps:

1. Write the system in matrix form:

```text
AX = B
```

2. Find the inverse of the coefficient matrix:

```text
A⁻¹
```

3. Multiply the inverse by the constant vector:

```text
X = A⁻¹B
```

4. Read the values of the unknown variables from the solution vector.

---

# Example

Consider the system

```text
2x + y = 5

x + 3y = 7
```

Matrix form:

```text
AX = B
```

where

```text
A = [2  1
     1  3]
```

and

```text
B = [5
     7]
```

After computing the inverse of **A**, the solution is obtained by

```text
X = A⁻¹B
```

The resulting vector contains the values of **x** and **y**.

---

# Comparison with Elimination Methods

| Gaussian Elimination        | Gauss-Jordan Elimination | Matrix Inverse Method            |
| --------------------------- | ------------------------ | -------------------------------- |
| Uses row operations         | Uses row operations      | Uses matrix multiplication       |
| Produces REF                | Produces RREF            | Computes (A^{-1})                |
| Requires back substitution  | No back substitution     | No back substitution             |
| Efficient for large systems | Slightly more operations | Less efficient for large systems |

---

# Advantages

* Simple mathematical formulation.
* Connects directly with matrix algebra.
* No back substitution is required.
* Useful when the inverse matrix has already been computed.
* Reinforces the relationship between inverse matrices and linear systems.

---

# Limitations

* Applicable only when the coefficient matrix is invertible.
* Cannot be used if the determinant is zero.
* Computing the inverse requires additional calculations.
* For large systems, Gaussian Elimination is generally more efficient and numerically stable.

---

# Applications

The Matrix Inverse Method is used in:

* Solving small systems of linear equations.
* Computer graphics and geometric transformations.
* Engineering analysis.
* Control systems.
* Scientific computing.
* Data analysis and machine learning, where inverse matrices appear in some analytical solutions.

---

# Python Implementation Concept

The implementation follows these steps:

1. Create the coefficient matrix **A**.
2. Create the constant vector **B**.
3. Compute the inverse of **A**.
4. Multiply **A⁻¹** by **B**.
5. Display the solution vector **X**.

In Python, the inverse can be computed manually (using the adjoint method for small matrices) or by using NumPy's linear algebra module.

---

# Summary

* The Matrix Inverse Method solves a linear system using the equation

```text
X = A⁻¹B
```

* It requires the coefficient matrix to be square and invertible.
* The method is elegant and closely connects matrix theory with linear systems.
* Although less efficient than Gaussian Elimination for large systems, it is an important technique in linear algebra and many mathematical applications.
