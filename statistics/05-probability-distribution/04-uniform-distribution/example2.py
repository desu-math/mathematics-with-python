"""
Uniform Distribution (SciPy)

This program demonstrates how to use scipy.stats.uniform
to analyze a continuous Uniform distribution.

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Lower bound
a = 0

# Upper bound
b = 20

# Interval length
scale = b - a

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Random Samples
# -------------------------------------------------

samples = uniform.rvs(
    loc=a,
    scale=scale,
    size=number_of_simulations,
    random_state=42
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
    (samples >= lower_interval) &
    (samples <= upper_interval)
)

experimental_probability = (
    values_inside_interval /
    number_of_simulations
)


# -------------------------------------------------
# Calculate Theoretical Probability
# -------------------------------------------------

theoretical_probability = (
    uniform.cdf(upper_interval, loc=a, scale=scale)
    -
    uniform.cdf(lower_interval, loc=a, scale=scale)
)


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

theoretical_mean = uniform.mean(
    loc=a,
    scale=scale
)

theoretical_variance = uniform.var(
    loc=a,
    scale=scale
)

theoretical_std = uniform.std(
    loc=a,
    scale=scale
)

experimental_mean = np.mean(samples)

experimental_variance = np.var(samples)

experimental_std = np.std(samples)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Uniform Distribution (SciPy)")
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
# Create Visualization
# -------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    samples,
    bins=20,
    density=True,
    edgecolor="black",
    alpha=0.7,
    label="Experimental Distribution"
)

x = np.linspace(a, b, 500)

plt.plot(
    x,
    uniform.pdf(x, loc=a, scale=scale),
    linewidth=2,
    label="Theoretical PDF"
)

plt.title("Uniform Distribution Using SciPy")

plt.xlabel("Value")

plt.ylabel("Probability Density")

plt.grid(True)

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/uniform_distribution_scipy.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()

