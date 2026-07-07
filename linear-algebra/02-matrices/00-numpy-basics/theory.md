# NumPy Basics

## Introduction

**NumPy** (Numerical Python) is the fundamental Python library for numerical computing. It provides efficient data structures and mathematical functions for working with arrays, matrices, and numerical data.

NumPy is widely used in Data Science, Machine Learning, Artificial Intelligence, Scientific Computing, and Engineering. Many other Python libraries, such as Pandas, SciPy, and Scikit-learn, are built on top of NumPy.

---

# Why Use NumPy?

Although Python lists can store numerical data, they are not designed for efficient mathematical computations.

NumPy provides:

* Faster numerical computations.
* Efficient memory usage.
* Built-in support for arrays and matrices.
* A large collection of mathematical functions.
* Easy integration with scientific Python libraries.

---

# Installing NumPy

Install NumPy using `pip`:

```bash
pip install numpy
```

Verify the installation:

```bash
pip show numpy
```

---

# Importing NumPy

The standard way to import NumPy is:

```python
import numpy as np
```

Here, **`np`** is an alias for the NumPy library. Using `np` is a widely accepted convention in the Python community.

---

# NumPy Arrays

The primary data structure in NumPy is the **ndarray** (N-dimensional array).

Unlike Python lists, NumPy arrays:

* Store elements of the same data type.
* Support fast mathematical operations.
* Can represent one-dimensional, two-dimensional, and higher-dimensional data.

---

# Creating Arrays

A one-dimensional array:

```python
np.array([1, 2, 3, 4])
```

A two-dimensional array (matrix):

```python
np.array([
    [1, 2],
    [3, 4]
])
```

---

# Accessing Array Elements

Elements are accessed using indices.

For a one-dimensional array:

```python
a[0]
```

returns the first element.

For a two-dimensional array:

```python
A[1, 0]
```

returns the element in the second row and first column.

---

# Basic Array Properties

Some useful attributes are:

| Attribute | Description               |
| --------- | ------------------------- |
| `ndim`    | Number of dimensions      |
| `shape`   | Size of each dimension    |
| `size`    | Total number of elements  |
| `dtype`   | Data type of the elements |

Example:

```python
A.shape
```

returns the dimensions of the array.

---

# Basic Mathematical Operations

NumPy performs element-wise operations.

Examples:

```python
A + B
```

```python
A - B
```

```python
A * 2
```

More advanced matrix operations will be covered in later lessons.

---

# Applications

NumPy is used in:

* Linear Algebra
* Statistics
* Data Science
* Machine Learning
* Scientific Computing
* Image Processing
* Artificial Intelligence

---

# Summary

* **NumPy** stands for **Numerical Python**.
* It is the standard Python library for numerical computing.
* The main NumPy data structure is the **ndarray**.
* NumPy arrays are faster and more efficient than Python lists for mathematical computations.
* NumPy provides the foundation for many scientific and data science libraries.
