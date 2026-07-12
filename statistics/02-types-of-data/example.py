"""
Types of Data

This example demonstrates how different types of
statistical data can be represented in Python.

Author: Desalu Horsa
"""

# -----------------------------------------
# Qualitative (Categorical) Data
# -----------------------------------------

gender = ["Male", "Female", "Male", "Female"]

blood_group = ["A", "O", "B", "AB"]

print("Qualitative Data")
print("Gender:", gender)
print("Blood Group:", blood_group)

# -----------------------------------------
# Quantitative Data
# -----------------------------------------

ages = [18, 20, 19, 21]

heights = [1.72, 1.68, 1.80, 1.75]

print("\nQuantitative Data")
print("Ages:", ages)
print("Heights (m):", heights)

# -----------------------------------------
# Discrete Data
# -----------------------------------------

number_of_books = [5, 8, 2, 10]

print("\nDiscrete Data")
print("Number of Books:", number_of_books)

# -----------------------------------------
# Continuous Data
# -----------------------------------------

temperatures = [22.5, 24.1, 23.8, 25.0]

print("\nContinuous Data")
print("Temperatures (°C):", temperatures)

# -----------------------------------------
# Measurement Scales
# -----------------------------------------

nominal = ["Red", "Blue", "Green"]

ordinal = ["Low", "Medium", "High"]

interval = [-5, 0, 15, 30]       # Celsius

ratio = [2.5, 5.0, 10.0, 20.0]   # Distance (km)

print("\nMeasurement Scales")
print("Nominal:", nominal)
print("Ordinal:", ordinal)
print("Interval (°C):", interval)
print("Ratio (km):", ratio)

# -----------------------------------------
# Python Data Types
# -----------------------------------------

print("\nPython Data Types")
print("gender      :", type(gender))
print("ages        :", type(ages))
print("heights     :", type(heights))
print("temperatures:", type(temperatures))

