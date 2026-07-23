# Gaussian Elimination

## Introduction

**Gaussian elimination** is an algorithm used to solve systems of linear equations by transforming the system into a simpler form called **row echelon form (REF)**.

The method works by applying **elementary row operations** to the augmented matrix until the solution can be obtained easily through **back substitution**.

For example, the system:

```text
2x + 3y = 7

4x - y = 5
```

can be represented as:

```text
[2   3 | 7
 4  -1 | 5]
```

Gaussian elimination transforms this matrix into an equivalent but simpler form.

---

# Main Idea

The main goal of Gaussian elimination is:

```text
Original System

        ↓

Augmented Matrix

        ↓

Row Echelon Form

        ↓

Back Substitution

        ↓

Solution
```

The transformed system has the same solution as the original system.

---

# Elementary Row Operations

Gaussian elimination uses three operations that do not change the solution of the system.

## 1. Row Switching

Two rows can be exchanged.

Notation:

```text
Rᵢ ↔ Rⱼ
```

Example:

```text
[1  2]
[3  4]
```

After switching rows:

```text
[3  4]
[1  2]
```

---

## 2. Row Multiplication

A row can be multiplied by a nonzero constant.

Notation:

```text
Rᵢ → kRᵢ
```

where:

```text
k ≠ 0
```

Example:

```text
[2  4]
```

Multiply by 1/2:

```text
[1  2]
```

---

## 3. Row Addition

A multiple of one row can be added to another row.

Notation:

```text
Rᵢ → Rᵢ + kRⱼ
```

Example:

```text
R₂ → R₂ - 2R₁
```

This operation is mainly used to eliminate variables.

---

# Pivot Element

A **pivot element** is the first nonzero element in a row.

Example:

```text
[2   3 | 7
 0   5 | 4]
```

The pivot elements are:

```text
2 and 5
```

Pivots are used to eliminate the elements below them.

---

# Row Echelon Form (REF)

A matrix is in row echelon form if it satisfies the following conditions:

1. All nonzero rows are above rows containing only zeros.

2. The first nonzero element of each row is to the right of the first nonzero element in the row above it.

3. All elements below each pivot are zero.

Example:

```text
[2   3 | 7
 0   5 | 4]
```

This matrix is in row echelon form.

---

# Gaussian Elimination Process

Consider the system:

```text
x + y = 5

2x + 3y = 12
```

The augmented matrix is:

```text
[1  1 | 5
 2  3 |12]
```

## Step 1: Choose the first pivot

The first pivot is:

```text
1
```

located in the first row.

---

## Step 2: Eliminate the element below the pivot

Use the operation:

```text
R₂ → R₂ - 2R₁
```

Calculation:

```text
[2  3 |12]

-

2[1  1 |5]

=

[0  1 |2]
```

The matrix becomes:

```text
[1  1 |5
 0  1 |2]
```

---

## Step 3: Back Substitution

The second row gives:

```text
y = 2
```

Substitute into the first equation:

```text
x + 2 = 5
```

Therefore:

```text
x = 3
```

The solution is:

```text
x = 3

y = 2
```

---

# Gaussian Elimination Algorithm Structure

The general process is:

```text
1. Convert the system into an augmented matrix.

2. Select a pivot element.

3. Use row operations to make all elements below
   the pivot equal to zero.

4. Move to the next pivot position.

5. Continue until row echelon form is obtained.

6. Solve the resulting system using back substitution.
```

---

# Gaussian Elimination and Matrices

Gaussian elimination is an application of matrix operations.

It uses:

* Matrix representation of systems.
* Augmented matrices.
* Elementary row operations.

These concepts connect directly with the previous matrix chapter.

---

# Applications

Gaussian elimination is used in:

* Solving large systems of equations.
* Engineering calculations.
* Physics simulations.
* Numerical methods.
* Linear regression.
* Machine learning algorithms.

---

# Python Implementation Concept

In Python, matrices are stored as arrays:

```python
import numpy as np

A = np.array([
    [1, 1, 5],
    [2, 3, 12]
])
```

Row operations are implemented using array operations.

For example:

Mathematical operation:

```text
R₂ → R₂ - 2R₁
```

Python representation:

```python
A[1] = A[1] - 2 * A[0]
```

This directly applies the Gaussian elimination step.

---

# Summary

* Gaussian elimination solves linear systems by transforming them into row echelon form.
* It uses three elementary row operations.
* Pivot elements are used to eliminate variables.
* The final system is solved using back substitution.
* Augmented matrices are the main computational representation.
* Gaussian elimination is a fundamental algorithm behind many scientific and data science applications.
