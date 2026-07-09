# Matrix Inverse

## Introduction

The **inverse of a matrix** is analogous to the reciprocal of a number. Just as multiplying a nonzero number by its reciprocal gives **1**, multiplying a square matrix by its inverse gives the **identity matrix**.

The inverse of a matrix **A** is denoted by

```text
A⁻¹
```

and satisfies

```text
AA⁻¹ = A⁻¹A = I
```

where **I** is the identity matrix.

---

# Identity Matrix

The **identity matrix** is a square matrix whose diagonal elements are **1** and all other elements are **0**.

Examples:

```text
2 × 2

[1 0
 0 1]
```

```text
3 × 3

[1 0 0
 0 1 0
 0 0 1]
```

The identity matrix plays the same role for matrices that the number **1** plays for real numbers.

---

# Condition for the Existence of an Inverse

A matrix has an inverse **if and only if**

```text
det(A) ≠ 0
```

If

```text
det(A) = 0
```

the matrix is called a **singular matrix** and has **no inverse**.

If

```text
det(A) ≠ 0
```

the matrix is called a **non-singular (invertible) matrix**.

---

# Minor of a Matrix

The **minor** of an element is the determinant of the matrix obtained by deleting the row and column containing that element.

The minor of the element **aᵢⱼ** is denoted by

```text
Mᵢⱼ
```

### Example

Given

```text
A =

[1 2 3
 4 5 6
 7 8 9]
```

To find the minor of **a₁₁**, remove the first row and first column:

```text
[5 6
 8 9]
```

Therefore,

```text
M₁₁

= det([5 6
       8 9])

= (5 × 9) − (6 × 8)

= 45 − 48

= -3
```

---

# Cofactor of a Matrix

The **cofactor** is obtained by multiplying the minor by

```text
(-1)^(i+j)
```

The formula is

```text
Cᵢⱼ = (-1)^(i+j) × Mᵢⱼ
```

The signs follow the pattern

```text
+   -   +
-   +   -
+   -   +
```

### Example

If

```text
M₁₂ = 8
```

then

```text
C₁₂

= (-1)^(1+2) × 8

= (-1)^3 × 8

= -8
```

---

# Cofactor Matrix

The **cofactor matrix** is obtained by replacing every element of the matrix with its corresponding cofactor.

If

```text
C₁₁  C₁₂  C₁₃
C₂₁  C₂₂  C₂₃
C₃₁  C₃₂  C₃₃
```

then this entire matrix is called the **cofactor matrix**.

---

# Adjoint (Adjugate) Matrix

The **adjoint** (also called the **adjugate**) of a matrix is the transpose of its cofactor matrix.

It is written as

```text
adj(A)
```

and is defined by

```text
adj(A) = (Cofactor Matrix)ᵀ
```

That is, convert the cofactor matrix into its transpose by interchanging rows and columns.

---

# Formula for the Inverse Matrix

Once the determinant and adjoint are known, the inverse is computed by

```text
A⁻¹ = (1 / det(A)) × adj(A)
```

This is the general formula for the inverse of any invertible square matrix.

---

# Special Case: 2 × 2 Matrix

For

```text
A =

[a  b
 c  d]
```

the determinant is

```text
det(A) = ad − bc
```

If

```text
ad − bc ≠ 0
```

then

```text
A⁻¹

= (1 / (ad − bc))

  [ d   -b
   -c    a ]
```

This formula is obtained from the general inverse formula using minors, cofactors, and the adjoint.

---

# Matrix Inverse in NumPy

NumPy computes the inverse of a matrix using

```python
np.linalg.inv(A)
```

If the matrix is singular, NumPy raises an error because the inverse does not exist.

---

# Applications

Matrix inverses are used in:

* Solving systems of linear equations
* Data Science
* Machine Learning
* Artificial Intelligence
* Computer Graphics
* Engineering
* Scientific Computing

---

# Summary

* The inverse of a matrix is denoted by **A⁻¹**.
* Only square matrices can have inverses.
* A matrix is invertible if and only if **det(A) ≠ 0**.
* The **minor** is the determinant obtained after deleting a row and column.
* The **cofactor** is computed using **Cᵢⱼ = (-1)^(i+j) × Mᵢⱼ**.
* The **cofactor matrix** is formed from all cofactors.
* The **adjoint (adjugate)** is the transpose of the cofactor matrix.
* The inverse is computed using **A⁻¹ = (1 / det(A)) × adj(A)**.
* NumPy computes inverses using **np.linalg.inv()**.
