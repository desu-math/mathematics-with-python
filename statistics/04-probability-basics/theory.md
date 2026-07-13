# Probability Basics

## Overview

Probability is the branch of mathematics that measures the likelihood of uncertain events.

It provides a mathematical framework for analyzing randomness, uncertainty, and possible outcomes.

In statistics and data science, probability is used to model uncertainty, make predictions, and understand patterns in data.

---

# Importance of Probability

Real-world events are often uncertain.

Probability helps us:

* model uncertain events,
* analyze random processes,
* estimate risks,
* make predictions,
* build statistical models,
* develop machine learning algorithms.

Many statistical methods are built upon probability theory.

---

# Basic Probability Concepts

## Experiment

An **experiment** is a process that produces one outcome from several possible outcomes.

Examples:

* Tossing a coin
* Rolling a die
* Drawing a card from a deck
* Selecting a student from a class

Before performing the experiment, the result is uncertain.

---

## Outcome

An **outcome** is a single possible result of an experiment.

Example:

Rolling a die:

```text
Possible Outcomes

1
2
3
4
5
6
```

Each number is one possible outcome.

---

## Sample Space

The **sample space** is the set of all possible outcomes of an experiment.

It is usually denoted by **S**.

Examples:

Coin Toss

```text
S = {Head, Tail}
```

Rolling a Die

```text
S = {1, 2, 3, 4, 5, 6}
```

---

## Event

An **event** is a collection of one or more outcomes from the sample space.

Events are usually denoted by **A**, **B**, **C**, ...

Example:

Event A = Rolling an even number

```text
A = {2, 4, 6}
```

---

# Probability of an Event

The probability of an event measures how likely that event is to occur.

For equally likely outcomes,

```text
               Number of Favorable Outcomes
P(A) = ----------------------------------------------
          Total Number of Possible Outcomes
```

The probability of any event satisfies

```text
0 ≤ P(A) ≤ 1
```

where

* **P(A) = 0** means the event is impossible.
* **P(A) = 1** means the event is certain.

---

# Types of Events

## Impossible Event

An impossible event cannot occur.

Example:

Rolling a **7** on a standard six-sided die.

```text
P(A) = 0
```

---

## Certain Event

A certain event must occur.

Example:

Rolling a number between **1 and 6** on a standard die.

```text
P(A) = 1
```

---

## Simple Event

A simple event contains exactly one outcome.

Example:

```text
A = {3}
```

---

## Compound Event

A compound event contains two or more outcomes.

Example:

```text
A = {2, 4, 6}
```

---

# Basic Probability Rules

## Complement Rule

The complement of an event represents the event **not occurring**.

```text
P(Aᶜ) = 1 − P(A)
```

Example:

If

```text
P(Rain) = 0.30
```

then

```text
P(No Rain) = 1 − 0.30 = 0.70
```

---

## Addition Rule

The probability that **at least one** of two events occurs is

```text
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
```

The overlap is subtracted to avoid counting it twice.

---

## Multiplication Rule

If two events are independent,

```text
P(A ∩ B) = P(A) × P(B)
```

Example:

Probability of obtaining two heads when tossing a coin twice:

```text
1/2 × 1/2 = 1/4
```

---

# Conditional Probability

Conditional probability measures the probability of an event occurring given that another event has already occurred.

It is written as

```text
P(A | B)
```

and is read as

> Probability of **A given B**.

The formula is

```text
          P(A ∩ B)
P(A | B) = --------
            P(B)
```

Conditional probability is widely used in

* medical diagnosis,
* machine learning,
* Bayesian statistics,
* decision-making.

---

# Independent Events

Two events are **independent** if the occurrence of one event does not affect the probability of the other.

For independent events,

```text
P(A ∩ B) = P(A) × P(B)
```

Example:

* Tossing a coin
* Rolling a die

The outcome of one experiment does not influence the other.

---

# Bayes' Theorem

Bayes' theorem updates the probability of an event when new information becomes available.

```text
            P(B | A) × P(A)
P(A | B) = -----------------
                P(B)
```

Bayes' theorem is widely used in

* machine learning,
* spam filtering,
* medical diagnosis,
* artificial intelligence.

---

# Probability and Python

Python provides powerful libraries for probability simulations and statistical analysis.

Common libraries include:

* **NumPy** for random number generation and simulations.
* **SciPy** for probability distributions.
* **Pandas** for analyzing experimental data.

Typical applications include:

* coin toss simulations,
* dice rolling simulations,
* random sampling,
* probability estimation,
* Monte Carlo simulation.

---

# Summary

* Probability measures the likelihood of uncertain events.
* Every experiment has a sample space containing all possible outcomes.
* An event is one or more outcomes from the sample space.
* Probability values range from **0** to **1**.
* Important concepts include conditional probability, independence, and Bayes' theorem.
* Probability forms the mathematical foundation of statistics, machine learning, and data science.

