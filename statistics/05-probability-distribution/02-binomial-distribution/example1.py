"""
Binomial Distribution

This program demonstrates the Binomial distribution by

1. Generating random Binomial samples.
2. Computing theoretical probabilities.
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

# Number of Bernoulli trials
n = 10

# Probability of success
p = 0.60

# Number of simulated experiments
number_of_simulations = 10000


# -------------------------------------------------
# Generate Binomial Random Samples
# -------------------------------------------------

data = rng.binomial(
    n=n,
    p=p,
    size=number_of_simulations
)


# -------------------------------------------------
# Possible Outcomes
# -------------------------------------------------

x = np.arange(n + 1)


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
        math.comb(n, value)
        * (p ** value)
        * ((1 - p) ** (n - value))
    )

    theoretical_probabilities.append(probability)


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

experimental_mean = np.mean(data)

experimental_variance = np.var(data)

experimental_std = np.std(data)

theoretical_mean = n * p

theoretical_variance = n * p * (1 - p)

theoretical_std = math.sqrt(theoretical_variance)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Binomial Distribution")
print("-" * 45)

print(f"Number of Trials           : {n}")
print(f"Probability of Success     : {p:.2f}")
print(f"Number of Simulations      : {number_of_simulations}")

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

plt.figure(figsize=(9, 5))

plt.bar(
    x - width/2,
    theoretical_probabilities,
    width=width,
    label="Theoretical"
)

plt.bar(
    x + width/2,
    experimental_probabilities,
    width=width,
    label="Experimental"
)

plt.title("Binomial Distribution")

plt.xlabel("Number of Successes")

plt.ylabel("Probability")

plt.xticks(x)

plt.legend()

plt.grid(axis="y")


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/binomial_distribution.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()

