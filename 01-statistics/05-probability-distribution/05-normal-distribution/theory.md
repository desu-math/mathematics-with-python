# Normal Distribution

## Overview

The **Normal distribution**, also called the **Gaussian distribution**, is the most important continuous probability distribution in statistics.

Many natural, biological, economic, and engineering measurements approximately follow a Normal distribution.

Examples include:

* Human heights
* Body weights
* Blood pressure
* IQ scores
* Measurement errors
* Examination scores
* Manufacturing measurements

Unlike the Uniform distribution, where every value is equally likely, the Normal distribution assigns **higher probability density to values near the center** and **lower probability density to values farther from the center**.

As a result, its graph forms the famous **bell-shaped curve**.

---

# Motivation

Suppose we record the heights of 10,000 adult students.

Will every height occur equally often?

No.

Most students have heights close to the average.

Very short and very tall students are much less common.

Therefore, the data naturally cluster around the center.

The Normal distribution was developed to model this type of behavior.

---

# Historical Background

The Normal distribution was first studied in connection with **measurement errors**.

Scientists observed that repeated measurements of the same quantity were not identical.

Instead,

* small errors occurred frequently,
* large errors occurred rarely,
* positive and negative errors appeared with similar frequency.

Later, mathematicians such as **Abraham de Moivre**, **Pierre-Simon Laplace**, and **Carl Friedrich Gauss** developed the mathematical theory of the Normal distribution.

Because of Gauss's major contributions, it is also known as the **Gaussian distribution**.

---

# Parameters

The Normal distribution has two parameters.

## Mean

```text
μ
```

The mean determines the **center** of the distribution.

Changing the mean moves the entire curve left or right.

---

## Standard Deviation

```text
σ
```

The standard deviation determines the **spread** of the distribution.

* Small σ → narrow and tall curve.
* Large σ → wide and flatter curve.

---

# Probability Density Function (PDF)

The Normal probability density function is

```text
                 1
f(x) = ------------------------- × e^(-(x−μ)²/(2σ²))
        σ √(2π)
```

where

* **μ** = mean,
* **σ** = standard deviation,
* **π** ≈ 3.14159,
* **e** ≈ 2.71828.

---

# Properties of the Normal Distribution

A Normal distribution has several important properties.

* Bell-shaped.
* Symmetric about the mean.
* Mean = Median = Mode.
* Total area under the curve equals 1.
* The curve extends infinitely in both directions.
* The tails approach, but never touch, the x-axis.

---

# The Empirical Rule (68–95–99.7 Rule)

One of the most important properties of the Normal distribution is the Empirical Rule.

Approximately

* **68%** of observations lie within **1 standard deviation** of the mean.
* **95%** lie within **2 standard deviations**.
* **99.7%** lie within **3 standard deviations**.

This rule is widely used to interpret normally distributed data.

---

# Shape of the Distribution

The shape depends on the parameters.

Changing **μ** shifts the curve horizontally.

Changing **σ** changes the spread while keeping the total area equal to 1.

---

# Real-World Applications

The Normal distribution is widely used in

* Statistics
* Data Science
* Machine Learning
* Artificial Intelligence
* Finance
* Engineering
* Physics
* Biology
* Medicine
* Quality Control

---

# Advantages

The Normal distribution

* models many natural phenomena,
* provides the foundation for statistical inference,
* simplifies probability calculations,
* is fundamental in data science and machine learning.

---

# Summary

* The Normal distribution is the most important continuous probability distribution.
* It models data that cluster around an average.
* It is completely determined by two parameters: **μ** and **σ**.
* Its graph is a symmetric bell-shaped curve.
* The total area under the curve equals 1.
* Approximately **68%**, **95%**, and **99.7%** of observations lie within one, two, and three standard deviations of the mean, respectively.
