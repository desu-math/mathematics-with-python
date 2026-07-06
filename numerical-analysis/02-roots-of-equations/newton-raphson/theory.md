# Newton–Raphson Method

## Introduction

The **Newton–Raphson Method**, commonly called **Newton's Method**, is an open numerical method for finding an approximate root of a nonlinear equation

```text
f(x) = 0
```

Unlike the Bisection and False Position methods, the Newton–Raphson Method does **not** require an interval containing the root. Instead, it starts with a single initial approximation and repeatedly improves it by using the **tangent line** to the curve.

Because it uses the exact derivative of the function, the Newton–Raphson Method usually converges much faster than the Bisection, False Position, and Secant methods when the initial approximation is sufficiently close to the root.

---

# Evolution of Root-Finding Methods

The Newton–Raphson Method is the next natural step in the evolution of numerical root-finding methods.

### 1. Bisection Method

Uses the midpoint of an interval.

```text
Next approximation = Midpoint
```

---

### 2. False Position Method

Uses the x-intercept of the secant line joining the interval endpoints.

---

### 3. Secant Method

Uses the x-intercept of the secant line joining the two most recent approximations.

---

### 4. Newton–Raphson Method

Instead of approximating the slope by a secant line, the Newton–Raphson Method uses the **exact slope of the tangent line**, obtained from the derivative.

Thus,

```text
Secant Line
        ↓
Tangent Line
```

This simple improvement greatly increases the speed of convergence.

---

# Basic Idea

Suppose the current approximation of the root is

```text
x₀
```

Evaluate the function at this point to obtain

```text
(x₀, f(x₀))
```

Draw the tangent line to the curve at this point.

The point where the tangent line intersects the x-axis becomes the next approximation,

```text
x₁
```

The same process is repeated:

* Draw the tangent at `(x₁, f(x₁))`.
* Its x-intercept becomes `x₂`.
* Continue until the desired accuracy is achieved.

---

# Geometric Interpretation

Insert a figure showing:

* the curve `y = f(x)`,
* the point `(x₀, f(x₀))`,
* the tangent line at this point,
* the x-axis,
* the tangent intersecting the x-axis at `x₁`.

This figure should clearly show that the tangent line provides the next approximation.

---

# Derivation of the Newton–Raphson Formula

The equation of the tangent line to the curve at the point

```text
(x₀, f(x₀))
```

is

```text
y − f(x₀) = f′(x₀)(x − x₀)
```

The next approximation is obtained where the tangent line intersects the x-axis.

Since every point on the x-axis satisfies

```text
y = 0
```

substitute

```text
y = 0
```

into the tangent equation.

```text
0 − f(x₀) = f′(x₀)(x − x₀)
```

Simplifying,

```text
−f(x₀) = f′(x₀)(x − x₀)
```

Divide both sides by

```text
f′(x₀)
```

to obtain

```text
x − x₀ = −f(x₀) / f′(x₀)
```

Therefore,

```text
x = x₀ − f(x₀) / f′(x₀)
```

The next approximation is denoted by

```text
x₁
```

Hence,

```text
x₁ = x₀ − f(x₀) / f′(x₀)
```

Repeating the same process for every iteration gives the general iterative formula

```text
xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)
```

This is the fundamental equation of the Newton–Raphson Method.

---

# Why Does the Method Work?

Near the root, a smooth function can be closely approximated by its tangent line.

Instead of solving the original nonlinear equation, the Newton–Raphson Method solves the much simpler linear equation represented by the tangent.

Each new tangent is drawn at a better approximation, causing the estimates to move rapidly toward the root.

---

# Convergence

When the initial approximation is sufficiently close to the root and

```text
f′(x) ≠ 0
```

near the root, the Newton–Raphson Method usually converges **quadratically**.

Quadratic convergence means that once the approximations are close to the root, the number of correct digits approximately doubles with each iteration.

This makes the Newton–Raphson Method one of the fastest root-finding methods.

---

# Advantages

* Very fast convergence near the root.
* Requires only one initial approximation.
* Uses the exact derivative, giving highly accurate updates.
* Widely used in science, engineering, and optimization.

---

# Limitations

* Requires the derivative of the function.
* A poor initial approximation may cause divergence or convergence to an unintended root.
* Cannot be applied when

```text
f′(x) = 0
```

at the current approximation because division by zero occurs.

* May fail or converge slowly near multiple roots.

---

# Comparison with Previous Methods

| Method         |      Initial Guess | Derivative Required | Bracketing Interval Required |
| -------------- | -----------------: | ------------------: | ---------------------------: |
| Bisection      |           Interval |                  No |                          Yes |
| False Position |           Interval |                  No |                          Yes |
| Secant         | Two approximations |                  No |                           No |
| Newton–Raphson |  One approximation |                 Yes |                           No |

---

# Applications

The Newton–Raphson Method is widely used in

* Numerical Analysis
* Engineering
* Physics
* Computer Science
* Machine Learning
* Optimization
* Scientific Computing

It is particularly useful when fast convergence is required and the derivative of the function is available.

---

# Summary

* The Newton–Raphson Method is an open root-finding method.
* It starts with one initial approximation.
* The tangent line at the current approximation is used to compute the next approximation.
* The general iterative formula is

```text
xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)
```

* The method usually converges much faster than the Bisection, False Position, and Secant methods.
* The derivative is required at every iteration.

---

# Connection to the Next Method

The Newton–Raphson Method uses the derivative

```text
f′(x)
```

to compute each new approximation.

A natural question now arises:

> **What if we transform the equation into the form**

```text
x = g(x)
```

**and repeatedly substitute the current approximation into `g(x)` instead of using derivatives?**

This idea leads to the **Fixed-Point Iteration Method**, where the focus shifts from tangent lines to iterative function evaluation. Studying it after the Newton–Raphson Method highlights a different perspective on solving nonlinear equations while building on the iterative concepts developed throughout this chapter.
