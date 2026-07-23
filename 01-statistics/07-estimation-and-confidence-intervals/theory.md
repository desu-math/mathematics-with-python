# Estimation and Confidence Intervals

## Introduction

In the previous chapter, we learned that a sample is used to represent a population. We also learned that different samples produce different sample statistics, leading to the concept of a **sampling distribution**.

A natural question now arises:

> **If we only have a sample, how can we estimate an unknown population parameter?**

This question is answered through **statistical estimation**.

Statistical estimation is one of the primary goals of inferential statistics. Instead of describing only the observed sample, it allows us to use sample information to make conclusions about the entire population.

For example, suppose we want to know the average height of all university students in Ethiopia. Measuring every student may be impossible. Instead, we select a random sample, calculate its average height, and use that information to estimate the true population mean.

However, because every sample is different, every estimate contains some uncertainty. Rather than reporting only a single estimated value, statisticians often report a range of plausible values together with a confidence level. This range is called a **confidence interval**.

Confidence intervals provide not only an estimate of the unknown parameter but also an indication of the precision of that estimate.

---

# What Is Statistical Estimation?

**Statistical estimation** is the process of using sample data to estimate an unknown population parameter.

The unknown quantity may be:

* the population mean,
* the population proportion,
* the population variance,
* or another population characteristic.

Since population parameters are usually unknown, they must be estimated using sample statistics.

For example,

```text
Population mean (μ) → estimated by Sample mean (x̄)

Population proportion (p) → estimated by Sample proportion (p̂)

Population variance (σ²) → estimated by Sample variance (s²)
```

Thus, statistical estimation provides a practical way to learn about large populations without observing every member.

---

# Types of Estimation

Statistical estimation is generally divided into two categories.

## Point Estimation

A **point estimate** is a single numerical value used to estimate an unknown population parameter.

Examples:

```text
Sample mean (x̄) estimates the population mean (μ).

Sample proportion (p̂) estimates the population proportion (p).

Sample variance (s²) estimates the population variance (σ²).
```

Although point estimates are simple and easy to compute, they do not indicate how accurate the estimate is.

For example,

```text
Estimated average income = 5,000 Birr
```

This provides only one value and gives no information about its possible error.

---

## Interval Estimation

An **interval estimate** provides a range of values that is likely to contain the true population parameter.

Example:

```text
Average income

Between

4,850 Birr

and

5,150 Birr
```

Unlike a point estimate, an interval estimate communicates both the estimated value and the uncertainty associated with it.

The most common interval estimate is the **confidence interval**.

---

# Properties of a Good Estimator

Not every estimator is equally useful. A good estimator should possess desirable statistical properties.

## 1. Unbiasedness

An estimator is **unbiased** if its average value over many samples equals the true population parameter.

Mathematically,

```text
Expected value of estimator

=

True population parameter
```

An unbiased estimator neither consistently overestimates nor consistently underestimates the parameter.

---

## 2. Consistency

An estimator is **consistent** if it becomes closer to the true population parameter as the sample size increases.

In other words,

```text
Larger sample

↓

Better estimate
```

Consistency ensures that increasing the amount of data improves the quality of the estimate.

---

## 3. Efficiency

Two unbiased estimators may both estimate the same parameter correctly on average.

The **more efficient** estimator is the one with the smaller variance.

Smaller variance means:

* less variability,
* greater precision,
* more reliable estimates.

---

## 4. Sufficiency (Introduction)

An estimator is **sufficient** if it uses all the relevant information in the sample about the parameter being estimated.

Although sufficiency is an advanced concept, it is important because sufficient estimators make the best possible use of the available data.

---

# Point Estimation

Point estimation involves calculating a single statistic from a sample to estimate a population parameter.

Common point estimators include:

| Population Parameter      | Point Estimator        |
| ------------------------- | ---------------------- |
| Population mean (μ)       | Sample mean (x̄)       |
| Population proportion (p) | Sample proportion (p̂) |
| Population variance (σ²)  | Sample variance (s²)   |

For example, suppose a sample of 100 students has an average score of:

```text
78.5
```

Then,

```text
Estimated population mean = 78.5
```

This value is the **point estimate** of the unknown population mean.

Although point estimates are widely used, they should be interpreted carefully because different samples generally produce different estimates.

---

# Confidence Intervals

Because point estimates vary from sample to sample, it is often preferable to estimate a parameter using an interval rather than a single value.

