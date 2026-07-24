# Bernoulli Distribution

## Overview

The **Bernoulli distribution** is the simplest probability distribution in probability theory.

It describes a random experiment that has **only two possible outcomes**.

These outcomes are commonly called:

* Success
* Failure

The names "success" and "failure" are only labels. They do not necessarily mean that one outcome is good and the other is bad. They simply distinguish the two possible outcomes.

Examples include:

* Head or Tail in a coin toss
* Pass or Fail in an examination
* Yes or No in a survey
* Defective or Non-defective product
* Spam or Not Spam email
* Purchased or Not Purchased
* Diseased or Healthy

Whenever an experiment has exactly two possible outcomes, the Bernoulli distribution is a suitable mathematical model.

---

# Historical Background

The Bernoulli distribution is named after the Swiss mathematician **Jacob Bernoulli (1655–1705)**.

While studying repeated experiments such as coin tossing and games of chance, Bernoulli developed mathematical ideas for describing experiments with only two possible outcomes.

His work laid the foundation for modern probability theory and later led to the development of the **Binomial distribution**, which models repeated Bernoulli experiments.

---

# Bernoulli Experiment

A **Bernoulli experiment** is a random experiment that satisfies four conditions.

## Condition 1: There are only two possible outcomes.

One outcome is labeled as **success**, and the other is labeled as **failure**.

Example:

```text
Coin Toss

Success → Head

Failure → Tail
```

---

## Condition 2: The probability of success remains constant.

If the probability of success is

```text
p
```

then every repetition of the experiment has the same probability of success.

Example:

For a fair coin,

```text
P(Head) = 0.5
```

for every toss.

---

## Condition 3: The probability of failure is

```text
1 − p
```

Since only two outcomes are possible,

```text
P(Success) + P(Failure) = 1
```

Therefore,

```text
P(Failure) = 1 − p
```

---

## Condition 4: Each experiment is independent.

The outcome of one experiment does not influence the outcome of another.

Example:

The result of the first coin toss does not affect the second coin toss.

---

# Bernoulli Random Variable

A Bernoulli random variable assigns numerical values to the two outcomes.

The standard assignment is

```text
X = 1   if Success occurs

X = 0   if Failure occurs
```

For example,

```text
Coin Toss

Head → 1

Tail → 0
```

or

```text
Email Classification

Spam → 1

Not Spam → 0
```

Using 0 and 1 allows mathematical analysis and forms the basis of many statistical and machine learning models.

---

# Probability Mass Function (PMF)

Since the Bernoulli distribution is a **discrete probability distribution**, it is described by a **Probability Mass Function (PMF)**.

The PMF is

```text
P(X = x) =

p       if x = 1

1 − p   if x = 0
```

where

* **p** is the probability of success,
* **1 − p** is the probability of failure.

---

## Example

Suppose a machine produces defective products with probability

```text
p = 0.08
```

Define

```text
X = 1   if the product is defective

X = 0   otherwise
```

Then

```text
P(X = 1) = 0.08

P(X = 0) = 0.92
```

---

# Graph of the Bernoulli Distribution

The Bernoulli distribution has only two possible values.

```text
Probability

1.0 ┤
    │
0.8 ┤
    │
0.6 ┤
    │
0.4 ┤
    │
0.2 ┤
    │
0.0 └───────────────
      0         1
```

The graph consists of **two bars only**, representing the probabilities of failure and success.

---

# Mean of the Bernoulli Distribution

The mean (expected value) is

```text
E(X) = p
```

This means that the average value of many repeated Bernoulli experiments approaches the probability of success.

For example,

if

```text
p = 0.70
```

then

```text
E(X) = 0.70
```

---

# Variance of the Bernoulli Distribution

The variance measures how much the outcomes vary.

The variance is

```text
Var(X) = p(1 − p)
```

Notice that the variance depends on both the probability of success and the probability of failure.

---

# Standard Deviation

The standard deviation is

```text
√[p(1 − p)]
```

It measures the typical spread of the outcomes around the mean.

---

# Real-World Applications

The Bernoulli distribution is widely used whenever an event has only two possible outcomes.

Examples include:

* Coin tossing
* Medical diagnosis (positive/negative)
* Product quality inspection (defective/non-defective)
* Customer purchase decisions (buy/not buy)
* Website click prediction (clicked/not clicked)
* Email classification (spam/not spam)
* Binary image processing (black/white)
* Machine learning binary classification

---

# Relationship with Other Distributions

The Bernoulli distribution is the foundation of several other probability distributions.

For example,

```text
One Bernoulli Trial
        │
        ▼
Bernoulli Distribution

Repeated Independent Bernoulli Trials
        │
        ▼
Binomial Distribution
```

In other words,

the **Binomial distribution** can be viewed as the sum of several independent Bernoulli experiments.

Therefore, understanding the Bernoulli distribution is essential before studying the Binomial distribution.

---

# Summary

* The Bernoulli distribution models experiments with exactly two possible outcomes.
* A Bernoulli experiment has two outcomes, constant probabilities, and independent trials.
* The random variable takes only two values: 0 and 1.
* The PMF assigns probability **p** to success and **1 − p** to failure.
* The mean is **p**.
* The variance is **p(1 − p)**.
* The Bernoulli distribution is the mathematical foundation of the Binomial distribution and many binary classification problems in statistics and machine learning.
