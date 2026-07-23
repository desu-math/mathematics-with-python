"""
Normal Distribution (SciPy)

This program demonstrates how to use scipy.stats.norm
to analyze a Normal distribution.

It includes:

1. Generating Normal random samples.
2. Calculating Z-score.
3. Calculating PDF.
4. Calculating probabilities using CDF.
5. Computing theoretical statistics.
6. Comparing theory with simulation.
7. Visualizing the distribution.

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Mean
mu = 50

# Standard deviation
sigma = 5

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Normal Random Samples
# -------------------------------------------------

samples = norm.rvs(
    loc=mu,
    scale=sigma,
    size=number_of_simulations,
    random_state=42
)


# -------------------------------------------------
# Define Value of Interest
# -------------------------------------------------

x = 55


# -------------------------------------------------
# Calculate Z-score
# -------------------------------------------------

z_score = (
    x - mu
) / sigma


# -------------------------------------------------
# Calculate PDF
# -------------------------------------------------

pdf_value = norm.pdf(
    x,
    loc=mu,
    scale=sigma
)


# -------------------------------------------------
# Calculate Probability Using CDF
# -------------------------------------------------

theoretical_probability = norm.cdf(
    x,
    loc=mu,
    scale=sigma
)


# -------------------------------------------------
# Calculate Experimental Probability
# -------------------------------------------------

values_below_x = np.count_nonzero(
    samples < x
)

experimental_probability = (
    values_below_x /
    number_of_simulations
)


# -------------------------------------------------
# Calculate Theoretical Statistics
# -------------------------------------------------

theoretical_mean = norm.mean(
    loc=mu,
    scale=sigma
)

theoretical_variance = norm.var(
    loc=mu,
    scale=sigma
)

theoretical_std = norm.std(
    loc=mu,
    scale=sigma
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

print("Normal Distribution (SciPy)")
print("-" * 45)

print(f"Mean (μ)                  : {mu}")

print(f"Standard Deviation (σ)    : {sigma}")

print(f"Number of Simulations     : {number_of_simulations}")

print()

print(f"Value of Interest (x)     : {x}")

print(f"Z-score                   : {z_score:.3f}")

print(f"PDF Value                 : {pdf_value:.5f}")

print()

print(f"P(X < {x}) Theoretical    : "
      f"{theoretical_probability:.4f}")

print(f"P(X < {x}) Experimental   : "
      f"{experimental_probability:.4f}")

print()

print("Theoretical Statistics")

print(f"Mean                 = {theoretical_mean:.3f}")

print(f"Variance             = {theoretical_variance:.3f}")

print(f"Standard Deviation   = {theoretical_std:.3f}")

print()

print("Experimental Statistics")

print(f"Mean                 = {experimental_mean:.3f}")

print(f"Variance             = {experimental_variance:.3f}")

print(f"Standard Deviation   = {experimental_std:.3f}")


# -------------------------------------------------
# Create Normal Curve
# -------------------------------------------------

x_values = np.linspace(
    mu - 4 * sigma,
    mu + 4 * sigma,
    500
)


pdf_values = norm.pdf(
    x_values,
    loc=mu,
    scale=sigma
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
    label="Normal PDF"
)


plt.axvline(
    x,
    linestyle="--",
    linewidth=2,
    label=f"x = {x}"
)


plt.title("Normal Distribution Using SciPy")

plt.xlabel("Value")

plt.ylabel("Probability Density")

plt.grid(True)

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/normal_distribution_scipy.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()
