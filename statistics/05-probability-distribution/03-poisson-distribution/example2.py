"""
Poisson Distribution (SciPy)

This program demonstrates how to use scipy.stats.poisson
to analyze a Poisson distribution.

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Average number of events
lam = 4

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Random Samples
# -------------------------------------------------

samples = poisson.rvs(
    mu=lam,
    size=number_of_simulations,
    random_state=42
)


# -------------------------------------------------
# Determine Possible Outcomes
# -------------------------------------------------

x = np.arange(0, np.max(samples) + 1)


# -------------------------------------------------
# Calculate Theoretical PMF
# -------------------------------------------------

theoretical_probabilities = poisson.pmf(x, mu=lam)


# -------------------------------------------------
# Calculate Experimental Probabilities
# -------------------------------------------------

experimental_probabilities = []

for value in x:

    probability = np.mean(samples == value)

    experimental_probabilities.append(probability)


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

theoretical_mean = poisson.mean(mu=lam)

theoretical_variance = poisson.var(mu=lam)

theoretical_std = poisson.std(mu=lam)

experimental_mean = np.mean(samples)

experimental_variance = np.var(samples)

experimental_std = np.std(samples)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Poisson Distribution (SciPy)")
print("-" * 45)

print(f"Lambda (λ)               : {lam}")
print(f"Number of Simulations    : {number_of_simulations}")

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
# Create Comparison Plot
# -------------------------------------------------

width = 0.4

plt.figure(figsize=(10, 5))

plt.bar(
    x - width / 2,
    theoretical_probabilities,
    width=width,
    label="Theoretical PMF"
)

plt.bar(
    x + width / 2,
    experimental_probabilities,
    width=width,
    label="Experimental PMF"
)

plt.title("Poisson Distribution Using SciPy")

plt.xlabel("Number of Events")

plt.ylabel("Probability")

plt.xticks(x)

plt.grid(axis="y")

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/poisson_distribution_scipy.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()

