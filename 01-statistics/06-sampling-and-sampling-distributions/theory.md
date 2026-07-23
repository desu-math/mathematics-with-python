# Sampling and Sampling Distributions

## Introduction

In statistics, we are often interested in studying a large group of individuals or objects, known as a **population**. However, collecting information from every member of a population is often impractical because it may be too expensive, time-consuming, or impossible.

Instead, statisticians collect information from a smaller subset of the population, called a **sample**, and use the information obtained from the sample to make conclusions about the entire population.

This process forms the foundation of **inferential statistics**.

---

# Population and Sample

A **population** is the complete collection of individuals, objects, or observations of interest.

Examples:

* All students in a university.
* All households in a city.
* All manufactured products in a factory.

A **sample** is a subset of the population selected for analysis.

Examples:

* 500 students selected from a university.
* 1,000 households selected from a city.
* 200 products selected from a production line.

The objective of sampling is to obtain information about the population by studying only the selected sample.

---

# Population Parameters and Sample Statistics

A **parameter** is a numerical characteristic of a population.

Common population parameters include:

* Population mean (μ)
* Population variance (σ²)
* Population standard deviation (σ)
* Population proportion (p)

A **statistic** is a numerical characteristic calculated from a sample.

Common sample statistics include:

* Sample mean (x bar)
* Sample variance ((s^2))
* Sample standard deviation (s)
* Sample proportion ((\hat p))

Population parameters are usually unknown, while sample statistics are used to estimate them.

---

# Census and Sampling

A **census** collects information from every member of a population.

Advantages:

* Complete information.
* No sampling error.

Disadvantages:

* Expensive.
* Time-consuming.
* Often impractical.

**Sampling** collects information from only part of the population.

Advantages:

* Faster.
* Less expensive.
* Practical for large populations.

Disadvantages:

* Results may differ from the true population values because only a subset is observed.

---

# Why Sampling Is Necessary

Sampling is preferred when:

* the population is very large,
* collecting all observations is impossible,
* measurements are destructive,
* limited time or resources are available.

Most scientific studies, surveys, and machine learning datasets are based on samples rather than complete populations.

---

# Sampling Methods

Sampling methods are generally classified into two categories.

## Probability Sampling

Every population member has a known probability of being selected.

Common probability sampling methods include:

* Simple Random Sampling
* Systematic Sampling
* Stratified Sampling
* Cluster Sampling

Probability sampling generally produces more representative samples and supports statistical inference.

---

## Non-Probability Sampling

The probability of selecting each population member is unknown.

Common non-probability sampling methods include:

* Convenience Sampling
* Judgment (Purposive) Sampling
* Quota Sampling
* Snowball Sampling

These methods are easier to implement but may introduce selection bias.

---

# Sampling Error

A sample rarely produces exactly the same result as the population.

The difference between a sample statistic and the corresponding population parameter is called the **sampling error**.

For example,

```text
Population mean = 70

Sample mean = 69.4
```

Sampling error:

```text
69.4 − 70 = −0.6
```

Sampling error occurs because different samples produce different statistics.

Increasing the sample size generally reduces sampling error.

---

# Sampling Distribution

Suppose we repeatedly draw samples of the same size from a population.

Each sample has its own statistic, such as a sample mean.

The distribution formed by these sample statistics is called the **sampling distribution**.

For example,

```text
Sample 1 → x̄ = 69.8

Sample 2 → x̄ = 70.5

Sample 3 → x̄ = 70.1

Sample 4 → x̄ = 69.9
```

The collection of these sample means forms the sampling distribution of the sample mean.

Sampling distributions are fundamental because statistical inference is based on them.

---

# Central Limit Theorem

The **Central Limit Theorem (CLT)** is one of the most important results in statistics.

It states that:

> As the sample size becomes sufficiently large, the sampling distribution of the sample mean approaches a Normal distribution, regardless of the shape of the population distribution.

In practice, a sample size of approximately:

```text
n ≥ 30
```

is often considered sufficient, although the required size depends on the population distribution.

The Central Limit Theorem explains why the Normal distribution appears so frequently in statistical inference.

---

# Standard Error

The **Standard Error (SE)** measures the variability of a sample statistic from one sample to another.

For the sample mean,

```text
           σ
SE = -------------
        √n
```

where:

* σ = population standard deviation
* n = sample size

The standard error decreases as the sample size increases.

Therefore, larger samples generally produce more precise estimates.

---

# Sampling Distribution of the Mean

The sampling distribution of the sample mean has the following properties.

Mean:

```text
E(x̄) = μ
```

The sample mean is an unbiased estimator of the population mean.

Standard Error:

```text
           σ
SE = -------------
        √n
```

If the population is Normal, the sampling distribution is also Normal.

If the population is not Normal, the Central Limit Theorem ensures that the sampling distribution becomes approximately Normal for sufficiently large sample sizes.

---

# Sampling Distribution of the Proportion

When studying proportions, the sample proportion is denoted by:

```text
p̂
```

The sampling distribution of the sample proportion has:

Mean:

```text
E(p̂) = p
```

Standard Error:

```text
            p(1−p)
SE = √ ---------------
               n
```

The sampling distribution of the proportion is approximately Normal when the sample size is sufficiently large.

---

# Relationship Between the Concepts

The concepts introduced in this chapter are closely connected.

```text
Population
      │
      ▼
Sampling
      │
      ▼
Sample
      │
      ▼
Sample Statistics
      │
      ▼
Sampling Distribution
      │
      ▼
Central Limit Theorem
      │
      ▼
Standard Error
      │
      ▼
Statistical Inference
```

Together, they provide the theoretical foundation for confidence intervals and hypothesis testing.

---

# Applications

Sampling and sampling distributions are widely used in:

* Survey research
* Scientific experiments
* Quality control
* Medical research
* Economics
* Data Science
* Machine Learning
* Artificial Intelligence

Whenever conclusions about a population are made from sample data, these concepts are involved.

---

# Summary

* A population is the complete collection of observations, while a sample is a subset selected for analysis.
* Population parameters are estimated using sample statistics.
* Sampling is often preferred over a census because it is faster, less expensive, and more practical.
* Sampling error is the difference between a sample statistic and the corresponding population parameter.
* A sampling distribution describes the distribution of a sample statistic obtained from repeated sampling.
* The Central Limit Theorem states that the sampling distribution of the sample mean approaches a Normal distribution as the sample size increases.
* The Standard Error measures the variability of a sample statistic across repeated samples.
* Sampling distributions form the theoretical foundation of inferential statistics, including confidence intervals and hypothesis testing.
