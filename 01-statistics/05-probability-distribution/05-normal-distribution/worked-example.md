# Worked Example: Normal Distribution

## Problem

A manufacturing process produces metal rods whose lengths are normally distributed with

```text
μ = 50 cm

σ = 2 cm
```

Find the value of the **Probability Density Function (PDF)** at

```text
x = 52 cm
```

---

# Step 1: Identify the Given Information

Mean:

```text
μ = 50
```

Standard deviation:

```text
σ = 2
```

Desired value:

```text
x = 52
```

---

# Step 2: Write the Normal Distribution Formula

The Probability Density Function is

```text
                 1
f(x) = ------------------------- × e^(-(x−μ)²/(2σ²))
        σ √(2π)
```

---

# Step 3: Substitute the Values

Substitute

```text
μ = 50

σ = 2

x = 52
```

into the formula.

```text
                 1
f(52) = ---------------------- × e^(-(52−50)²/(2×2²))
          2√(2π)
```

---

# Step 4: Simplify the Expression

Calculate the exponent.

```text
(52 − 50)² = 4
```

```text
2 × 2² = 8
```

Therefore,

```text
−4 / 8 = −0.5
```

The exponential term becomes

```text
e^(−0.5) ≈ 0.60653
```

Now calculate the coefficient.

```text
2√(2π) ≈ 5.0133
```

Therefore,

```text
1 / 5.0133 ≈ 0.19947
```

---

# Step 5: Calculate the Final Answer

Multiply the two values.

```text
0.19947 × 0.60653

≈ 0.12099
```

Therefore,

```text
f(52) ≈ 0.1210
```

---

# Final Answer

```text
f(52) ≈ 0.1210
```

---

# Interpretation

The value

```text
f(52) = 0.1210
```

is the **probability density** at **52 cm**.

It is **not** the probability that a rod has exactly length 52 cm.

For a continuous distribution,

```text
P(X = 52) = 0
```

Instead, the PDF tells us how densely the observations are concentrated around that value.

Actual probabilities are computed over **intervals**, such as

```text
P(51 ≤ X ≤ 53)
```

These interval probabilities will be calculated after studying the **Standard Normal Distribution (Z-distribution)**.

---

# Key Takeaways

* The Normal distribution is described by its Probability Density Function (PDF).
* The PDF gives probability density, not probability.
* The probability of a single exact value is zero.
* Interval probabilities require the CDF or Z-table.
* The Standard Normal Distribution will be introduced next to simplify probability calculations.
