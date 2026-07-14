"""
Bernoulli Distribution

This program simulates a Bernoulli distribution,
calculates its statistical properties,
and visualizes the Probability Mass Function (PMF).

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# Create Random Number Generator
# -------------------------------------------------

rng = np.random.default_rng()


# -------------------------------------------------
# Define Distribution Parameters
# -------------------------------------------------

# Probability of success
p = 0.70

# Number of Bernoulli trials
number_of_trials = 1000


# -------------------------------------------------
# Generate Bernoulli Random Variables
# -------------------------------------------------

# 1 = Success
# 0 = Failure

data = rng.binomial(
    n=1,
    p=p,
    size=number_of_trials
)


# -------------------------------------------------
# Count Successes and Failures
# -------------------------------------------------

successes = np.count_nonzero(data == 1)

failures = np.count_nonzero(data == 0)


# -------------------------------------------------
# Experimental Probabilities
# -------------------------------------------------

experimental_success = successes / number_of_trials

experimental_failure = failures / number_of_trials


# -------------------------------------------------
# Statistical Properties
# -------------------------------------------------

mean = np.mean(data)

variance = np.var(data)

standard_deviation = np.std(data)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Bernoulli Distribution")
print("-" * 40)

print(f"Probability of Success (p) : {p:.2f}")
print(f"Number of Trials           : {number_of_trials}")

print()

print(f"Successes                  : {successes}")
print(f"Failures                   : {failures}")

print()

print("Theoretical Probabilities")
print(f"P(Success) = {p:.2f}")
print(f"P(Failure) = {1-p:.2f}")

print()

print("Experimental Probabilities")
print(f"P(Success) = {experimental_success:.3f}")
print(f"P(Failure) = {experimental_failure:.3f}")

print()

print("Statistical Properties")
print(f"Mean                 = {mean:.3f}")
print(f"Variance             = {variance:.3f}")
print(f"Standard Deviation   = {standard_deviation:.3f}")


# -------------------------------------------------
# Create PMF Bar Chart
# -------------------------------------------------

x = [0, 1]

probabilities = [
    experimental_failure,
    experimental_success
]

plt.figure(figsize=(6, 5))

plt.bar(
    x,
    probabilities,
    width=0.5
)

plt.xticks(
    [0, 1],
    ["Failure (0)", "Success (1)"]
)

plt.ylim(0, 1)

plt.xlabel("Outcome")

plt.ylabel("Probability")

plt.title("Bernoulli Distribution (Experimental PMF)")

plt.grid(axis="y")


# -------------------------------------------------
# Save Figure
# -------------------------------------------------

plt.savefig(
    "images/bernoulli_distribution.png",
    dpi=300,
    bbox_inches="tight"
)


# -------------------------------------------------
# Display Figure
# -------------------------------------------------

plt.show()

