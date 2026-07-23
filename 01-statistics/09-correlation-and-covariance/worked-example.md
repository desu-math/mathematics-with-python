# Worked Example: Calculating Covariance and Pearson Correlation

## Problem

A researcher wants to investigate whether the number of hours students study is related to their examination scores.

The following data were collected from five students.

| Student | Study Hours (X) | Exam Score (Y) |
| ------- | --------------- | -------------- |
| A       | 2               | 50             |
| B       | 3               | 55             |
| C       | 5               | 65             |
| D       | 6               | 70             |
| E       | 8               | 85             |

Calculate:

1. Sample covariance between study hours and examination scores.
2. Pearson correlation coefficient.
3. Interpret the relationship.

---

# Step 1: Calculate the Sample Means

The sample mean formula is:

```text
X̄ = ΣX / n
```

The total study hours are:

```text
ΣX = 2 + 3 + 5 + 6 + 8

ΣX = 24
```

The number of observations is:

```text
n = 5
```

Therefore:

```text
X̄ = 24 / 5

X̄ = 4.8
```

---

The sample mean of examination scores is:

```text
Ȳ = ΣY / n
```

The total scores are:

```text
ΣY = 50 + 55 + 65 + 70 + 85

ΣY = 325
```

Therefore:

```text
Ȳ = 325 / 5

Ȳ = 65
```

---

# Step 2: Calculate Deviations from the Mean

For each observation, calculate:

```text
Deviation of X = Xi - X̄

Deviation of Y = Yi - Ȳ
```

| Student | X | Y  | Xi - X̄ | Yi - Ȳ |
| ------- | - | -- | ------- | ------ |
| A       | 2 | 50 | -2.8    | -15    |
| B       | 3 | 55 | -1.8    | -10    |
| C       | 5 | 65 | 0.2     | 0      |
| D       | 6 | 70 | 1.2     | 5      |
| E       | 8 | 85 | 3.2     | 20     |

---

# Step 3: Calculate Product of Deviations

The covariance formula requires:

```text
(Xi - X̄)(Yi - Ȳ)
```

Calculate each product:

| Student | Xi - X̄ | Yi - Ȳ | Product |
| ------- | ------- | ------ | ------- |
| A       | -2.8    | -15    | 42      |
| B       | -1.8    | -10    | 18      |
| C       | 0.2     | 0      | 0       |
| D       | 1.2     | 5      | 6       |
| E       | 3.2     | 20     | 64      |

Sum of products:

```text
Σ(Xi - X̄)(Yi - Ȳ)

= 42 + 18 + 0 + 6 + 64

= 130
```

---

# Step 4: Calculate Sample Covariance

The sample covariance formula is:

```text
sXY = Σ(Xi - X̄)(Yi - Ȳ) / (n - 1)
```

Substitute the values:

```text
sXY = 130 / (5 - 1)

sXY = 130 / 4

sXY = 32.5
```

Therefore:

```text
Sample Covariance = 32.5
```

---

# Interpretation of Covariance

The covariance is positive:

```text
sXY > 0
```

This means:

* Study hours and examination scores move in the same direction.
* Students who study more hours tend to obtain higher scores.

However, covariance alone cannot tell the strength of the relationship because it depends on measurement units.

Therefore, we calculate correlation.

---

# Step 5: Calculate Standard Deviation of X

The sample standard deviation formula is:

```text
sX = √(Σ(Xi - X̄)² / (n - 1))
```

Calculate squared deviations:

| Student | Xi - X̄ | (Xi - X̄)² |
| ------- | ------- | ---------- |
| A       | -2.8    | 7.84       |
| B       | -1.8    | 3.24       |
| C       | 0.2     | 0.04       |
| D       | 1.2     | 1.44       |
| E       | 3.2     | 10.24      |

Sum:

```text
Σ(Xi - X̄)² = 22.8
```

Therefore:

```text
sX = √(22.8 / 4)

sX = √5.7

sX = 2.39
```

---

# Step 6: Calculate Standard Deviation of Y

The squared deviations are:

| Student | Yi - Ȳ | (Yi - Ȳ)² |
| ------- | ------ | --------- |
| A       | -15    | 225       |
| B       | -10    | 100       |
| C       | 0      | 0         |
| D       | 5      | 25        |
| E       | 20     | 400       |

Sum:

```text
Σ(Yi - Ȳ)² = 750
```

Therefore:

```text
sY = √(750 / 4)

sY = √187.5

sY = 13.69
```

---

# Step 7: Calculate Pearson Correlation Coefficient

The correlation formula is:

```text
r = sXY / (sX × sY)
```

Substitute the values:

```text
r = 32.5 / (2.39 × 13.69)

r = 32.5 / 32.73

r ≈ 0.99
```

Therefore:

```text
Pearson Correlation Coefficient = 0.99
```

---

# Step 8: Interpretation of Correlation

The correlation coefficient is:

```text
r = 0.99
```

Since:

```text
r > 0
```

the relationship is positive.

Since:

```text
r is very close to +1
```

the relationship is very strong.

Therefore:

> There is a very strong positive linear relationship between study hours and examination scores.

Students who study more hours generally achieve higher scores.

---

# Step 9: Comparing Covariance and Correlation

From the calculation:

```text
Covariance:

sXY = 32.5
```

and

```text
Correlation:

r = 0.99
```

The difference is:

| Measure     | Meaning                                          |
| ----------- | ------------------------------------------------ |
| Covariance  | Shows the direction of the relationship          |
| Correlation | Shows direction and strength of the relationship |

Therefore:

* Covariance tells us **how variables move together**.
* Correlation tells us **how strongly they move together**.

---

# Final Conclusion

The analysis shows that study hours and examination scores have a very strong positive relationship.

However, we must remember:

> Correlation does not prove causation.

Higher study hours may contribute to better scores, but other factors may also influence examination performance, such as:

* previous knowledge,
* learning ability,
* teaching quality,
* study environment.

Statistical relationships must always be interpreted carefully.

---

