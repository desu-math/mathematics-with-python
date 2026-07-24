
"""
Descriptive Statistics
(Library-Based Implementation)

This program computes descriptive statistics
using NumPy and Pandas.

Author: Desalu Horsa
"""

import numpy as np
import pandas as pd

# -------------------------------------------------
# Create Dataset
# -------------------------------------------------

data = np.array([12, 15, 18, 15, 20, 22, 15, 25, 28, 30])

print("Dataset:")
print(data)

# -------------------------------------------------
# Measures of Central Tendency
# -------------------------------------------------

mean = np.mean(data)

median = np.median(data)

mode = pd.Series(data).mode()

# -------------------------------------------------
# Measures of Dispersion
# -------------------------------------------------

data_range = np.max(data) - np.min(data)

variance = np.var(data)

standard_deviation = np.std(data)

# -------------------------------------------------
# Quartiles and IQR
# -------------------------------------------------

q1 = np.percentile(data, 25)

q3 = np.percentile(data, 75)

iqr = q3 - q1

# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("\nDescriptive Statistics")
print("-" * 30)

print(f"Mean                : {mean:.2f}")
print(f"Median              : {median}")
print(f"Mode                : {list(mode)}")
print(f"Range               : {data_range}")
print(f"Variance            : {variance:.2f}")
print(f"Standard Deviation  : {standard_deviation:.2f}")
print(f"First Quartile (Q1) : {q1}")
print(f"Third Quartile (Q3) : {q3}")
print(f"Interquartile Range : {iqr}")

