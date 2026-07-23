# Round-off Error

## Introduction

In the previous sections, we learned how to measure the difference between a true value and its approximation using **absolute error**, **relative error**, and **percentage error**.

A natural question now arises:

> **Where do these errors come from?**

One of the most common sources of error in numerical computation is **rounding**.

Many numbers cannot be represented exactly because they contain infinitely many decimal digits or because computers have limited storage for numbers. To make calculations practical, these numbers are often **rounded** to a specified number of decimal places or significant figures.

Although rounding simplifies calculations, it also introduces a small difference between the exact value and the rounded value. This difference is called the **round-off error**.

Understanding round-off error is essential because almost every numerical computation performed by a computer involves rounding.

---

# What Is Rounding?

**Rounding** is the process of replacing a number with a nearby value that has fewer decimal places or fewer significant figures while remaining as close as possible to the original number.

For example,

| Exact Value | Rounded Value |
| ----------- | ------------: |
| 3.14159265  |          3.14 |
| 8.7463      |          8.75 |
| 125.678     |           126 |

The rounded value is easier to use, but it is not exactly the same as the original value.

---

# What Is Round-off Error?

A **round-off error** is the error introduced when an exact value is replaced by its rounded approximation.

It is the difference between the original value and the rounded value.

### Definition

> **Round-off error** is the difference between the exact value and the value obtained after rounding.

Mathematically,

[
\boxed{
\text{Round-off Error}
======================

## \text{Exact Value}

\text{Rounded Value}
}
]

In practice, we are usually interested in the magnitude of the error, so we often use

[
\boxed{
\text{Round-off Error}
======================

\left|
\text{Exact Value}
------------------

\text{Rounded Value}
\right|
}
]

which is simply the **absolute error caused by rounding**.

---

# Why Does Round-off Error Occur?

Round-off error occurs because it is often impossible or impractical to keep every digit of a number.

Common reasons include:

### 1. Infinite Decimal Expansions

Some numbers have infinitely many decimal digits.

For example,

[
\pi
===

3.141592653589793\ldots
]

Since the decimal expansion never ends, we must use an approximation such as

```text
3.14
```

or

```text
3.1416.
```

---

### 2. Irrational Numbers

Numbers such as

[
\sqrt{2},
\sqrt{3},
e
]

have infinitely many non-repeating decimal digits.

Their exact decimal representations cannot be stored completely.

---

### 3. Limited Computer Memory

Computers store numbers using a fixed number of binary digits (bits).

Because memory is finite, only a limited number of digits can be stored.

Consequently, many numbers must be rounded before they are stored or used in calculations.

---

### 4. Simplifying Manual Calculations

Even when performing calculations by hand, people often round numbers to make arithmetic easier.

For example,

Instead of multiplying

```text
19.98 × 5.03
```

someone may estimate

```text
20 × 5 = 100.
```

This simplification introduces round-off error.

---

# Examples of Round-off Error

## Example 1

Round

```text
3.14159265
```

to two decimal places.

Rounded value:

```text
3.14
```

Round-off error:

[
|3.14159265-3.14|
=================

0.00159265
]

---

## Example 2

Round

```text
12.768
```

to one decimal place.

Rounded value:

```text
12.8
```

Round-off error:

[
|12.768-12.8|
=============

0.032
]

---

## Example 3

Round

```text
245.678
```

to the nearest whole number.

Rounded value:

```text
246
```

Round-off error:

[
|245.678-246|
=============

0.322
]

---

# Round-off Error in Computers

Round-off error is especially important in computer programming.

Computers cannot represent most real numbers exactly because they use finite binary representations.

For example,

the decimal number

```text
0.1
```

cannot be represented exactly in binary floating-point arithmetic.

Instead, the computer stores a nearby value.

Although the stored value is extremely close to 0.1, it is not exactly equal to 0.1.

During long computations involving thousands or millions of operations, these tiny round-off errors can accumulate and affect the final result.

---

# Factors Affecting Round-off Error

The size of the round-off error depends on several factors.

### Number of Decimal Places

Keeping more decimal places generally reduces round-off error.

Example:

| Rounded Value | Round-off Error |
| ------------: | --------------: |
|           3.1 |          Larger |
|          3.14 |         Smaller |
|        3.1416 |    Even smaller |

---

### Number of Significant Figures

Retaining more significant figures usually decreases the round-off error.

---

### Repeated Computations

Repeated arithmetic operations may accumulate round-off errors, causing the final result to differ noticeably from the exact value.

---

# Advantages of Rounding

Although rounding introduces error, it also provides important benefits.

* Simplifies calculations.
* Makes numbers easier to read and communicate.
* Reduces storage requirements.
* Improves computational efficiency.

Therefore, rounding is an essential part of numerical computation.

---

# Minimizing Round-off Error

Round-off error cannot usually be eliminated, but it can often be reduced by:

* retaining more decimal places,
* retaining more significant figures,
* avoiding unnecessary repeated rounding,
* using higher-precision arithmetic when required.

---

# Applications of Round-off Error

Round-off error is important in

* Numerical analysis
* Scientific computing
* Computer programming
* Engineering simulations
* Financial calculations
* Machine learning
* Data science

Understanding round-off error helps ensure that numerical results are reliable and sufficiently accurate.

---

# Summary

* Round-off error arises when an exact value is replaced by a rounded value.
* It is the difference between the exact value and the rounded value.
* Round-off error occurs because of infinite decimal expansions, irrational numbers, limited computer precision, and practical rounding during calculations.
* Although unavoidable, round-off error can often be reduced by retaining more digits and avoiding unnecessary rounding.
* In long numerical computations, many small round-off errors may accumulate, making it important to understand and control them.
