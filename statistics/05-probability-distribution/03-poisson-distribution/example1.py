"""
Poisson Distribution

This program demonstrates the Poisson distribution by

1. Generating random Poisson samples.
2. Computing theoretical probabilities manually.
3. Computing experimental probabilities.
4. Comparing theory with simulation.
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
# Create Random Number Generator
# -------------------------------------------------

rng = np.random.default_rng()


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Average number of events
lam = 4

# Number of simulations
number_of_simulations = 10000


# -------------------------------------------------
# Generate Poisson Random Samples
# -------------------------------------------------

data = rng.poisson(
    lam=lam,
    size=number_of_simulations
)


# -------------------------------------------------
# Determine Possible Outcomes
# -------------------------------------------------

max_value = np.max(data)

x = np.arange(max_value + 1)


# -------------------------------------------------
# Calculate Experimental Probabilities
# -------------------------------------------------

experimental_probabilities = []

for value in x:

    count = np.count_nonzero(data == value)

    probability = count / number_of_simulations

    experimental_probabilities.append(probability)


# -------------------------------------------------
# Calculate Theoretical Probabilities
# -------------------------------------------------

theoretical_probabilities = []

for value in x:

    probability = (
        math.exp(-lam)
        * (lam ** value)
        / math.factorial(value)
    )

    theoretical_probabilities.append(probability)


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

experimental_mean = np.mean(data)

experimental_variance = np.var(data)

experimental_std = np.std(data)

theoretical_mean = lam

theoretical_variance = lam

theoretical_std = math.sqrt(lam)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Poisson Distribution")
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
    label="Theoretical"
)

plt.bar(
    x + width / 2,
    experimental_probabilities,
    width=width,
    label="Experimental"
)

plt.title("Poisson Distribution")

plt.xlabel("Number of Events")

plt.ylabel("Probability")

plt.xticks(x)

plt.grid(axis="y")

plt.legend()


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/poisson_distribution.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()