A **confidence interval** is a range of values that is likely to contain the true population parameter.

Instead of reporting:

```text
Population mean = 78.5
```

we may report:

```text
Population mean

Between

76.8

and

80.2
```

This interval expresses the uncertainty associated with sampling.

Confidence intervals therefore provide more information than point estimates.

---

# Confidence Level

A **confidence level** represents the long-run success rate of the confidence interval procedure.

Common confidence levels are:

```text
90%

95%

99%
```

For example,

a **95% confidence level** means that if we repeatedly selected samples and constructed confidence intervals using the same method, approximately **95% of those intervals would contain the true population parameter**.

It does **not** mean that there is a 95% probability that the already computed interval contains the parameter.

The confidence level refers to the **method**, not to one specific interval.

---

# Margin of Error

The **margin of error** measures the maximum expected difference between the sample estimate and the true population parameter.

It determines how far the confidence interval extends on either side of the point estimate.

The relationship is:

```text
Confidence Interval

=

Point Estimate

±

Margin of Error
```

A smaller margin of error produces a narrower confidence interval and therefore a more precise estimate.

The margin of error depends mainly on:

* the confidence level,
* the sample size,
* the variability of the data.

---

# Critical Value

The **critical value** is the multiplier used to determine the margin of error.

Its value depends on:

* the confidence level,
* the probability distribution being used.

The two most common critical values are:

* **Z critical value**, based on the Standard Normal distribution.
* **t critical value**, based on Student's t-distribution.

Generally:

* Z values are used when the population standard deviation is known or the sample size is sufficiently large.
* t values are used when the population standard deviation is unknown and must be estimated from the sample.

The choice between Z and t will be discussed in detail later in this chapter.

---

# General Confidence Interval Formula

The general structure of every confidence interval is:

```text
Confidence Interval

=

Point Estimate

±

Critical Value × Standard Error
```

This formula has three main components:

* **Point Estimate** — the best estimate obtained from the sample.
* **Critical Value** — determined by the chosen confidence level.
* **Standard Error** — measures the variability of the estimator.

This general formula serves as the foundation for constructing confidence intervals for means, proportions, variances, and many other population parameters.
# Confidence Interval for the Population Mean

The primary objective of statistical estimation is to estimate an unknown population mean using information obtained from a sample.

Because different samples produce different sample means, a single point estimate is usually insufficient to describe the true population mean with certainty.

Instead of reporting only one estimated value, statisticians construct a **confidence interval**, which provides a range of plausible values for the unknown population mean.

The method used to construct the confidence interval depends on whether the **population standard deviation** is known.

There are two common situations:

* Population standard deviation is known.
* Population standard deviation is unknown.

Each situation requires a different probability distribution.

---

# Confidence Interval When the Population Standard Deviation Is Known (Z-Interval)

Suppose the population standard deviation (σ) is known.

In this situation, the sampling distribution of the sample mean follows the **Standard Normal (Z) distribution** (or approximately follows it when the sample size is sufficiently large).

Therefore, the confidence interval for the population mean is

```text
                 σ
μ = x̄ ± Zα/2 × ------
                √n
```

where

* **μ** = population mean
* **x̄** = sample mean (point estimate)
* **Zα/2** = critical value from the Standard Normal distribution
* **σ** = population standard deviation
* **n** = sample size

---

# Understanding the Formula

Notice that the formula has three important components.

### 1. Point Estimate

The center of the confidence interval is

```text
x̄
```

which is the best estimate of the unknown population mean.

---

### 2. Standard Error

The quantity

```text
     σ
-----------
    √n
```

is called the **standard error of the sample mean**.

It measures how much the sample mean varies from one sample to another.

A smaller standard error indicates a more precise estimate.

---

### 3. Margin of Error

The quantity

```text
          σ
Zα/2 × --------
         √n
```

is called the **margin of error**.

Therefore,

```text
                 σ
ME = Zα/2 × ----------
                √n
```

The margin of error determines how far the confidence interval extends on either side of the sample mean.

---

# General Form

The confidence interval can therefore be written more simply as

```text
Confidence Interval

=

Point Estimate

±

Margin of Error
```

This form applies to almost every confidence interval encountered in statistics.

Only the formulas for the point estimate, standard error, and critical value change.

---

# Concept Note

A confidence interval is always centered at the sample statistic.

