# Absolute Error

## Introduction

In numerical analysis, exact values are often replaced by approximate values because of limitations in measurement, computation, or numerical methods. Once an approximation has been obtained, an important question arises:

> **How far is the approximate value from the true value?**

The simplest way to answer this question is by calculating the **absolute error**.

Absolute error measures the magnitude of the difference between the exact (true) value and the approximate value, without considering whether the approximation is greater than or less than the true value.

---

# Why Do We Need Absolute Error?

Suppose two students approximate the value of π.

Student A writes

```text
3.14
```

Student B writes

```text
3.1415
```

Which approximation is better?

Simply looking at the numbers may not be enough. We need a numerical measure that tells us how close each approximation is to the true value.

Absolute error provides this measure.

The smaller the absolute error, the better the approximation.

---

# Definition

The **absolute error** of an approximation is the absolute value of the difference between the true value and the approximate value.

Mathematically,

[
\boxed{\text{Absolute Error} = \left| \text{True Value} - \text{Approximate Value} \right|}
]

where

* **True Value** is the exact value of the quantity.
* **Approximate Value** is the measured or computed value.
* The vertical bars ( | ; | ) denote the **absolute value**.

The absolute value ensures that the error is always **non-negative**.

---

# Why Do We Use Absolute Value?

Suppose the true value is

```text
20
```

and two approximations are

```text
19
```

and

```text
21
```

Without taking the absolute value,

* Error of 19 =

```text
20 − 19 = 1
```

* Error of 21 =

```text
20 − 21 = −1
```

Although one error is positive and the other is negative, **both approximations are equally far from the true value**.

Taking the absolute value gives

```text
|1| = 1
```

and

```text
|-1| = 1
```

Therefore, both approximations have the same absolute error.

This shows that absolute error measures **distance**, not direction.

---

# Formula

If

* (T) = True value
* (A) = Approximate value

then

[
\boxed{E_a = |T - A|}
]

where

* (E_a) denotes the absolute error.

---

# Worked Examples

## Example 1

Find the absolute error if

* True value = 50
* Approximate value = 49.8

### Solution

[
E_a = |50-49.8|
]

[
E_a = |0.2|
]

[
\boxed{E_a=0.2}
]

Therefore, the approximation differs from the true value by **0.2 units**.

---

## Example 2

Find the absolute error if

* True value = 12.75
* Approximate value = 12.82

### Solution

[
E_a=|12.75-12.82|
]

[
E_a=|-0.07|
]

[
\boxed{E_a=0.07}
]

Although the approximate value is larger than the true value, the absolute error is still positive.

---

## Example 3

Approximate

[
\pi \approx 3.14
]

The true value is approximately

```text
3.14159265
```

Absolute error

[
E_a=|3.14159265-3.14|
]

[
\boxed{E_a\approx0.00159265}
]

---

# Interpretation of Absolute Error

Absolute error tells us **how far** an approximation is from the true value.

For example,

An absolute error of

```text
0.001
```

means the approximation differs from the true value by only one thousandth.

Generally,

* Smaller absolute error → Better approximation
* Larger absolute error → Less accurate approximation

---

# Limitations of Absolute Error

Although absolute error is easy to understand, it has an important limitation.

Consider two approximations.

### Case 1

True value

```text
1000
```

Approximate value

```text
999
```

Absolute error

```text
1
```

---

### Case 2

True value

```text
2
```

Approximate value

```text
1
```

Absolute error

```text
1
```

In both cases, the absolute error is **1**.

However, the second approximation is much worse because an error of **1** is much more significant when the true value is **2** than when it is **1000**.

Therefore, absolute error alone does not indicate how **large the error is relative to the size of the true value**.

This limitation motivates the next concept:

> **Relative Error**

---

# Applications of Absolute Error

Absolute error is widely used in

* Numerical analysis
* Scientific computing
* Engineering
* Experimental science
* Measurement and instrumentation
* Computer simulations

It provides a simple measure of the difference between an exact value and its approximation.

---

# Summary

* Absolute error measures the distance between the true value and the approximate value.
* It is always non-negative because the absolute value is used.
* A smaller absolute error indicates a better approximation.
* Absolute error does not account for the size of the true value.
* The limitation of absolute error leads naturally to the concept of **relative error**, which measures the error in proportion to the true value.
