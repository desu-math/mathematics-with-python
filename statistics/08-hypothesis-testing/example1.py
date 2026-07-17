"""
One-Sample Z-Test: Manual Implementation

This program demonstrates the complete process
of hypothesis testing using a one-sample Z-test.

The example follows the statistical procedure:

1. Define hypotheses
2. Select significance level
3. Calculate standard error
4. Calculate test statistic
5. Compare with critical value
6. Make statistical decision
7. Interpret the result

No statistical library is used.

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math


# =================================================
# Step 1: Define Sample Information
# =================================================

sample_mean = 504

hypothesized_mean = 500

population_std = 12

sample_size = 64


# Significance level

alpha = 0.05


print("One-Sample Z-Test")
print("-" * 40)


# =================================================
# Step 2: State Hypotheses
# =================================================

print("Null Hypothesis:")
print("H0: μ = 500")

print()

print("Alternative Hypothesis:")
print("H1: μ ≠ 500")


# =================================================
# Step 3: Calculate Standard Error
# =================================================

standard_error = (
    population_std /
    math.sqrt(sample_size)
)


print()

print(
    f"Standard Error = {standard_error:.3f}"
)


# =================================================
# Step 4: Calculate Z-Test Statistic
# =================================================

z_score = (
    (sample_mean - hypothesized_mean)
    /
    standard_error
)


print(
    f"Z-Test Statistic = {z_score:.3f}"
)


# =================================================
# Step 5: Determine Critical Values
# =================================================

# For a two-tailed test with α = 0.05
# Critical values are ±1.96

critical_lower = -1.96

critical_upper = 1.96


print()

print(
    f"Critical Values = "
    f"{critical_lower} and {critical_upper}"
)


# =================================================
# Step 6: Make Statistical Decision
# =================================================

if z_score < critical_lower or z_score > critical_upper:

    decision = "Reject H0"

else:

    decision = "Fail to Reject H0"


print()

print(
    "Decision:",
    decision
)


# =================================================
# Step 7: Interpretation
# =================================================

print()

if decision == "Reject H0":

    print(
        "There is sufficient evidence "
        "to conclude that the population mean "
        "is different from 500."
    )

else:

    print(
        "There is insufficient evidence "
        "to conclude that the population mean "
        "is different from 500."
    )


# =================================================
# Step 8: Type I Error Information
# =================================================

print()

print(
    f"Significance Level (α) = {alpha}"
)

print(
    "Probability of Type I Error = α"
)

