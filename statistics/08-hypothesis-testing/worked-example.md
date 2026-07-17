# Worked Example: One-Sample Z-Test for the Population Mean

## Problem

A bottled water company claims that the average amount of water contained in each bottle is **500 mL**.

A quality control inspector suspects that the average filling amount is different from **500 mL**.

To investigate this claim, a random sample of **64 bottles** is selected.

The sample results are

```text
Sample Mean (x̄) = 504 mL

Population Standard Deviation (σ) = 12 mL

Sample Size (n) = 64
```

Use a **5% significance level** to test the company's claim.

---

# Step 1: State the Research Question

The objective is to determine whether the true average filling amount differs from **500 mL**.

Since we are testing whether the mean is **different**, a **two-tailed hypothesis test** is appropriate.

---

# Step 2: State the Hypotheses

Null Hypothesis

```text
H₀ : μ = 500
```

Alternative Hypothesis

```text
H₁ : μ ≠ 500
```

---

# Step 3: Identify the Type of Test

Population standard deviation is known.

Therefore,

```text
Use a Z-test.
```

Since the alternative hypothesis contains

```text
≠
```

this is a

```text
Two-Tailed Test.
```

---

# Step 4: Choose the Level of Significance

The problem specifies

```text
α = 0.05
```

For a two-tailed test,

```text
α/2 = 0.025
```

is placed in each tail.

---

# Step 5: Determine the Critical Values

From the Standard Normal Distribution,

```text
Critical Values

=

−1.96

and

+1.96
```

Therefore,

```text
Reject H₀

if

Z < −1.96

or

Z > +1.96
```

---

# Step 6: Calculate the Standard Error

The standard error is

```text
      σ
SE = ------
     √n
```

Substitute the values

```text
      12
SE = -------
      √64
```

Since

```text
√64 = 8
```

then

```text
SE = 12 / 8

SE = 1.5
```

---

# Step 7: Calculate the Test Statistic

The Z-test statistic is

```text
          x̄ − μ₀
Z = -------------------
         σ
        ------
         √n
```

Substitute the values

```text
        504 − 500
Z = ----------------
          1.5
```

Therefore,

```text
Z = 2.67
```

---

# Step 8: Critical Value Decision

The rejection region is

```text
Z < −1.96

or

Z > +1.96
```

Since

```text
2.67 > 1.96
```

the test statistic lies inside the **critical region**.

Therefore,

```text
Reject H₀
```

---

# Step 9: p-value Decision

Using the Standard Normal Distribution,

```text
p-value ≈ 0.0076
```

Compare with

```text
α = 0.05
```

Since

```text
0.0076 < 0.05
```

we again

```text
Reject H₀
```

Notice that both approaches produce the same statistical decision.

---

# Step 10: Statistical Conclusion

There is sufficient statistical evidence to conclude that

```text
the average amount of water per bottle is different from 500 mL.
```

The company's claim is **not supported** by the sample.

---

# Step 11: Interpretation

The observed sample mean is unlikely to occur if the true population mean were exactly **500 mL**.

Therefore, the sample provides strong evidence against the null hypothesis.

---

# Connection with Confidence Intervals

Suppose a **95% confidence interval** for the population mean is

```text
(501.06 , 506.94)
```

Notice that

```text
500
```

does **not** lie inside this interval.

Therefore,

```text
Reject H₀
```

This agrees exactly with both

* the critical value approach, and
* the p-value approach.

---

# Type I Error

If the true population mean actually is **500 mL**, but we rejected

```text
H₀
```

then we have committed a

```text
Type I Error.
```

The probability of making this error is

```text
α = 0.05
```

---

# Type II Error

Suppose the true population mean is actually **504 mL**, but we fail to reject

```text
H₀.
```

Then we have committed a

```text
Type II Error.
```

Its probability is denoted by

```text
β.
```

---

# Statistical Power

The probability of correctly rejecting the false null hypothesis is called

```text
Statistical Power
```

and is

```text
Power = 1 − β
```

A larger sample size generally increases the statistical power.

---

# Final Summary

This worked example demonstrates the complete hypothesis testing procedure:

```text
Research Question

↓

State H₀ and H₁

↓

Choose Test

↓

Choose α

↓

Find Critical Value

↓

Compute Standard Error

↓

Compute Test Statistic

↓

Critical Value Decision

↓

p-value Decision

↓

Interpretation

↓

Confidence Interval Connection

↓

Type I Error

↓

Type II Error

↓

Statistical Power
```

This example integrates every major concept introduced in the theory chapter into one complete statistical investigation.
