"""
Normal Distribution

Manual implementation of Normal distribution.

This program demonstrates:

1. Generating Normal random samples.
2. Calculating Z-score manually.
3. Calculating Normal PDF manually.
4. Estimating probabilities using simulation.
5. Comparing theoretical and experimental statistics.
6. Visualizing the Normal distribution.

Author: Desalu Horsa
"""


# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt


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

rng = np.random.default_rng()

samples = rng.normal(
    loc=mu,
    scale=sigma,
    size=number_of_simulations
)


# -------------------------------------------------
# Define Value of Interest
# -------------------------------------------------

x = 55


# -------------------------------------------------
# Calculate Z-score Manually
# -------------------------------------------------

z_score = (x - mu) / sigma


# -------------------------------------------------
# Calculate Normal PDF Manually
# -------------------------------------------------

coefficient = 1 / (sigma * math.sqrt(2 * math.pi))

exponent = math.exp(
    -((x - mu) ** 2) / (2 * sigma ** 2)
)

pdf_value = coefficient * exponent


# -------------------------------------------------
# Calculate Experimental Probability
# -------------------------------------------------

# Probability that X is less than x

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

theoretical_mean = mu

theoretical_variance = sigma ** 2

theoretical_std = sigma


# -------------------------------------------------
# Calculate Experimental Statistics
# -------------------------------------------------

experimental_mean = np.mean(samples)

experimental_variance = np.var(samples)

experimental_std = np.std(samples)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Normal Distribution")
print("-" * 45)

print(f"Mean (μ)                  : {mu}")

print(f"Standard Deviation (σ)    : {sigma}")

print(f"Number of Simulations     : {number_of_simulations}")

print()

print(f"Value of Interest (x)     : {x}")

print(f"Z-score                   : {z_score:.3f}")

print(f"PDF Value                 : {pdf_value:.5f}")

print()

print("Probability")

print(f"P(X < {x}) Experimental = "
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


pdf_values = (
    1 /
    (sigma * math.sqrt(2 * math.pi))
) * np.exp(
    -((x_values - mu) ** 2) /
    (2 * sigma ** 2)
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


plt.title("Normal Distribution")

plt.xlabel("Value")

plt.ylabel("Probability Density")

plt.grid(True)

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/normal_distribution.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()
