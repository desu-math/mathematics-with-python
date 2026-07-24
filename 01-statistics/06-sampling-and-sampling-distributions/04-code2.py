"""
Sampling and Sampling Distributions (Library-Based)

This program demonstrates professional statistical
analysis of sampling distributions using NumPy and SciPy.

It includes:

1. Creating a population.
2. Drawing repeated random samples.
3. Constructing the sampling distribution.
4. Computing descriptive statistics.
5. Computing the standard error.
6. Computing a 95% confidence interval.
7. Visualizing the population and sampling distribution.

Author: Desalu Horsa
"""

# -------------------------------------------------
# Import Libraries
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import (
    describe,
    sem,
    norm
)


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
# Sampling Parameters
# -------------------------------------------------

sample_size = 50

number_of_samples = 1000


# -------------------------------------------------
# Generate Sampling Distribution
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

population_statistics = describe(population)


# -------------------------------------------------
# Sampling Distribution Statistics
# -------------------------------------------------

sampling_statistics = describe(sample_means)


# -------------------------------------------------
# Standard Error
# -------------------------------------------------

experimental_se = sem(sample_means)

theoretical_se = (
    np.std(population, ddof=0)
    /
    np.sqrt(sample_size)
)


# -------------------------------------------------
# 95% Confidence Interval
# -------------------------------------------------

confidence_interval = norm.interval(
    confidence=0.95,
    loc=np.mean(sample_means),
    scale=experimental_se
)


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("Sampling Distribution (Library-Based)")
print("-" * 50)

print(f"Population Size      : {population_size}")

print(f"Sample Size          : {sample_size}")

print(f"Repeated Samples     : {number_of_samples}")

print()

print("Population")

print(f"Mean                 : {population_statistics.mean:.3f}")

print(f"Variance             : {population_statistics.variance:.3f}")

print()

print("Sampling Distribution")

print(f"Mean                 : {sampling_statistics.mean:.3f}")

print(f"Variance             : {sampling_statistics.variance:.3f}")

print()

print("Standard Error")

print(f"Theoretical          : {theoretical_se:.3f}")

print(f"Experimental         : {experimental_se:.3f}")

print()

print("95% Confidence Interval")

print(
    f"({confidence_interval[0]:.3f}, "
    f"{confidence_interval[1]:.3f})"
)


# -------------------------------------------------
# Population Visualization
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
    "images/population_distribution_library.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -------------------------------------------------
# Sampling Distribution Visualization
# -------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    sample_means,
    bins=30,
    density=True,
    edgecolor="black",
    alpha=0.7,
    label="Sample Means"
)

x = np.linspace(
    sample_means.min(),
    sample_means.max(),
    500
)

plt.plot(
    x,
    norm.pdf(
        x,
        np.mean(sample_means),
        np.std(sample_means, ddof=1)
    ),
    linewidth=2,
    label="Normal Curve"
)

plt.title("Sampling Distribution of the Sample Mean")

plt.xlabel("Sample Mean")

plt.ylabel("Density")

plt.grid(True)

plt.legend()

plt.savefig(
    "images/sampling_distribution_library.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

