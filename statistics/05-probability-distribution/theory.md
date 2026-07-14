# Probability Distributions

A **probability distribution** describes how probabilities are assigned to the possible values of a random variable.

It answers the question:

> **"How likely is each possible value of a random variable?"**

Instead of studying a single outcome, a probability distribution describes the behavior of **all possible outcomes** of a random experiment.

---

## Example: Rolling a Fair Die

Let **X** represent the result of rolling a fair six-sided die.

The possible values are:

```text
X = {1, 2, 3, 4, 5, 6}
```

Since the die is fair, each outcome has the same probability.

```text
P(X = 1) = 1/6

P(X = 2) = 1/6

P(X = 3) = 1/6

P(X = 4) = 1/6

P(X = 5) = 1/6

P(X = 6) = 1/6
```

Together, these probabilities form the **probability distribution** of the random variable **X**.

---
**Random Variables**

A random variable is a variable whose value is determined by the outcome of a random experiment.

Unlike ordinary variables, a random variable does not have a fixed value before the experiment occurs.

It assigns a numerical value to each possible outcome.

Example: Coin Toss

Suppose we toss a coin.

The possible outcomes are:

Head
Tail

We can define a random variable X as:

X = 1  if the result is Head

X = 0  if the result is Tail

Now the random experiment produces numerical values:

X = {0, 1}

This numerical representation allows us to apply mathematical analysis.

Types of Random Variables

Random variables are divided into two main categories:

**Discrete Random Variables
Continuous Random Variables**

**Discrete Random Variables**

A discrete random variable can take a countable number of possible values.

The possible values are usually separated and distinct.

Examples:

Number of students in a classroom

Possible values:

40, 41, 42, 43, ...
Number of defective products

Possible values:

0, 1, 2, 3, ...
Number of heads in 10 coin tosses

Possible values:

0, 1, 2, ..., 10

Discrete variables are usually produced by counting.

**Continuous Random Variables**

A continuous random variable can take any value within an interval.

The possible values are infinite.

Examples:

Height of a person

A person can have:

170 cm

170.5 cm

170.52 cm

170.523 cm

and infinitely many more possibilities.

Temperature

Between:

20°C and 21°C

there are infinitely many possible values.

Continuous variables are usually produced by measurement.


# Types of Probability Distributions

Probability distributions are generally classified into **two major categories**.

```text
Probability Distributions
│
├── Discrete Probability Distributions
│
└── Continuous Probability Distributions
```

The classification depends on the type of random variable being studied.

---

## Discrete Probability Distributions

A **discrete probability distribution** describes the behavior of a **discrete random variable**.

A discrete random variable can take only **countable values**. Therefore, the probability of each individual value can be calculated directly.

Examples of discrete random variables include:

* Number of heads in 10 coin tosses
* Number of customers entering a shop
* Number of defective products in a factory
* Number of goals scored in a football match

Common discrete probability distributions include:

* Bernoulli Distribution
* Binomial Distribution
* Geometric Distribution
* Poisson Distribution

Discrete probability distributions are described using the **Probability Mass Function (PMF)**.

---

## Continuous Probability Distributions

A **continuous probability distribution** describes the behavior of a **continuous random variable**.

A continuous random variable can take infinitely many values within an interval. Consequently, the probability of an exact value is zero, and probabilities are calculated over intervals.

Examples of continuous random variables include:

* Height
* Weight
* Temperature
* Time
* Rainfall
* Blood pressure

Common continuous probability distributions include:

* Uniform Distribution
* Normal Distribution
* Exponential Distribution

Continuous probability distributions are described using the **Probability Density Function (PDF)**.

---

## Comparison of Discrete and Continuous Distributions

| Discrete Distribution                         | Continuous Distribution                |
| --------------------------------------------- | -------------------------------------- |
| Describes discrete random variables           | Describes continuous random variables  |
| Countable possible values                     | Infinitely many possible values        |
| Uses PMF                                      | Uses PDF                               |
| Probability can be assigned to an exact value | Probability is assigned over intervals |
| Usually represents counting                   | Usually represents measurement         |

