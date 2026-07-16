# Algorithm: Estimation and Confidence Intervals

## Overview

A confidence interval algorithm uses sample information to estimate an unknown population parameter.

The algorithm follows a sequence of steps:

1. Identify the population parameter.
2. Collect sample data.
3. Calculate the sample statistic.
4. Select the appropriate probability distribution.
5. Calculate the standard error.
6. Determine the critical value.
7. Calculate the margin of error.
8. Construct the confidence interval.
9. Interpret the result.

---

# General Algorithm

## Step 1: Define the Population Parameter

First, determine what population characteristic needs to be estimated.

Common parameters include:

```text id="h6qj4p"
Population Mean:

μ


Population Proportion:

p
```

Example:

```text id="0k2l3m"
Estimate the average income of all households.
```

The target parameter is:

```text id="g1h7vk"
Population Mean (μ)
```

---

# Step 2: Collect Sample Data

Select a random sample from the population.

The sample should contain:

* Sample size
* Observed values
* Appropriate sampling method

Example:

```text id="5i6w9e"
Sample size:

n = 50
```

---

# Step 3: Calculate the Sample Statistic

The sample statistic is used as the point estimate.

Depending on the parameter:

For the population mean:

```text id="z2p3i8"
Point Estimate = x̄
```

For the population proportion:

```text id="v9s8j1"
Point Estimate = p̂
```

---

# Step 4: Determine the Confidence Level

Choose the required confidence level.

Common choices are:

```text id="m4j9yx"
90%

95%

99%
```

Then calculate the significance level:

```text id="6k8f2q"
α = 1 - Confidence Level
```

For a two-sided confidence interval:

```text id="d7c1mb"
α/2
```

is used.

---

# Step 5: Select the Appropriate Distribution

Determine whether to use the Z-distribution or t-distribution.

## Case 1: Population Standard Deviation Known

Use the Z-distribution.

Conditions:

```text id="x8p4vz"
σ is known
```

Confidence interval:

```text id="w2n5qa"
                 σ
CI = x̄ ± Zα/2 × ------
                √n
```

---

## Case 2: Population Standard Deviation Unknown

Use the t-distribution.

Conditions:

```text id="y5v9kx"
σ is unknown
```

Confidence interval:

```text id="c7m3qd"
                 s
CI = x̄ ± tα/2 × ------
                √n
```

---

# Step 6: Calculate the Standard Error

The standard error measures the variability of the estimator.

For the population mean when σ is known:

```text id="e3f6am"
      σ
SE = ------
     √n
```

For the population mean when σ is unknown:

```text id="r8d2wl"
      s
SE = ------
     √n
```

For a population proportion:

```text id="p4x7nz"
            p̂(1-p̂)
SE = √ -------------
                 n
```

---

# Step 7: Determine the Critical Value

The critical value depends on:

* Confidence level
* Probability distribution
* Degrees of freedom (for t-distribution)

For Z-distribution:

```text id="m7q3pv"
Critical Value = Zα/2
```

For t-distribution:

```text id="a8w2lx"
Critical Value = tα/2,n-1
```

---

# Step 8: Calculate the Margin of Error

The margin of error is:

```text id="k4r6dy"
ME = Critical Value × Standard Error
```

For example:

Z-confidence interval:

```text id="z9n1ks"
ME = Zα/2 × SE
```

t-confidence interval:

```text id="w8f5qm"
ME = tα/2 × SE
```

---

# Step 9: Construct the Confidence Interval

The final confidence interval is:

```text id="p3x7fv"
Confidence Interval

=

Point Estimate

±

Margin of Error
```

Therefore:

Lower limit:

```text id="m2k8qs"
Estimate - Margin of Error
```

Upper limit:

```text id="n9v4az"
Estimate + Margin of Error
```

---

# Step 10: Interpret the Result

The final step is explaining the confidence interval in the context of the problem.

Example:

Incorrect:

```text id="j7f3lm"
There is a 95% chance that the true mean is inside this interval.
```

Correct:

```text id="u5p8cx"
We are 95% confident that the interval produced by this method contains the true population mean.
```

---

# Complete Pseudocode

```text id="c2m8vz"
START

Input sample data

Identify population parameter

Calculate sample statistic

Choose confidence level

Calculate significance level

Determine whether σ is known

IF σ is known THEN

        Use Z-distribution

        Calculate Z critical value

ELSE

        Use t-distribution

        Calculate degrees of freedom

        Calculate t critical value

END IF


Calculate standard error

Calculate margin of error

Construct confidence interval

Interpret result

END
```

---

# Algorithm Complexity

Let:

```text id="q6h1zs"
n = sample size
```

Calculating the sample statistic:

```text id="k8v2rx"
O(n)
```

Calculating the standard error:

```text id="m3p9qa"
O(1)
```

Finding the critical value:

```text id="r5t7lx"
O(1)
```

Constructing the confidence interval:

```text id="a1c6nz"
O(1)
```

Therefore, the overall computational complexity is:

```text id="w9m2kf"
O(n)
```

The main computational cost comes from processing the sample data.

---

# Summary

The confidence interval algorithm follows these steps:

1. Define the population parameter.
2. Obtain sample data.
3. Calculate the point estimate.
4. Select confidence level.
5. Choose Z or t distribution.
6. Calculate standard error.
7. Find the critical value.
8. Calculate margin of error.
9. Construct the confidence interval.
10. Interpret the result.

This algorithm transforms theoretical concepts of estimation into a practical statistical procedure.
