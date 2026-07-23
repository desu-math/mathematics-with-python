# Algorithm: Working with Probability Distributions

## Overview

A probability distribution algorithm describes the general steps used to:

* define a random variable,
* generate random observations,
* calculate probabilities,
* analyze the distribution,
* visualize the results.

The specific mathematical formula changes depending on the distribution, but the computational workflow remains similar.

---

# General Algorithm for Probability Distribution Analysis

## Step 1: Define the Random Variable

First, identify what the random variable represents.

A random variable should describe the uncertain quantity being studied.

Examples:

```text
X = Number of heads in 10 coin tosses

X = Number of customers arriving in one hour

X = Height of a person
```

Determine whether the variable is:

* discrete,
* continuous.

---

# Step 2: Define Possible Values

Determine the possible values that the random variable can take.

For discrete variables:

Example:

```text
Number of heads in 5 coin tosses

X = {0,1,2,3,4,5}
```

For continuous variables:

Example:

```text
Height

X = all values within a possible range
```

---

# Step 3: Choose an Appropriate Probability Distribution

Select the mathematical distribution that describes the random process.

Examples:

| Problem Type                           | Distribution |
| -------------------------------------- | ------------ |
| Success/failure experiment             | Bernoulli    |
| Number of successes in repeated trials | Binomial     |
| Number of events in a fixed interval   | Poisson      |
| Equal likelihood over an interval      | Uniform      |
| Measurement data around an average     | Normal       |
| Waiting time between events            | Exponential  |

Choosing the correct distribution is one of the most important steps.

---

# Step 4: Generate Random Samples

Use the selected distribution to generate observations.

The generated values simulate real-world experiments.

Example:

```text
Generate 10,000 coin toss experiments
```

or

```text
Generate 5,000 human height measurements
```

In Python, this is commonly done using:

* NumPy random functions
* SciPy probability functions

---

# Step 5: Calculate Statistical Properties

After generating data, calculate important characteristics.

## Mean

The mean represents the expected value.

```text
Mean = Average value of observations
```

---

## Variance

Variance measures how spread out the data is.

```text
Large variance:

Values are widely spread.

Small variance:

Values are close together.
```

---

## Standard Deviation

Standard deviation is the square root of variance.

It measures the typical distance from the mean.

---

# Step 6: Estimate Probabilities

Use the generated data to estimate probabilities.

Example:

Suppose we simulate 10,000 coin tosses.

Results:

```text
Heads = 4980
```

Estimated probability:

```text
P(Heads)

= 4980 / 10000

= 0.498
```

The estimated value approaches the theoretical probability as the sample size increases.

---

# Step 7: Visualize the Distribution

Visualization helps us understand the shape and behavior of the distribution.

Choose the appropriate graph:

## Discrete Distributions

Use:

* bar charts

Examples:

* Bernoulli
* Binomial
* Poisson

---

## Continuous Distributions

Use:

* histograms
* density curves

Examples:

* Normal
* Uniform
* Exponential

---

# Step 8: Compare with Theoretical Distribution

Compare the simulated results with the expected mathematical distribution.

Example:

Simulation:

```text
Mean = 49.8
```

Theory:

```text
Expected Mean = 50
```

A close result indicates that the simulation follows the expected distribution.

---

# General Pseudocode

```text
START

Define random variable X

Identify type:
    If count → Discrete
    If measurement → Continuous

Choose probability distribution

Generate random samples

Calculate:
    Mean
    Variance
    Standard deviation
    Probability estimates

Create visualization

Compare simulation with theoretical results

END
```

---

# Algorithm Complexity

The computational complexity mainly depends on the number of generated samples.

If we generate **n observations**:

## Sample Generation

```text
O(n)
```

Each observation must be created once.

---

## Statistical Calculations

Mean:

```text
O(n)
```

Variance:

```text
O(n)
```

Probability estimation:

```text
O(n)
```

---

## Visualization

Plotting also depends on the number of observations:

```text
O(n)
```

---

# Important Concept

The purpose of simulation is not to replace mathematical probability.

Instead:

```text
Mathematical Probability
          +
Computational Simulation
          =
Better Understanding
```

Theoretical probability tells us what should happen.

Simulation allows us to observe how it happens in practice.

---

# Summary

The general algorithm for probability distributions is:

1. Define the random variable.
2. Determine possible values.
3. Select an appropriate distribution.
4. Generate random samples.
5. Calculate statistical properties.
6. Estimate probabilities.
7. Visualize the distribution.
8. Compare results with theory.

This workflow is the foundation for implementing individual probability distributions in Python.