The uncertainty comes from the **margin of error**, not from the sample mean itself.

Consequently,

```text
Larger Margin of Error

↓

Wider Confidence Interval

↓

Less Precise Estimate
```

whereas

```text
Smaller Margin of Error

↓

Narrower Confidence Interval

↓

More Precise Estimate
```

---

# Confidence Interval When the Population Standard Deviation Is Unknown (t-Interval)

In practical applications, the population standard deviation is almost never known.

Instead, it must be estimated using the **sample standard deviation**, denoted by

```text
s
```

Because the standard deviation is now estimated rather than known exactly, additional uncertainty is introduced into the estimation process.

To account for this uncertainty, statisticians use **Student's t-distribution** instead of the Standard Normal distribution.

The confidence interval becomes

```text
                 s
μ = x̄ ± tα/2 × ------
                √n
```

where

* **μ** = population mean
* **x̄** = sample mean
* **tα/2** = critical value from Student's t-distribution
* **s** = sample standard deviation
* **n** = sample size

---

# Standard Error

When the population standard deviation is unknown, the standard error becomes

```text
      s
SE = ------
     √n
```

Notice that only one symbol has changed.

Instead of

```text
σ
```

we now use

```text
s
```

because the sample standard deviation is estimating the unknown population standard deviation.

---

# Why Do We Use the t-Distribution?

The sample standard deviation is only an estimate of the true population standard deviation.

Therefore, more uncertainty exists.

Student's t-distribution compensates for this additional uncertainty.

Compared with the Standard Normal distribution, the t-distribution

* has the same bell-shaped appearance,
* has heavier tails,
* produces larger critical values,
* produces wider confidence intervals.

This additional width reflects the uncertainty introduced by estimating the population standard deviation.

---

# Effect of Sample Size

As the sample size increases,

the estimate of the population standard deviation becomes more accurate.

Consequently, the t-distribution gradually approaches the Standard Normal distribution.

This relationship can be summarized as

```text
Larger Sample Size

↓

Smaller Estimation Error

↓

t Distribution Approaches

↓

Standard Normal Distribution
```

For large samples, the difference between the two distributions becomes very small.

---

# Which Formula Should We Use?

The choice between the two confidence interval formulas is straightforward.

Use the **Z-interval** when

* the population standard deviation is known, or
* the sample size is sufficiently large and the Z approximation is appropriate.

Use the **t-interval** when

* the population standard deviation is unknown.

Since the population standard deviation is rarely known in real-world problems, the **t-interval is the method used most frequently in practice**.

---

# Confidence Interval for a Population Proportion

Not every statistical study estimates a population mean.

Sometimes the objective is to estimate the **proportion** of a population possessing a particular characteristic.

Examples include

* the proportion of voters supporting a candidate,
* the proportion of defective products,
* the proportion of customers satisfied with a service,
* the proportion of students who passed an examination.

Suppose

```text
p
```

denotes the population proportion and

```text
p̂
```

denotes the sample proportion.

The confidence interval for the population proportion is

```text
                     p̂(1 − p̂)
p = p̂ ± Zα/2 × √ -------------
                         n
```

where

* **p** = population proportion
* **p̂** = sample proportion
* **Zα/2** = critical value
* **n** = sample size

---

# Standard Error of the Sample Proportion

The standard error of the sample proportion is

```text
            p̂(1 − p̂)
SE = √ -------------------
                 n
```

The confidence interval therefore follows the same general structure used throughout this chapter:

```text
Confidence Interval

=

Point Estimate

±

Critical Value × Standard Error
```

Although the formulas for the standard error differ, the underlying principle remains exactly the same.
# Factors Affecting the Width of a Confidence Interval

Not all confidence intervals have the same width.

Some confidence intervals are narrow, while others are much wider.

The width of a confidence interval depends mainly on three factors:

* Sample size
* Confidence level
* Population variability

Understanding these factors helps us determine how to obtain more precise estimates.

---

# 1. Effect of Sample Size

The sample size has one of the greatest influences on the width of a confidence interval.

Recall that the standard error of the sample mean is

```text
      σ
SE = ------
     √n
```

or, when the population standard deviation is unknown,

```text
      s
SE = ------
     √n
```

Notice that the sample size appears in the denominator.

As the sample size increases,

* the denominator becomes larger,
* the standard error becomes smaller,
* the margin of error decreases,
* the confidence interval becomes narrower.

