# Introduction to Linear Systems

## Introduction

A **linear system** (or **system of linear equations**) is a collection of two or more linear equations that involve the same unknown variables.

The goal of a linear system is to find values of the variables that satisfy **all equations simultaneously**.

Example:

```text
2x + 3y = 7

4x - y = 5
```

The values of `x` and `y` must make both equations true at the same time.

---

# Linear Equation

A **linear equation** is an equation in which each variable has a power of 1 and variables are not multiplied together.

The general form of a linear equation with n variables is:

```text
a₁x₁ + a₂x₂ + ... + aₙxₙ = b
```

where:

* `x₁, x₂, ..., xₙ` are unknown variables.
* `a₁, a₂, ..., aₙ` are coefficients.
* `b` is the constant term.

Example:

```text
3x + 2y - 5z = 10
```

is a linear equation because:

* Variables have power 1.
* Variables are not multiplied together.
* No nonlinear functions are involved.

---

# Nonlinear Equations

An equation is not linear if it contains:

### Powers greater than 1

Example:

```text
x² + y = 5
```

### Multiplication between variables

Example:

```text
xy + 2 = 6
```

### Nonlinear functions

Examples:

```text
sin(x) + y = 3
```

```text
eˣ + y = 5
```

These equations belong to nonlinear systems, which are studied separately.

---

# System of Linear Equations

A system of linear equations contains multiple linear equations with the same variables.

For example:

```text
2x + y = 5

x - y = 1
```

The solution must satisfy both equations.

Solving:

From the second equation:

```text
x = y + 1
```

Substitute into the first equation:

```text
2(y + 1) + y = 5

3y + 2 = 5

y = 1
```

Therefore:

```text
x = 2
```

The solution is:

```text
(x, y) = (2, 1)
```

---

# Number of Equations and Unknowns

A linear system can contain:

* Fewer equations than unknowns.
* The same number of equations and unknowns.
* More equations than unknowns.

Example:

Two equations with two unknowns:

```text
2x + y = 5

x - y = 1
```

This is called a **2 × 2 system**.

Three equations with three unknowns:

```text
x + y + z = 6

2x - y + z = 3

x + 2y - z = 4
```

This is called a **3 × 3 system**.

---

# Geometric Interpretation

A linear system can be understood geometrically.

## Two Variables

A linear equation with two variables represents a line.

Example:

```text
y = 2x + 1
```

A system of two equations represents two lines.

The solution is the point where the lines intersect.

---

# Types of Solutions

A system of linear equations can have three possible outcomes.

## 1. Unique Solution

The equations intersect at exactly one point.

Example:

```text
x + y = 5

x - y = 1
```

There is only one solution.

Geometrically:

```text
Two lines intersect once.
```

---

## 2. No Solution

The equations represent parallel lines.

Example:

```text
x + y = 3

x + y = 7
```

They have the same slope but never intersect.

Therefore:

```text
No solution exists.
```

---

## 3. Infinite Solutions

The equations represent the same line.

Example:

```text
x + y = 5

2x + 2y = 10
```

Both equations describe the same relationship.

Therefore:

```text
Infinitely many solutions exist.
```

---

# Matrix Connection

A system of linear equations can be represented using matrices.

For example:

```text
2x + 3y = 7

4x - y = 5
```

can be written as:

```text
A X = B
```

where:

Coefficient matrix:

```text
A = [2  3
     4 -1]
```

Variable vector:

```text
X = [x
     y]
```

Constant vector:

```text
B = [7
     5]
```

This representation allows us to use matrix methods such as:

* Gaussian elimination.
* Gauss-Jordan elimination.
* Matrix inverse methods.

---

# Applications

Systems of linear equations appear in:

* Data Science.
* Machine Learning.
* Engineering.
* Physics.
* Economics.
* Computer Graphics.
* Optimization problems.

---

# Summary

* A linear system is a collection of linear equations with the same variables.
* A linear equation has variables only with power one.
* The solution of a system must satisfy all equations simultaneously.
* A system can have one solution, no solution, or infinitely many solutions.
* Linear systems can be represented as matrix equations.
* Matrix methods provide efficient ways to solve large systems.
