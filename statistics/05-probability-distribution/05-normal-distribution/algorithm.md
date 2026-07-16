# Algorithm: Normal Distribution

## Overview

The Normal distribution algorithm models continuous data that follows a bell-shaped distribution.

The algorithm allows us to:

* define a Normal distribution,
* standardize values using Z-scores,
* calculate probabilities,
* generate random samples,
* compare theoretical and experimental results,
* visualize the distribution.

---

# Distribution Parameters

A Normal distribution is defined by two parameters.

## Mean

```text
μ
```

The mean determines the center of the distribution.

---

## Standard Deviation

```text
σ
```

The standard deviation determines the spread of the distribution.

Example:

```text
μ = 50

σ = 5
```

---

# General Algorithm

## Step 1: Define the Normal Distribution Parameters

Specify:

* mean,
* standard deviation,
* number of simulations.

Example:

```text
μ = 50

σ = 5

Number of Simulations = 10000
```

---

# Step 2: Generate Normal Random Samples

Generate random values from the Normal distribution.

Each generated value represents one observation.

Example:

```text
48.6

51.2

53.8

46.9

50.5
```

Store all generated values for analysis.

---

# Step 3: Define the Value or Interval of Interest

Choose the value or interval for which probability is required.

Example:

Single value:

```text
x = 55
```

or interval:

```text
50 ≤ X ≤ 60
```

---

# Step 4: Standardize the Value

Convert the original value into a Z-score.

Formula:

```text
        x − μ
Z = -------------
          σ
```

Example:

```text
x = 55

μ = 50

σ = 5
```

Therefore:

```text
        55 − 50
Z = -------------
            5

Z = 1
```

---

# Step 5: Calculate Probability Using the Standard Normal Distribution

After standardization:

```text
X

↓

Z
```

The probability is obtained using the cumulative distribution function (CDF).

Example:

```text
P(X < 55)

↓

P(Z < 1)
```

Then:

```text
Probability = CDF(1)
```

---

# Step 6: Calculate Probability From Simulation

Using the generated samples:

1. Count the values satisfying the condition.
2. Divide by the total number of simulations.

Example:

```text
Values below x = 8413

Total simulations = 10000
```

Experimental probability:

```text
8413
─────

10000

= 0.8413
```

---

# Step 7: Calculate Statistical Properties

Calculate theoretical values.

## Mean

```text
Mean = μ
```

---

## Variance

```text
Variance = σ²
```

---

## Standard Deviation

```text
Standard Deviation = σ
```

Also calculate experimental statistics from generated samples.

---

# Step 8: Compare Theory and Simulation

Compare:

```text
Theoretical probability

Experimental probability
```

and:

```text
Theoretical mean

Experimental mean
```

```text
Theoretical variance

Experimental variance
```

```text
Theoretical standard deviation

Experimental standard deviation
```

The experimental values should approach the theoretical values as the number of simulations increases.

---

# Step 9: Visualize the Distribution

Create visualizations using:

## Histogram

Shows the distribution of simulated observations.

---

## Probability Density Curve

Shows the theoretical Normal distribution curve.

The final graph should show:

* a symmetric bell shape,
* maximum density near the mean,
* decreasing density away from the mean.

---

# Pseudocode

```text
START

Input μ

Input σ

Input number_of_simulations

Generate Normal random samples

Input value or interval

Convert value to Z-score

Calculate probability using CDF

Calculate experimental probability

Calculate theoretical statistics

Calculate experimental statistics

Create histogram

Plot Normal density curve

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

## Calculate Z-score

```text
O(1)
```

---

## Calculate CDF Probability

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
Overall Complexity = O(n)
```

---

# Summary

The complete Normal distribution algorithm consists of:

1. Define mean and standard deviation.
2. Generate Normal random samples.
3. Select a value or interval.
4. Convert values into Z-scores.
5. Use the Standard Normal Distribution to calculate probabilities.
6. Estimate probabilities from simulations.
7. Calculate theoretical and experimental statistics.
8. Visualize the bell-shaped distribution.
9. Compare theoretical and experimental results.

Standardization is the key step that allows any Normal distribution to be transformed into the Standard Normal Distribution and analyzed using a common probability scale.
