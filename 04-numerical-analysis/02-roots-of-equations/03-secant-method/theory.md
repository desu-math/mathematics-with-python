# Secant Method

## Introduction

The **Secant Method** is an open numerical method used to find an approximate root of a nonlinear equation

```text
f(x) = 0
```

Unlike the Bisection Method and the False Position Method, the Secant Method **does not require the root to be bracketed by an interval**. Instead, it starts with two initial approximations and repeatedly constructs a secant line through the corresponding points on the graph of the function.

The x-intercept of the secant line becomes the next approximation of the root.

Because the Secant Method does not require the computation of derivatives, it is often considered an efficient alternative to the Newton–Raphson Method when the derivative of the function is unavailable or difficult to compute.

---

# Evolution of Root-Finding Methods

The Secant Method can be understood as the natural evolution of the previous methods.

### 1. Bisection Method

The next approximation is simply the midpoint of the interval.

```text
c = (a + b) / 2
```

The method ignores the shape of the function.

---

### 2. False Position Method

Instead of taking the midpoint, a secant line is drawn through the endpoints of the interval.

The point where this secant line intersects the x-axis becomes the next approximation.

However, the interval is always updated so that

```text
f(a) × f(b) < 0
```

remains true.

---

### 3. Secant Method

The Secant Method keeps the idea of using a secant line but removes the requirement of maintaining a bracketing interval.

Instead of using the interval endpoints, it always uses the **two most recent approximations**.

This simple modification often leads to faster convergence.

---

# Basic Idea

Suppose the two most recent approximations of the root are

```text
x₀

x₁
```

These correspond to the points

```text
(x₀, f(x₀))

(x₁, f(x₁))
```

Draw the secant line joining these two points.

The point where this secant line intersects the x-axis becomes the next approximation,

```text
x₂
```

The process is then repeated using

```text
x₁

x₂
```

to compute

```text
x₃
```

and so on until the desired accuracy is achieved.

---

# Geometric Interpretation

Draw and see a figure with the following contents to understand more about secant method.

* the curve `y = f(x)`,
* the two approximation points `(x₀, f(x₀))` and `(x₁, f(x₁))`,
* the secant line passing through these points,
* the x-axis,
* the point `x₂` where the secant line intersects the x-axis.

Unlike the False Position Method, the two points are **not interval endpoints**. They are simply the two most recent approximations.

---

# Derivation of the Secant Formula

Let the two approximation points be

```text
(x₀, f(x₀))

(x₁, f(x₁))
```

The equation of the straight line passing through these two points is

```text
(y − f(x₀)) / (f(x₁) − f(x₀)) = (x − x₀) / (x₁ − x₀)
```

The next approximation is obtained where this line intersects the x-axis.

Since every point on the x-axis satisfies

```text
y = 0
```

substitute

```text
y = 0
```

into the equation of the line.

```text
(0 − f(x₀)) / (f(x₁) − f(x₀)) = (x − x₀) / (x₁ − x₀)
```

Multiply both sides by

```text
(x₁ − x₀)
```

to obtain

```text
x − x₀ = −f(x₀)(x₁ − x₀) / (f(x₁) − f(x₀))
```

Therefore,

```text
x = x₀ − f(x₀)(x₁ − x₀) / (f(x₁) − f(x₀))
```

The next approximation is denoted by

```text
x₂
```

Hence,

```text
x₂ = x₀ − f(x₀)(x₁ − x₀) / (f(x₁) − f(x₀))
```

After each iteration, the notation is updated.

Instead of

```text
x₀

x₁
```

we use

```text
x₁

x₂
```

Then

```text
x₂

x₃
```

This leads to the general iterative formula

```text
xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))
```

This formula is the fundamental equation of the Secant Method.

---

# Why Does the Method Work?

The method works because the secant line provides a linear approximation to the function.

Near the root, a smooth function behaves approximately like a straight line. Therefore, the x-intercept of the secant line is often a good estimate of the actual root.

Each iteration replaces the older approximation with the newer one, causing the estimates to move closer to the root.

---

# Advantages

* Does not require computation of derivatives.
* Usually converges faster than the Bisection Method and the False Position Method.
* Simple to implement.
* Requires only function evaluations.

---

# Limitations

* Does not guarantee convergence.
* The choice of initial approximations affects performance.
* May diverge if the initial guesses are poor.
* Fails if

```text
f(xₙ) = f(xₙ₋₁)
```

because the denominator becomes zero.

---

# Comparison with Previous Methods

| Method         | Uses an Interval? | Uses a Secant Line? | Requires Derivative? |
| -------------- | ----------------: | ------------------: | -------------------: |
| Bisection      |               Yes |                  No |                   No |
| False Position |               Yes |                 Yes |                   No |
| Secant         |                No |                 Yes |                   No |

---

# Applications

The Secant Method is widely used in

* Numerical Analysis
* Scientific Computing
* Engineering
* Physics
* Computational Mathematics
* Computer Simulations

It is particularly useful when the derivative of the function is unknown or expensive to compute.

---

# Summary

* The Secant Method is an open root-finding method.
* It begins with two initial approximations.
* A secant line is drawn through the two approximation points.
* The x-intercept of the secant line becomes the next approximation.
* The general iterative formula is

```text
xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))
```

* The method usually converges faster than the Bisection and False Position methods but does not guarantee convergence.
