"""
Confidence Interval Estimation Using Statistical Libraries

This example demonstrates how to calculate confidence
intervals using Python libraries.

Methods included:

1. Z-confidence interval
   - Population standard deviation is known.

2. t-confidence interval
   - Population standard deviation is unknown.

Libraries:
- NumPy
- SciPy

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
from scipy import stats


# =================================================
# Example 1: Z-Confidence Interval
# =================================================

print("Z-Confidence Interval")
print("-" * 40)


# Sample information

sample_mean = 72

population_std = 8

sample_size = 64

confidence_level = 0.95


# Calculate confidence interval

alpha = 1 - confidence_level


critical_value = stats.norm.ppf(
    1 - alpha / 2
)


standard_error = (
    population_std /
    np.sqrt(sample_size)
)


margin_of_error = (
    critical_value *
    standard_error
)


lower_limit = (
    sample_mean -
    margin_of_error
)


upper_limit = (
    sample_mean +
    margin_of_error
)


print(f"Sample Mean       : {sample_mean}")

print(f"Critical Value    : {critical_value:.3f}")

print(f"Standard Error    : {standard_error:.3f}")

print(f"Margin of Error   : {margin_of_error:.3f}")

print(
    f"Confidence Interval: "
    f"({lower_limit:.3f}, {upper_limit:.3f})"
)


# =================================================
# Example 2: t-Confidence Interval
# =================================================

print("\n\n")

print("t-Confidence Interval")
print("-" * 40)


# Sample information

sample_data = np.array(
    [
        5.2, 6.1, 7.0, 5.8, 6.5,
        7.2, 6.8, 5.9, 6.4, 6.7,
        5.5, 6.9, 7.1, 6.3, 6.0,
        6.6, 5.7, 6.2, 7.3, 6.8,
        6.1, 5.6, 6.4, 6.9, 6.5
    ]
)


confidence_level = 0.95


# Calculate sample statistics

sample_size = len(sample_data)

sample_mean = np.mean(sample_data)

sample_std = np.std(
    sample_data,
    ddof=1
)


# Degrees of freedom

degrees_of_freedom = (
    sample_size - 1
)


# Find t critical value

alpha = 1 - confidence_level


critical_value = stats.t.ppf(
    1 - alpha / 2,
    degrees_of_freedom
)


# Standard error

standard_error = (
    sample_std /
    np.sqrt(sample_size)
)


# Margin of error

margin_of_error = (
    critical_value *
    standard_error
)


# Confidence interval

lower_limit = (
    sample_mean -
    margin_of_error
)


upper_limit = (
    sample_mean +
    margin_of_error
)


print(f"Sample Size       : {sample_size}")

print(f"Sample Mean       : {sample_mean:.3f}")

print(f"Sample Std        : {sample_std:.3f}")

print(f"Degrees of Freedom: {degrees_of_freedom}")

print(f"Critical Value    : {critical_value:.3f}")

print(f"Standard Error    : {standard_error:.3f}")

print(f"Margin of Error   : {margin_of_error:.3f}")

print(
    f"Confidence Interval: "
    f"({lower_limit:.3f}, {upper_limit:.3f})"
)

