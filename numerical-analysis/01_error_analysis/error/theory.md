# Error

## Introduction

Numerical analysis is concerned with finding approximate solutions to mathematical problems. Unlike pure mathematics, where exact answers are often possible, numerical methods usually produce **approximations** because computers and measuring instruments have limited precision.

Since approximations are used instead of exact values, there is almost always a difference between the computed result and the true value.

This difference is called the **error**.

Understanding error is one of the most important topics in numerical analysis because the reliability of a numerical result depends on how large or small its error is.

---

# Why Do Errors Occur?

Errors occur because exact values are not always available or cannot always be represented.

For example,

```text
π = 3.141592653589793...
```

The decimal expansion of π continues forever.

A computer cannot store infinitely many digits, so it may store

```text
3.14159
```

instead.

The difference between the exact value and the stored value is an example of numerical error.

Similarly,

```text
√2 = 1.414213562373...
```

is an irrational number.

In practice, we often use

```text
1.4142
```

which introduces a small error.

---

# Definition of Error

Suppose

* **True value** = the exact value of a quantity.
* **Approximate value** = the value obtained from measurement or computation.

Then,

> **Error is the difference between the true value and the approximate value.**

Mathematically,

```text
Error = True Value − Approximate Value
```

Sometimes the order is reversed depending on the context, but in numerical analysis we are usually interested in the **magnitude** of the difference rather than its sign.

---

# Understanding Error Through an Example

Suppose the exact value is

```text
50
```

and a numerical method gives

```text
49.8
```

The error is

```text
50 − 49.8 = 0.2
```

This means the computed value differs from the true value by **0.2 units**.

---

# Is Error Always Bad?

The word "error" often suggests that something is wrong.

In numerical analysis, however, **error does not necessarily mean a mistake**.

It simply indicates that a value is **approximate rather than exact**.

For example,

```text
π ≈ 3.14
```

is not incorrect.

It is an approximation with a small error.

Therefore,

> An error measures the difference between an exact value and its approximation; it does not necessarily imply that the computation was performed incorrectly.

---

# Sources of Error

Errors may arise from different sources.

The most common sources are:

### 1. Measurement Errors

Measurements made with instruments are never perfectly exact.

Example:

A ruler measures a length as

```text
12.4 cm
```

The actual length might be

```text
12.43 cm.
```

---

### 2. Round-off Errors

Computers often round numbers because only a limited number of digits can be stored.

Example:

```text
1/3 = 0.333333...
```

stored as

```text
0.3333
```

---

### 3. Truncation Errors

Some numerical methods replace an infinite mathematical process with a finite one.

Example:

Approximating

```text
sin(x)
```

using only the first few terms of its Taylor series.

---

### 4. Human Errors

Errors may also occur because of mistakes in calculations, typing, or recording data.

These are generally **not** the focus of numerical analysis.

Numerical analysis mainly studies errors caused by approximation and finite computation.

---

# Why Do We Study Errors?

Understanding error helps us to:

* evaluate the reliability of numerical results,
* compare different numerical methods,
* estimate how close an approximation is to the true value,
* determine whether an approximation is sufficiently accurate for practical use.

Without error analysis, we cannot judge whether a computed answer should be trusted.

---

# Types of Errors

In this chapter, we will study:

* Absolute Error
* Relative Error
* Percentage Error
* Round-off Error
* Truncation Error
* Propagation of Error
* Estimated Error Bounds

Each type describes a different aspect of how numerical errors arise or how they are measured.

---

# Summary

* Numerical methods usually produce approximate rather than exact results.
* The difference between the true value and the approximate value is called the error.
* Errors arise because of limited precision, measurements, and approximation methods.
* In numerical analysis, an error does not necessarily indicate a mistake; it often reflects the unavoidable limitations of computation.
* Studying errors allows us to assess the accuracy and reliability of numerical results.
