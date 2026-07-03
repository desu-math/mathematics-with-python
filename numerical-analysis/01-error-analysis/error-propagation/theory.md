# Theory of Error Propagation

## Introduction

In the previous chapters, we studied several types of numerical errors, including absolute error, relative error, percentage error, round-off error, and truncation error. Each of these describes either the size of an error or its source.

A natural question now arises:

> **What happens to an error after it enters a mathematical calculation?**

Suppose you measure the length of a rectangle with a small measurement error. If you use that measurement to calculate the rectangle's area, will the area also contain an error?

The answer is **yes**.

In fact, almost every mathematical computation transfers the errors present in its input values to the final result. This process is called **error propagation**.

Understanding how errors propagate is one of the central objectives of numerical analysis because it allows us to estimate the reliability of computed results.

---

## What Is Error Propagation?

**Error propagation** is the process by which errors in one or more input values influence the value of a computed result.

Whenever approximate values are substituted into a mathematical function, the resulting output generally differs from the exact value because the input errors are carried through the computation.

---

## Definition

> **Error propagation** is the transmission of errors from the input variables of a mathematical function to its output.

These input errors may arise from

* measurement errors,
* round-off errors,
* truncation errors,
* instrument limitations,
* observational uncertainties,
* numerical approximations.

Regardless of their source, the function transforms these input errors into an output error.

---

## General Idea

Suppose a function is written as
y=f(x).

If the input value changes from
x

to
x + delta x,

then the output changes from


f(x)

to


f(x+delta x).

The difference between these two outputs represents the propagated error in the function.

The main objective of error propagation is to estimate this output error using mathematical techniques such as differentiation.

---

## Types of Error Propagation

Depending on the number of input variables, error propagation is usually divided into two categories.

### Error Propagation in a Function of One Variable

The output depends on a single input variable.

Examples include:
y=x^2
y=1/sin x
y=e^x

---

### Error Propagation in Functions of Several Variables

The output depends on two or more variables.

Examples include:
z=x+y,
z=xy
z=1/xy
V=lwh

In these cases, errors from multiple variables contribute to the final error.

---

## Importance of Error Propagation

Understanding error propagation enables us to

* estimate the accuracy of numerical results,
* determine the sensitivity of mathematical models,
* compare different numerical methods,
* identify variables that contribute most to the overall error,
* design more reliable computational algorithms.

---

## Applications

Error propagation is widely used in

* numerical analysis,
* engineering,
* scientific computing,
* physics,
* chemistry,
* statistics,
* machine learning,
* data science,
* economics,
* experimental research.

It is an essential tool whenever numerical computations involve uncertain or approximate data.

---

## Summary

* Error propagation describes how input errors affect the output of a mathematical function.
* Input errors may originate from measurement, rounding, truncation, or other approximations.
* Every mathematical function transforms input errors into output errors.
* Error propagation can be studied for functions of one variable or functions of several variables.
* The next sections develop mathematical techniques for estimating propagated errors using differential calculus.
