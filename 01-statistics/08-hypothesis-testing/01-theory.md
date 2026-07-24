# Hypothesis Testing

## Introduction

In the previous chapter, we learned how to estimate unknown population parameters using **point estimates** and **confidence intervals**.

Although confidence intervals provide a range of plausible values for an unknown population parameter, researchers often need to answer a different type of question.

Instead of asking,

> **"What is the value of the population parameter?"**

they ask,

> **"Is there enough statistical evidence to support a particular claim about the population?"**

Answering this type of question is the purpose of **hypothesis testing**.

Hypothesis testing is one of the most important methods in inferential statistics. It provides a systematic procedure for using sample data to evaluate claims about a population.

Rather than proving a claim with absolute certainty, hypothesis testing measures whether the available evidence is strong enough to support or reject that claim.

---

# Why Do We Need Hypothesis Testing?

Many practical problems involve making decisions under uncertainty.

Consider the following situations:

* A pharmaceutical company claims that a new medicine lowers blood pressure more effectively than the current treatment.
* A manufacturer claims that the average lifetime of a light bulb is **1,000 hours**.
* A university claims that its students score higher than the national average.
* A farmer claims that a new fertilizer increases crop yield.
* A data scientist claims that a machine learning model performs better than an existing model.

In each case, the claim concerns an entire population, but collecting data from every member of the population is usually impossible.

Instead, we collect a sample and use statistical methods to determine whether the observed evidence supports the claim.

This decision-making process is called **hypothesis testing**.

---

# What Is Hypothesis Testing?

**Hypothesis testing** is a statistical procedure used to determine whether sample data provide sufficient evidence to support or reject a claim about a population parameter.

The procedure begins with a statement about the population, called a **hypothesis**.

Sample data are then collected and analyzed to determine whether the observed results are consistent with that hypothesis.

The conclusion is based on probability rather than certainty.

---

# Definition

> **Hypothesis testing is the process of using sample data to evaluate a claim about a population parameter by making a statistical decision based on the available evidence.**

The decision is always made with the understanding that sampling variability exists.

For this reason, hypothesis testing never guarantees absolute certainty.

Instead, it quantifies the strength of the evidence provided by the sample.

---

# Statistical Hypotheses

A **statistical hypothesis** is a statement or claim about a population parameter.

The parameter may be

* a population mean,
* a population proportion,
* a population variance,
* or another characteristic of the population.

Examples include:

```text 
The average height of students is 170 cm.

The average waiting time is 15 minutes.

The proportion of defective products is 2%.

The average monthly income is 8,000 birr.
```

Each of these statements can be tested using sample data.

---

# Types of Statistical Hypotheses

Every hypothesis test involves two competing hypotheses.

These are

* the **Null Hypothesis**, and
* the **Alternative Hypothesis**.

Together, they represent two opposing explanations for the observed data.

The objective of hypothesis testing is to determine which explanation is better supported by the sample.

---

# Null Hypothesis (H₀)

The **Null Hypothesis**, denoted by

```text id="r6v8x2"
H₀
```

is the initial claim about the population.

It usually represents

* no effect,
* no difference,
* no change,
* or the current belief about the population.

The null hypothesis is assumed to be true unless the sample provides strong evidence against it.

---

## Examples

Example 1

A company claims that the average lifetime of its batteries is **500 hours**.

The null hypothesis is

```text id="w2f9j8"
H₀ : μ = 500
```

---

Example 2

A university claims that the average GPA of its students is **3.20**.

```text id="g7m3n5"
H₀ : μ = 3.20
```

---

Example 3

A factory claims that **2%** of its products are defective.

```text id="x1q4z6"
H₀ : p = 0.02
```

---

# Why Is It Called the Null Hypothesis?

The word **null** means *no effect* or *no difference*.

The null hypothesis serves as the default assumption.

Unless the sample provides convincing evidence to the contrary, we continue to accept this assumption.

For this reason, statistical testing begins by assuming that the null hypothesis is true.

---

# Alternative Hypothesis (H₁ or Hₐ)

The **Alternative Hypothesis**, denoted by

