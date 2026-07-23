# Fixed-Point Iteration Method

## Introduction

The **Fixed-Point Iteration Method** is an open numerical method for finding an approximate root of a nonlinear equation.

Unlike the Bisection, False Position, Secant, and Newton–Raphson methods, the Fixed-Point Iteration Method does **not** solve the equation

```text
f(x) = 0
```

directly.

Instead, the equation is first transformed into an equivalent form

```text
x = g(x)
```

Starting from an initial approximation, the method repeatedly substitutes the current approximation into the function `g(x)` until the approximations converge to a fixed value.

---

# Evolution of Root-Finding Methods

The Fixed-Point Iteration Method represents a different way of thinking compared with the previous methods.

### Bisection Method

Uses the midpoint of an interval.

### False Position Method

Uses the x-intercept of a secant line while maintaining a bracketing interval.

### Secant Method

Uses the x-intercept of a secant line through the two most recent approximations.

### Newton–Raphson Method

Uses the x-intercept of the tangent line.

### Fixed-Point Iteration Method

Instead of constructing lines, the equation is rewritten into the form

```text
x = g(x)
```

and the next approximation is obtained simply by evaluating

```text
x_(n+1) = g(x_n)
```

Thus, the Fixed-Point Iteration Method is based on **iterative function evaluation** rather than geometric constructions.

---

# What Is a Fixed Point?

A **fixed point** of a function `g(x)` is a number `α` that satisfies

```text
g(α) = α
```

In other words, applying the function does not change the value.

For example, if

```text
g(2) = 2
```

then `2` is a fixed point of the function.

The goal of the Fixed-Point Iteration Method is to approximate this fixed point.

---

# Why Rewrite the Equation?

Suppose we want to solve

```text
f(x) = 0
```

Instead of solving it directly, we rearrange it into

```text
x = g(x)
```

If a number `α` satisfies

```text
α = g(α)
```

then

```text
g(α) − α = 0
```

which is equivalent to the original equation.

Therefore, finding a fixed point of `g(x)` is equivalent to finding a root of `f(x)`.

---

# One Equation Can Have Many Fixed-Point Forms

An important feature of this method is that a single equation may be rewritten in many different ways.

For example,

```text
x² − 3 = 0
```

may be written as

```text
x = √3
```

or

```text
x = (x² + 3)/(2x)
```

or

```text
x = 3/x
```

Each rearrangement defines a different function `g(x)`.

Although these equations are mathematically equivalent, **their iterations may behave very differently**.

Some converge rapidly.

Some converge slowly.

Some diverge completely.

Therefore, choosing an appropriate function `g(x)` is one of the most important parts of the Fixed-Point Iteration Method.

---

# Basic Idea

Choose an initial approximation

```text
x₀
```

Compute the next approximation using

```text
x₁ = g(x₀)
```

Then compute

```text
x₂ = g(x₁)
```

Continue the process

```text
x₃ = g(x₂)

...

x_(n+1) = g(x_n)
```

If the sequence approaches a constant value,

```text
α
```

then `α` is the approximate root.

---

# Geometric Interpretation

The Fixed-Point Iteration Method has a simple geometric interpretation.

Draw the graphs

```text
y = g(x)

y = x
```

The point where these two graphs intersect is the fixed point because

```text
g(α) = α
```

Insert a figure showing

* the curve `y = g(x)`,
* the straight line `y = x`,
* their intersection at `α`.

A second figure (a cobweb diagram) may be included to illustrate how successive approximations move toward the fixed point.

---

# Derivation of the Iteration Formula

Suppose the equation

```text
f(x) = 0
```

has been rewritten as

```text
x = g(x)
```

Choose an initial approximation

```text
x₀
```

Evaluate the function at this point.

```text
x₁ = g(x₀)
```

Using the same idea,

```text
x₂ = g(x₁)
```

Again,

```text
x₃ = g(x₂)
```

Repeating the process gives the general iterative formula

```text
x_(n+1) = g(x_n)
```

This simple equation is the foundation of the Fixed-Point Iteration Method.

---

# Convergence of the Method

The Fixed-Point Iteration Method does not always converge.

A sufficient condition for convergence is

```text
|g′(α)| < 1
```

where `α` is the fixed point.

This means that, near the fixed point, the slope of `g(x)` must have magnitude less than one.

If

```text
|g′(α)| < 1
```

the approximations usually converge to the fixed point.

If

```text
|g′(α)| > 1
```

the approximations usually move away from the fixed point, causing divergence.

When

```text
|g′(α)| = 1
```

the behavior is uncertain and requires further analysis.

---

# Choosing a Good Function g(x)

The success of the Fixed-Point Iteration Method depends heavily on the choice of `g(x)`.

A good choice should satisfy:

* It is algebraically equivalent to the original equation.
* It is easy to evaluate.
* It satisfies

```text
|g′(x)| < 1
```

in a neighborhood of the fixed point.

* It produces a sequence that converges rapidly.

A poor choice may lead to slow convergence or complete divergence.

---

# Advantages

* Simple iterative formula.
* Easy to implement.
* Requires only function evaluations.
* Does not require derivatives of the original function.
* Useful for introducing iterative numerical methods.

---

# Limitations

* Convergence is not guaranteed.
* Different choices of `g(x)` may produce completely different results.
* A poor initial approximation may cause divergence.
* Usually converges more slowly than the Newton–Raphson Method.

---

# Comparison with Previous Methods

| Method                | Main Idea                   | Derivative Required |
| --------------------- | --------------------------- | ------------------: |
| Bisection             | Midpoint                    |                  No |
| False Position        | Secant line with bracketing |                  No |
| Secant                | Secant line                 |                  No |
| Newton–Raphson        | Tangent line                |                 Yes |
| Fixed-Point Iteration | Function iteration          |                  No |

---

# Applications

The Fixed-Point Iteration Method is widely used in

* Numerical Analysis
* Nonlinear Equation Solving
* Engineering
* Scientific Computing
* Differential Equations
* Optimization
* Computational Mathematics

It also forms the theoretical foundation for many advanced iterative algorithms.

---

# Summary

* The Fixed-Point Iteration Method solves equations by rewriting

```text
f(x) = 0
```

as

```text
x = g(x)
```

* The iterative formula is

```text
x_(n+1) = g(x_n)
```

* The method converges to a fixed point when an appropriate function `g(x)` is chosen.
* A commonly used convergence condition is

```text
|g′(α)| < 1
```

* Choosing a suitable function `g(x)` is essential for the success of the method.

---

# Connection to the Next Topics

The root-finding methods studied in this chapter differ in their assumptions, convergence speed, computational cost, and reliability.

This naturally leads to three important questions:

* Which method converges the fastest?
* Which method is the most reliable?
* Which method should be chosen for a particular problem?

These questions will be answered in the next topic, where the root-finding methods are compared in terms of convergence, efficiency, and practical applications.
