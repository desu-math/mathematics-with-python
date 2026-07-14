# Algorithm: Binomial Distribution

## Overview

The Binomial distribution algorithm simulates a fixed number of independent Bernoulli trials and analyzes the number of successes obtained.

The algorithm performs the following tasks:

* define the Binomial distribution parameters,
* generate Binomial random samples,
* calculate experimental probabilities,
* calculate theoretical probabilities,
* compute statistical properties,
* visualize the probability distribution.

---

# Distribution Parameters

A Binomial distribution is completely defined by two parameters.

## Number of Trials

```text
n
```

The total number of independent Bernoulli trials.

Example:

```text
n = 10
```

means that the experiment is repeated ten times.

---

## Probability of Success

```text
p
```

The probability that a single trial results in success.

Example:

```text
p = 0.60
```

means that each trial has a 60% chance of success.

Since there are only two possible outcomes,

```text
Probability of Failure = 1 − p
```

---

# General Algorithm

## Step 1: Define the Distribution Parameters

Specify:

* number of trials (**n**),
* probability of success (**p**),
* number of simulations.

Example:

```text
n = 20

p = 0.50

Number of Simulations = 10,000
```

---

## Step 2: Generate Binomial Random Samples

For each simulation:

1. Perform **n** independent Bernoulli trials.
2. Count the number of successes.
3. Store the total number of successes.

Example:

```text
Simulation 1

1 0 1 1 0 1 0 0 1 1

Number of Successes = 6
```

Each simulation produces one Binomial random variable.

---

## Step 3: Determine the Possible Outcomes

A Binomial random variable can take the values

```text
0, 1, 2, ..., n
```

Example:

If

```text
n = 5
```

then the possible values are

```text
0, 1, 2, 3, 4, 5
```

---

## Step 4: Count the Frequency of Each Outcome

Count how many times each possible value appears in the simulated data.

Example:

Simulation Results

```text
2, 3, 1, 2, 4, 3, 2, 1, 3, 2
```

Frequency Table

| Number of Successes | Frequency |
| ------------------- | --------: |
| 0                   |         0 |
| 1                   |         2 |
| 2                   |         4 |
| 3                   |         3 |
| 4                   |         1 |
| 5                   |         0 |

---

## Step 5: Calculate Experimental Probabilities

Estimate the probability of each outcome using

```text
Experimental Probability

=

Frequency of Outcome
────────────────────────
Total Number of Simulations
```

Example:

```text
Frequency of X = 2 = 4000

Total Simulations = 10000
```

Therefore,

```text
P(X = 2) = 4000 / 10000 = 0.40
```

---

## Step 6: Calculate Theoretical Probabilities

For every possible value

```text
x = 0, 1, 2, ..., n
```

compute the probability using the Binomial Probability Mass Function (PMF):

```text
P(X = x) = C(n,x) · p^x · (1 − p)^(n − x)
```

These values represent the theoretical Binomial distribution.

---

## Step 7: Calculate Statistical Properties

Compute the following quantities.

### Mean

```text
Mean = np
```

---

### Variance

```text
Variance = np(1 − p)
```

---

### Standard Deviation

```text
Standard Deviation = √[np(1 − p)]
```

Compare these theoretical values with those obtained from the simulated data.

---

## Step 8: Visualize the Distribution

Create visualizations to better understand the distribution.

Recommended visualizations include:

* **Bar Chart** for the theoretical Probability Mass Function (PMF).
* **Histogram** for the simulated Binomial observations.

Compare the two graphs to observe how simulation approximates the theoretical distribution.

---

# Pseudocode

```text
START

Input n

Input p

Input number_of_simulations

Generate Binomial random samples

Determine all possible outcomes

Count the frequency of each outcome

Calculate experimental probabilities

Calculate theoretical probabilities

Calculate mean

Calculate variance

Calculate standard deviation

Create visualizations

Save figures

Display figures

END
```

---

# Algorithm Complexity

Let

```text
m = number of simulations
```

and

```text
n = number of trials
```

### Generate Binomial Samples

```text
O(m)
```

---

### Count Frequencies

```text
O(m)
```

---

### Calculate Theoretical Probabilities

```text
O(n)
```

---

### Create Visualizations

```text
O(n)
```

---

### Overall Time Complexity

Since the number of simulations is usually much larger than the number of trials,

```text
Overall Complexity = O(m)
```

---

# Summary

The Binomial distribution algorithm consists of the following steps:

1. Define the number of trials and probability of success.
2. Generate repeated Binomial experiments.
3. Count the number of successes.
4. Estimate experimental probabilities.
5. Calculate theoretical probabilities using the Binomial PMF.
6. Compute the mean, variance, and standard deviation.
7. Visualize the probability distribution.
8. Compare simulated results with theoretical values.

This algorithm extends the Bernoulli distribution by combining multiple independent Bernoulli trials into a single experiment and analyzing the total number of successes.
