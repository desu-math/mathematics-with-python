# Binomial Distribution

## Overview

The **Binomial distribution** is a discrete probability distribution that describes the probability of obtaining a certain number of successes in a fixed number of **independent Bernoulli trials**.

Unlike the Bernoulli distribution, which models only **one trial**, the Binomial distribution models **multiple independent trials** and counts how many successes occur.

For example:

* How many heads are obtained when tossing a coin 10 times?
* How many students pass an exam out of 50 students?
* How many defective products are found in a sample of 100 items?
* How many customers purchase a product out of 200 visitors?

In each case, we are interested in the **number of successes**, not the outcome of a single trial.

---

# Relationship with the Bernoulli Distribution

The Binomial distribution is a direct extension of the Bernoulli distribution.

```text
One Bernoulli Trial
        │
        ▼
Outcome:
Success or Failure

Repeated Independent Bernoulli Trials
        │
        ▼
Count the Number of Successes

        │
        ▼
Binomial Distribution
```

A Bernoulli distribution answers:

> **"Did the event succeed?"**

A Binomial distribution answers:

> **"How many times did the event succeed?"**

---

# Binomial Experiment

A random experiment follows a Binomial distribution if it satisfies the following conditions.

## Condition 1: A Fixed Number of Trials

The experiment consists of a predetermined number of trials.

This number is denoted by

```text
n
```

Example:

```text
A coin is tossed 10 times.

n = 10
```

---

## Condition 2: Each Trial Is a Bernoulli Experiment

Every trial has exactly two possible outcomes:

* Success
* Failure

Example:

```text
Coin Toss

Success → Head

Failure → Tail
```

---

## Condition 3: Constant Probability of Success

The probability of success remains the same in every trial.

Let

```text
p
```

represent the probability of success.

Then

```text
Probability of Failure = 1 − p
```

Example:

For a fair coin,

```text
p = 0.5
```

for every toss.

---

## Condition 4: Independent Trials

The outcome of one trial does not affect the outcomes of the remaining trials.

Example:

The result of the first coin toss does not influence the second coin toss.

---

# Binomial Random Variable

A Binomial random variable represents the **total number of successes** obtained in **n independent Bernoulli trials**.

It is commonly denoted by

```text
X
```

Possible values are

```text
X = 0, 1, 2, ..., n
```

Example:

If a coin is tossed three times,

Possible numbers of heads are

```text
0
1
2
3
```

Notice that the Binomial random variable counts **how many successes occur**, not the order in which they occur.

---

# Probability Mass Function (PMF)

The probability mass function of the Binomial distribution is

```text
               nCx · p^x · (1 − p)^(n − x)
```

or equivalently,

```text
P(X = x) = C(n, x) · p^x · (1 − p)^(n − x)
```

where

* **n** = number of trials
* **x** = number of successes
* **p** = probability of success
* **1 − p** = probability of failure
* **C(n, x)** = number of different ways to choose **x** successes from **n** trials

---

# Understanding the Formula

The PMF has three parts.

## 1. Combination

```text
C(n, x)
```

Counts the number of possible arrangements of the successes.

Example:

If two heads occur in four coin tosses,

Possible arrangements include

```text
HHTT
HTHT
HTTH
THHT
THTH
TTHH
```

The combination term counts all such arrangements.

---

## 2. Probability of Successes

```text
p^x
```

represents the probability of obtaining exactly **x successes**.

---

## 3. Probability of Failures

```text
(1 − p)^(n − x)
```

represents the probability of obtaining the remaining failures.

Multiplying these three parts gives the probability of obtaining exactly **x successes**.

---

# Mean

The mean (expected number of successes) is

```text
E(X) = np
```

Example:

```text
n = 20

p = 0.60

Mean = 20 × 0.60 = 12
```

On average, about 12 successes are expected.

---

# Variance

The variance is

```text
Var(X) = np(1 − p)
```

It measures the spread of the number of successes.

---

# Standard Deviation

The standard deviation is

```text
√[np(1 − p)]
```

It measures the typical deviation from the expected number of successes.

---

# Shape of the Binomial Distribution

The shape depends on the value of **p**.

### When p = 0.5

The distribution is approximately symmetric.

### When p < 0.5

Most observations are concentrated near smaller values of **x**, producing a distribution skewed toward larger values.

### When p > 0.5

Most observations are concentrated near larger values of **x**, producing a distribution skewed toward smaller values.

As the number of trials becomes very large, the Binomial distribution gradually resembles the Normal distribution.

---

# Real-World Applications

The Binomial distribution is widely used in situations involving repeated independent trials.

Examples include:

* Number of heads in repeated coin tosses
* Number of students passing an examination
* Number of defective products in quality control
* Number of successful sales calls
* Number of customers purchasing a product
* Number of patients responding to a treatment
* Number of correctly classified emails
* Number of successful network transmissions

---

# Advantages

The Binomial distribution

* models repeated binary experiments,
* predicts the probability of different numbers of successes,
* forms the basis for many statistical methods,
* is widely used in engineering, medicine, economics, and machine learning.

---

# Summary

* The Binomial distribution models the number of successes in a fixed number of independent Bernoulli trials.
* A Binomial experiment requires a fixed number of trials, two possible outcomes, constant success probability, and independent trials.
* The random variable counts the total number of successes.
* The PMF combines combinations, success probabilities, and failure probabilities.
* The mean is **np**.
* The variance is **np(1 − p)**.
* As the number of trials increases, the Binomial distribution approaches the Normal distribution.