```text id="j5l2w9"
H₁

or

Hₐ
```

is the statement that contradicts the null hypothesis.

It represents the claim that the researcher wishes to investigate.

The alternative hypothesis states that

* an effect exists,
* a difference exists,
* or the population parameter differs from the value specified in the null hypothesis.

---

## Examples

Continuing the previous examples:

Battery lifetime

```text id="m8d1r4"
H₀ : μ = 500

H₁ : μ ≠ 500
```

---

Student GPA

```text id="n3v7p6"
H₀ : μ = 3.20

H₁ : μ > 3.20
```

---

Defective products

```text id="c4k8s2"
H₀ : p = 0.02

H₁ : p < 0.02
```

---

# Relationship Between H₀ and H₁

The null hypothesis and the alternative hypothesis are mutually exclusive.

This means that only one of them can correctly describe the population.

Their relationship can be summarized as

```text id="u9y6b3"
Null Hypothesis (H₀)

        versus

Alternative Hypothesis (H₁)
```

The purpose of hypothesis testing is **not** to prove that the alternative hypothesis is true.

Instead, the goal is to determine whether there is sufficient statistical evidence to reject the null hypothesis in favor of the alternative hypothesis.

---

# Important Concept

One of the most common misunderstandings in statistics is believing that hypothesis testing proves a hypothesis.

This is not true.

Hypothesis testing does **not** prove that the null hypothesis is true or false.

Instead, it evaluates whether the sample provides enough evidence to reject the null hypothesis.

Consequently, the final decision is always expressed as one of the following:

```text id="e2n5k7"
Reject H₀

or

Fail to Reject H₀
```

Notice that statisticians do **not** say

```text id="q8p3m1"
Accept H₀
```

because the available evidence may simply be insufficient to reject it.

Failing to reject the null hypothesis does not prove that it is true; it only indicates that the sample does not provide strong enough evidence against it.

---

# Summary

* Hypothesis testing is a statistical procedure used to evaluate claims about population parameters.
* It uses sample data to make decisions under uncertainty.
* Every hypothesis test begins with two competing hypotheses.
* The **Null Hypothesis (H₀)** represents the default assumption or existing claim.
* The **Alternative Hypothesis (H₁ or Hₐ)** represents the competing claim that the researcher wants to investigate.
* Hypothesis testing never proves a hypothesis; it determines whether the sample provides sufficient evidence to reject the null hypothesis.
# Types of Hypothesis Tests

The form of the alternative hypothesis determines the type of hypothesis test that should be performed.

Depending on the research question, a hypothesis test may investigate whether

* the population parameter is **different** from a specified value,
* the population parameter is **greater** than a specified value,
* the population parameter is **less** than a specified value.

Consequently, hypothesis tests are classified into three categories:

* Two-tailed test
* Right-tailed test
* Left-tailed test

Understanding these three tests is essential because they determine

* the rejection region,
* the critical value,
* and the final statistical decision.

---

# Two-Tailed Test

A **two-tailed test** is used when the researcher wants to determine whether the population parameter is **different** from a specified value.

In other words, both larger and smaller values are considered evidence against the null hypothesis.

The hypotheses are written as

```text id="rj5w1c"
H₀ : μ = μ₀

H₁ : μ ≠ μ₀
```

where

* **μ** = population mean
* **μ₀** = hypothesized population mean

The symbol

```text id="c8v2ze"
≠
```

means that the true population mean may be either greater than or less than the hypothesized value.

---

## Example

A manufacturer claims that the average weight of a package is **500 g**.

A quality inspector wants to determine whether the average weight has changed.

The hypotheses are

```text id="f2x7kv"
H₀ : μ = 500

H₁ : μ ≠ 500
```

Since any deviation from **500 g** is important, a **two-tailed test** is appropriate.

---

## Decision Idea

In a two-tailed test,

evidence against the null hypothesis may appear in either tail of the sampling distribution.

Therefore, the significance level is divided equally between the two tails.

For a significance level of

```text id="n3u8mp"
α = 0.05
```

each tail contains

```text id="q9m6wa"
α/2 = 0.025
```

---

# Right-Tailed Test

