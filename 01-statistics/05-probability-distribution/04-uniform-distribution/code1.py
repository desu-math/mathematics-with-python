"""
Uniform Distribution

This program demonstrates the continuous Uniform distribution by

1. Generating Uniform random samples.
2. Computing theoretical statistics manually.
3. Computing experimental statistics.
4. Estimating interval probability.
5. Comparing theory with simulation.
6. Visualizing the distribution.

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# Create Random Number Generator
# -------------------------------------------------

rng = np.random.default_rng()


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Lower bound
a = 0

# Upper bound
b = 20

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Uniform Random Samples
# -------------------------------------------------

data = rng.uniform(
    low=a,
    high=b,
    size=number_of_simulations
)


# -------------------------------------------------
# Define the Desired Interval
# -------------------------------------------------

lower_interval = 5

upper_interval = 12


# -------------------------------------------------
# Calculate Experimental Probability
# -------------------------------------------------

values_inside_interval = np.count_nonzero(
    (data >= lower_interval) &
    (data <= upper_interval)
)

experimental_probability = (
    values_inside_interval /
    number_of_simulations
)


# -------------------------------------------------
# Calculate Theoretical Probability
# -------------------------------------------------

theoretical_probability = (
    (upper_interval - lower_interval) /
    (b - a)
)


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

# Theoretical

theoretical_mean = (a + b) / 2

theoretical_variance = ((b - a) ** 2) / 12

theoretical_std = math.sqrt(theoretical_variance)

# Experimental

experimental_mean = np.mean(data)

experimental_variance = np.var(data)

experimental_std = np.std(data)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Uniform Distribution")
print("-" * 45)

print(f"Interval                  : [{a}, {b}]")

print(f"Number of Simulations     : {number_of_simulations}")

print()

print(
    f"Probability ({lower_interval} ≤ X ≤ {upper_interval})"
)

print(f"Theoretical = {theoretical_probability:.4f}")

print(f"Experimental = {experimental_probability:.4f}")

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
# Create Histogram
# -------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    data,
    bins=20,
    density=True,
    edgecolor="black",
    label="Experimental Distribution"
)

plt.axhline(
    y=1 / (b - a),
    linestyle="--",
    linewidth=2,
    label="Theoretical PDF"
)

plt.title("Uniform Distribution")

plt.xlabel("Value")

plt.ylabel("Probability Density")

plt.grid(True)

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/uniform_distribution.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()
