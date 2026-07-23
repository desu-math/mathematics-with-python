# Systems of Linear Equations

> **Solving mathematical problems using equations, matrices, and computational methods.**

## Introduction

A **system of linear equations** is a collection of two or more linear equations involving the same unknown variables.

For example:

```text
2x + 3y = 7

4x - y = 5
```

The goal is to find values of the unknown variables that satisfy all equations simultaneously.

Systems of linear equations are one of the most important applications of Linear Algebra and provide the foundation for many areas of mathematics, engineering, and Data Science.

---

# Learning Objectives

After completing this chapter, you should be able to:

* Understand the concept of linear systems.
* Represent systems using matrices.
* Convert equations into augmented matrices.
* Solve systems using elimination methods.
* Understand different types of solutions.
* Implement solving methods using Python.

---

# Topics Covered

```text
01. Introduction to Linear Systems

02. Matrix Representation of Linear Systems

03. Gaussian Elimination

04. Gauss-Jordan Elimination

05. Solving Systems Using Matrix Inverse
```

---

# Learning Structure

Each computational topic includes:

```text
topic/

├── theory.md
├── algorithm.md
└── example.py
```

The theory explains the mathematics, the algorithm describes the computational steps, and the Python implementation demonstrates how the method works.

---

# Mathematical Representation

A system of linear equations can be written in matrix form:

```text
AX = B
```

where:

* **A** → coefficient matrix
* **X** → vector of unknown variables
* **B** → constant vector

Example:

```text
2x + 3y = 7
4x - y  = 5
```

can be written as:

```text
[2  3] [x]   [7]
[4 -1] [y] = [5]
```

---

# Types of Solutions

A linear system can have:

### 1. Unique Solution

There is exactly one solution.

Example:

```text
x = 2
y = 1
```

---

### 2. No Solution

The equations are inconsistent.

Graphically, the lines do not intersect.

---

### 3. Infinite Solutions

The equations represent the same relationship.

There are infinitely many solutions.

---

# Python Libraries

This chapter introduces:

* **NumPy** for matrix representation and computation.
* **SymPy** for symbolic mathematical operations (when needed).

---

# Applications

Systems of linear equations are used in:

* Data Science
* Machine Learning
* Linear Regression
* Computer Graphics
* Engineering Problems
* Physics
* Optimization

---

# Data Science Connection

Many machine learning algorithms require solving systems of equations.

For example, linear regression uses matrix equations involving:

* Matrix multiplication
* Transpose
* Inverse
* Systems of equations

The concepts learned in this chapter become the foundation for understanding these algorithms.

---

# Summary

In this chapter, you will learn how to transform mathematical problems into matrix form and solve them using both classical mathematical methods and Python implementations.

Systems of linear equations provide the bridge between fundamental Linear Algebra concepts and real-world computational applications.
