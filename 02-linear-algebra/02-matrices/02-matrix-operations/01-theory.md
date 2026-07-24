# Matrix Operations

## Introduction

Matrix operations are mathematical procedures used to combine or manipulate matrices. They are fundamental in Linear Algebra and form the basis for solving systems of equations, computer graphics, machine learning, scientific computing, and many other applications.

---

# 1. Matrix Addition

Two matrices can be added only if they have the **same order** (same number of rows and columns).

If

```text
A = [aᵢⱼ]

B = [bᵢⱼ]
```

then

```text
A + B = [aᵢⱼ + bᵢⱼ]
```

### Example

```text
A = [1  2]
    [3  4]

B = [5  6]
    [7  8]

A + B = [6   8]
        [10 12]
```

---

# 2. Matrix Subtraction

Two matrices can be subtracted only if they have the **same order**.

If

```text
A = [aᵢⱼ]

B = [bᵢⱼ]
```

then

```text
A − B = [aᵢⱼ − bᵢⱼ]
```

### Example

```text
A = [5  6]
    [7  8]

B = [1  2]
    [3  4]

A − B = [4  4]
        [4  4]
```

---

# 3. Scalar Multiplication

A matrix is multiplied by a scalar by multiplying **every element** by the scalar.

If

```text
k
```

is a scalar and

```text
A = [aᵢⱼ]
```

then

```text
kA = [k · aᵢⱼ]
```

### Example

```text
A = [1 2]
    [3 4]

2A = [2 4]
     [6 8]
```

---

# 4. Matrix Multiplication

Matrix multiplication is different from ordinary multiplication.

Suppose

```text
A is an m × n matrix

B is an n × p matrix
```

Then

```text
AB
```

is defined and produces an

```text
m × p
```

matrix.

The element in row **i** and column **j** is

```text
cᵢⱼ = aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + ⋯ + aᵢₙbₙⱼ
```

### Condition

Matrix multiplication is possible only when

```text
Number of columns of A = Number of rows of B
```

### Example

```text
A = [1 2]
    [3 4]

B = [5 6]
    [7 8]

AB = [19 22]
     [43 50]
```

---

# 5. Matrix Transpose

The transpose of a matrix is obtained by exchanging its rows and columns.

The transpose of matrix

```text
A
```

is written as

```text
Aᵀ
```

If

```text
A = [aᵢⱼ]
```

then

```text
Aᵀ = [aⱼᵢ]
```

### Example

```text
A = [1 2 3
     4 5 6]

Aᵀ = [1 4
      2 5
      3 6]
```

---

# Applications

Matrix operations are used in:

* Solving systems of linear equations
* Data Science
* Machine Learning
* Computer Graphics
* Image Processing
* Scientific Computing
* Artificial Intelligence

---

# Summary

* Matrix addition and subtraction require matrices of the same order.
* Scalar multiplication multiplies every matrix element by the same scalar.
* Matrix multiplication requires the number of columns of the first matrix to equal the number of rows of the second matrix.
* The transpose of a matrix exchanges rows and columns.