A **right-tailed test** is used when the researcher wants to determine whether the population parameter is **greater** than a specified value.

The hypotheses are

```text id="v4h1sy"
H₀ : μ = μ₀

H₁ : μ > μ₀
```

The symbol

```text id="h6z3bn"
>
```

indicates that only values larger than the hypothesized value support the alternative hypothesis.

---

## Example

A university introduces a new teaching method and claims that it increases students' average examination scores.

Suppose the previous average score was **70**.

The hypotheses become

```text id="t8c4qx"
H₀ : μ = 70

H₁ : μ > 70
```

Only an increase in the average score supports the research claim.

Therefore, a **right-tailed test** is appropriate.

---

## Decision Idea

In a right-tailed test,

the entire significance level is placed in the **right tail** of the sampling distribution.

For example,

```text id="a5n8vr"
α = 0.05
```

is located entirely in the right tail.

Only sufficiently large test statistics lead to rejection of the null hypothesis.

---

# Left-Tailed Test

A **left-tailed test** is used when the researcher wants to determine whether the population parameter is **less** than a specified value.

The hypotheses are

```text id="w2k9ep"
H₀ : μ = μ₀

H₁ : μ < μ₀
```

The symbol

```text id="d7m5xt"
<
```

indicates that only values smaller than the hypothesized value support the alternative hypothesis.

---

## Example

A company claims that a new production process reduces the average manufacturing time.

Suppose the current average production time is **45 minutes**.

The hypotheses are

```text id="y6f3cb"
H₀ : μ = 45

H₁ : μ < 45
```

Since only a reduction is important,

a **left-tailed test** is appropriate.

---

## Decision Idea

In a left-tailed test,

the entire significance level is placed in the **left tail** of the sampling distribution.

Only sufficiently small test statistics provide evidence against the null hypothesis.

---

# Comparing the Three Types of Tests

The three hypothesis tests differ only in the form of the alternative hypothesis.

| Type of Test | Null Hypothesis | Alternative Hypothesis | Rejection Region |
| ------------ | --------------- | ---------------------- | ---------------- |
| Two-tailed   | H₀ : μ = μ₀     | H₁ : μ ≠ μ₀            | Both tails       |
| Right-tailed | H₀ : μ = μ₀     | H₁ : μ > μ₀            | Right tail       |
| Left-tailed  | H₀ : μ = μ₀     | H₁ : μ < μ₀            | Left tail        |

---

# Choosing the Correct Test

The choice of hypothesis test depends entirely on the research question.

Ask the following questions:

### Question 1

Do we want to determine whether the population parameter has **changed**?

Use

```text id="m8v1rs"
Two-tailed Test
```

---

### Question 2

Do we want to determine whether the population parameter has **increased**?

Use

```text id="x4g7qw"
Right-tailed Test
```

---

### Question 3

Do we want to determine whether the population parameter has **decreased**?

Use

```text id="j2c5na"
Left-tailed Test
```

---

# Test Statistic

After formulating the hypotheses, the next step is to measure how well the sample agrees with the null hypothesis.

This measurement is performed using a **test statistic**.

A **test statistic** is a numerical value calculated from the sample data that measures the difference between the observed sample statistic and the value stated in the null hypothesis.

It summarizes the evidence contained in the sample into a single number that can be compared with a probability distribution.

---

# Definition

> **A test statistic is a standardized numerical measure computed from sample data and used to decide whether the null hypothesis should be rejected.**

The larger the disagreement between the sample and the null hypothesis,

the more extreme the test statistic becomes.

---

# Why Do We Need a Test Statistic?

Suppose a manufacturer claims that the average weight of a package is

```text id="b5q8nu"
500 g
```

A sample of packages has an average weight of

```text id="n7r3fz"
506 g
```

Is a difference of **6 g** large enough to reject the manufacturer's claim?

It depends on

* the sample size,
* the variability of the data,
* and the sampling distribution.

The test statistic accounts for all of these factors and provides an objective basis for making a statistical decision.

---

# Common Test Statistics

Different statistical problems require different test statistics.

The two most common test statistics for estimating population means are