This relationship can be summarized as

```text
Larger Sample Size

↓

Smaller Standard Error

↓

Smaller Margin of Error

↓

Narrower Confidence Interval
```

---

## Concept Note

A larger sample provides more information about the population.

Therefore, larger samples generally produce more reliable and more precise estimates.

---

# 2. Effect of the Confidence Level

The confidence level also affects the width of the confidence interval.

Common confidence levels are

```text
90%

95%

99%
```

As the confidence level increases,

the corresponding critical value also increases.

For example,

```text
90%  →  Smaller Critical Value

95%  →  Larger Critical Value

99%  →  Largest Critical Value
```

A larger critical value produces a larger margin of error.

Consequently,

```text
Higher Confidence Level

↓

Larger Critical Value

↓

Larger Margin of Error

↓

Wider Confidence Interval
```

---

## Concept Note

Higher confidence means greater certainty that the interval contains the true population parameter.

However, this increased certainty comes at the cost of lower precision because the interval becomes wider.

---

# 3. Effect of Population Variability

Population variability is measured by the population standard deviation (σ).

A population with large variability produces a larger standard error.

Since

```text
      σ
SE = ------
     √n
```

a larger standard deviation increases the standard error.

Consequently,

```text
Greater Variability

↓

Larger Standard Error

↓

Larger Margin of Error

↓

Wider Confidence Interval
```

Populations with little variability produce much narrower confidence intervals.

---

# Interpretation of Confidence Intervals

Interpreting a confidence interval correctly is one of the most important concepts in inferential statistics.

Suppose a 95% confidence interval for the population mean is

```text
(68.4 , 71.6)
```

The correct interpretation is

> We are **95% confident** that the interval from **68.4 to 71.6** was produced by a method that captures the true population mean in approximately **95% of repeated random samples**.

Notice that the confidence level refers to the **procedure**, not to one particular interval.

---

# Common Misconceptions

Confidence intervals are often misunderstood.

The following statements are incorrect.

---

## Misconception 1

> "There is a 95% probability that the true population mean lies inside this interval."

This statement is incorrect.

The population mean is a fixed (although unknown) value.

The interval either contains the true mean or it does not.

The probability applies to the **sampling procedure**, not to the already constructed interval.

---

## Misconception 2

> "A 99% confidence interval is always better than a 95% confidence interval."

Not necessarily.

A 99% confidence interval is wider.

It provides greater confidence but lower precision.

Whether it is better depends on the purpose of the study.

---

## Misconception 3

> "Increasing the sample size changes the population mean."

Incorrect.

Increasing the sample size does **not** change the population parameter.

It simply produces a more precise estimate of that parameter.

---

# Relationship Between Sampling, Standard Error, and Confidence Intervals

The concepts introduced throughout Chapters 6 and 7 are closely connected.

The complete process can be summarized as

```text
Population

↓

Random Sampling

↓

Sample

↓

Sample Statistic

↓

Sampling Distribution

↓

Standard Error

↓

Margin of Error

↓

Confidence Interval

↓

Estimate of Population Parameter
```

This flow illustrates the foundation of inferential statistics.

Without sampling,

there is no sampling distribution.

Without a sampling distribution,

there is no standard error.

Without the standard error,

there is no confidence interval.

---

# Applications

Confidence intervals are used in almost every field that relies on data.

Examples include

* Medical research
* Engineering
* Economics
* Business analytics
* Agriculture
* Data Science
* Machine Learning
* Artificial Intelligence
* Scientific research
* Government surveys
* Opinion polling
* Quality control

Whenever researchers estimate an unknown population characteristic from sample data, confidence intervals provide a measure of the reliability and precision of the estimate.

---

# Summary

* Statistical estimation uses sample data to estimate unknown population parameters.
* Point estimation provides a single estimated value.
* Interval estimation provides a range of plausible values for the unknown parameter.
* Confidence intervals combine a point estimate with a margin of error.
* The margin of error depends on the critical value and the standard error.
* Z-intervals are used when the population standard deviation is known.
* t-intervals are used when the population standard deviation is unknown.
* Increasing the sample size narrows the confidence interval.
* Increasing the confidence level widens the confidence interval.
* Increasing population variability widens the confidence interval.
* Confidence intervals provide the mathematical foundation for hypothesis testing, which is the next major topic in inferential statistics.

