# Error Propagation

## Overview

In practical applications, measurements and numerical computations are rarely exact. Every measurement contains some degree of uncertainty, and every numerical approximation introduces a certain amount of error.

When these measured or approximated values are used in mathematical formulas, the original errors do not disappear. Instead, they influence the computed result. This phenomenon is known as **error propagation**.

Error propagation is one of the most important topics in numerical analysis because it helps us understand how small errors in the input of a mathematical model affect the accuracy of its output.

Understanding error propagation enables us to evaluate the reliability of numerical computations and determine whether an approximation is sufficiently accurate for a particular application.

---

## Why Study Error Propagation?

Suppose the radius of a circle is measured as

```text
5.00 ± 0.01 cm
```

If we use this measurement to compute the area,


Area= Pi * radius square

the computed area will also contain an error.

Similarly,

* a small error in measuring time affects the computed velocity,
* a small error in measuring voltage affects electrical power,
* a small error in measuring temperature affects scientific calculations,
* a small error in a dataset influences the results of statistical analysis and machine learning models.

Error propagation allows us to estimate how these input errors affect the final result.

---

## Learning Objectives

After completing this chapter, you should be able to

* explain the concept of error propagation,
* distinguish propagated error from measurement error,
* estimate propagated error in functions of one variable,
* estimate propagated error in functions of several variables,
* apply differential approximations to estimate errors,
* implement error propagation methods using Python,
* interpret the accuracy of computed results.

---

## Prerequisites

Before studying this chapter, you should understand

* significant figures,
* decimal places,
* absolute error,
* relative error,
* percentage error,
* round-off error,
* truncation error,
* basic differentiation.

---

## Chapter Contents

This chapter is organized into two main sections.

### 1. Error Propagation in Functions of One Variable

In this section, we study how an error in a single input variable affects the output of a function.

### 2. Error Propagation in Functions of Several Variables

In this section, we extend the concept to functions that depend on two or more variables and learn how errors from multiple inputs combine to affect the final result.

---

## Real-World Applications

Error propagation plays an important role in many fields, including

* Numerical analysis
* Engineering
* Physics
* Chemistry
* Statistics
* Data Science
* Machine Learning
* Scientific Computing
* Experimental Research

Understanding error propagation helps us determine how trustworthy a computed result is and whether the accumulated error is acceptable for the intended application.

---

## Final Remark

Every mathematical model begins with inputs. If the inputs contain errors, the outputs will generally contain errors as well.

The goal of error propagation is not to eliminate these errors but to understand, estimate, and control their effect on the final result.
