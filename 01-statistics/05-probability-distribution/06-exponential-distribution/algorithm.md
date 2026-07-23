# Algorithm: Exponential Distribution

## Overview

The Exponential distribution algorithm models the **waiting time between independent events occurring at a constant rate**.

The algorithm allows us to:

* define the event rate,
* generate waiting-time samples,
* calculate probabilities,
* compute statistical properties,
* compare theoretical and experimental results,
* visualize the distribution.

---

# Distribution Parameter

The Exponential distribution has one main parameter.

## Rate Parameter

```text
λ (lambda)
```

The rate parameter represents the average number of events occurring per unit of time.

Example:

```text
λ = 4 events/hour
```

means:

```text
Average events = 4 per hour
```

The relationship between rate and average waiting time is:

```text
Mean waiting time = 1 / λ
```

---

# General Algorithm

## Step 1: Define the Distribution Parameter

Specify:

* rate parameter (λ),
* number of simulations.

Example:

```text
λ = 4

Number of simulations = 10000
```

---

# Step 2: Generate Exponential Random Samples

Generate random waiting times from the Exponential distribution.

Each generated value represents one possible waiting time.

Example:

```text
0.12 hours

0.38 hours

0.05 hours

0.72 hours

0.26 hours
```

Store all generated waiting times.

---

# Step 3: Define the Time Interval of Interest

Choose the waiting time threshold.

Example:

```text
x = 0.25 hours
```

or

```text
15 minutes
```

---

# Step 4: Calculate Theoretical Probability

Use the Exponential CDF:

```text
P(X ≤ x) = 1 − e^(-λx)
```

where:

```text
λ = rate parameter

x = waiting time
```

This gives the probability that an event occurs before time x.

---

# Step 5: Calculate Experimental Probability

Using the simulated waiting times:

1. Count values less than or equal to x.
2. Divide by the total number of simulations.

Formula:

```text
Experimental Probability

=

Number of values ≤ x
─────────────────────
Total simulations
```

Example:

```text
Values ≤ x = 6320

Total simulations = 10000
```

Therefore:

```text
6320
───── = 0.632
10000
```

---

# Step 6: Calculate Statistical Properties

Calculate theoretical statistics.

## Mean

```text
Mean = 1 / λ
```

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

---

Also calculate:

* experimental mean,
* experimental variance,
* experimental standard deviation.

Compare them with theoretical values.

---

# Step 7: Compare Theory and Simulation

Compare:

## Probability

```text
Theoretical probability

vs

Experimental probability
```

---

## Mean

```text
Theoretical mean

vs

Experimental mean
```

---

## Variability

```text
Theoretical variance

vs

Experimental variance
```

As the number of simulations increases, experimental results approach theoretical values.

---

# Step 8: Visualize the Distribution

Create visualizations of the generated waiting times.

Recommended visualization:

## Histogram

Shows the distribution of simulated waiting times.

Expected shape:

* high density near zero,
* decreasing density as time increases,
* long right tail.

---

## Probability Density Curve

Plot the theoretical Exponential PDF:

```text
f(x) = λe^(-λx)
```

The simulation should follow the theoretical curve.

---

# Connection With Poisson Distribution

The algorithm is connected with the Poisson process.

Poisson:

```text
Number of events in time interval
```

Exponential:

```text
Waiting time between events
```

Both use the same rate parameter:

```text
λ
```

Example:

```text
λ = 10 customers/hour
```

Poisson question:

```text
How many customers arrive in one hour?
```

Exponential question:

```text
How long until the next customer arrives?
```

---

# Pseudocode

```text
START

Input λ

Input number_of_simulations

Generate exponential random samples

Input waiting time x

Calculate theoretical probability using CDF

Count simulated values below x

Calculate experimental probability

Calculate theoretical statistics

Calculate experimental statistics

Create histogram

Plot exponential density curve

Compare results

END
```

---

# Algorithm Complexity

Let:

```text
n = number of simulations
```

---

## Generate Random Samples

```text
O(n)
```

---

## Calculate Experimental Probability

```text
O(n)
```

---

## Calculate Statistics

```text
O(n)
```

---

## Calculate Theoretical Probability

```text
O(1)
```

---

## Create Visualization

```text
O(n)
```

---

# Overall Complexity

```text
O(n)
```

---

# Summary

The Exponential distribution algorithm consists of:

1. Define the rate parameter λ.
2. Generate random waiting times.
3. Select a time threshold.
4. Calculate theoretical probability using the CDF.
5. Estimate probability from simulation.
6. Compute theoretical and experimental statistics.
7. Visualize the waiting-time distribution.
8. Compare simulation results with theoretical expectations.

The Exponential distribution completes the probability distribution section by connecting **event counts (Poisson)** with **waiting times (Exponential)**.
