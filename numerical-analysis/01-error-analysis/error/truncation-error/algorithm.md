# General Procedure for Determining Truncation Error

Unlike absolute error, relative error, and percentage error, **truncation error does not have a single universal algorithm**. This is because truncation error depends on the numerical method being used.

However, the general procedure for determining truncation error is the same in most applications.

---

## Algorithm

**Step 1**

Identify the exact mathematical expression or process.

**Step 2**

Choose an approximation by truncating the process.

For example,

* use only the first few terms of an infinite series,
* replace a limit with a finite difference,
* use a finite number of subintervals for numerical integration.

**Step 3**

Compute the approximate value.

**Step 4**

Obtain the exact value (if it is known) or a highly accurate reference value.

**Step 5**

Calculate the truncation error.

[
\text{Truncation Error}
=======================

\left|
\text{Exact Value}
------------------

\text{Approximate Value}
\right|
]

**Step 6**

Interpret the result.

A smaller truncation error indicates that the approximation is closer to the exact mathematical result.

---

## Important Note

The way the approximation is computed depends on the numerical method being used.

Therefore, each numerical method has its own specific algorithm for producing the approximation, while the general procedure above explains how the truncation error is determined once an approximation has been obtained.

For e^x
Start

Input x.
Input the number of Taylor series terms (n).

Set approximation = 0.

Repeat for k = 0 to n−1
    approximation = approximation + x^k / k!

Compute the exact value using exp(x).

Compute truncation error:
    |exact value − approximation|

Display
    Exact value
    Approximate value
    Truncation error

End
