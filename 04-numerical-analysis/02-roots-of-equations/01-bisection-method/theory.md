# Bisection Method

## Introduction

The **Bisection Method** is one of the simplest and most reliable numerical methods for finding the root of a nonlinear equation.

It is based on the idea that if a continuous function changes its sign over an interval, then the function must have at least one root within that interval.

Instead of trying to find the root directly, the method repeatedly divides the interval into two equal parts and determines which half contains the root. By repeating this process, the interval becomes smaller and the approximate root becomes more accurate.

Because the interval is repeatedly divided into two equal halves, this method is called the **Bisection Method**.

---

# Basic Idea

Suppose we have a continuous function

```text
f(x)
```

and we wish to solve

```text
f(x) = 0
```

Assume there exists an interval

```text
[a, b]
```

such that

```text
f(a) × f(b) < 0
```

This means:

* `f(a)` and `f(b)` have opposite signs.
* Therefore, the function crosses the x-axis somewhere between `a` and `b`.
* Hence, at least one root exists in the interval `[a, b]`.

This conclusion follows from the **Intermediate Value Theorem**, which states that a continuous function that changes sign over an interval must have at least one root within that interval.

---

# Midpoint of the Interval

The midpoint of the interval is computed by

```text
c = (a + b) / 2
```

The value

```text
f(c)
```

is then evaluated to determine where the root lies.

There are three possible cases.

### Case 1

If

```text
f(c) = 0
```

then

```text
c
```

is the exact root, and the algorithm stops.

---

### Case 2

If

```text
f(a) × f(c) < 0
```

then the root lies between

```text
[a, c]
```

The new interval becomes

```text
[a, c]
```

---

### Case 3

If

```text
f(c) × f(b) < 0
```

then the root lies between

```text
[c, b]
```

The new interval becomes

```text
[c, b]
```

The same procedure is repeated until the desired accuracy is achieved.

---

# Why Does the Method Work?

The Bisection Method works because of two important ideas.

**1. Continuity**

The function must be continuous on the interval `[a, b]`. If the function is not continuous, a change in sign does not necessarily imply the existence of a root.

**2. Opposite Signs**

The function values at the endpoints must have opposite signs.

```text
f(a) × f(b) < 0
```

This guarantees that at least one root lies within the interval.

---

# Advantages

The Bisection Method

* is simple to understand,
* is easy to implement,
* always converges if its conditions are satisfied,
* guarantees that the root remains inside the interval.

---

# Limitations

Although the Bisection Method is reliable, it has some disadvantages.

* It converges slowly compared with methods such as Newton-Raphson or the Secant Method.
* It requires the function to be continuous.
* It requires an initial interval whose endpoints have opposite signs.
* It cannot be applied if `f(a) × f(b) > 0`, because the method cannot guarantee that a root exists within the interval.

---

# Applications

The Bisection Method is widely used in

* Numerical Analysis
* Engineering
* Physics
* Scientific Computing
* Computer Simulations
* Mathematical Modeling

It is often used when reliability is more important than computational speed.

---

# Summary

* The Bisection Method finds the root of a continuous function by repeatedly dividing an interval into two equal parts.
* The method requires

```text
f(a) × f(b) < 0
```

before the iteration begins.

* The midpoint

```text
c = (a + b) / 2
```

is used to determine which half of the interval contains the root.

* The interval is repeatedly reduced until the approximate root satisfies the desired accuracy.
* The Bisection Method is simple, reliable, and guaranteed to converge when its assumptions are satisfied.
