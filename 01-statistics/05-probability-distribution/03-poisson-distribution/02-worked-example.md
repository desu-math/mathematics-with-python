# Worked Example: Poisson Distribution

## Problem

A customer service center receives an average of **4 phone calls per minute**.

Assuming that the number of phone calls follows a Poisson distribution, what is the probability that **exactly 3 phone calls** are received during one minute?

---

# Step 1: Identify the Given Information

Average number of events:

```text
λ = 4
```

Number of events of interest:

```text
x = 3
```

---

# Step 2: Write the Poisson Probability Formula

The Probability Mass Function (PMF) of the Poisson distribution is

```text
          e^(−λ) λ^x
P(X = x) = ----------
              x!
```

---

# Step 3: Substitute the Values

Substitute

```text
λ = 4

x = 3
```

into the formula.

```text
          e^(−4) · 4^3
P(X = 3) = -------------
                3!
```

---

# Step 4: Simplify the Expression

Calculate each part separately.

First,

```text
4^3 = 64
```

Next,

```text
3! = 3 × 2 × 1 = 6
```

Also,

```text
e^(−4) ≈ 0.018315
```

Now substitute these values.

```text
          0.018315 × 64
P(X = 3) = ----------------
                 6
```

---

# Step 5: Compute the Final Answer

Multiply the numerator.

```text
0.018315 × 64 = 1.17216
```

Then divide by 6.

```text
P(X = 3)

= 1.17216 / 6

≈ 0.1954
```

---

# Final Answer

```text
P(X = 3) ≈ 0.1954
```

Therefore, the probability of receiving **exactly three phone calls** in one minute is approximately

```text
0.1954

or

19.54%
```

---

# Interpretation

Although the average number of phone calls is **4 per minute**, it is still possible to receive exactly **3 calls** during a particular minute.

The Poisson distribution tells us that this occurs with a probability of approximately **19.54%**.

This does **not** mean that exactly three calls will occur every minute. Instead, it means that if we observe many one-minute intervals, about **19.54%** of those intervals are expected to contain exactly three phone calls.

---

# Key Takeaways

* The Poisson distribution models the probability of a specific number of events occurring within a fixed interval.
* The parameter **λ** represents the average number of events per interval.
* The value **x** represents the exact number of events whose probability is being calculated.
* The probability is obtained by substituting **λ** and **x** into the Poisson PMF and evaluating the formula.
