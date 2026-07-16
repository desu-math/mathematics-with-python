# Algorithm: Uniform Distribution

## Overview

The Uniform distribution algorithm simulates continuous random values within a fixed interval and compares the experimental probabilities with the theoretical probabilities.

The algorithm performs the following tasks:

* define the interval,
* generate Uniform random samples,
* calculate theoretical probabilities,
* estimate experimental probabilities,
* compute statistical properties,
* visualize the distribution.

---

# Distribution Parameters

A continuous Uniform distribution requires two parameters.

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
a = 0

b = 20
```

---

# General Algorithm

## Step 1: Define the Distribution Parameters

Specify

* lower bound (**a**),
* upper bound (**b**),
* number of simulations.

Example:

```text
a = 0

b = 20

Number of Simulations = 10000
```

---

## Step 2: Generate Uniform Random Samples

For each simulation:

1. Generate one random value between **a** and **b**.
2. Store the generated value.

Example:

```text
6.42

14.81

3.75

18.26

9.54
```

Each generated value represents one observation from the Uniform distribution.

---

## Step 3: Define the Desired Interval

Specify the interval whose probability is to be estimated.

Example:

```text
5 ≤ X ≤ 12
```

---

## Step 4: Estimate the Experimental Probability

Count how many generated values fall inside the desired interval.

Example:

```text
Values inside interval = 3512

Total simulations = 10000
```

Calculate

```text
Experimental Probability

=

Values Inside Interval
────────────────────────
Total Simulations
```

Example:

```text
3512
─────
10000

=

0.3512
```

---

## Step 5: Calculate the Theoretical Probability

Use the Uniform distribution formula

```text
               d − c
P(c ≤ X ≤ d) = -------
               b − a
```

where

* **a** = lower bound,
* **b** = upper bound,
* **c** = beginning of the desired interval,
* **d** = end of the desired interval.

Example:

```text
           12 − 5
P = ----------------
           20 − 0

  = 7 / 20

  = 0.35
```

---

## Step 6: Calculate Statistical Properties

Compute the theoretical values.

### Mean

```text
Mean

=

(a + b) / 2
```

---

### Variance

```text
Variance

=

(b − a)² / 12
```

---

### Standard Deviation

```text
Standard Deviation

=

(b − a) / √12
```

Also compute the experimental mean, variance, and standard deviation from the simulated data.

---

## Step 7: Compare Theory and Simulation

Compare

* theoretical probability,
* experimental probability,
* theoretical statistics,
* experimental statistics.

As the number of simulations increases, the experimental values should become closer to the theoretical values.

---

## Step 8: Visualize the Distribution

Create visualizations of the simulated data.

Recommended visualizations include

* Histogram of the simulated values.
* Horizontal reference line representing the constant probability density.

These visualizations show that the values are approximately uniformly distributed across the interval.

---

# Pseudocode

```text
START

Input a

Input b

Input number_of_simulations

Generate Uniform random samples

Define the desired interval

Count values inside the interval

Calculate experimental probability

Calculate theoretical probability

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
n = number of simulations
```

---

### Generate Uniform Samples

```text
O(n)
```

---

### Count Values Inside the Interval

```text
O(n)
```

---

### Calculate Theoretical Probability

```text
O(1)
```

---

### Create Visualization

```text
O(n)
```

---

### Overall Time Complexity

```text
Overall Complexity = O(n)
```

---

# Summary

The Uniform distribution algorithm consists of the following steps:

1. Define the lower bound (**a**) and upper bound (**b**).
2. Specify the number of simulations.
3. Generate Uniform random samples.
4. Define the interval of interest.
5. Estimate the experimental probability.
6. Calculate the theoretical probability.
7. Compute the mean, variance, and standard deviation.
8. Visualize the distribution.
9. Compare the theoretical and experimental results.

Unlike the discrete distributions studied previously, the Uniform distribution models **continuous values**, and probabilities are calculated over **intervals** rather than individual outcomes.
