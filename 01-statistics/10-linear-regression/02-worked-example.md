# Worked Example: Simple Linear Regression

## Problem

A researcher wants to study the relationship between study hours and examination scores.

The following data were collected from five students.

| Student | Study Hours (X) | Exam Score (Y) |
| ------- | --------------- | -------------- |
| A       | 2               | 50             |
| B       | 3               | 55             |
| C       | 5               | 65             |
| D       | 6               | 70             |
| E       | 8               | 85             |

Determine:

1. The regression coefficients.
2. The regression equation.
3. The predicted examination score for a student who studies **7 hours**.
4. The residuals.
5. The coefficient of determination (R²).
6. Interpret the results.

---

# Step 1: Calculate the Means

The mean of the independent variable is

```text id="y65rkm"
X̄ = ΣX / n

= (2 + 3 + 5 + 6 + 8) / 5

= 24 / 5

= 4.8
```

The mean of the dependent variable is

```text id="w2x8af"
Ȳ = ΣY / n

= (50 + 55 + 65 + 70 + 85) / 5

= 325 / 5

= 65
```

---

# Step 2: Construct the Calculation Table

|         X |  Y | X − X̄ | Y − Ȳ | (X − X̄)(Y − Ȳ) | (X − X̄)² |
| --------: | -: | -----: | ----: | --------------: | --------: |
|         2 | 50 |   -2.8 |   -15 |            42.0 |      7.84 |
|         3 | 55 |   -1.8 |   -10 |            18.0 |      3.24 |
|         5 | 65 |    0.2 |     0 |             0.0 |      0.04 |
|         6 | 70 |    1.2 |     5 |             6.0 |      1.44 |
|         8 | 85 |    3.2 |    20 |            64.0 |     10.24 |
| **Total** |    |        |       |         **130** | **22.80** |

---

# Step 3: Calculate the Slope

The slope is

```text id="e5d4ua"
b = Σ[(Xi − X̄)(Yi − Ȳ)] / Σ[(Xi − X̄)²]
```

Substitute the values.

```text id="x9v3kc"
b = 130 / 22.8

b = 5.70
```

Therefore,

```text id="c3r6mf"
Slope (b) = 5.70
```

---

# Step 4: Calculate the Intercept

The intercept is

```text id="u4p9we"
a = Ȳ − bX̄
```

Substitute the values.

```text id="fg0mns"
a = 65 − (5.70 × 4.8)

a = 65 − 27.36

a = 37.64
```

Therefore,

```text id="pr9c0t"
Intercept (a) = 37.64
```

---

# Step 5: Construct the Regression Equation

Substitute the values of **a** and **b**.

```text id="b1y6rx"
Y = a + bX
```

Therefore,

```text id="a5w8nk"
Y = 37.64 + 5.70X
```

This equation is called the **regression equation**.

---

# Step 6: Predict a New Observation

Suppose a student studies

```text id="x4d2qz"
7 hours.
```

The predicted examination score is

```text id="p7s5jh"
Y = 37.64 + 5.70(7)

Y = 37.64 + 39.90

Y = 77.54
```

Therefore,

```text id="n8m4fw"
Predicted Score = 77.54
```

---

# Step 7: Calculate Predicted Values and Residuals

Use the regression equation to predict every observation.

|  X | Observed Y | Predicted Ŷ | Residual (Y − Ŷ) |
| -: | ---------: | ----------: | ---------------: |
|  2 |         50 |       49.04 |             0.96 |
|  3 |         55 |       54.74 |             0.26 |
|  5 |         65 |       66.14 |            -1.14 |
|  6 |         70 |       71.84 |            -1.84 |
|  8 |         85 |       83.24 |             1.76 |

The residuals are all relatively small, indicating that the regression line fits the data well.

---

# Step 8: Calculate the Coefficient of Determination

For simple linear regression,

```text id="m7u2vr"
R² = r²
```

From the previous chapter,

```text id="j4f8lx"
r = 0.99
```

Therefore,

```text id="g9z5pa"
R² = (0.99)²

R² = 0.98
```

Thus,

```text id="r5v1md"
R² = 0.98
```

---

# Interpretation of R²

An

```text id="h8w3qt"
R² = 0.98
```

means that approximately

```text id="z6n2ke"
98%
```

of the variation in examination scores is explained by study hours.

The remaining

```text id="m3q9pb"
2%
```

is due to other factors or random variation.

---

# Final Interpretation

The regression analysis indicates that:

* The relationship between study hours and examination scores is positive.
* Each additional hour of study increases the predicted examination score by approximately

```text id="p2x7cr"
5.70 points.
```

* A student who studies

```text id="q9v5ah"
7 hours
```

is expected to obtain a score of approximately

```text id="t4w8ys"
77.54.
```

* The regression model explains approximately

```text id="y8r3kn"
98%
```

of the variation in examination scores, indicating an excellent fit.

---

# Summary of the Computational Procedure

```text id="n5c2zx"
Calculate Means

↓

Construct Calculation Table

↓

Calculate Slope

↓

Calculate Intercept

↓

Construct Regression Equation

↓

Predict New Observation

↓

Calculate Residuals

↓

Calculate R²

↓

Interpret Results
```
