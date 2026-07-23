"""
Example 2: Covariance and Correlation Analysis Using Python Libraries

This program demonstrates a practical Data Science workflow:

    - Creating a dataset
    - Using Pandas DataFrame
    - Calculating covariance
    - Calculating correlation
    - Visualizing relationship using scatter plot

Libraries:
    NumPy
    Pandas
    Matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------
# Create Dataset
# -------------------------------------------------

data = {
    "Study_Hours": [2, 3, 5, 6, 8],
    "Exam_Score": [50, 55, 65, 70, 85]
}


# Convert dictionary into DataFrame

df = pd.DataFrame(data)


# Display dataset

print("Dataset:")
print(df)


# -------------------------------------------------
# Calculate Covariance
# -------------------------------------------------

covariance_matrix = df.cov()

print("\nCovariance Matrix:")
print(covariance_matrix)


# Extract covariance between variables

cov = covariance_matrix.loc[
    "Study_Hours",
    "Exam_Score"
]


# -------------------------------------------------
# Calculate Correlation
# -------------------------------------------------

correlation_matrix = df.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)


# Extract Pearson correlation coefficient

r = correlation_matrix.loc[
    "Study_Hours",
    "Exam_Score"
]


# -------------------------------------------------
# Display Results
# -------------------------------------------------

print("\nStudy Hours and Exam Score Analysis")

print("-----------------------------------")

print("Covariance:")
print(round(cov, 2))

print()

print("Correlation:")
print(round(r, 2))


# -------------------------------------------------
# Interpretation
# -------------------------------------------------

print()

if r > 0:
    print("Direction: Positive relationship")

elif r < 0:
    print("Direction: Negative relationship")

else:
    print("Direction: No linear relationship")


if abs(r) >= 0.8:
    print("Strength: Very strong relationship")

elif abs(r) >= 0.6:
    print("Strength: Strong relationship")

elif abs(r) >= 0.4:
    print("Strength: Moderate relationship")

else:
    print("Strength: Weak relationship")


# -------------------------------------------------
# Visualization
# -------------------------------------------------

plt.scatter(
    df["Study_Hours"],
    df["Exam_Score"]
)


plt.xlabel("Study Hours")

plt.ylabel("Exam Score")

plt.title(
    "Relationship Between Study Hours and Exam Score"
)


plt.grid(True)

plt.show()