* **Z-statistic**
* **t-statistic**

Both measure the number of **standard errors** separating the sample statistic from the hypothesized population value.

The difference between them lies in whether the population standard deviation is known.

---

# Z-Test

A **Z-test** is used when

* the population standard deviation is known, or
* the sample size is sufficiently large and the normal approximation is appropriate.

The Z-test statistic is

```text id="v3x5hj"
          x̄ − μ₀
Z = -------------------
         σ
        ------
         √n
```

where

* **x̄** = sample mean
* **μ₀** = hypothesized population mean
* **σ** = population standard deviation
* **n** = sample size

The numerator measures the difference between the sample mean and the hypothesized mean.

The denominator converts this difference into units of standard error.

---

# t-Test

In practice, the population standard deviation is rarely known.

Instead, we estimate it using the sample standard deviation.

In this situation, we use the **t-test**.

The test statistic is

```text id="y9n4bc"
          x̄ − μ₀
t = -------------------
         s
        ------
         √n
```

where

* **s** = sample standard deviation

All other symbols have the same meanings as before.

The t-test follows **Student's t-distribution**, which accounts for the additional uncertainty introduced by estimating the population standard deviation.

---

# Comparing the Z-Test and the t-Test

| Z-Test                                 | t-Test                                         |
| -------------------------------------- | ---------------------------------------------- |
| Population standard deviation is known | Population standard deviation is unknown       |
| Uses the Standard Normal distribution  | Uses Student's t-distribution                  |
| Usually applied to large samples       | Commonly applied to small and moderate samples |
| Uses σ                                 | Uses s                                         |

---

# Level of Significance (α)

Hypothesis testing is based on probability.

Whenever we make a statistical decision, there is always a possibility of making an incorrect conclusion.

To control this risk, statisticians choose a **level of significance**, denoted by

```text id="r4m8qe"
α
```

before analyzing the data.

The level of significance represents the maximum probability of rejecting the null hypothesis when it is actually true.

---

# Definition

> **The level of significance (α) is the maximum probability of making a Type I error that the researcher is willing to accept.**

It establishes the criterion used to decide whether the sample evidence is sufficiently strong to reject the null hypothesis.

---

# Common Significance Levels

The most frequently used significance levels are

```text id="z6k2vf"
α = 0.10

α = 0.05

α = 0.01
```

These correspond to confidence levels of

```text id="u1p5jd"
90%

95%

99%
```

respectively.

The relationship is

```text id="n8q3lx"
Confidence Level

=

1 − α
```

---

# Concept Note

A smaller significance level makes it more difficult to reject the null hypothesis because stronger evidence is required.

Conversely, a larger significance level makes rejection easier but increases the risk of making an incorrect decision.

The significance level chosen at this stage determines the critical values and decision rules that will be developed in the next section of this chapter.
# Critical Value

After selecting the significance level and calculating the test statistic, the next step is to determine the **critical value**.

The critical value separates the values of the test statistic that are considered **consistent** with the null hypothesis from those that are considered **unlikely** if the null hypothesis is true.

In other words, the critical value serves as the decision boundary in hypothesis testing.

---

# Definition

> **A critical value is a value obtained from a probability distribution that separates the rejection region from the non-rejection region.**

The critical value depends on

* the probability distribution used (Z or t),
* the significance level (α),
* the type of hypothesis test,
* and, for the t-distribution, the degrees of freedom.

---

# Why Do We Need a Critical Value?

Suppose a hypothesis test produces the following test statistic:

```text id="x2d9pv"
Z = 2.15
```

Is this value large enough to reject the null hypothesis?

The answer cannot be determined simply by looking at the number **2.15**.

Instead, it must be compared with a reference value obtained from the appropriate probability distribution.

This reference value is called the **critical value**.

The comparison determines whether the sample result is statistically significant.

---

# Determining the Critical Value

The critical value is obtained from the appropriate probability distribution.

The choice depends on the type of test.

---

## Two-Tailed Test

For a two-tailed test,

the significance level is divided equally between the two tails.

If

```text id="m6k4zr"
α = 0.05
```

then

