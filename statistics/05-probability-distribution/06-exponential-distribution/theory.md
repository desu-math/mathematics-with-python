# Exponential Distribution

## Introduction

The **Exponential distribution** is a continuous probability distribution used to model the **waiting time until an event occurs**.

While the Poisson distribution models the **number of events** occurring in a fixed interval, the Exponential distribution models the **time between those events**.

For example:

* Time until the next customer arrives.
* Time until a machine fails.
* Time between phone calls.
* Time between radioactive particle emissions.
* Time until a website receives the next request.

The Exponential distribution is one of the most important continuous distributions in probability theory and statistics.

---

# Relationship With Poisson Distribution

The Exponential and Poisson distributions are closely connected.

The Poisson distribution answers:

```text
"How many events occur in a given time interval?"
```

Example:

```text
How many customers arrive in 10 minutes?
```

The Exponential distribution answers:

```text
"How long do we wait until the next event?"
```

Example:

```text
How long until the next customer arrives?
```

Therefore:

```text
Poisson → Number of events

Exponential → Waiting time between events
```

Both assume events occur independently at a constant average rate.

---

# Exponential Distribution Parameters

The Exponential distribution has one main parameter.

## Rate Parameter

```text
λ (lambda)
```

The rate parameter represents the average number of events per unit time.

Example:

```text
λ = 5 events/hour
```

means:

On average, 5 events occur every hour.

A larger value of λ means:

* events occur more frequently,
* waiting times are shorter.

A smaller value of λ means:

* events occur less frequently,
* waiting times are longer.

---

# Probability Density Function (PDF)

The Probability Density Function of the Exponential distribution is:

```text
f(x) = λe^(-λx)
```

where:

```text
λ = rate parameter

x = waiting time

x ≥ 0
```

The distribution only accepts non-negative values because waiting time cannot be negative.

---

# Cumulative Distribution Function (CDF)

The cumulative probability is:

```text
P(X ≤ x) = 1 − e^(-λx)
```

This gives the probability that an event occurs within a certain time period.

---

# Mean and Variance

The theoretical properties are:

## Mean

```text
Mean = 1 / λ
```

The mean represents the average waiting time.

---

## Variance

```text
Variance = 1 / λ²
```

---

## Standard Deviation

```text
Standard Deviation = 1 / λ
```

The mean and standard deviation are equal for an Exponential distribution.

---

# Memoryless Property

One unique property of the Exponential distribution is the **memoryless property**.

It means:

> The probability of waiting a certain amount of additional time does not depend on how long we have already waited.

Example:

Suppose a machine has an Exponential lifetime distribution.

The probability that it survives another hour is the same whether:

```text
The machine is new

or

The machine has already worked for 5 hours
```

This property makes the Exponential distribution useful in reliability analysis.

---

# Shape of the Distribution

The Exponential distribution is right-skewed.

Characteristics:

* Maximum density occurs near zero.
* Probability decreases as waiting time increases.
* Long waiting times are possible but less likely.

When λ increases:

```text
Higher λ

↓

Events happen faster

↓

Curve becomes more concentrated near zero
```

---

# Applications

The Exponential distribution is used in:

* Queueing theory
* Reliability engineering
* Survival analysis
* Telecommunications
* Finance
* Computer networks
* Medical research
* Operations research

Examples:

```text
Customer arrival times

Machine failure times

Server response times

Radioactive decay waiting times
```

---

# Comparison of Probability Distributions

The probability distributions studied in this chapter can be classified into two main groups.

## Discrete Distributions

Discrete distributions describe **countable outcomes**.

Examples:

| Distribution | Main Question                         | Data Type    | Example                     |
| ------------ | ------------------------------------- | ------------ | --------------------------- |
| Bernoulli    | Did an event happen?                  | Two outcomes | Success/failure             |
| Binomial     | How many successes occur?             | Count        | Number of successful trials |
| Poisson      | How many events occur in an interval? | Count        | Number of arrivals per hour |

---

## Continuous Distributions

Continuous distributions describe **measurements and intervals**.

Examples:

| Distribution | Main Question                                 | Data Type        | Example                     |
| ------------ | --------------------------------------------- | ---------------- | --------------------------- |
| Uniform      | Are all values equally likely?                | Continuous value | Random value in an interval |
| Normal       | How are values distributed around an average? | Measurement      | Height, weight, exam scores |
| Exponential  | How long until an event occurs?               | Waiting time     | Time until next arrival     |

---

# Complete Distribution Comparison

| Distribution | Discrete / Continuous | Main Purpose                        | Parameters      |
| ------------ | --------------------- | ----------------------------------- | --------------- |
| Bernoulli    | Discrete              | Single success/failure experiment   | Probability (p) |
| Binomial     | Discrete              | Number of successes in fixed trials | (n, p)          |
| Poisson      | Discrete              | Number of events in fixed interval  | Rate (λ)        |
| Uniform      | Continuous            | Equal probability over interval     | (a,b)           |
| Normal       | Continuous            | Values around a mean                | (μ,σ)           |
| Exponential  | Continuous            | Waiting time between events         | (λ)             |

---

# Choosing the Appropriate Distribution

When solving a probability problem, first identify the type of question.

## Question Type 1

```text
Is there only success or failure?
```

Use:

```text
Bernoulli Distribution
```

---

## Question Type 2

```text
How many successes occur in a fixed number of trials?
```

Use:

```text
Binomial Distribution
```

---

## Question Type 3

```text
How many events occur in a fixed interval?
```

Use:

```text
Poisson Distribution
```

---

## Question Type 4

```text
Are all values equally likely within a range?
```

Use:

```text
Uniform Distribution
```

---

## Question Type 5

```text
Are values clustered around an average?
```

Use:

```text
Normal Distribution
```

---

## Question Type 6

```text
How long until an event happens?
```

Use:

```text
Exponential Distribution
```

---

# Summary

* The Exponential distribution models waiting times between events.
* It is closely related to the Poisson distribution.
* It has one main parameter: the rate (λ).
* Higher rates produce shorter waiting times.
* It has the unique memoryless property.
* It is widely used in reliability, queueing, and survival analysis.
* Probability distributions are selected based on the type of problem being modeled.
* Discrete distributions model counts, while continuous distributions model measurements and waiting times.
