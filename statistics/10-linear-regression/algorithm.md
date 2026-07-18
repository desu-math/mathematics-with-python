# Algorithm: Simple Linear Regression

## Introduction

The purpose of the linear regression algorithm is to determine the equation of the best-fitting straight line for a set of paired observations.

Given two variables:

```text id="x8q3mv"
X = Independent Variable

Y = Dependent Variable
```

the algorithm computes:

* Regression slope
* Regression intercept
* Regression equation
* Predicted values
* Residuals
* Coefficient of determination (R²)

---

# Input

Two numerical datasets with equal length:

```text id="b4r7tn"
X = [x1, x2, x3, ..., xn]

Y = [y1, y2, y3, ..., yn]
```

where

```text id="d2m8ks"
n = Number of observations
```

---

# Output

The algorithm returns:

```text id="k9v5aq"
Regression Equation

Predicted Values

Residuals

Coefficient of Determination (R²)
```

---

# Algorithm Steps

## Step 1: Validate the Input

Check that:

* both datasets have the same number of observations,
* the number of observations is greater than one.

If either condition is not satisfied, terminate the algorithm.

---

## Step 2: Calculate the Means

Compute the mean of each variable.

```text id="p7x2mz"
X̄ = ΣX / n

Ȳ = ΣY / n
```

---

## Step 3: Calculate the Regression Slope

Compute

```text id="j4q6nf"
Σ[(Xi − X̄)(Yi − Ȳ)]
```

and

```text id="v8k3cw"
Σ[(Xi − X̄)²]
```

Then calculate

```text id="r2t9bx"
b = Σ[(Xi − X̄)(Yi − Ȳ)] /
    Σ[(Xi − X̄)²]
```

---

## Step 4: Calculate the Intercept

Compute

```text id="g5n8pl"
a = Ȳ − bX̄
```

---

## Step 5: Construct the Regression Equation

The regression model is

```text id="w9f4rm"
Y = a + bX
```

---

## Step 6: Calculate Predicted Values

For each observation,

```text id="h7m2zd"
Ŷ = a + bX
```

Store every predicted value.

---

## Step 7: Calculate Residuals

For every observation,

```text id="c8p5kv"
Residual = Y − Ŷ
```

Residuals measure the prediction error.

---

## Step 8: Calculate the Coefficient of Determination

First compute the Pearson correlation coefficient:

```text id="u3r9xn"
r
```

Then compute

```text id="q6v4ws"
R² = r²
```

This measures how much of the variation in the dependent variable is explained by the regression model.

---

## Step 9: Interpret the Model

Interpret the slope:

* Positive slope → Positive linear relationship.
* Negative slope → Negative linear relationship.
* Zero slope → No linear relationship.

Interpret R²:

* Larger R² indicates a better-fitting regression model.

---

# Complete Algorithm

```text id="m5x8qa"
Algorithm: Simple Linear Regression

Input:
    X, Y

Begin

    1. Validate the datasets.

    2. Compute X̄ and Ȳ.

    3. Compute the slope:

           b

    4. Compute the intercept:

           a

    5. Construct:

           Y = a + bX

    6. For each observation:

           Calculate Ŷ

    7. Compute residuals:

           Y − Ŷ

    8. Compute:

           R² = r²

    9. Interpret the regression model.

End
```

---

# Computational Complexity

Assume there are

```text id="t4w7cn"
n
```

observations.

The algorithm performs several linear passes through the data to compute:

* means,
* slope,
* intercept,
* predictions,
* residuals,
* evaluation metrics.

Therefore,

```text id="f9k3yb"
Time Complexity = O(n)
```

The algorithm stores the input data and the predicted values.

Thus,

```text id="e2v6mp"
Space Complexity = O(n)
```

---

# Numerical Considerations

When implementing linear regression:

* Ensure both datasets have the same length.
* Avoid division by zero if all X values are identical.
* Check for extreme outliers that may influence the regression line.
* Use floating-point arithmetic for accurate calculations.

---

# Summary of the Algorithm

```text id="s8r2qd"
Input Data

↓

Validate Data

↓

Calculate Means

↓

Calculate Slope

↓

Calculate Intercept

↓

Construct Regression Equation

↓

Predict Values

↓

Calculate Residuals

↓

Calculate R²

↓

Interpret Results
```

This algorithm forms the basis of simple linear regression and is directly implemented in the accompanying Python examples.