```text id="a9f2qx"
α/2 = 0.025
```

is placed in each tail.

The critical values are

```text id="q7j8tb"
−Zα/2

and

+Zα/2
```

For a 95% confidence level,

```text id="t4w1np"
Critical Values

=

−1.96

and

+1.96
```

---

## Right-Tailed Test

For a right-tailed test,

the entire significance level is placed in the right tail.

If

```text id="u8p5vk"
α = 0.05
```

the critical value is

```text id="r2n9cf"
+Zα
```

For the Standard Normal distribution,

```text id="f3y7qa"
Critical Value

=

+1.645
```

---

## Left-Tailed Test

For a left-tailed test,

the entire significance level is placed in the left tail.

If

```text id="v5k8mz"
α = 0.05
```

the critical value is

```text id="k1m4wx"
−Zα
```

For the Standard Normal distribution,

```text id="e9r6bj"
Critical Value

=

−1.645
```

---

# Critical Region

The **critical region** is the set of all values of the test statistic that lead to rejection of the null hypothesis.

These values are considered sufficiently unlikely under the assumption that the null hypothesis is true.

Whenever the calculated test statistic falls inside the critical region,

the null hypothesis is rejected.

---

# Definition

> **The critical region is the region of the probability distribution that contains values of the test statistic leading to rejection of the null hypothesis.**

The size of the critical region is determined by the significance level.

For example,

```text id="w4t2jp"
α = 0.05
```

means that the critical region occupies **5%** of the total probability.

---

# Critical Region in a Two-Tailed Test

In a two-tailed test,

the critical region is divided equally between the two tails.

For

```text id="x7f3nd"
α = 0.05
```

the rejection regions are

```text id="d5q8lv"
Z < −1.96

or

Z > +1.96
```

Any test statistic outside the interval

```text id="j3v6pk"
−1.96

to

+1.96
```

belongs to the critical region.

---

# Critical Region in a Right-Tailed Test

For a right-tailed test,

the rejection region is located entirely in the right tail.

When

```text id="s9m4zy"
α = 0.05
```

the rejection region is

```text id="h8n2cf"
Z > +1.645
```

Only sufficiently large positive values provide evidence against the null hypothesis.

---

# Critical Region in a Left-Tailed Test

For a left-tailed test,

the rejection region is located entirely in the left tail.

When

```text id="g2w7rb"
α = 0.05
```

the rejection region is

```text id="p6x3jq"
Z < −1.645
```

Only sufficiently small values support the alternative hypothesis.

---

# Non-Rejection Region

The **non-rejection region** (sometimes called the acceptance region) consists of all values of the test statistic that do **not** lead to rejection of the null hypothesis.

If the calculated test statistic falls inside this region,

the available sample evidence is not strong enough to reject the null hypothesis.

---

# Definition

> **The non-rejection region is the set of values of the test statistic for which the null hypothesis is not rejected.**

Notice that we say

```text id="b7k5nt"
Fail to Reject H₀
```

rather than

```text id="a4q9mz"
Accept H₀
```

because failing to reject the null hypothesis does not prove that it is true.

It simply means that the sample does not provide sufficient evidence against it.

---

# Relationship Between the Two Regions

Every probability distribution used in hypothesis testing is divided into two parts.

```text id="f9v3kx"
Probability Distribution

↓

Non-Rejection Region

+

Critical Region
```

The boundary separating these two regions is the **critical value**.

This relationship can be summarized as

```text id="n6w2qc"
Critical Value

↓

Decision Boundary

↓

Separates

↓

Non-Rejection Region

and

Critical Region
```

---

# Decision Using the Critical Region

Once the test statistic has been calculated,

compare it with the critical value.

### If the test statistic falls inside the critical region

```text id="c8j4ty"
Reject H₀
```

because the observed sample result is unlikely if the null hypothesis is true.

---

### If the test statistic falls inside the non-rejection region

```text id="m5r7zp"
Fail to Reject H₀
```

because the sample does not provide sufficient evidence against the null hypothesis.

---

# Concept Note

The critical value does **not** measure the probability that the null hypothesis is true.

Instead,

