# Introduction to Matrices

## Introduction

A **matrix** is a rectangular arrangement of numbers, symbols, or expressions organized into **rows** and **columns**.

Matrices provide a convenient way to store, organize, and manipulate data. They are one of the fundamental objects in Linear Algebra and are widely used in Data Science, Machine Learning, Computer Graphics, Engineering, and Scientific Computing.

---

# Matrix Notation

Matrices are usually denoted by **capital letters**, such as:

```text
A, B, C
```

A general matrix **A** is written as

```text
        Columns
          1    2      ⋯     n
       ┌─────────────────────────┐
Row 1  │ a11  a12   ⋯    a1n      │
Row 2  │ a21  a22   ⋯    a2n      │
  ⋮    │  ⋮    ⋮     ⋱     ⋮        │
Row m  │ am1  am2   ⋯    amn      │
       └─────────────────────────┘
```

Each value in the matrix is called an **element** (or **entry**).

The notation

```text
aij
```

represents the element located at:

* row **i**
* column **j**

For example,

```text
A =
[ 2   5
  7   1 ]
```

contains four elements:

```text
a11 = 2
a12 = 5
a21 = 7
a22 = 1
```

---

# Rows and Columns

A **row** is a horizontal collection of elements.

Example:

```text
[3  4  5]
```

A **column** is a vertical collection of elements.

Example:

```text
[3
 4
 5]
```

The number of rows and columns determines the size of a matrix.

---

# Order (Dimension) of a Matrix

The **order** (or **dimension**) of a matrix is written as

```text
m × n
```

where:

* **m** = number of rows
* **n** = number of columns

Examples:

```text
2 × 3

[1 2 3
 4 5 6]
```

has

* 2 rows
* 3 columns

---

```text
3 × 2

[1 2
 3 4
 5 6]
```

has

* 3 rows
* 2 columns

---

# Matrix Representation in Python

In NumPy, a matrix is represented as a two-dimensional array.

Example:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])
```

Each inner list represents one row of the matrix.

---

# Matrix Indexing

In mathematics,

```text
a11
```

means:

* first row
* first column

In Python, indexing starts from **0**.

Therefore,

```python
A[0, 0]
```

returns the first element.

Similarly,

```python
A[1, 0]
```

returns the element in the second row and first column.

This difference between mathematical notation and Python indexing is important to remember.

---

# Applications

Matrices are used in:

* Solving systems of linear equations
* Data Science
* Machine Learning
* Artificial Intelligence
* Image Processing
* Computer Graphics
* Scientific Computing

---

# Summary

* A matrix is a rectangular arrangement of elements in rows and columns.
* Matrix elements are identified by their row and column positions.
* The order of a matrix is written as **m × n**.
* NumPy represents matrices as two-dimensional arrays.
* Matrix indexing in Python starts at **0**, while mathematical indexing starts at **1**.
