```python
"""
Magnitude and Direction of a Vector
----------------------------------
This program calculates the magnitude and direction
of a two-dimensional vector.

Author: Desalu Horsa
Repository: mathematics-with-python
"""

import math

# ---------------------------------
# Input
# ---------------------------------

x = float(input("Enter the x-component: "))
y = float(input("Enter the y-component: "))

# ---------------------------------
# Magnitude
# ---------------------------------

magnitude = math.sqrt(x**2 + y**2)

# ---------------------------------
# Direction
# ---------------------------------

# Direction angle in radians
angle_radians = math.atan2(y, x)

# Convert radians to degrees
angle_degrees = math.degrees(angle_radians)

# ---------------------------------
# Output
# ---------------------------------

print("\nVector:")
print(f"v = ({x}, {y})")

print(f"\nMagnitude = {magnitude:.4f}")

print(f"Direction = {angle_degrees:.2f}°")
```
