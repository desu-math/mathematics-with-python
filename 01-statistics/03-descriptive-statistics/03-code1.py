"""
Descriptive Statistics
(Manual Implementation)

This program computes common descriptive statistics
without using NumPy or other statistical libraries.

Author: Desalu Horsa
"""

import math
from collections import Counter

# -------------------------------------------------
# Sample Dataset
# -------------------------------------------------

data = [12, 15, 18, 15, 20, 22, 15, 25, 28, 30]

print("Dataset:")
print(data)

# -------------------------------------------------
# Mean
# -------------------------------------------------

def mean(values):
    return sum(values) / len(values)

# -------------------------------------------------
# Median
# -------------------------------------------------

def median(values):
    values = sorted(values)
    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]

# -------------------------------------------------
# Mode
# -------------------------------------------------

def mode(values):
    counts = Counter(values)
    highest = max(counts.values())

    modes = []

    for value, frequency in counts.items():
        if frequency == highest:
            modes.append(value)

    return modes

# -------------------------------------------------
# Range
# -------------------------------------------------

def data_range(values):
    return max(values) - min(values)

# -------------------------------------------------
# Variance (Population)
# -------------------------------------------------

def variance(values):
    m = mean(values)

    squared_deviations = []

    for value in values:
        squared_deviations.append((value - m) ** 2)

    return sum(squared_deviations) / len(values)

# -------------------------------------------------
# Standard Deviation
# -------------------------------------------------

def standard_deviation(values):
    return math.sqrt(variance(values))

# -------------------------------------------------
# Interquartile Range (IQR)
# -------------------------------------------------

def iqr(values):
    values = sorted(values)
    n = len(values)
    mid = n // 2

    lower = values[:mid]
    upper = values[mid:]

    q1 = median(lower)
    q3 = median(upper)

    return q1, q3, q3 - q1

# -------------------------------------------------
# Display Results
# -------------------------------------------------

q1, q3, interquartile_range = iqr(data)

print("\nDescriptive Statistics")
print("-" * 30)

print(f"Mean                : {mean(data):.2f}")
print(f"Median              : {median(data)}")
print(f"Mode                : {mode(data)}")
print(f"Range               : {data_range(data)}")
print(f"Variance            : {variance(data):.2f}")
print(f"Standard Deviation  : {standard_deviation(data):.2f}")
print(f"First Quartile (Q1) : {q1}")
print(f"Third Quartile (Q3) : {q3}")
print(f"Interquartile Range : {interquartile_range}")