it defines the boundary used to determine whether the observed sample evidence is statistically significant.

Everything beyond that boundary belongs to the critical region,

while everything inside the boundary belongs to the non-rejection region.

These ideas provide the foundation for the **decision-making process** in hypothesis testing.
# p-value

In the previous section, we learned that a hypothesis test can be completed by comparing the test statistic with a critical value.

Although this approach is widely used, modern statistical software usually reports another quantity called the **p-value**.

Today, the **p-value approach** is the most common method of hypothesis testing because it provides a direct measure of the strength of the sample evidence against the null hypothesis.

---

# What Is a p-value?

The **p-value** is the probability of obtaining a test statistic **at least as extreme as the one observed**, assuming that the null hypothesis is true.

In other words, the p-value measures how unusual the observed sample result would be if the null hypothesis were actually correct.

---

# Definition

> **The p-value is the probability of observing a test statistic as extreme as, or more extreme than, the calculated value under the assumption that the null hypothesis is true.**

The p-value is always computed **under the assumption that the null hypothesis is true**.

This assumption is essential because hypothesis testing begins by treating the null hypothesis as the default explanation.

---

# Understanding the p-value

Suppose a hypothesis test produces

```text id="u7k2df"
p-value = 0.03
```

This means

> **If the null hypothesis is true, there is a 3% probability of obtaining a sample result at least as extreme as the one observed.**

A very small probability indicates that the observed result is unlikely under the null hypothesis.

Consequently, the null hypothesis becomes difficult to believe.

---

# Interpreting the Size of the p-value

The p-value indicates the strength of the evidence against the null hypothesis.

### Small p-value

A small p-value means

* the observed sample result is unusual,
* the evidence against the null hypothesis is strong,
* rejection of the null hypothesis is justified.

---

### Large p-value

A large p-value means

* the observed sample result is not unusual,
* the evidence against the null hypothesis is weak,
* the null hypothesis should not be rejected.

---

# Relationship Between the p-value and the Significance Level

The significance level

```text id="v5r9tm"
α
```

is chosen **before** collecting the data.

The p-value is calculated **after** analyzing the sample.

The statistical decision is made by comparing these two quantities.

---

## Case 1

If

```text id="k8w4qy"
p-value ≤ α
```

then

```text id="j6f2pn"
Reject H₀
```

because the observed sample evidence is sufficiently strong.

---

## Case 2

If

```text id="n3x7bh"
p-value > α
```

then

```text id="e9q5rv"
Fail to Reject H₀
```

because the evidence is not strong enough.

---

# Decision Rule Using the p-value

The p-value decision process can be summarized as

```text id="c2m8zk"
Calculate p-value

↓

Compare with α

↓

p-value ≤ α ?

↓

YES

↓

Reject H₀


NO

↓

Fail to Reject H₀
```

This simple rule is used by almost every statistical software package.

---

# Why Is the p-value Popular?

The p-value has several advantages.

It

* provides a numerical measure of statistical evidence,
* avoids looking up critical value tables,
* works for many different statistical tests,
* is reported automatically by statistical software.

For these reasons, the p-value approach has become the standard method used in modern statistical analysis.

---

# Decision Rule Using the Critical Value

The **critical value approach** was introduced in the previous section.

Its decision process is

```text id="r4k1fs"
Calculate Test Statistic

↓

Find Critical Value

↓

Compare the Two

↓

Test Statistic Inside Critical Region?

↓

YES

↓

Reject H₀


NO

↓

Fail to Reject H₀
```

The decision depends on whether the calculated test statistic falls inside the rejection region.

---

# Decision Rule Using the p-value

The **p-value approach** follows a slightly different procedure.

Instead of comparing the test statistic with a critical value,

it compares the p-value directly with the significance level.

```text id="m8v3qt"
Calculate Test Statistic

↓

Calculate p-value

↓

Compare with α

↓

p-value ≤ α ?

↓

YES

↓

Reject H₀


NO

↓

Fail to Reject H₀
```

Although the procedures differ,

both methods always produce the same statistical decision.

---

# Comparing the Two Approaches

