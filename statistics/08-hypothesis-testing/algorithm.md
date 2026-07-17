# Algorithm for Hypothesis Testing

## Introduction

Hypothesis testing follows a systematic procedure for making statistical decisions from sample data.

Although different statistical tests (such as the Z-test, t-test, chi-square test, and F-test) use different test statistics, they all follow the same general decision-making process.

The algorithm below provides a general framework applicable to most hypothesis testing problems.

---

# Algorithm

### Step 1: Define the Research Question

Clearly identify the population parameter to be investigated and state the research objective.

Determine whether the goal is to

* compare a population parameter with a specified value,
* compare two populations,
* or evaluate the effect of a treatment or process.

---

### Step 2: Formulate the Hypotheses

State the two competing hypotheses.

Null hypothesis:

```text
H₀
```

Alternative hypothesis:

```text
H₁ (or Hₐ)
```

The hypotheses should be expressed in terms of the population parameter.

---

### Step 3: Determine the Type of Test

Choose the appropriate hypothesis test based on the form of the alternative hypothesis.

```text
If H₁ : parameter ≠ value

↓

Use a Two-Tailed Test
```

```text
If H₁ : parameter > value

↓

Use a Right-Tailed Test
```

```text
If H₁ : parameter < value

↓

Use a Left-Tailed Test
```

---

### Step 4: Choose the Appropriate Test Statistic

Select the statistical test according to the available information.

Examples include

* Z-test
* t-test
* Chi-square test
* F-test

For tests involving the population mean,

```text
Known population standard deviation

↓

Use Z-test
```

```text
Unknown population standard deviation

↓

Use t-test
```

---

### Step 5: Select the Significance Level

Choose the probability of committing a Type I Error.

Common choices are

```text
α = 0.10

α = 0.05

α = 0.01
```

This value must be selected **before** analyzing the sample data.

---

### Step 6: Collect Sample Data

Obtain a representative sample from the population.

Calculate the necessary sample statistics, such as

* sample size,
* sample mean,
* sample standard deviation,
* sample proportion,

depending on the hypothesis being tested.

---

### Step 7: Compute the Test Statistic

Use the appropriate statistical formula to calculate the test statistic.

For example,

```text
Z-test

↓

Compute Z
```

or

```text
t-test

↓

Compute t
```

The test statistic measures how far the observed sample result is from the value stated in the null hypothesis.

---

### Step 8: Determine the Decision Criterion

Choose one of the following approaches.

---

#### Approach A: Critical Value Method

1. Determine the appropriate critical value.
2. Identify the rejection region.
3. Compare the calculated test statistic with the critical value.

Decision rule:

```text
Test Statistic

↓

Inside Critical Region?

↓

YES

↓

Reject H₀


NO

↓

Fail to Reject H₀
```

---

#### Approach B: p-value Method

1. Compute the p-value.
2. Compare it with the significance level.

Decision rule:

```text
p-value ≤ α

↓

Reject H₀
```

```text
p-value > α

↓

Fail to Reject H₀
```

Both approaches always produce the same statistical decision.

---

### Step 9: Make the Statistical Decision

Based on the selected decision criterion,

choose one of the following conclusions.

```text
Reject H₀
```

or

```text
Fail to Reject H₀
```

Never state

```text
Accept H₀
```

because failing to reject the null hypothesis does not prove that it is true.

---

### Step 10: Interpret the Result

Translate the statistical decision into the context of the original problem.

Explain what the conclusion means in practical terms.

For example,

```text
There is sufficient evidence to conclude that the average lifetime differs from 500 hours.
```

or

```text
There is insufficient evidence to conclude that the new fertilizer increases crop yield.
```

---

### Step 11: Consider Possible Decision Errors

Interpret the conclusion while recognizing the possibility of statistical errors.

If H₀ is rejected,

there remains a probability of

```text
Type I Error

=

α
```

If H₀ is not rejected,

there remains the possibility of

```text
Type II Error

=

β
```

No statistical decision is completely free from uncertainty.

---

# Algorithm Flow

```text
Define Research Question
          │
          ▼
State H₀ and H₁
          │
          ▼
Determine Test Type
          │
          ▼
Choose Test Statistic
          │
          ▼
Select Significance Level (α)
          │
          ▼
Collect Sample Data
          │
          ▼
Compute Test Statistic
          │
          ▼
 ┌───────────────────────────────┐
 │ Choose Decision Method        │
 └──────────────┬────────────────┘
                │
     ┌──────────┴──────────┐
     ▼                     ▼
Critical Value         p-value
 Method                 Method
     │                     │
     └──────────┬──────────┘
                ▼
      Statistical Decision
                │
                ▼
 Practical Interpretation
                │
                ▼
 Consider Type I and Type II Errors
```

---

# Summary

The hypothesis testing algorithm can be summarized as

```text
Research Question

↓

Hypotheses

↓

Test Type

↓

Test Statistic

↓

Significance Level

↓

Sample Data

↓

Compute Test Statistic

↓

Critical Value or p-value

↓

Reject H₀

or

Fail to Reject H₀

↓

Interpretation

↓

Consider Possible Errors
```

This algorithm provides a complete framework for statistical hypothesis testing and serves as the foundation for implementing hypothesis tests in Python and statistical software.
