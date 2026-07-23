# Uniform Distribution

## Overview

The **Uniform distribution** is a probability distribution in which **every value within a specified interval has an equal probability of occurring**.

Unlike the Bernoulli, Binomial, and Poisson distributions, which deal with **countable (discrete)** outcomes, the Uniform distribution models **continuous** values.

Examples include:

* A random number chosen between 0 and 1.
* The exact time (in minutes) that a customer arrives during a one-hour period.
* The position of a point selected randomly along a line segment.
* A random angle between 0° and 360°.

In each of these situations, every value within the interval is equally likely.

---

# Motivation

Suppose you generate a random decimal number between

```text
0
```

and

```text
1
```

Would

```text
0.25
```

be more likely than

```text
0.80
```

The answer is **No**.

Every number between 0 and 1 has the same chance of being selected.

This is the fundamental idea behind the Uniform distribution.

---

# Types of Uniform Distribution

There are two types of Uniform distributions.

## 1. Discrete Uniform Distribution

The outcomes are **countable** and every outcome has the same probability.

Example:

Rolling a fair six-sided die.

Possible outcomes:

```text
1, 2, 3, 4, 5, 6
```

Each outcome has probability

```text
1 / 6
```

---

## 2. Continuous Uniform Distribution

The outcomes are **continuous values** within an interval.

Example:

Choosing a random real number between

```text
0
```

and

```text
10
```

Every value in this interval is equally likely.

In statistics and data science, when we say **Uniform distribution**, we usually mean the **continuous Uniform distribution**.

The remainder of this chapter focuses on the continuous Uniform distribution.

---

# Parameters

A continuous Uniform distribution has two parameters.

## Lower Bound

```text
a
```

The smallest possible value.

---

## Upper Bound

```text
b
```

The largest possible value.

The interval is written as

```text
[a, b]
```

Example:

```text
a = 2

b = 8
```

Possible values lie between 2 and 8.

---

# Probability Density Function (PDF)

The Probability Density Function (PDF) is

```text
          1
f(x) = --------
        b − a
```

for

```text
a ≤ x ≤ b
```

and

```text
f(x) = 0
```

outside the interval.

---

# Understanding the PDF

Notice that the PDF is **constant**.

Its value does not change as **x** changes.

This means the graph of the Uniform distribution is simply a **horizontal line**.

Example:

If

```text
a = 0

b = 10
```

then

```text
          1
f(x) = -------
           10
```

for every value between 0 and 10.

---

# Why Is the PDF Constant?

Because every value inside the interval is equally likely.

No value is preferred over another.

Therefore, the probability density must remain constant across the interval.

---

# Mean

The mean is

```text
      a + b
Mean = -----
         2
```

It is simply the midpoint of the interval.

Example:

If

```text
a = 2

b = 10
```

then

```text
Mean = (2 + 10) / 2 = 6
```

---

# Variance

The variance is

```text
             (b − a)²
Variance = -----------
                12
```

It measures the spread of the distribution.

---

# Standard Deviation

The standard deviation is

```text
           _________
          √(b − a)²
SD = -------------------
            √12
```

or equivalently,

```text
         b − a
SD = -------------
          √12
```

---

# Shape of the Distribution

The graph of the continuous Uniform distribution is a rectangle.

* The height is constant.
* Every value has equal probability density.
* The total area under the curve is exactly **1**.

---

# Important Note

Unlike discrete distributions, the probability of obtaining **one exact value** is zero.

For example,

```text
P(X = 5) = 0
```

Instead, probabilities are calculated over **intervals**.

For example,

```text
P(3 ≤ X ≤ 7)
```

This is one of the most important differences between discrete and continuous probability distributions.

---

# Real-World Applications

The Uniform distribution is commonly used in:

* Random number generation
* Computer simulations
* Monte Carlo methods
* Game development
* Cryptography
* Sampling algorithms
* Machine learning
* Statistical modeling

---

# Advantages

The Uniform distribution

* is the simplest continuous probability distribution,
* assumes every value is equally likely,
* forms the basis for many random number generation techniques,
* is widely used in simulations and computational statistics.

---

# Summary

* The Uniform distribution models continuous values within a fixed interval.
* Every value in the interval has the same probability density.
* It has two parameters: the lower bound (**a**) and the upper bound (**b**).
* The Probability Density Function is constant.
* The mean is **(a + b) / 2**.
* The variance is **(b − a)² / 12**.
* The probability of any single exact value is zero.
* Probabilities are computed over intervals rather than individual points.