| Critical Value Approach                           | p-value Approach                                                  |
| ------------------------------------------------- | ----------------------------------------------------------------- |
| Compare the test statistic with a critical value. | Compare the p-value with the significance level.                  |
| Uses probability distribution tables.             | Uses the probability associated with the observed test statistic. |
| Common in introductory statistics.                | Common in statistical software and modern research.               |
| Decision based on rejection region.               | Decision based on the p-value.                                    |

---

# Important Concept

The critical value approach and the p-value approach are **two different ways of answering the same question**.

They do **not** represent different statistical tests.

Instead,

they simply provide two equivalent methods for deciding whether the sample evidence is sufficient to reject the null hypothesis.

---

# Common Misconceptions About the p-value

The p-value is one of the most misunderstood concepts in statistics.

The following statements are incorrect.

---

## Misconception 1

> "The p-value is the probability that the null hypothesis is true."

This statement is incorrect.

The p-value is calculated **assuming that the null hypothesis is true**.

It does **not** measure the probability that the null hypothesis itself is true.

---

## Misconception 2

> "A large p-value proves that the null hypothesis is true."

This is also incorrect.

A large p-value simply indicates that the sample does not provide sufficient evidence against the null hypothesis.

It does not prove the null hypothesis.

---

## Misconception 3

> "A small p-value measures the size or importance of an effect."

Incorrect.

The p-value measures **statistical evidence**, not **practical importance**.

A statistically significant result may have little practical significance, especially with very large sample sizes.

---

# Relationship Among the Main Concepts

The decision-making process developed throughout this chapter can now be summarized as

```text id="z5n7pr"
State H₀ and H₁

↓

Choose α

↓

Collect Sample

↓

Calculate Test Statistic

↓

Find Critical Value
        or
Calculate p-value

↓

Make Statistical Decision

↓

Reject H₀

or

Fail to Reject H₀
```

This sequence forms the core procedure of hypothesis testing and is the foundation for all hypothesis tests discussed in statistics.
# Errors in Hypothesis Testing

Hypothesis testing is a statistical decision-making procedure based on sample data rather than complete population information.

Because the decision is made using only a sample, there is always a possibility of reaching an incorrect conclusion.

Even when the hypothesis testing procedure is applied correctly, uncertainty due to random sampling can lead to errors.

There are two possible types of decision errors:

* **Type I Error**
* **Type II Error**

Understanding these errors is essential because every hypothesis test involves a balance between them.

---

# The Four Possible Outcomes

At the end of every hypothesis test, one of two decisions is made:

```text id="y6m8pa"
Reject H₀

or

Fail to Reject H₀
```

At the same time, the null hypothesis itself is either

```text id="v2r5kq"
True

or

False
```

Combining these possibilities produces four possible outcomes.

| Actual Situation | Statistical Decision | Result           |
| ---------------- | -------------------- | ---------------- |
| H₀ is true       | Fail to Reject H₀    | Correct Decision |
| H₀ is true       | Reject H₀            | Type I Error     |
| H₀ is false      | Reject H₀            | Correct Decision |
| H₀ is false      | Fail to Reject H₀    | Type II Error    |

Thus, two outcomes are correct decisions, while the remaining two are statistical errors.

---

# Type I Error

A **Type I Error** occurs when the null hypothesis is rejected even though it is actually true.

In other words,

we conclude that an effect or difference exists when, in reality, it does not.

---

# Definition

> **A Type I Error is the error of rejecting a true null hypothesis.**

The probability of making a Type I Error is denoted by

```text id="h9v2zt"
α
```

which is exactly the **level of significance** selected before conducting the hypothesis test.

Therefore,

```text id="k7f5mw"
P(Type I Error)

=

α
```

---

# Example

A pharmaceutical company tests a new medicine.

The null hypothesis states that

```text id="g4n8rs"
The new medicine is no more effective than the current medicine.
```

Suppose the researchers reject the null hypothesis and conclude that the medicine is better.

Later, further research shows that the medicine is **not actually better**.

The researchers have committed a

```text id="x6m3pc"
Type I Error
```

because they rejected a true null hypothesis.

---

