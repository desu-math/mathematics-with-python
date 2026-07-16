"""
Confidence Interval Estimation

Manual implementation of a Z-confidence interval
for the population mean.

This example demonstrates:

1. Point estimation
2. Standard error calculation
3. Critical value selection
4. Margin of error calculation
5. Confidence interval construction

Case:
Population standard deviation is known.

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math


# -------------------------------------------------
# Sample Information
# -------------------------------------------------

# Sample mean
sample_mean = 72


# Population standard deviation
population_std = 8


# Sample size
sample_size = 64


# Confidence level
confidence_level = 0.95


# -------------------------------------------------
# Critical Value
# -------------------------------------------------

# For a 95% confidence interval:
# Z(alpha/2) = 1.96

z_value = 1.96


# -------------------------------------------------
# Calculate Standard Error
# -------------------------------------------------

standard_error = (
    population_std /
    math.sqrt(sample_size)
)


# -------------------------------------------------
# Calculate Margin of Error
# -------------------------------------------------

margin_of_error = (
    z_value *
    standard_error
)


# -------------------------------------------------
# Construct Confidence Interval
# -------------------------------------------------

lower_limit = (
    sample_mean -
    margin_of_error
)


upper_limit = (
    sample_mean +
    margin_of_error
)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Confidence Interval Estimation")
print("-" * 40)

print(f"Sample Mean          : {sample_mean}")

print(f"Population Std       : {population_std}")

print(f"Sample Size          : {sample_size}")

print(f"Confidence Level     : {confidence_level * 100}%")

print()

print(f"Standard Error       : {standard_error:.3f}")

print(f"Margin of Error      : {margin_of_error:.3f}")

print()

print(
    f"Confidence Interval  : "
    f"({lower_limit:.3f}, {upper_limit:.3f})"
)


# -------------------------------------------------
# Interpretation
# -------------------------------------------------

print()

print(
    "Interpretation:"
)

print(
    "We are 95% confident that the true "
    "population mean lies within this interval."
)

