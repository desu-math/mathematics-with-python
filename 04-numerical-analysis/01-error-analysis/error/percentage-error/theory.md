# Percentage Error

## Introduction

In the previous section, we learned that **relative error** measures the size of the error compared with the true value. Although relative error is useful in numerical analysis, it is usually expressed as a decimal or fraction.

For example,

```text
Relative Error = 0.004
```

While mathematically correct, this value may not be immediately meaningful to many readers.

In everyday life, people often express proportions using **percentages** rather than decimals. For this reason, relative error is commonly multiplied by **100** and expressed as a percentage.

This quantity is called the **percentage error**.

---

# What Is Percentage Error?

**Percentage error** is the relative error expressed as a percentage.

It tells us what percentage of the true value is represented by the error.

Because percentages are easier to interpret, percentage error is one of the most commonly reported measures of accuracy in science, engineering, and experimental work.

---

# Definition

The **percentage error** is defined as

[
\boxed{
\text{Percentage Error}
=======================

\text{Relative Error}
\times100%
}
]

Since

[
\text{Relative Error}
=====================

\frac{|T-A|}{|T|},
]

the percentage error can also be written as

[
\boxed{
E_p
===

\frac{|T-A|}{|T|}
\times100%
}
]

where

* (T) = True value
* (A) = Approximate value
* (E_p) = Percentage error

---

# Why Do We Multiply by 100?

A relative error is a ratio.

Multiplying the ratio by **100** converts it into a percentage.

For example,

[
0.25
====

25%
]

and

[
0.004
=====

0.4%.
]

Expressing errors as percentages makes them easier to understand and compare.

---

# Worked Examples

## Example 1

Find the percentage error if

* True value = 50
* Approximate value = 49.8

### Solution

Step 1: Find the absolute error.

[
|50-49.8|
=========

0.2
]

Step 2: Find the relative error.

[
\frac{0.2}{50}
==============

0.004
]

Step 3: Convert to a percentage.

[
0.004\times100%
===============

0.4%
]

**Answer**

[
\boxed{0.4%}
]

---

## Example 2

Find the percentage error if

* True value = 12.75
* Approximate value = 12.82

### Solution

Absolute error

[
|12.75-12.82|
=============

0.07
]

Relative error

[
\frac{0.07}{12.75}
==================

0.00549
]

Percentage error

[
0.00549\times100%
=================

0.549%
]

---

## Example 3

Approximate

[
\pi\approx3.14
]

Take the true value as

[
3.14159265.
]

Absolute error

[
|3.14159265-3.14|
=================

0.00159265
]

Relative error

[
\frac{0.00159265}{3.14159265}
\approx0.000507
]

Percentage error

[
0.000507\times100%
==================

0.0507%
]

---

# Interpretation of Percentage Error

Percentage error indicates how large the error is as a percentage of the true value.

In general,

* Smaller percentage error → Better approximation.
* Larger percentage error → Less accurate approximation.

For example,

* A percentage error of **0.2%** indicates a highly accurate approximation.
* A percentage error of **15%** indicates a much less accurate approximation.

---

# Advantages of Percentage Error

Percentage error

* is easy to understand,
* allows fair comparison of approximations,
* is independent of the units of measurement,
* is widely used in science, engineering, economics, and experimental work.

---

# Limitation of Percentage Error

Percentage error cannot be computed when the true value is zero because it is based on relative error, which involves division by the true value.

Therefore,

[
T\neq0.
]

---

# Applications of Percentage Error

Percentage error is commonly used in

* Numerical analysis
* Scientific experiments
* Engineering measurements
* Physics
* Chemistry
* Data analysis
* Quality control

It provides an intuitive way to describe the accuracy of measurements and numerical approximations.

---

# Summary

* Percentage error is the relative error expressed as a percentage.
* It is obtained by multiplying the relative error by **100%**.
* It provides an intuitive measure of the quality of an approximation.
* Percentage error is dimensionless and has no physical units.
* Percentage error cannot be calculated when the true value is zero.
