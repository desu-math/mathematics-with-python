"""
Sampling and Sampling Distributions

Manual simulation of the sampling process.

This program demonstrates:

1. Creating a population.
2. Drawing repeated random samples.
3. Calculating sample means.
4. Constructing a sampling distribution.
5. Computing the standard error.
6. Comparing population and sampling statistics.
7. Visualizing the results.

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# Create Population
# -------------------------------------------------

population_size = 10000

population_mean = 70

population_std = 12

rng = np.random.default_rng(42)

population = rng.normal(
    loc=population_mean,
    scale=population_std,
    size=population_size
)


# -------------------------------------------------
# Define Sampling Parameters
# -------------------------------------------------

sample_size = 50

number_of_samples = 1000


# -------------------------------------------------
# Draw Repeated Samples
# -------------------------------------------------

sample_means = []

for _ in range(number_of_samples):

    sample = rng.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_means.append(
        np.mean(sample)
    )

sample_means = np.array(sample_means)


# -------------------------------------------------
# Population Statistics
# -------------------------------------------------

pop_mean = np.mean(population)

pop_variance = np.var(population)

pop_std = np.std(population)


# -------------------------------------------------
# Sampling Distribution Statistics
# -------------------------------------------------

sampling_mean = np.mean(sample_means)

sampling_variance = np.var(sample_means)

sampling_std = np.std(sample_means)


# -------------------------------------------------
# Standard Error
# -------------------------------------------------

theoretical_se = (
    pop_std /
    math.sqrt(sample_size)
)

experimental_se = sampling_std


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Sampling Distribution")
print("-" * 45)

print(f"Population Size            : {population_size}")

print(f"Sample Size                : {sample_size}")

print(f"Number of Samples          : {number_of_samples}")

print()

print("Population Statistics")

print(f"Mean                       : {pop_mean:.3f}")

print(f"Variance                   : {pop_variance:.3f}")

print(f"Standard Deviation         : {pop_std:.3f}")

print()

print("Sampling Distribution")

print(f"Mean of Sample Means       : {sampling_mean:.3f}")

print(f"Variance                   : {sampling_variance:.3f}")

print(f"Standard Deviation         : {sampling_std:.3f}")

print()

print("Standard Error")

print(f"Theoretical SE             : {theoretical_se:.3f}")

print(f"Experimental SE            : {experimental_se:.3f}")


# -------------------------------------------------
# Visualization 1: Population
# -------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    population,
    bins=30,
    edgecolor="black"
)

plt.title("Population Distribution")

plt.xlabel("Value")

plt.ylabel("Frequency")

plt.grid(True)

plt.savefig(
    "images/population_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -------------------------------------------------
# Visualization 2: Sampling Distribution
# -------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    sample_means,
    bins=30,
    edgecolor="black"
)

plt.title("Sampling Distribution of the Sample Mean")

plt.xlabel("Sample Mean")

plt.ylabel("Frequency")

plt.grid(True)

plt.savefig(
    "images/sampling_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
