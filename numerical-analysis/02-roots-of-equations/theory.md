# Finding Numerical Solutions of Equations

## Introduction

Many problems in mathematics, science, engineering, economics, and data science require finding the value of an unknown variable that satisfies a given equation.

For example,

```text
2x + 5 = 15
```

has the solution

```text
x = 5
```

because substituting `x = 5` into the equation makes both sides equal.

Such a value is called the **solution** or **root** of the equation.

For simple equations, the solution can often be found using algebraic techniques. However, many real-world equations are much more complicated and cannot be solved exactly. In such cases, numerical methods are used to obtain approximate solutions.

---

# What Is a Root of an Equation?

A **root** (or **zero**) of a function is a value of `x` that makes the function equal to zero.

If a function is written as

```text
f(x)
```

then a root is any value of `x` satisfying

```text
f(x) = 0
```

For example,

```text
f(x) = x² − 9
```

has two roots because

```text
f(3) = 0

f(−3) = 0
```

Therefore,

```text
x = 3

x = −3
```

are the roots of the function.

A root is also called:

* Zero of a function
* Solution of an equation
* x-intercept of the graph (when the graph crosses or touches the x-axis)

---

# Graphical Interpretation of a Root

A root of a function can also be understood graphically.

Suppose a function is written as

```text
y = f(x)
```

A root is the **x-coordinate** at which the graph intersects or touches the x-axis.

For example, consider the function

```text
f(x) = x² − 4
```

The graph intersects the x-axis at

```text
x = -2

x = 2
```

because

```text
f(-2) = 0

f(2) = 0
```

Therefore,

> **Finding the root of an equation is equivalent to finding the x-coordinate where the graph of the function crosses or touches the x-axis.**

This graphical interpretation is the foundation of many numerical methods. Methods such as the **Bisection Method** and **False Position Method** search for an interval in which the graph crosses the x-axis, while methods such as **Newton-Raphson** use the slope of the graph to approach the root.

---

# Analytical and Numerical Solutions

There are two main approaches for solving equations.

## 1. Analytical (Exact) Solution

An analytical solution is obtained using algebraic or mathematical techniques to determine the exact value of the root.

Examples include:

* Linear equations
* Many quadratic equations
* Some polynomial equations
* Some trigonometric equations

For example,

```text
x² − 9 = 0
```

can be solved by factorization:

```text
(x − 3)(x + 3) = 0
```

Hence,

```text
x = 3

x = −3
```

are the exact solutions.

---

## 2. Numerical (Approximate) Solution

Many equations cannot be solved exactly using elementary algebra.

Examples include

```text
x = cos(x)
```

and

```text
e^(−x) = x
```

Instead of finding the exact root, numerical methods compute an approximation that is sufficiently accurate for practical applications.

For example,

```text
x ≈ 0.739085
```

is the numerical solution of

```text
x = cos(x)
```

---

# Why Do We Need Numerical Methods?

Many practical problems lead to equations that are difficult or impossible to solve exactly.

Examples include:

* High-degree polynomial equations
* Transcendental equations
* Nonlinear equations
* Engineering design equations
* Scientific models
* Optimization problems in machine learning
* Mathematical models in data science

In such situations, numerical methods provide approximate solutions with a desired level of accuracy.

---

# General Procedure for Finding Numerical Roots

Although different numerical methods use different algorithms, they all follow the same general procedure.

```text
Step 1

Write the problem in the standard form

f(x) = 0

Step 2

Choose an initial approximation or an interval that is likely to contain a root.

Step 3

Apply a numerical method to compute a better approximation.

Step 4

Repeat the computation until the desired accuracy is achieved.

Step 5

Report the approximate root.
```

---

# Characteristics of a Good Numerical Method

A good numerical method should:

* Produce accurate approximations.
* Converge to the correct root.
* Require a reasonable amount of computation.
* Be stable and reliable.
* Be easy to implement on a computer.

Different numerical methods satisfy these characteristics to different degrees.

---

# Common Numerical Methods for Finding Roots

Some of the most widely used numerical methods include:

* Bisection Method
* False Position (Regula Falsi) Method
* Fixed-Point Iteration Method
* Newton-Raphson Method
* Secant Method

Each method uses a different strategy to approximate the root of an equation.

---

# Applications

Finding numerical solutions of equations is fundamental in many fields, including:

* Numerical Analysis
* Engineering
* Physics
* Chemistry
* Economics
* Statistics
* Data Science
* Machine Learning
* Artificial Intelligence
* Computer Graphics
* Scientific Computing

Many computational problems can ultimately be formulated as finding the root of an equation.

---

# Summary

* A root of a function is a value of `x` that satisfies `f(x) = 0`.
* Graphically, a root is the x-coordinate where the graph of the function crosses or touches the x-axis.
* Some equations can be solved exactly using analytical methods.
* Many practical equations require numerical methods because exact solutions are difficult or impossible to obtain.
* Numerical methods compute approximate roots with a desired level of accuracy.
* Different numerical methods use different algorithms to approach the same goal: finding the numerical solution of an equation.
