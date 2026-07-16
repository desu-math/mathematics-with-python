# Standard Normal Distribution (Standardization)

## Introduction

The Normal distribution is one of the most important probability distributions in statistics.

However, different datasets can have different:

* means,
* standard deviations,
* measurement units,
* scales.

For example:

```text
Dataset A:

Mean = 50
Standard deviation = 5


Dataset B:

Mean = 100
Standard deviation = 20
```

Both may follow a Normal distribution, but they have different centers and spreads.

This creates a problem:

> How can we compare values from different Normal distributions?

The solution is **standardization**.

---

# What Is Standardization?

**Standardization** is the process of converting a value from a Normal distribution into a standard scale called the **Standard Normal Distribution**.

Instead of working with the original value:

```text
x
```

we transform it into a standardized value called a:

```text
Z-score
```

The Z-score tells us how many standard deviations a value is away from the mean.

---

# Standard Normal Distribution

The Standard Normal Distribution is a special Normal distribution with:

```text
Mean = 0

Standard Deviation = 1
```

It is represented as:

```text
Z ~ N(0, 1)
```

where:

```text
0 = mean

1 = standard deviation
```

Every Normal distribution can be transformed into this standard form.

---

# Z-score Formula

The formula for standardization is:

```text
        x − μ
Z = -------------
          σ
```

where:

```text
Z = standardized value

x = original observation

μ = population mean

σ = population standard deviation
```

---

# Understanding the Z-score

The Z-score measures the distance from the mean in terms of standard deviations.

## Positive Z-score

If:

```text
Z > 0
```

the value is above the mean.

Example:

```text
Z = 2
```

means:

"The value is 2 standard deviations above the mean."

---

## Negative Z-score

If:

```text
Z < 0
```

the value is below the mean.

Example:

```text
Z = -1.5
```

means:

"The value is 1.5 standard deviations below the mean."

---

## Z-score Equal to Zero

If:

```text
Z = 0
```

the value is exactly equal to the mean.

---

# Why Do We Use Z-scores?

Standardization allows us to:

* compare values from different datasets,
* calculate probabilities using one standard table,
* identify unusual observations,
* detect outliers,
* apply statistical methods consistently.

---

# Relationship Between Normal and Standard Normal Distribution

The original Normal distribution:

```text
X ~ N(μ, σ²)
```

can be transformed into:

```text
Z ~ N(0,1)
```

using:

```text
        X − μ
Z = -------------
          σ
```

The shape does not change.

Only the scale changes.

---

# Example 1: Calculating a Z-score

## Problem

A student's exam score is:

```text
x = 85
```

The class average is:

```text
μ = 75
```

The standard deviation is:

```text
σ = 5
```

Find the Z-score.

---

## Step 1: Write the Formula

```text
        x − μ
Z = -------------
          σ
```

---

## Step 2: Substitute Values

```text
        85 − 75
Z = -------------
            5
```

---

## Step 3: Calculate

```text
        10
Z = -----
         5
```

Therefore:

```text
Z = 2
```

---

## Interpretation

The student's score is:

```text
2 standard deviations above the mean.
```

---

# Example 2: Finding Probability Using Z-score

## Problem

The heights of students are normally distributed:

```text
μ = 170 cm

σ = 10 cm
```

Find the probability that a student has height less than:

```text
x = 180 cm
```

---

## Step 1: Convert x to Z-score

Formula:

```text
        x − μ
Z = -------------
          σ
```

Substitute:

```text
        180 − 170
Z = -------------
            10
```

Therefore:

```text
Z = 1
```

---

## Step 2: Use the Standard Normal Distribution

Now the problem becomes:

```text
P(X < 180)

↓

P(Z < 1)
```

From the Standard Normal table:

```text
P(Z < 1) ≈ 0.8413
```

---

## Final Answer

```text
P(X < 180) = 0.8413
```

or

```text
84.13%
```

---

# Interpretation

There is approximately an:

```text
84.13%
```

chance that a randomly selected student has a height less than 180 cm.

---

# The 68–95–99.7 Rule Connection

The Standard Normal Distribution also explains the Empirical Rule.

For a Normal distribution:

```text
Within ±1σ:

≈ 68%
```

```text
Within ±2σ:

≈ 95%
```

```text
Within ±3σ:

≈ 99.7%
```

After standardization, these become:

```text
Z = ±1

Z = ±2

Z = ±3
```

---

# Applications

Standardization is used in:

* hypothesis testing,
* confidence intervals,
* machine learning preprocessing,
* anomaly detection,
* quality control,
* data normalization.

---

# Summary

* Standardization converts any Normal distribution into the Standard Normal Distribution.
* The Standard Normal Distribution has:

```text
Mean = 0

Standard deviation = 1
```

* The transformation uses the Z-score:

```text
        x − μ
Z = -------------
          σ
```

* A Z-score tells how many standard deviations a value is from the mean.
* Positive Z-scores indicate values above the mean.
* Negative Z-scores indicate values below the mean.
* Standardization allows probabilities to be calculated using a single standard scale.
