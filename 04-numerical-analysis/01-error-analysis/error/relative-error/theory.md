# Relative Error

## Introduction

In the previous section, we learned that **absolute error** measures the difference between the true value and the approximate value. Although it tells us how far an approximation is from the true value, it does not indicate whether that difference is **large or small compared with the size of the true value**.

For example, consider the following two approximations.

### Case 1

* True value = 1000
* Approximate value = 999

Absolute error:

[
|1000 - 999| = 1
]

### Case 2

* True value = 2
* Approximate value = 1

Absolute error:

[
|2 - 1| = 1
]

In both cases, the absolute error is **1**.

However, the two approximations do not have the same quality.

* In the first case, an error of **1** is very small compared with the true value of **1000**.
* In the second case, an error of **1** is very large compared with the true value of **2**.

This shows that **absolute error alone cannot always describe the quality of an approximation.**

To compare errors fairly for quantities of different sizes, we use **relative error**.

---

# What Is Relative Error?

**Relative error** is the ratio of the absolute error to the magnitude of the true value.

It tells us how large the error is **relative to the true value**.

Instead of measuring the error in units, relative error expresses the error as a fraction of the true value.

---

# Definition

The **relative error** of an approximation is defined as

[
\boxed{\text{Relative Error}
============================

\frac{\text{Absolute Error}}{|\text{True Value}|}}
]

Since

[
\text{Absolute Error}=|T-A|,
]

the formula may also be written as

[
\boxed{
E_r=
\frac{|T-A|}{|T|}
}
]

where

* (T) = True value
* (A) = Approximate value
* (E_r) = Relative error

The denominator uses the absolute value of the true value so that the relative error is always non-negative.

---

# Why Do We Divide by the True Value?

Suppose two people make an error of **5 meters**.

### Person A

Measures the distance from one classroom to another.

True distance:

```text
20 m
```

Absolute error:

```text
5 m
```

Relative error:

[
\frac{5}{20}=0.25
]

---

### Person B

Measures the distance between two cities.

True distance:

```text
500 km
```

Absolute error:

```text
5 m
```

Relative error:

[
\frac{5}{500000}=0.00001
]

Although both measurements have the same absolute error, the second measurement is much better because the error is extremely small compared with the total distance.

This illustrates why relative error is often a more meaningful measure than absolute error.

---

# Worked Examples

## Example 1

Find the relative error if

* True value = 50
* Approximate value = 49.8

### Solution

Step 1: Find the absolute error.

[
|50-49.8|=0.2
]

Step 2: Divide by the true value.

[
E_r=\frac{0.2}{50}
]

[
E_r=0.004
]

**Answer**

[
\boxed{E_r=0.004}
]

---

## Example 2

Find the relative error if

* True value = 12.75
* Approximate value = 12.82

### Solution

Absolute error

[
|12.75-12.82|=0.07
]

Relative error

[
E_r=\frac{0.07}{12.75}
]

[
E_r\approx0.00549
]

---

## Example 3

Approximate

[
\pi \approx 3.14
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

Thus, the approximation has a relative error of approximately

[
0.000507.
]

---

# Interpretation of Relative Error

Relative error describes the size of the error compared with the size of the true value.

In general,

* Smaller relative error → Better approximation.
* Larger relative error → Less accurate approximation.

Unlike absolute error, relative error allows us to compare approximations of quantities having different magnitudes.

---

# Advantages of Relative Error

Relative error

* compares errors fairly for quantities of different sizes,
* provides a dimensionless measure (it has no units),
* is widely used to evaluate the quality of numerical approximations.

---

# Limitation of Relative Error

Relative error cannot be computed when the true value is zero because division by zero is undefined.

Therefore, the formula

[
E_r=\frac{|T-A|}{|T|}
]

is valid only when

[
T\neq0.
]

---

# Applications of Relative Error

Relative error is widely used in

* Numerical analysis
* Scientific computing
* Engineering
* Physics
* Experimental sciences
* Machine precision analysis

It is one of the most common measures for evaluating the accuracy of numerical computations.

---

# Summary

* Relative error measures the size of the error compared with the true value.
* It is obtained by dividing the absolute error by the magnitude of the true value.
* Relative error has no units because it is a ratio.
* It provides a better basis for comparing approximations than absolute error alone.
* Relative error is often converted into a percentage, leading to the next concept: **percentage error**.
