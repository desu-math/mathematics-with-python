"""
Example 1: Manual Implementation of Covariance and Pearson Correlation

This program calculates:
    - Sample covariance
    - Sample standard deviation
    - Pearson correlation coefficient

without using statistical libraries.
"""

import math


# -------------------------------------------------
# Function to calculate mean
# -------------------------------------------------

def mean(data):
    return sum(data) / len(data)


# -------------------------------------------------
# Function to calculate sample covariance
# -------------------------------------------------

def covariance(x, y):

    n = len(x)

    # Calculate means
    x_mean = mean(x)
    y_mean = mean(y)

    # Calculate sum of products of deviations
    total = 0

    for i in range(n):
        total += (x[i] - x_mean) * (y[i] - y_mean)

    # Sample covariance
    return total / (n - 1)


# -------------------------------------------------
# Function to calculate sample standard deviation
# -------------------------------------------------

def standard_deviation(data):

    n = len(data)

    data_mean = mean(data)

    total = 0

    for value in data:
        total += (value - data_mean) ** 2

    variance = total / (n - 1)

    return math.sqrt(variance)


# -------------------------------------------------
# Function to calculate Pearson correlation
# -------------------------------------------------

def correlation(x, y):

    cov = covariance(x, y)

    sx = standard_deviation(x)

    sy = standard_deviation(y)

    return cov / (sx * sy)


# -------------------------------------------------
# Main Program
# -------------------------------------------------

# Study hours
X = [2, 3, 5, 6, 8]

# Examination scores
Y = [50, 55, 65, 70, 85]


# Calculate results

cov = covariance(X, Y)

sx = standard_deviation(X)

sy = standard_deviation(Y)

r = correlation(X, Y)


# Display results

print("Study Hours:", X)

print("Exam Scores:", Y)

print()

print("Covariance:")
print(round(cov, 2))

print()

print("Standard Deviation of X:")
print(round(sx, 2))

print()

print("Standard Deviation of Y:")
print(round(sy, 2))

print()

print("Pearson Correlation Coefficient:")
print(round(r, 2))


# Interpretation

print()

if r > 0:
    print("The variables have a positive relationship.")

elif r < 0:
    print("The variables have a negative relationship.")

else:
    print("The variables have no linear relationship.")


if abs(r) >= 0.8:
    print("The relationship strength is very strong.")

elif abs(r) >= 0.6:
    print("The relationship strength is strong.")

elif abs(r) >= 0.4:
    print("The relationship strength is moderate.")

else:
    print("The relationship strength is weak.")

