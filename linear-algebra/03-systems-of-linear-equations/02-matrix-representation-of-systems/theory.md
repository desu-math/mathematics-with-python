# Matrix Representation of Linear Systems

## Introduction

A system of linear equations can be represented using matrices to make the system easier to organize and solve.

Instead of writing every equation separately, we can write the entire system in the form:

```text id="1d3y9c"
AX = B
```

where:

* **A** is the coefficient matrix.
* **X** is the variable vector.
* **B** is the constant vector.

---

# General Form of a Linear System

A system of `m` linear equations with `n` unknown variables can be written as:

```text id="7ny0p7"
a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ = b₁

a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ = b₂

⋮

aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ = bₘ
```

where:

* `x₁, x₂, ..., xₙ` are unknown variables.
* `aᵢⱼ` are coefficients.
* `b₁, b₂, ..., bₘ` are constants.

---

# Matrix Form

The system can be written as:

```text id="c9f64o"
AX = B
```

where:

## Coefficient Matrix (A)

The coefficient matrix contains only the coefficients of variables.

Example:

```text id="03g1yh"
2x + 3y = 7

4x - y = 5
```

The coefficient matrix is:

```text id="hfkg6m"
A = [2   3
     4  -1]
```

---

## Variable Vector (X)

The variable vector contains the unknown variables.

```text id="s0y35l"
X = [x
     y]
```

---

## Constant Vector (B)

The constant vector contains the values on the right side of equations.

```text id="0m7u2k"
B = [7
     5]
```

---

# Verification of AX = B

The matrix equation:

```text id="69z9g7"
AX = B
```

means:

```text id="v1r6u7"
[2  3] [x]   [7]
[4 -1] [y] = [5]
```

Performing matrix multiplication:

```text id="x0t6ud"
[2x + 3y]
[4x - y]
```

gives:

```text id="7h92m2"
[7]
[5]
```

which is exactly the original system.

Therefore:

```text id="kmk1sl"
AX = B
```

is an equivalent representation of the system.

---

# Augmented Matrix Representation

Another common representation is the **augmented matrix**.

An augmented matrix combines the coefficient matrix and constant vector into one matrix.

For:

```text id="g6y0pk"
2x + 3y = 7

4x - y = 5
```

the augmented matrix is:

```text id="0j13mv"
[2   3 | 7
 4  -1 | 5]
```

The vertical line separates:

* Coefficients of variables.
* Constants.

---

# Why Use Augmented Matrices?

Augmented matrices are useful because they:

* Remove unnecessary symbols.
* Make row operations easier.
* Are the foundation of elimination methods.

Methods such as:

* Gaussian elimination.
* Gauss-Jordan elimination.

operate directly on augmented matrices.

---

# Types of Matrix Representation

A linear system can be represented in three ways:

## 1. Equation Form

Example:

```text id="f8m7wj"
2x + y = 5

x - y = 1
```

---

## 2. Matrix Equation Form

```text id="a6y6fh"
AX = B
```

---

## 3. Augmented Matrix Form

```text id="x0l5qi"
[2  1 | 5
 1 -1 | 1]
```

All three forms represent the same mathematical system.

---

# Dimension of a Linear System

If a system has:

* `m` equations
* `n` unknowns

then:

The coefficient matrix has size:

```text id="8j7bfr"
m × n
```

Examples:

### Two equations, two variables:

```text id="s7eqxc"
2 × 2 system
```

Coefficient matrix:

```text id="3t5j6j"
2 × 2
```

---

### Three equations, two variables:

```text id="9m5q2y"
3 × 2 system
```

Coefficient matrix:

```text id="4f0f4v"
3 × 2
```

---

# Python Representation

In Python, matrices are represented using NumPy arrays.

Example:

```python
import numpy as np

A = np.array([
    [2, 3],
    [4, -1]
])

X = np.array([
    [x],
    [y]
])

B = np.array([
    [7],
    [5]
])
```

Then the matrix equation:

```text id="ql3xj6"
AX = B
```

can be computed using:

```python
A @ X
```

---

# Applications

Matrix representation of systems is used in:

* Gaussian elimination algorithms.
* Linear regression.
* Machine learning models.
* Optimization.
* Engineering simulations.

---

# Summary

* Linear systems can be written in matrix form as **AX = B**.
* The coefficient matrix contains variable coefficients.
* The variable vector contains unknowns.
* The constant vector contains right-side values.
* Augmented matrices combine coefficients and constants.
* Matrix representation prepares systems for computational solving methods.
