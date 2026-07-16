"""
Exponential Distribution

Manual implementation of Exponential distribution.

This program demonstrates:

1. Generating exponential random samples.
2. Calculating probability using the CDF formula.
3. Estimating probability using simulation.
4. Comparing theoretical and experimental statistics.
5. Visualizing the distribution.

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# Define Distribution Parameter
# -------------------------------------------------

# Rate parameter
lam = 4

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Exponential Random Samples
# -------------------------------------------------

rng = np.random.default_rng()

samples = rng.exponential(
    scale=1 / lam,
    size=number_of_simulations
)


# -------------------------------------------------
# Define Time Interval
# -------------------------------------------------

# Time until event occurs
x = 0.25


# -------------------------------------------------
# Calculate Theoretical Probability
# -------------------------------------------------

# P(X <= x) = 1 - e^(-λx)

theoretical_probability = (
    1 -
    math.exp(
        -lam * x
    )
)


# -------------------------------------------------
# Calculate Experimental Probability
# -------------------------------------------------

values_below_x = np.count_nonzero(
    samples <= x
)

experimental_probability = (
    values_below_x /
    number_of_simulations
)


# -------------------------------------------------
# Calculate Theoretical Statistics
# -------------------------------------------------

theoretical_mean = 1 / lam

theoretical_variance = 1 / (lam ** 2)

theoretical_std = 1 / lam


# -------------------------------------------------
# Calculate Experimental Statistics
# -------------------------------------------------

experimental_mean = np.mean(samples)

experimental_variance = np.var(samples)

experimental_std = np.std(samples)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Exponential Distribution")
print("-" * 45)

print(f"Rate Parameter (λ)        : {lam}")

print(f"Number of Simulations     : {number_of_simulations}")

print()

print(f"Waiting Time (x)          : {x} hours")

print()

print("Probability")

print(
    f"P(X ≤ {x}) Theoretical  = "
    f"{theoretical_probability:.4f}"
)

print(
    f"P(X ≤ {x}) Experimental = "
    f"{experimental_probability:.4f}"
)

print()

print("Theoretical Statistics")

print(
    f"Mean                 = "
    f"{theoretical_mean:.4f}"
)

print(
    f"Variance             = "
    f"{theoretical_variance:.4f}"
)

print(
    f"Standard Deviation   = "
    f"{theoretical_std:.4f}"
)

print()

print("Experimental Statistics")

print(
    f"Mean                 = "
    f"{experimental_mean:.4f}"
)

print(
    f"Variance             = "
    f"{experimental_variance:.4f}"
)

print(
    f"Standard Deviation   = "
    f"{experimental_std:.4f}"
)


# -------------------------------------------------
# Create Exponential Curve
# -------------------------------------------------

x_values = np.linspace(
    0,
    max(samples),
    500
)


pdf_values = (
    lam *
    np.exp(
        -lam * x_values
    )
)


# -------------------------------------------------
# Visualization
# -------------------------------------------------

plt.figure(figsize=(10, 5))


plt.hist(
    samples,
    bins=30,
    density=True,
    alpha=0.6,
    edgecolor="black",
    label="Simulation"
)


plt.plot(
    x_values,
    pdf_values,
    linewidth=2,
    label="Exponential PDF"
)


plt.axvline(
    x,
    linestyle="--",
    linewidth=2,
    label=f"x = {x}"
)


plt.title("Exponential Distribution")

plt.xlabel("Waiting Time")

plt.ylabel("Probability Density")

plt.grid(True)

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/exponential_distribution.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()
