# Determinants

## Introduction

A **determinant** is a numerical value associated with a **square matrix**. It provides important information about the properties of a matrix, such as whether the matrix is invertible and how it transforms space.

The determinant is denoted by

```text
det(A)
```

or

```text
|A|
```

where **A** is a square matrix.

---

# Condition

The determinant is defined **only for square matrices**, that is, matrices with the same number of rows and columns.

Examples of square matrices are:

```text
2 × 2

[1 2
 3 4]
```

```text
3 × 3

[1 2 3
 4 5 6
 7 8 9]
```

A matrix such as

```text
2 × 3

[1 2 3
 4 5 6]
```

does **not** have a determinant.

---

# Determinant of a 2 × 2 Matrix

For

```text
A = [a  b
     c  d]
```

the determinant is

```text
det(A) = ad − bc
```

### Example

```text
A = [2 3
     1 4]

det(A)

= (2 × 4) − (3 × 1)

= 8 − 3

= 5
```

---

# Determinant of a 3 × 3 Matrix

For

```text
A =
[a11  a12  a13
 a21  a22  a23
 a31  a32  a33]
```

the determinant can be computed by **cofactor expansion** or **Sarrus' Rule** (for 3 × 3 matrices).

One common formula is

```text
det(A)

= a11(a22a33 − a23a32)

− a12(a21a33 − a23a31)

+ a13(a21a32 − a22a31)
```

This formula is widely used in manual calculations.

---

# Properties of Determinants

Some important properties are:

* The determinant exists only for square matrices.
* If `det(A) = 0`, the matrix is **singular** (not invertible).
* If `det(A) ≠ 0`, the matrix is **non-singular** (invertible).
* The determinant of the identity matrix is **1**.
* Swapping two rows changes the sign of the determinant.
* If two rows (or columns) are identical, the determinant is **0**.

---

# Why Are Determinants Important?

Determinants are used to:

* Determine whether a matrix has an inverse.
* Solve systems of linear equations.
* Compute matrix inverses.
* Measure area and volume scaling under linear transformations.
* Study eigenvalues and eigenvectors.

---

# Determinants in NumPy

NumPy computes determinants using

```python
np.linalg.det(A)
```

where **A** is a square matrix.

---

# Applications

Determinants are used in:

* Linear Algebra
* Data Science
* Machine Learning
* Engineering
* Physics
* Computer Graphics
* Scientific Computing

---

# Summary

* A determinant is a numerical value associated with a square matrix.
* Determinants are defined only for square matrices.
* The determinant of a 2 × 2 matrix is computed using `ad − bc`.
* A matrix is invertible if and only if its determinant is not zero.
* NumPy computes determinants using `np.linalg.det()`.
