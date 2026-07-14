"""
Binomial Distribution (SciPy)

This program demonstrates how to use scipy.stats.binom
to analyze a Binomial distribution.

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Number of trials
n = 10

# Probability of success
p = 0.60

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Possible Outcomes
# -------------------------------------------------

x = np.arange(n + 1)


# -------------------------------------------------
# Theoretical PMF
# -------------------------------------------------

theoretical_probabilities = binom.pmf(x, n, p)


# -------------------------------------------------
# Generate Random Samples
# -------------------------------------------------

samples = binom.rvs(
    n,
    p,
    size=number_of_simulations,
    random_state=42
)


# -------------------------------------------------
# Experimental Probabilities
# -------------------------------------------------

experimental_probabilities = []

for value in x:

    probability = np.mean(samples == value)

    experimental_probabilities.append(probability)


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

theoretical_mean = binom.mean(n, p)

theoretical_variance = binom.var(n, p)

theoretical_std = binom.std(n, p)

experimental_mean = np.mean(samples)

experimental_variance = np.var(samples)

experimental_std = np.std(samples)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Binomial Distribution (SciPy)")
print("-" * 45)

print(f"Number of Trials      : {n}")
print(f"Probability           : {p:.2f}")
print(f"Simulations           : {number_of_simulations}")

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
# Visualization
# -------------------------------------------------

width = 0.4

plt.figure(figsize=(9,5))

plt.bar(
    x - width/2,
    theoretical_probabilities,
    width,
    label="Theoretical PMF"
)

plt.bar(
    x + width/2,
    experimental_probabilities,
    width,
    label="Experimental PMF"
)

plt.title("Binomial Distribution Using SciPy")

plt.xlabel("Number of Successes")

plt.ylabel("Probability")

plt.xticks(x)

plt.grid(axis="y")

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/binomial_distribution_scipy.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()