---

## Why Are There Many Probability Distributions?

Different real-world phenomena exhibit different patterns of randomness.

For example:

* A coin toss has only two possible outcomes.
* The number of customers arriving at a store can be any non-negative integer.
* Human height varies continuously around an average.
* Waiting time until the next bus follows a different pattern from both coin tosses and human heights.

Because these situations behave differently, a single mathematical model cannot accurately describe them all.

Therefore, probability theory provides several probability distributions, each designed for a particular type of random phenomenon.

---

## Choosing an Appropriate Probability Distribution

Selecting the appropriate probability distribution is one of the most important tasks in statistics and data science.

The following table provides a general guideline.

| Real-World Problem                                 | Suitable Distribution    |
| -------------------------------------------------- | ------------------------ |
| One success or failure                             | Bernoulli Distribution   |
| Number of successes in repeated independent trials | Binomial Distribution    |
| Number of events occurring within a fixed interval | Poisson Distribution     |
| Values equally likely within an interval           | Uniform Distribution     |
| Natural measurements clustered around an average   | Normal Distribution      |
| Waiting time until an event occurs                 | Exponential Distribution |

The remaining sections of this chapter study each of these distributions in detail, including their mathematical foundations, algorithms, Python implementations, and visualizations.


Probability Distribution

A probability distribution describes the relationship between:

possible values of a random variable,
and the probabilities associated with those values.

It answers:

"How likely is each possible value of this random variable?"

Example: Rolling a Fair Die

Let X represent the result of rolling a die.

Possible values:

X = {1,2,3,4,5,6}

Since the die is fair:

P(X=1)=1/6

P(X=2)=1/6

P(X=3)=1/6

...

P(X=6)=1/6

The complete table is the probability distribution of X.

Probability Mass Function (PMF)

The Probability Mass Function (PMF) describes the probability distribution of a discrete random variable.

It gives the probability that a discrete random variable takes a specific value.

It is written as:

P(X = x)

where:

X is the random variable.
x is a possible value.
Example: Dice Roll

The PMF is:

Value (x)      Probability

1              1/6
2              1/6
3              1/6
4              1/6
5              1/6
6              1/6

The sum of all probabilities must equal 1:

1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1
Probability Density Function (PDF)

The Probability Density Function (PDF) describes the probability distribution of a continuous random variable.

Unlike PMF, PDF does not give the probability at an exact point.

Instead, probability is measured over an interval.

Important Idea

For a continuous variable:

P(X = exact value) = 0

because there are infinitely many possible values.

For example:

P(Height = 170.523456 cm)

is essentially zero.

Instead, we calculate probabilities over ranges:

Example:

P(170 cm < Height < 180 cm)
Cumulative Distribution Function (CDF)

The Cumulative Distribution Function (CDF) gives the probability that a random variable is less than or equal to a certain value.

It is written as:

F(x) = P(X ≤ x)

It answers:

"What is the probability that the random variable does not exceed x?"

Example

Suppose:

X = Exam score

The CDF value:

F(80)=0.75

means:

75% of students scored 80 or below.
Relationship Between PMF, PDF, and CDF

These three concepts describe the same idea from different perspectives.

Discrete Case
PMF
 |
 |
 ↓
Individual probabilities
 |
 |
 ↓
CDF

PMF gives individual probabilities.

CDF accumulates them.

Continuous Case
PDF
 |
 |
 ↓
Probability density
 |
 |
 ↓
CDF

PDF describes the shape of the distribution.

CDF accumulates probability up to a value.

Expected Value

A probability distribution allows us to calculate the expected value of a random variable.

The expected value represents the long-term average outcome.

For a discrete random variable:

E(X) = Σ xP(x)

where:

x = possible value
P(x) = probability of that value
Example

For a fair die:

E(X)

= 1(1/6)+2(1/6)+3(1/6)
+4(1/6)+5(1/6)+6(1/6)

= 3.5

Although 3.5 cannot appear in one roll, it represents the average result over many rolls.
