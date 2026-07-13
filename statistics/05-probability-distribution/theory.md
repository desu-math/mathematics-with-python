# Probability Distributions

## Overview

In probability basics, we studied individual events and calculated their probabilities.

However, in many real-world problems, we are not interested in only one event. Instead, we want to understand the behavior of a variable that can take different possible values.

For example:

* The number of customers arriving at a shop in one hour.
* The height of students in a university.
* The number of defective products in a factory.
* The daily rainfall amount.

These quantities are uncertain and can have different possible values.

A **probability distribution** describes how probabilities are assigned to these possible values.

---

# Random Variables

A **random variable** is a variable whose value is determined by the outcome of a random experiment.

Unlike ordinary variables, a random variable does not have a fixed value before the experiment occurs.

It assigns a numerical value to each possible outcome.

---

## Example: Coin Toss

Suppose we toss a coin.

The possible outcomes are:

```text
Head
Tail
```

We can define a random variable X as:

```text
X = 1  if the result is Head

X = 0  if the result is Tail
```

Now the random experiment produces numerical values:

```text
X = {0, 1}
```

This numerical representation allows us to apply mathematical analysis.

---

# Types of Random Variables

Random variables are divided into two main categories:

1. Discrete Random Variables
2. Continuous Random Variables

---

# Discrete Random Variables

A discrete random variable can take a **countable number of possible values**.

The possible values are usually separated and distinct.

Examples:

### Number of students in a classroom

Possible values:

```text
40, 41, 42, 43, ...
```

### Number of defective products

Possible values:

```text
0, 1, 2, 3, ...
```

### Number of heads in 10 coin tosses

Possible values:

```text
0, 1, 2, ..., 10
```

Discrete variables are usually produced by **counting**.

---

# Continuous Random Variables

A continuous random variable can take any value within an interval.

The possible values are infinite.

Examples:

### Height of a person

A person can have:

```text
170 cm

170.5 cm

170.52 cm

170.523 cm
```

and infinitely many more possibilities.

---

### Temperature

Between:

```text
20°C and 21°C
```

there are infinitely many possible values.

Continuous variables are usually produced by **measurement**.

---

# Probability Distribution

A probability distribution describes the relationship between:

* possible values of a random variable,
* and the probabilities associated with those values.

It answers:

> "How likely is each possible value of this random variable?"

---

## Example: Rolling a Fair Die

Let X represent the result of rolling a die.

Possible values:

```text
X = {1,2,3,4,5,6}
```

Since the die is fair:

```text
P(X=1)=1/6

P(X=2)=1/6

P(X=3)=1/6

...

P(X=6)=1/6
```

The complete table is the probability distribution of X.

---

# Probability Mass Function (PMF)

The **Probability Mass Function (PMF)** describes the probability distribution of a discrete random variable.

It gives the probability that a discrete random variable takes a specific value.

It is written as:

```text
P(X = x)
```

where:

* X is the random variable.
* x is a possible value.

---

## Example: Dice Roll

The PMF is:

```text
Value (x)      Probability

1              1/6
2              1/6
3              1/6
4              1/6
5              1/6
6              1/6
```

The sum of all probabilities must equal 1:

```text
1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1
```

---

# Probability Density Function (PDF)

The **Probability Density Function (PDF)** describes the probability distribution of a continuous random variable.

Unlike PMF, PDF does not give the probability at an exact point.

Instead, probability is measured over an interval.

---

## Important Idea

For a continuous variable:

```text
P(X = exact value) = 0
```

because there are infinitely many possible values.

For example:

```text
P(Height = 170.523456 cm)
```

is essentially zero.

Instead, we calculate probabilities over ranges:

Example:

```text
P(170 cm < Height < 180 cm)
```

---

# Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function (CDF)** gives the probability that a random variable is less than or equal to a certain value.

It is written as:

```text
F(x) = P(X ≤ x)
```

It answers:

> "What is the probability that the random variable does not exceed x?"

---

## Example

Suppose:

```text
X = Exam score
```

The CDF value:

```text
F(80)=0.75
```

means:

```text
75% of students scored 80 or below.
```

---

# Relationship Between PMF, PDF, and CDF

These three concepts describe the same idea from different perspectives.

## Discrete Case

```text
PMF
 |
 |
 ↓
Individual probabilities
 |
 |
 ↓
CDF
```

PMF gives individual probabilities.

CDF accumulates them.

---

## Continuous Case

```text
PDF
 |
 |
 ↓
Probability density
 |
 |
 ↓
CDF
```

PDF describes the shape of the distribution.

CDF accumulates probability up to a value.

---

# Expected Value

A probability distribution allows us to calculate the expected value of a random variable.

The expected value represents the long-term average outcome.

For a discrete random variable:

```text
E(X) = Σ xP(x)
```

where:

* x = possible value
* P(x) = probability of that value

---

## Example

For a fair die:

```text
E(X)

= 1(1/6)+2(1/6)+3(1/6)
+4(1/6)+5(1/6)+6(1/6)

= 3.5
```

Although 3.5 cannot appear in one roll, it represents the average result over many rolls.

---

# Importance in Data Science

Probability distributions are fundamental in:

* statistical modeling,
* machine learning,
* hypothesis testing,
* data simulation,
* uncertainty estimation.

Machine learning models often assume that data follows certain distributions.

Examples:

* Normal distribution for measurement errors.
* Bernoulli distribution for binary classification.
* Poisson distribution for counting events.

---

# Summary

* A random variable assigns numerical values to random outcomes.
* Random variables can be discrete or continuous.
* A probability distribution describes how probabilities are assigned to values.
* PMF is used for discrete random variables.
* PDF is used for continuous random variables.
* CDF gives cumulative probability.
* Probability distributions are the foundation of statistical analysis and machine learning.
