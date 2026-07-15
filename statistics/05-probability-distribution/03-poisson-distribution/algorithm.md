# Algorithm: Poisson Distribution

## Overview

The Poisson distribution algorithm simulates the number of events occurring within a fixed interval and compares the simulated results with the theoretical Poisson distribution.

The algorithm performs the following tasks:

* define the Poisson distribution parameter,
* generate Poisson random samples,
* calculate experimental probabilities,
* calculate theoretical probabilities,
* compute statistical properties,
* visualize the probability distribution.

---

# Distribution Parameter

Unlike the Binomial distribution, the Poisson distribution requires only **one parameter**.

## Average Rate of Events

```text
λ (lambda)
```

The parameter **λ** represents the average number of events expected during one fixed interval.

Examples:

```text
λ = 5
```

means that, on average, five events occur per interval.

Examples of intervals include:

* five customers per minute,
* twelve phone calls per hour,
* two machine failures per month.

---

# General Algorithm

## Step 1: Define the Distribution Parameter

Specify:

* average number of events (**λ**),
* number of simulations.

Example:

```text
λ = 4

Number of Simulations = 10000
```

---

## Step 2: Generate Poisson Random Samples

For each simulation:

1. Observe one interval.
2. Count the number of events occurring in that interval.
3. Store the event count.

Example:

```text
Interval 1 → 3 events

Interval 2 → 5 events

Interval 3 → 2 events

Interval 4 → 4 events
```

Each observation represents one Poisson random variable.

---

## Step 3: Determine the Possible Outcomes

Identify the observed event counts.

Possible values begin at

```text
0
```

and continue indefinitely:

```text
0, 1, 2, 3, ...
```

In practice, only a limited range of values appears in the simulation.

For example:

```text
0, 1, 2, ..., 12
```

---

## Step 4: Count the Frequency of Each Outcome

Count how many times each event count occurs.

Example:

| Number of Events | Frequency |
| ---------------- | --------: |
| 0                |       180 |
| 1                |       730 |
| 2                |      1495 |
| 3                |      1968 |
| 4                |      1946 |
| 5                |      1562 |

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
Frequency of X = 4 = 1946

Total Simulations = 10000
```

Therefore,

```text
P(X = 4) = 1946 / 10000 = 0.1946
```

---

## Step 6: Calculate Theoretical Probabilities

For each possible value

```text
x = 0, 1, 2, ...
```

calculate the theoretical probability using the Poisson PMF

```text
          e^(−λ) λ^x
P(X = x) = ----------
              x!
```

These probabilities form the theoretical Poisson distribution.

---

## Step 7: Calculate Statistical Properties

Compute the following quantities.

### Mean

```text
Mean = λ
```

---

### Variance

```text
Variance = λ
```

---

### Standard Deviation

```text
Standard Deviation = √λ
```

Compare these theoretical values with those obtained from the simulated data.

---

## Step 8: Visualize the Distribution

Create visualizations to compare theory and simulation.

Recommended visualizations include:

* **Bar Chart** for the theoretical Probability Mass Function (PMF).
* **Histogram** for the simulated observations.

Comparing these graphs illustrates how simulated data approximates the theoretical Poisson distribution.

---

# Pseudocode

```text
START

Input λ

Input number_of_simulations

Generate Poisson random samples

Determine observed outcomes

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
k = number of observed event counts
```

where **k** is the number of distinct values appearing in the simulation.

### Generate Poisson Samples

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
O(k)
```

---

### Create Visualizations

```text
O(k)
```

---

### Overall Time Complexity

Since the number of simulations is usually much larger than the number of distinct event counts,

```text
Overall Complexity = O(m)
```

---

# Summary

The Poisson distribution algorithm consists of the following steps:

1. Define the average event rate (**λ**).
2. Specify the number of simulations.
3. Generate Poisson random samples.
4. Count the frequency of each event count.
5. Estimate experimental probabilities.
6. Calculate theoretical probabilities using the Poisson PMF.
7. Compute the mean, variance, and standard deviation.
8. Visualize the distribution.
9. Compare simulated results with theoretical values.

The Poisson algorithm models **how many events occur within a fixed interval**, making it suitable for analyzing arrivals, defects, failures, and other random event-counting processes.
