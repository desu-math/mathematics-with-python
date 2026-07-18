"""
Example 2: Linear Regression Using Scikit-Learn

This program demonstrates a complete
Linear Regression workflow.

Steps:
    1. Create a dataset
    2. Store the data in a DataFrame
    3. Train a Linear Regression model
    4. Display the regression equation
    5. Make predictions
    6. Evaluate the model
    7. Visualize the regression line

Libraries:
    NumPy
    Pandas
    Matplotlib
    Scikit-Learn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# -------------------------------------------------
# Create Dataset
# -------------------------------------------------

data = {
    "Study_Hours": [2, 3, 5, 6, 8],
    "Exam_Score": [50, 55, 65, 70, 85]
}

df = pd.DataFrame(data)

print("Dataset")
print("-------")
print(df)

print()


# -------------------------------------------------
# Prepare Input and Output Variables
# -------------------------------------------------

X = df[["Study_Hours"]]

Y = df["Exam_Score"]


# -------------------------------------------------
# Create and Train the Model
# -------------------------------------------------

model = LinearRegression()

model.fit(X, Y)


# -------------------------------------------------
# Regression Coefficients
# -------------------------------------------------

intercept = model.intercept_

slope = model.coef_[0]

print("Regression Equation")
print("-------------------")

print(
    f"Y = {intercept:.2f} + {slope:.2f}X"
)

print()


# -------------------------------------------------
# Predict New Observation
# -------------------------------------------------

new_hours = np.array([[7]])

predicted_score = model.predict(new_hours)

print(
    f"Predicted score for {new_hours[0][0]} study hours:"
)

print(f"{predicted_score[0]:.2f}")

print()


# -------------------------------------------------
# Predict Existing Observations
# -------------------------------------------------

predicted = model.predict(X)

results = pd.DataFrame({
    "Study Hours": X["Study_Hours"],
    "Observed Score": Y,
    "Predicted Score": predicted,
    "Residual":
        Y - predicted
})

print("Prediction Results")
print("------------------")

print(results)

print()


# -------------------------------------------------
# Model Evaluation
# -------------------------------------------------

r2 = r2_score(Y, predicted)

print("Model Evaluation")
print("----------------")

print(f"R² = {r2:.4f}")

print()


if r2 >= 0.80:
    print("Excellent model fit.")

elif r2 >= 0.60:
    print("Good model fit.")

elif r2 >= 0.40:
    print("Moderate model fit.")

else:
    print("Weak model fit.")


# -------------------------------------------------
# Visualization
# -------------------------------------------------

plt.scatter(
    X,
    Y,
    label="Observed Data"
)

plt.plot(
    X,
    predicted,
    linewidth=2,
    label="Regression Line"
)

plt.title(
    "Simple Linear Regression"
)

plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Exam Score"
)

plt.legend()

plt.grid(True)

plt.show()

