# False Position (Regula Falsi) Method

## Introduction

The **False Position Method**, also known as the **Regula Falsi Method**, is a numerical technique for finding an approximate root of a nonlinear equation.

Like the Bisection Method, it starts with a continuous function

```text
f(x)
```

and an interval

```text
[a, b]
```

such that

```text
f(a) × f(b) < 0
```

which guarantees that at least one root lies within the interval.

The main difference between the two methods is how the next approximation is chosen.

* The **Bisection Method** always chooses the midpoint of the interval.
* The **False Position Method** chooses the point where the secant line joining the endpoints intersects the x-axis.

Since the secant line often follows the shape of the function better than the midpoint, the False Position Method frequently converges faster than the Bisection Method.

---

# Basic Idea

Suppose the graph of the function passes through the points

```text
(a, f(a))
```

and

```text
(b, f(b))
```

Instead of dividing the interval into two equal parts, draw the straight line joining these two points.

The point where this line intersects the x-axis is taken as the next approximation of the root.

This approximation is called the **false position**, which gives the method its name.

---

# Geometric Interpretation

Draw a figure similar to the one below.

The figure should contain:

* the curve `y = f(x)`,
* the points `(a, f(a))` and `(b, f(b))`,
* the secant line joining these points,
* the x-axis,
* the point `c` where the secant line intersects the x-axis.

If you draw the graph with the above contents, you understend why the method usually provides a better approximation than simply taking the midpoint.

---

# Derivation of the Formula

Let the two endpoints of the interval be

```text
(a, f(a))

(b, f(b))
```

The equation of the straight line passing through these two points is

```text
(y − f(a)) / (f(b) − f(a)) = (x − a) / (b − a)
```

The approximate root is the point where this line crosses the x-axis.

Since every point on the x-axis has

```text
y = 0
```

substitute

```text
y = 0
```

into the equation of the line:

```text
(0 − f(a)) / (f(b) − f(a)) = (x − a) / (b − a)
```

Multiply both sides by

```text
(b − a)
```

to obtain

```text
x − a = −f(a)(b − a) / (f(b) − f(a))
```

Therefore,

```text
x = a − f(a)(b − a) / (f(b) − f(a))
```

This is one form of the False Position formula.

Expanding and simplifying gives the equivalent form

```text
x = (a f(b) − b f(a)) / (f(b) − f(a))
```

The approximation is usually denoted by

```text
c
```

Hence,

```text
c = (a f(b) − b f(a)) / (f(b) − f(a))
```

This formula computes the x-coordinate of the point where the secant line intersects the x-axis.

---

# Iteration Procedure

After computing

```text
c
```

evaluate

```text
f(c)
```

There are three possibilities.

If

```text
f(c) = 0
```

then

```text
c
```

is the exact root.

If

```text
f(a) × f(c) < 0
```

replace

```text
b = c
```

Otherwise,

replace

```text
a = c
```

Repeat the procedure until the desired accuracy is obtained.

---

# Why Does the Method Work?

The method works because:

* the function is continuous on the interval,
* the endpoints have opposite signs,
* the secant line provides a better estimate of the root than the midpoint in many situations,
* each iteration preserves an interval that still brackets the root.

---

# Advantages

* Easy to understand and implement.
* Uses the shape of the function through linear interpolation.
* Usually converges faster than the Bisection Method.
* Always maintains an interval containing the root.

---

# Limitations

* Requires a continuous function.
* Requires an initial interval satisfying

```text
f(a) × f(b) < 0
```

* May converge slowly for some functions because one endpoint can remain fixed for many iterations.

---

# Comparison with the Bisection Method

| Bisection Method                        | False Position Method                                     |
| --------------------------------------- | --------------------------------------------------------- |
| Uses the midpoint of the interval.      | Uses the intersection of the secant line with the x-axis. |
| Does not use the shape of the function. | Uses linear interpolation.                                |
| Very reliable but relatively slow.      | Often faster while remaining reliable.                    |

---

# Applications

The False Position Method is widely used in:

* Numerical Analysis
* Engineering
* Physics
* Scientific Computing
* Mathematical Modelling
* Computational Mathematics

---

# Summary

* The False Position Method is a bracketing method for finding numerical roots.
* It requires a continuous function with

```text
f(a) × f(b) < 0
```

* The next approximation is obtained from the intersection of the secant line joining the endpoints with the x-axis.
* The approximation is computed using

```text
c = (a f(b) − b f(a)) / (f(b) − f(a))
```

* The interval is updated until the desired accuracy is achieved.