# Type II Error

A **Type II Error** occurs when the null hypothesis is not rejected even though it is actually false.

In other words,

we fail to detect a real effect that truly exists.

---

# Definition

> **A Type II Error is the error of failing to reject a false null hypothesis.**

The probability of making a Type II Error is denoted by

```text id="b5q9yd"
β
```

Therefore,

```text id="r8p3lu"
P(Type II Error)

=

β
```

---

# Example

Suppose a new fertilizer genuinely increases crop production.

However,

after analyzing a sample,

the researcher concludes that the fertilizer has **no effect**.

The researcher has failed to detect a real improvement.

This is a

```text id="q3w6fa"
Type II Error
```

---

# Comparing the Two Errors

Although both errors represent incorrect decisions, they occur under different circumstances.

| Type I Error     | Type II Error             |
| ---------------- | ------------------------- |
| Reject a true H₀ | Fail to reject a false H₀ |
| False positive   | False negative            |
| Probability = α  | Probability = β           |

Neither error is desirable.

The objective of hypothesis testing is to minimize both, although reducing one often increases the other.

---

# Statistical Power

Since a Type II Error occurs when we fail to detect a real effect,

it is useful to measure the probability of correctly detecting that effect.

This probability is called the **statistical power** of a hypothesis test.

---

# Definition

> **Statistical power is the probability of correctly rejecting a false null hypothesis.**

It is calculated as

```text id="m2k7sv"
Power

=

1 − β
```

where

```text id="9q4xje"
β
```

is the probability of a Type II Error.

A hypothesis test with high statistical power is more likely to detect genuine differences or effects.

---

# Factors Affecting Statistical Power

Several factors influence the power of a hypothesis test.

These include

* sample size,
* significance level,
* population variability,
* and the magnitude of the true effect.

Generally,

```text id="v4n8cw"
Larger Sample Size

↓

Higher Statistical Power
```

because larger samples provide more information about the population.

---

# Relationship Between Confidence Intervals and Hypothesis Testing

Although confidence intervals and hypothesis testing are introduced as separate topics,

they are closely related.

Both methods are based on

* sampling distributions,
* standard errors,
* probability distributions,
* and significance levels.

In fact,

they often lead to exactly the same statistical conclusion.

---

# Relationship for a Two-Tailed Test

Consider a two-tailed hypothesis test at the

```text id="f8w2km"
5%

Significance Level
```

This corresponds to a

```text id="g3r6xp"
95%

Confidence Interval
```

If the hypothesized population parameter lies **inside** the confidence interval,

```text id="z7p5nr"
Fail to Reject H₀
```

If the hypothesized value lies **outside** the confidence interval,

```text id="u6m9by"
Reject H₀
```

Thus,

confidence intervals and hypothesis tests provide two different perspectives on the same statistical evidence.

---

# Applications of Hypothesis Testing

Hypothesis testing is used in almost every field that relies on data.

Examples include

* Medical research
* Clinical trials
* Engineering
* Manufacturing
* Agriculture
* Economics
* Finance
* Marketing
* Psychology
* Education
* Scientific research
* Data Science
* Artificial Intelligence
* Machine Learning
* Quality control

Whenever researchers need to evaluate claims or compare competing ideas using data, hypothesis testing provides an objective statistical framework for decision making.

---

# Summary

* Hypothesis testing uses sample data to evaluate claims about population parameters.
* Every hypothesis test begins with two competing hypotheses: the null hypothesis and the alternative hypothesis.
* Depending on the research question, hypothesis tests may be two-tailed, right-tailed, or left-tailed.
* Test statistics summarize the sample evidence and are compared using either the critical value approach or the p-value approach.
* The significance level determines the probability of committing a Type I Error.
* A p-value measures the strength of the evidence against the null hypothesis.
* Every hypothesis test may lead to a correct decision, a Type I Error, or a Type II Error.
* Statistical power measures the probability of correctly rejecting a false null hypothesis.
* Confidence intervals and hypothesis tests are closely connected and often produce the same statistical conclusion.
* Hypothesis testing forms one of the most important foundations of modern statistical inference and scientific research.

