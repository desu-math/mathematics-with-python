# Truncation Error

## Introduction

In the previous section, we studied **round-off error**, which arises when an exact number is replaced by a rounded value. Round-off error is caused by representing numbers with a limited number of digits.

However, not all numerical errors arise from rounding. In many mathematical and numerical computations, we deliberately replace an exact mathematical process with an approximation that is easier to compute.

For example,

* replacing an infinite series with only its first few terms,
* approximating a derivative using finite differences,
* approximating an integral by dividing the interval into a finite number of subintervals.

These approximations simplify computations but introduce another type of error known as **truncation error**.

Unlike round-off error, truncation error is not caused by storing numbers with limited precision. Instead, it is caused by **terminating (truncating) a mathematical process before it is completed exactly**.

---

# What Does "Truncate" Mean?

The word **truncate** means **to cut off or shorten**.

In numerical analysis, truncation means replacing an exact process that may require infinitely many operations with a finite number of operations.

For example,

instead of evaluating

[
e^x
===

1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\cdots
]

we may keep only the first three terms:

[
e^x
\approx
1+x+\frac{x^2}{2!}.
]

Although this approximation is easier to compute, it is not exact because the remaining terms have been omitted.

The error caused by omitting these terms is called the **truncation error**.

---

# What Is Truncation Error?

A **truncation error** is the error introduced when an exact mathematical procedure is replaced by an approximate one by discarding part of the process.

It represents the difference between the exact mathematical result and the approximation obtained after truncation.

---

# Definition

> **Truncation error** is the difference between the exact value obtained from a complete mathematical process and the approximate value obtained after truncating that process.

Mathematically,

[
\boxed{
\text{Truncation Error}
=======================

\left|
\text{Exact Value}
------------------

\text{Approximate Value}
\right|
}
]

Notice that this formula has the same mathematical form as absolute error. The difference lies in **the source of the approximation**.

For truncation error, the approximation results from stopping a mathematical process early.

---

# Why Does Truncation Error Occur?

Truncation error occurs whenever an exact mathematical procedure is replaced by a finite approximation.

Common causes include:

### 1. Truncating Infinite Series

Many mathematical functions are represented by infinite series.

For example,

[
e^x
===

1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
]

Since infinitely many terms cannot be computed in practice, only a finite number of terms are used.

---

### 2. Approximating Derivatives

The derivative

[
f'(x)
]

is defined using a limit.

In numerical analysis, it is often approximated by

[
\frac{f(x+h)-f(x)}{h}.
]

Because this approximation replaces the exact limit with a finite value of (h), a truncation error is introduced.

---

### 3. Approximating Integrals

Many definite integrals cannot be evaluated exactly.

Numerical methods such as the trapezoidal rule and Simpson's rule approximate the integral using a finite number of subintervals.

This approximation introduces truncation error.

---

### 4. Solving Differential Equations

Numerical methods such as Euler's method approximate the solution of differential equations using finite step sizes.

These approximations also produce truncation error.

---

# Examples of Truncation Error

## Example 1

Approximate

[
e^1
]

using only the first three terms of its Taylor series.

Approximation:

[
1+1+\frac{1}{2}
===============

2.5
]

Exact value:

[
e
\approx
2.718281828
]

Truncation error:

[
|2.718281828-2.5|
=================

0.218281828.
]

---

## Example 2

Approximate

[
\sin(0.2)
]

using

[
\sin x
\approx
x.
]

Approximation:

[
0.2
]

Exact value:

[
\sin(0.2)
\approx
0.198669331.
]

Truncation error:

[
|0.198669331-0.2|
\approx
0.001330669.
]

---

# Truncation Error versus Round-off Error

Although both are numerical errors, they arise from different causes.

| Round-off Error                           | Truncation Error                                                                                         |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Caused by rounding numbers.               | Caused by shortening a mathematical process.                                                             |
| Depends on the number of digits retained. | Depends on the approximation method used.                                                                |
| Reduced by using higher precision.        | Reduced by improving the numerical approximation (for example, using more terms or a smaller step size). |

---

# How Can Truncation Error Be Reduced?

Truncation error can often be reduced by improving the approximation.

For example,

* using more terms of a series,
* decreasing the step size in numerical methods,
* increasing the number of subintervals in numerical integration,
* using a higher-order numerical method.

Although these approaches usually reduce truncation error, they may increase the amount of computation required.

---

# Applications of Truncation Error

Understanding truncation error is essential in

* Numerical analysis,
* Scientific computing,
* Engineering,
* Computational physics,
* Machine learning,
* Data science.

It helps determine how accurate a numerical approximation is and guides the choice of appropriate numerical methods.

---

# Summary

* Truncation error arises when an exact mathematical process is replaced by a finite approximation.
* It is caused by terminating a process early rather than by rounding numbers.
* Common sources include truncated series, finite-difference approximations, numerical integration, and numerical solutions of differential equations.
* Truncation error can usually be reduced by using a better approximation, such as more terms in a series or a smaller step size.
* Unlike round-off error, truncation error is related to the numerical method itself rather than the precision of number representation.
