# Algorithm: Bernoulli Distribution

## Overview

The Bernoulli distribution models a random experiment with **exactly two possible outcomes**:

* Success (1)
* Failure (0)

The objective of the algorithm is to simulate Bernoulli experiments, estimate the probabilities of the outcomes, and compare the simulation with the theoretical Bernoulli distribution.

---

# General Algorithm

## Step 1: Define the Probability of Success

Choose the probability of success.

Let

```text
p = Probability of Success
```

Since there are only two possible outcomes, the probability of failure is

```text
1 − p
```

Example:

```text
p = 0.70

Probability of Success = 0.70

Probability of Failure = 0.30
```

---

## Step 2: Define the Number of Experiments

Decide how many Bernoulli trials will be performed.

Example:

```text
Number of trials = 1000
```

A larger number of trials generally produces results closer to the theoretical probabilities.

---

## Step 3: Generate Bernoulli Outcomes

Perform the experiment repeatedly.

For each trial:

* Generate one random outcome.
* If success occurs, record **1**.
* Otherwise, record **0**.

Example:

```text
1 0 1 1 0 0 1 1 1 0 ...
```

---

## Step 4: Count the Outcomes

Count

* Number of successes
* Number of failures

Example:

```text
Successes = 702

Failures = 298
```

---

## Step 5: Estimate Experimental Probabilities

Compute

```text
Estimated Success Probability

=

Number of Successes
────────────────────
Total Number of Trials
```

Similarly,

```text
Estimated Failure Probability

=

Number of Failures
──────────────────
Total Number of Trials
```

---

## Step 6: Compare with Theory

The theoretical probabilities are

```text
P(Success) = p

P(Failure) = 1 − p
```

Compare them with the estimated probabilities obtained from the simulation.

As the number of trials increases, the experimental probabilities should approach the theoretical values.

---

## Step 7: Visualize the Distribution

Create a bar chart containing two bars.

```text
Outcome

0 → Failure

1 → Success
```

The height of each bar represents its probability.

Save the figure for documentation and display it on the screen.

---

# Pseudocode

```text
START

Input p

Input number_of_trials

Generate Bernoulli outcomes

Count successes

Count failures

Estimate success probability

Estimate failure probability

Display numerical results

Create bar chart

Save figure

Display figure

END
```

---

# Time Complexity

Suppose

```text
n = number of Bernoulli trials
```

Generating observations:

```text
O(n)
```

Counting outcomes:

```text
O(n)
```

Computing probabilities:

```text
O(1)
```

Creating the bar chart:

```text
O(1)
```

Therefore, the overall computational complexity is

```text
O(n)
```

---

# Summary

The Bernoulli distribution algorithm follows these steps:

1. Define the probability of success.
2. Specify the number of trials.
3. Generate Bernoulli outcomes.
4. Count successes and failures.
5. Estimate probabilities.
6. Compare experimental and theoretical probabilities.
7. Visualize the distribution using a bar chart.

This workflow forms the foundation for the Binomial distribution, where multiple independent Bernoulli trials are combined into a single probability model.
