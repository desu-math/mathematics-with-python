# Worked Example: Uniform Distribution

## Problem

The waiting time for a bus at a station is uniformly distributed between **0 and 20 minutes**.

Find the probability that a passenger waits between **5 and 12 minutes**.

---

# Step 1: Identify the Given Information

Lower bound:

```text
a = 0
```

Upper bound:

```text
b = 20
```

Desired interval:

```text
c = 5

d = 12
```

Therefore,

```text
X ~ U(0, 20)
```

---

# Step 2: Write the Uniform Probability Formula

The probability of an interval for a continuous Uniform distribution is

```text
               d − c
P(c ≤ X ≤ d) = -------
               b − a
```

where

* **a** = lower bound,
* **b** = upper bound,
* **c** = beginning of the desired interval,
* **d** = end of the desired interval.

---

# Step 3: Substitute the Values

Substitute

```text
a = 0

b = 20

c = 5

d = 12
```

into the formula.

```text
                12 − 5
P(5 ≤ X ≤ 12) = -------
                20 − 0
```

---

# Step 4: Simplify the Expression

Calculate the numerator.

```text
12 − 5 = 7
```

Calculate the denominator.

```text
20 − 0 = 20
```

Now substitute these values.

```text
                  7
P(5 ≤ X ≤ 12) = ----
                 20
```

---

# Step 5: Calculate the Final Probability

Divide the numerator by the denominator.

```text
7 ÷ 20 = 0.35
```

Therefore,

```text
P(5 ≤ X ≤ 12) = 0.35
```

or

```text
35%
```

---

# Final Answer

```text
P(5 ≤ X ≤ 12) = 0.35
```

Therefore, the probability that a passenger waits between **5 and 12 minutes** is

```text
0.35

or

35%
```

---

# Interpretation

The waiting time can be **any value between 0 and 20 minutes**.

Since every waiting time within this interval is equally likely, the probability depends only on the **length of the desired interval**.

The desired interval has length

```text
12 − 5 = 7 minutes
```

while the entire interval has length

```text
20 − 0 = 20 minutes
```

Therefore,

```text
Probability

=

Desired Interval Length
────────────────────────
 Total Interval Length

=

7
──
20

=

0.35
```

This means that if we observe many passengers, approximately **35%** of them are expected to wait between **5 and 12 minutes**.

---

# Key Takeaways

* A Uniform distribution assigns equal probability density to every value within the interval.
* Probabilities are calculated over **intervals**, not individual values.
* The probability is obtained by dividing the length of the desired interval by the length of the entire interval.
* Longer intervals have larger probabilities.
* The probability of any single exact value is zero.
