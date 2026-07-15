# Poisson Distribution

## Overview

The **Poisson distribution** is a discrete probability distribution that describes the probability of a given number of events occurring within a fixed interval of **time**, **space**, **distance**, or **volume**, provided that the events occur independently and at a constant average rate.

Unlike the Binomial distribution, which counts the number of successes in a fixed number of trials, the Poisson distribution counts the number of events that occur naturally within a specified interval.

Examples include:

* Number of customers entering a supermarket in one hour
* Number of phone calls received by a call center in one minute
* Number of accidents occurring at an intersection in one month
* Number of typing errors on a page
* Number of radioactive particles emitted in one second
* Number of emails received during one day

In all these situations, we are interested in **how many events occur**, not **how many trials are performed**.

---

# Historical Background

The Poisson distribution is named after the French mathematician **Siméon Denis Poisson (1781–1840)**.

While studying rare events, Poisson developed a mathematical model to describe how often such events occur over a fixed interval.

Today, the Poisson distribution is widely used in engineering, telecommunications, biology, finance, medicine, traffic analysis, and many other fields.

---

# When Should We Use the Poisson Distribution?

The Poisson distribution is appropriate when we want to count events occurring within a fixed interval.

The interval may represent:

* Time
* Distance
* Area
* Volume
* Space

Examples:

| Interval        | Event                     |
| --------------- | ------------------------- |
| One minute      | Phone calls received      |
| One hour        | Customers entering a shop |
| One kilometer   | Road accidents            |
| One page        | Typographical errors      |
| One cubic meter | Air particles detected    |

---

# Conditions of a Poisson Experiment

A random experiment follows a Poisson distribution if it satisfies the following conditions.

## Condition 1: Events Are Counted

The random variable represents the **number of events** occurring during a fixed interval.

Example:

```text
Number of customers entering a store in one hour.
```

---

## Condition 2: Events Occur Independently

The occurrence of one event does not influence another.

Example:

One customer's arrival does not affect when the next customer arrives.

---

## Condition 3: Constant Average Rate

Events occur at a constant average rate throughout the interval.

This average rate is denoted by

```text
λ (lambda)
```

where

```text
λ = average number of events per interval
```

Example:

If a shop receives, on average, 12 customers per hour,

```text
λ = 12
```

---

## Condition 4: Events Cannot Occur Simultaneously

Within an extremely small interval, at most one event can occur.

This assumption simplifies the mathematical model and is reasonable for most practical applications.

---

# Poisson Random Variable

A Poisson random variable represents the **number of events** occurring during a fixed interval.

It is commonly denoted by

```text
X
```

Possible values are

```text
X = 0, 1, 2, 3, ...
```

Unlike the Binomial distribution, there is **no upper limit** on the number of possible events.

---

# Probability Mass Function (PMF)

The Probability Mass Function of the Poisson distribution is

```text
          e^(−λ) λ^x
P(X = x) = ----------
               x!
```

where

* **λ** = average number of events,
* **x** = number of observed events,
* **e** ≈ 2.71828 (Euler's number).

---

# Understanding the Formula

The PMF contains three important parts.

## 1. Average Rate

```text
λ
```

determines the average number of events expected during the interval.

---

## 2. Number of Events

```text
x
```

represents the exact number of events whose probability is being calculated.

---

## 3. Euler's Number

```text
e^(−λ)
```

adjusts the probability so that the sum of all possible probabilities equals 1.

---

# Mean

The mean of a Poisson distribution is

```text
E(X) = λ
```

The expected number of events is exactly equal to the average rate.

Example:

If

```text
λ = 8
```

then

```text
Mean = 8
```

---

# Variance

The variance is

```text
Var(X) = λ
```

One remarkable property of the Poisson distribution is that its **mean and variance are equal**.

---

# Standard Deviation

The standard deviation is

```text
√λ
```

---

# Shape of the Poisson Distribution

The shape depends on the value of λ.

### Small λ

The distribution is strongly skewed to the right.

### Moderate λ

The distribution becomes less skewed.

### Large λ

The distribution gradually resembles the Normal distribution.

Thus, as λ increases, the Poisson distribution becomes increasingly symmetric.

---

# Relationship with the Binomial Distribution

The Poisson distribution can be viewed as a special case of the Binomial distribution.

If

* the number of trials (**n**) is very large,
* the probability of success (**p**) is very small,
* and the product **np = λ** remains constant,

then the Binomial distribution approaches the Poisson distribution.

```text
Large n

Small p

np = λ

        │
        ▼

Poisson Distribution
```

This approximation is especially useful when calculating Binomial probabilities becomes difficult.

---

# Real-World Applications

The Poisson distribution is commonly used to model:

* Number of customers arriving at a store
* Number of phone calls received
* Number of website visits
* Number of traffic accidents
* Number of defects in manufactured products
* Number of machine failures
* Number of insurance claims
* Number of radioactive emissions
* Number of mutations in DNA sequences

---

# Advantages

The Poisson distribution

* models random event counts,
* requires only one parameter (λ),
* is simple to compute,
* approximates the Binomial distribution under certain conditions,
* is widely used in science, engineering, business, and data science.

---

# Summary

* The Poisson distribution models the number of events occurring within a fixed interval.
* Events must occur independently and at a constant average rate.
* The parameter **λ** represents the average number of events per interval.
* The PMF gives the probability of observing exactly **x** events.
* The mean and variance are both equal to **λ**.
* As **λ** increases, the distribution approaches the Normal distribution.
* The Poisson distribution can also serve as an approximation to the Binomial distribution when the number of trials is very large and the probability of success is very small.
