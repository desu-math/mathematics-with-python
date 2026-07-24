# Worked Example: Exponential Distribution

## Problem

A customer service center receives calls at an average rate of:

```text
λ = 4 calls per hour
```

The waiting time until the next call follows an Exponential distribution.

Find the probability that the waiting time is less than **15 minutes**.

---

# Step 1: Identify the Given Information

Rate parameter:

```text
λ = 4 calls/hour
```

The required waiting time is:

```text
x = 15 minutes
```

Since the rate is given per hour, convert minutes to hours.

```text
15 minutes = 15 / 60 hours

= 0.25 hours
```

Therefore:

```text
x = 0.25 hours
```

---

# Step 2: Write the Exponential Probability Formula

For an Exponential distribution, the probability that an event occurs within time x is:

```text
P(X ≤ x) = 1 − e^(-λx)
```

where:

```text
λ = event rate

x = waiting time
```

---

# Step 3: Substitute the Values

Given:

```text
λ = 4

x = 0.25
```

Substitute into the formula:

```text
P(X ≤ 0.25)

=

1 − e^(-(4)(0.25))
```

---

# Step 4: Simplify the Expression

Calculate the exponent:

```text
(4)(0.25) = 1
```

Therefore:

```text
P(X ≤ 0.25)

=

1 − e^(-1)
```

We know:

```text
e^(-1) ≈ 0.3679
```

Therefore:

```text
P(X ≤ 0.25)

=

1 − 0.3679
```

---

# Step 5: Calculate the Final Probability

```text
P(X ≤ 0.25)

=

0.6321
```

Therefore:

```text
P(X ≤ 0.25) = 0.6321
```

or

```text
63.21%
```

---

# Final Answer

```text
P(X ≤ 15 minutes) = 0.6321
```

The probability that the next customer call arrives within 15 minutes is approximately:

```text
63.21%
```

---

# Interpretation

A probability of:

```text
63.21%
```

means that if we observe many waiting times, approximately **63% of calls will arrive within 15 minutes**.

The remaining probability:

```text
1 − 0.6321 = 0.3679
```

represents the chance that we wait longer than 15 minutes.

Therefore:

```text
P(X > 15 minutes) = 36.79%
```

---

# Connection With Poisson Distribution

This example shows the relationship between Poisson and Exponential distributions.

The Poisson distribution asks:

```text
How many calls arrive in an hour?
```

Example:

```text
Number of calls = 4 per hour
```

The Exponential distribution asks:

```text
How long until the next call arrives?
```

Example:

```text
Waiting time = 15 minutes
```

The same rate parameter:

```text
λ = 4 calls/hour
```

connects both distributions.

---

# Key Takeaways

* The Exponential distribution models waiting times.
* The rate parameter determines how frequently events occur.
* Higher λ values produce shorter waiting times.
* The CDF gives the probability that an event occurs before a given time.
* Exponential and Poisson distributions are closely related.
