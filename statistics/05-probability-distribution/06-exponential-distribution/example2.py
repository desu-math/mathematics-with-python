"""
Exponential Distribution (SciPy)

This program demonstrates how to use scipy.stats.expon
to analyze an Exponential distribution.

It includes:

1. Generating exponential random samples.
2. Calculating probabilities using CDF.
3. Calculating PDF.
4. Computing theoretical statistics.
5. Comparing theory with simulation.
6. Visualizing the distribution.

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon


# -------------------------------------------------
# Define Distribution Parameter
# -------------------------------------------------

# Rate parameter
lam = 4

# SciPy uses scale = 1 / lambda
scale = 1 / lam

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Exponential Random Samples
# -------------------------------------------------

samples = expon.rvs(
    scale=scale,
    size=number_of_simulations,
    random_state=42
)


# -------------------------------------------------
# Define Time Interval
# -------------------------------------------------

x = 0.25


# -------------------------------------------------
# Calculate Probability Using CDF
# -------------------------------------------------

theoretical_probability = expon.cdf(
    x,
    scale=scale
)


# -------------------------------------------------
# Calculate PDF
# -------------------------------------------------

pdf_value = expon.pdf(
    x,
    scale=scale
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

theoretical_mean = expon.mean(
    scale=scale
)

theoretical_variance = expon.var(
    scale=scale
)

theoretical_std = expon.std(
    scale=scale
)


# -------------------------------------------------
# Calculate Experimental Statistics
# -------------------------------------------------

experimental_mean = np.mean(samples)

experimental_variance = np.var(samples)

experimental_std = np.std(samples)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Exponential Distribution (SciPy)")
print("-" * 45)

print(f"Rate Parameter (λ)        : {lam}")

print(f"Scale Parameter           : {scale}")

print(f"Number of Simulations     : {number_of_simulations}")

print()

print(f"Waiting Time (x)          : {x}")

print(f"PDF Value                 : {pdf_value:.5f}")

print()

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


pdf_values = expon.pdf(
    x_values,
    scale=scale
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


plt.title("Exponential Distribution Using SciPy")

plt.xlabel("Waiting Time")

plt.ylabel("Probability Density")

plt.grid(True)

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/exponential_distribution_scipy.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()

