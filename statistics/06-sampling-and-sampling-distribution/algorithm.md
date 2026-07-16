# Algorithm: Sampling and Sampling Distributions

## Overview

Sampling is the process of selecting a subset of a population to estimate unknown population characteristics.

The algorithm demonstrates how repeated sampling produces sampling distributions and how these distributions form the basis of statistical inference.

The complete process consists of:

* defining the population,
* selecting samples,
* calculating sample statistics,
* repeating the sampling process,
* constructing the sampling distribution,
* estimating the standard error,
* interpreting the results.

---

# General Algorithm

## Step 1: Define the Population

Identify the population to be studied.

Examples:

* All university students
* All households
* All manufactured products

Determine:

* Population size (N)
* Population parameter(s)

Example:

```text
Population size = 10,000

Population mean (μ) = 70

Population standard deviation (σ) = 12
```

---

## Step 2: Choose a Sampling Method

Select an appropriate sampling technique.

Possible methods include:

### Probability Sampling

* Simple Random Sampling
* Systematic Sampling
* Stratified Sampling
* Cluster Sampling

### Non-Probability Sampling

* Convenience Sampling
* Judgment Sampling
* Quota Sampling
* Snowball Sampling

The sampling method determines how observations are selected.

---

## Step 3: Select a Sample

Choose a sample of size:

```text
n
```

Example:

```text
n = 50
```

The selected observations form one sample.

---

## Step 4: Calculate Sample Statistics

Compute statistics from the selected sample.

Examples:

* Sample mean

```text
x̄
```

* Sample variance

```text
s²
```

* Sample standard deviation

```text
s
```

* Sample proportion

```text
p̂
```

These statistics estimate the corresponding population parameters.

---

## Step 5: Repeat the Sampling Process

Repeat Steps 3 and 4 many times.

Example:

```text
Repeat = 1000 times
```

Each repetition produces a different sample statistic.

Example:

```text
Sample 1

x̄ = 69.8

----------------

Sample 2

x̄ = 70.4

----------------

Sample 3

x̄ = 69.9

...

Sample 1000
```

---

## Step 6: Construct the Sampling Distribution

Collect all sample statistics.

Example:

```text
69.8

70.4

69.9

70.1

69.7

...
```

These values form the sampling distribution.

---

## Step 7: Calculate the Standard Error

For the sampling distribution of the mean:

```text
           σ
SE = -------------
        √n
```

If σ is unknown, estimate it using:

```text
           s
SE = -------------
        √n
```

The standard error measures the variability of sample statistics.

---

## Step 8: Analyze the Sampling Distribution

Evaluate important properties.

### Center

The average of the sampling distribution should approach:

```text
μ
```

---

### Spread

The spread is measured by:

```text
Standard Error
```

---

### Shape

If:

```text
Population is Normal
```

then:

```text
Sampling Distribution is Normal
```

If:

```text
Population is not Normal
```

the Central Limit Theorem states that the sampling distribution becomes approximately Normal when the sample size is sufficiently large.

---

## Step 9: Interpret the Results

Use the sampling distribution to estimate:

* population mean,
* population proportion,
* confidence intervals,
* hypothesis tests.

This step connects sampling with inferential statistics.

---

# Pseudocode

```text
START

Input population

Choose sampling method

Input sample size

Select sample

Calculate sample statistics

Repeat sampling many times

Construct sampling distribution

Calculate standard error

Analyze center

Analyze spread

Interpret results

END
```

---

# Algorithm Complexity

Let:

```text
N = population size

n = sample size

k = number of repeated samples
```

Selecting one sample:

```text
O(n)
```

Calculating one sample statistic:

```text
O(n)
```

Repeating the process:

```text
O(kn)
```

Constructing the sampling distribution:

```text
O(k)
```

Overall complexity:

```text
O(kn)
```

---

# Relationship Between the Steps

```text
Population
      │
      ▼
Choose Sampling Method
      │
      ▼
Select Sample
      │
      ▼
Calculate Sample Statistics
      │
      ▼
Repeat Sampling
      │
      ▼
Sampling Distribution
      │
      ▼
Standard Error
      │
      ▼
Statistical Inference
```

---

# Summary

The sampling algorithm consists of the following steps:

1. Define the population.
2. Choose a sampling method.
3. Select a sample.
4. Calculate sample statistics.
5. Repeat the sampling process.
6. Construct the sampling distribution.
7. Calculate the standard error.
8. Analyze the sampling distribution.
9. Draw conclusions about the population.

This algorithm provides the computational foundation for confidence intervals, hypothesis testing, and many machine learning and data science techniques.
