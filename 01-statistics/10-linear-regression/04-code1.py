"""
Example 1: Manual Implementation of Simple Linear Regression

This program calculates:

    - Mean
    - Regression slope
    - Regression intercept
    - Regression equation
    - Prediction
    - Residuals
    - Coefficient of determination (R²)

using only basic Python.
"""

import math


# -----------------------------------------
# Mean
# -----------------------------------------

def mean(data):
    return sum(data) / len(data)


# -----------------------------------------
# Standard Deviation (Sample)
# -----------------------------------------

def standard_deviation(data):

    n = len(data)

    m = mean(data)

    total = 0

    for value in data:
        total += (value - m) ** 2

    variance = total / (n - 1)

    return math.sqrt(variance)


# -----------------------------------------
# Covariance (Sample)
# -----------------------------------------

def covariance(x, y):

    n = len(x)

    x_mean = mean(x)

    y_mean = mean(y)

    total = 0

    for i in range(n):
        total += (x[i] - x_mean) * (y[i] - y_mean)

    return total / (n - 1)


# -----------------------------------------
# Pearson Correlation
# -----------------------------------------

def correlation(x, y):

    cov = covariance(x, y)

    sx = standard_deviation(x)

    sy = standard_deviation(y)

    return cov / (sx * sy)


# -----------------------------------------
# Regression Coefficients
# -----------------------------------------

def regression_coefficients(x, y):

    x_mean = mean(x)

    y_mean = mean(y)

    numerator = 0
    denominator = 0

    for i in range(len(x)):

        numerator += (x[i] - x_mean) * (y[i] - y_mean)

        denominator += (x[i] - x_mean) ** 2

    b = numerator / denominator

    a = y_mean - b * x_mean

    return a, b


# -----------------------------------------
# Prediction Function
# -----------------------------------------

def predict(a, b, x):

    return a + b * x


# -----------------------------------------
# Main Program
# -----------------------------------------

study_hours = [2, 3, 5, 6, 8]

exam_scores = [50, 55, 65, 70, 85]


# Calculate regression coefficients

a, b = regression_coefficients(
    study_hours,
    exam_scores
)


# Display equation

print("Regression Equation")

print("-------------------")

print(f"Y = {a:.2f} + {b:.2f}X")

print()


# Predict a new observation

new_hours = 7

predicted_score = predict(
    a,
    b,
    new_hours
)

print(f"Predicted score for {new_hours} study hours:")

print(f"{predicted_score:.2f}")

print()


# Display residuals

print("Residuals")

print("---------")

for x, y in zip(study_hours, exam_scores):

    y_hat = predict(a, b, x)

    residual = y - y_hat

    print(
        f"X={x:2d}  "
        f"Observed={y:5.1f}  "
        f"Predicted={y_hat:6.2f}  "
        f"Residual={residual:6.2f}"
    )

print()


# Calculate R²

r = correlation(
    study_hours,
    exam_scores
)

r_squared = r ** 2

print(f"Correlation (r): {r:.4f}")

print(f"Coefficient of Determination (R²): {r_squared:.4f}")

print()


# Interpretation

if b > 0:
    print("Positive linear relationship.")

elif b < 0:
    print("Negative linear relationship.")

else:
    print("No linear relationship.")

print()

print(
    f"The model explains "
    f"{r_squared * 100:.2f}% "
    f"of the variation in the data."
)

