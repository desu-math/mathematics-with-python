"""
One-Sample Z-Test Using Statistical Libraries

This program demonstrates hypothesis testing
using Python statistical libraries.

The example performs:

1. One-sample Z-test
2. Critical value approach
3. p-value approach
4. Statistical decision

Libraries:
- NumPy
- SciPy

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math
from scipy import stats


# =================================================
# Step 1: Define Sample Information
# =================================================

sample_mean = 504

hypothesized_mean = 500

population_std = 12

sample_size = 64


# Significance level

alpha = 0.05


print("One-Sample Z-Test Using SciPy")
print("-" * 45)


# =================================================
# Step 2: Calculate Standard Error
# =================================================

standard_error = (
    population_std /
    math.sqrt(sample_size)
)


print(
    f"Standard Error: {standard_error:.3f}"
)


# =================================================
# Step 3: Calculate Test Statistic
# =================================================

z_score = (
    (sample_mean - hypothesized_mean)
    /
    standard_error
)


print(
    f"Z-Test Statistic: {z_score:.3f}"
)


# =================================================
# Step 4: Calculate Critical Values
# =================================================

# Two-tailed test

critical_value = stats.norm.ppf(
    1 - alpha / 2
)


critical_lower = -critical_value

critical_upper = critical_value


print()

print(
    f"Critical Values: "
    f"{critical_lower:.3f} and {critical_upper:.3f}"
)


# =================================================
# Step 5: Critical Value Decision
# =================================================

if z_score < critical_lower or z_score > critical_upper:

    critical_decision = "Reject H0"

else:

    critical_decision = "Fail to Reject H0"


print()

print(
    "Critical Value Approach:"
)

print(
    critical_decision
)


# =================================================
# Step 6: Calculate p-value
# =================================================

# Two-tailed p-value

p_value = (
    2 *
    (1 - stats.norm.cdf(abs(z_score)))
)


print()

print(
    f"p-value: {p_value:.5f}"
)


# =================================================
# Step 7: p-value Decision
# =================================================

if p_value <= alpha:

    p_decision = "Reject H0"

else:

    p_decision = "Fail to Reject H0"


print()

print(
    "p-value Approach:"
)

print(
    p_decision
)


# =================================================
# Step 8: Statistical Interpretation
# =================================================

print()

if p_decision == "Reject H0":

    print(
        "There is sufficient statistical evidence "
        "that the population mean is different "
        "from 500."
    )

else:

    print(
        "There is insufficient statistical evidence "
        "that the population mean is different "
        "from 500."
    )


# =================================================
# Step 9: Error Information
# =================================================

print()

print(
    f"Significance Level (α): {alpha}"
)

print(
    "Type I Error Probability = α"
)

