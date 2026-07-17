# Algorithm: Covariance and Pearson Correlation

## Introduction

Covariance and correlation are calculated by analyzing how two variables change together.

The algorithm receives two datasets:

```text id="m3zv0a"
X = First Variable

Y = Second Variable
```

and calculates:

* Sample covariance
* Pearson correlation coefficient

The correlation calculation is based on covariance and standard deviations.

---

# Input

Two numerical datasets with equal length:

```text id="k8m2px"
X = [x1, x2, x3, ..., xn]

Y = [y1, y2, y3, ..., yn]
```

where:

```text id="x4k9vq"
n = Number of observations
```

---

# Output

The algorithm returns:

```text id="p6q8fz"
Sample Covariance

Pearson Correlation Coefficient
```

and an interpretation of the relationship.

---

# Algorithm Steps

## Step 1: Validate the Input Data

Check that:

* Both datasets contain the same number of observations.
* The number of observations is greater than one.

If the lengths are different, the calculation cannot be performed.

Example:

```text id="j4x9rm"
Length(X) ≠ Length(Y)

↓

Invalid Input
```

---

# Step 2: Calculate the Means

Calculate the mean of each variable.

For X:

```text id="5f7p0w"
X̄ = ΣX / n
```

For Y:

```text id="8v2l6a"
Ȳ = ΣY / n
```

---

# Step 3: Calculate Deviations from the Means

For every observation, calculate:

```text id="9m4k2s"
Deviation of X:

Xi - X̄
```

and

```text id="2s8q4b"
Deviation of Y:

Yi - Ȳ
```

These values show how far each observation is from its average.

---

# Step 4: Calculate Products of Deviations

For each pair of observations:

```text id="w5r8c3"
(Xi - X̄)(Yi - Ȳ)
```

These products determine whether the variables move together or in opposite directions.

---

# Step 5: Calculate Sample Covariance

Sum all products:

```text id="q3v7nm"
Σ(Xi - X̄)(Yi - Ȳ)
```

Then divide by:

```text id="h9s2kd"
n - 1
```

The covariance is:

```text id="c6x1fz"
sXY = Σ(Xi - X̄)(Yi - Ȳ) / (n - 1)
```

---

# Step 6: Calculate Standard Deviations

Calculate the standard deviation of X:

```text id="m1z8qa"
sX = √(Σ(Xi - X̄)² / (n - 1))
```

Calculate the standard deviation of Y:

```text id="v7q2lm"
sY = √(Σ(Yi - Ȳ)² / (n - 1))
```

---

# Step 7: Calculate Pearson Correlation Coefficient

Use the formula:

```text id="n8p4rw"
r = sXY / (sX × sY)
```

The result always satisfies:

```text id="b4t9sx"
-1 ≤ r ≤ +1
```

---

# Step 8: Interpret the Result

The sign determines the direction.

Positive correlation:

```text id="x7m2kp"
r > 0

Variables move in the same direction.
```

Negative correlation:

```text id="z5r8bn"
r < 0

Variables move in opposite directions.
```

No linear correlation:

```text id="k2v9ds"
r ≈ 0

No significant linear relationship.
```

---

# Complete Algorithm

```text id="a7c5mx"
Algorithm: Covariance and Correlation

Input:
    Two numerical datasets X and Y

Begin:

    1. Check that X and Y have equal length.

    2. Calculate:
           X̄ = Mean(X)
           Ȳ = Mean(Y)

    3. For each observation:
           Calculate Xi - X̄
           Calculate Yi - Ȳ

    4. Calculate:
           Sum of (Xi - X̄)(Yi - Ȳ)

    5. Compute covariance:

           sXY = Σ(Xi - X̄)(Yi - Ȳ) / (n - 1)

    6. Compute standard deviations:

           sX = Standard deviation of X
           sY = Standard deviation of Y

    7. Compute correlation:

           r = sXY / (sX × sY)

    8. Interpret r.

End
```

---

# Computational Complexity

Assume the dataset contains `n` observations.

The algorithm performs several passes through the data:

* calculating means,
* calculating deviations,
* calculating covariance,
* calculating standard deviations.

The total time complexity is:

```text id="t8p2qm"
O(n)
```

The algorithm requires storing the input data.

Therefore, the space complexity is:

```text id="w6r3vz"
O(n)
```

---

# Numerical Considerations

When implementing correlation calculations, consider:

* Avoid division by zero when standard deviation is zero.
* Handle missing values carefully.
* Check for extreme outliers.
* Use appropriate numerical precision for large datasets.

---

# Summary

The covariance and correlation algorithm follows these steps:

```text id="r5m8qy"
Input Data

↓

Calculate Means

↓

Calculate Deviations

↓

Calculate Covariance

↓

Calculate Standard Deviations

↓

Calculate Correlation

↓

Interpret Result
```

This algorithm provides the mathematical foundation for implementing covariance and correlation calculations in Python.
